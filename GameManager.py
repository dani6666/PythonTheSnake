import random

import Util
from Model.GameState import GameState
from GameObjects.Snake import Snake
from Model.SpecialAction import SpecialAction
from Model.Vector import Vector
from GameObjects.Apple import Apple
from Rendering.ActionFrame import ActionFrame
from InfoTracker.ScoreTracker import ScoreTracker
from InfoTracker.TimeTracker import TimeTracker
from InfoTracker.InfoTracker import InfoTracker

from PopupManagement.PopupAssembly import PopupAssembly
from PopupManagement.Reason import Reason


class GameManager:

    def __init__(self, grid_size, amount_of_players=1):
        self.grid_size = grid_size

        self.is_multi = (amount_of_players > 1)
        self.amount_of_players = amount_of_players
        self.snakes = []
        snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        self.snakes.append(Snake(snake_pos))
        self.snakes[0].grow_pending = True
        self.snakes[0].move()
        self.handle_border_cross(self.snakes[0])
        for i in range(1, amount_of_players):
            occupied_axis = [snake.head.position.y for snake in self.snakes]
            snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
            while snake_pos.y in occupied_axis:
                snake_pos.y = random.randrange(grid_size.y)
            self.snakes.append(Snake(snake_pos, num=i))
            self.snakes[i].grow_pending = True
            self.snakes[i].move()
            self.handle_border_cross(self.snakes[i])
        apple_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        while apple_pos in [s.head.position for s in self.snakes]:
            apple_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        self.apple = Apple(apple_pos)

        score_tracker = ScoreTracker(Vector(0, 0), grid_size.x)
        time_tracker = TimeTracker(Vector(0, 0))
        self.info_tracker = InfoTracker(Vector(0, 0), score_tracker, time_tracker)

        self.action_frame = None
        self.popup = None

    def simulate_move(self, actions):
        if actions == SpecialAction.reset_game:
            self.reset()
            return False
        elif actions == SpecialAction.game_paused:
            return Reason.game_pause
        place_new_apple = False
        for i, snake in enumerate(self.snakes):
            if snake.alive:
                action = actions[i]

                if action and not Util.is_opposite(snake.moving_direction, action):
                    snake.moving_direction = action
                snake.move()
                self.handle_border_cross(snake)

                # eating apple
                if not place_new_apple and snake.head.get_pos() == self.apple.get_pos():
                    snake.grow_pending = True
                    self.info_tracker.increment_score()
                    if self.info_tracker.score == self.grid_size.x * self.grid_size.y - 1:
                        return self.determine_winner_apple()
                    place_new_apple = True

        if place_new_apple:
            self.place_new_apple()

        self.info_tracker.update_time()

        # check if there are any collisions; if there are - determine the winner
        return self.handle_collisions()

    def handle_border_cross(self, snake):
        snake_head_pos = snake.head.get_pos()
        if snake_head_pos.x < 0:
            snake.head.change_pos(Vector(self.grid_size.x - 1, snake_head_pos.y))
        elif snake_head_pos.x > self.grid_size.x - 1:
            snake.head.change_pos(Vector(0, snake_head_pos.y))
        elif snake_head_pos.y < 0:
            snake.head.change_pos(Vector(snake_head_pos.x, self.grid_size.y - 1))
        elif snake_head_pos.y > self.grid_size.y - 1:
            snake.head.change_pos(Vector(snake_head_pos.x, 0))

    def determine_winner_apple(self):
        if not self.is_multi:
            return Reason.game_won
        else:
            if self.snakes[0].get_size() > self.snakes[1].get_size():
                return Reason.p1_wins
            elif self.snakes[0].get_size() < self.snakes[1].get_size():
                return Reason.p2_wins
            else:
                return Reason.tie

    def place_new_apple(self):
        potential_apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        slots_occupied_by_snakes = [a for s in self.snakes for a in s.get_slots_occupied_by_snake()]
        while potential_apple_pos in slots_occupied_by_snakes:
            potential_apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        self.apple.change_pos(potential_apple_pos)

    def get_game_score(self):
        return self.info_tracker.score

    def handle_collisions(self):
        if not self.is_multi:
            if self.snakes[0].check_collision():
                return Reason.game_lost
        else:
            alive_n = 0
            dead = []
            for i, snake in enumerate(self.snakes):
                if snake.alive:
                    slots_occupied_by_other_snakes = [
                        slot for j in range(self.amount_of_players)
                        for slot in self.snakes[j].get_slots_occupied_by_snake() if j != i and self.snakes[j].alive
                    ]
                    dead.append((snake.check_collision() or snake.head.position in slots_occupied_by_other_snakes))
                else:
                    dead.append(True)
            for i, snake in enumerate(self.snakes):
                snake.alive = not dead[i]
                if snake.alive:
                    alive_n += 1
            if not alive_n:
                return Reason.tie
            elif alive_n == 1:
                alive_i = [i for i in range(self.amount_of_players) if self.snakes[i].alive][0]
                return alive_i
        return False

    def call_popup(self, reason):
        self.popup = PopupAssembly.get_standard_finish_popup(
            Vector((self.grid_size.x - 11) // 2, (self.grid_size.y - 5) // 2),
            self.grid_size.x,
            reason
        )
        self.action_frame.add_rendering_component(self.popup)

    def reset(self):
        new_snakes = []
        snake_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        self.snakes[0].reset(snake_pos)
        new_snakes.append(self.snakes[0])
        new_snakes[0].grow_pending = True
        new_snakes[0].move()
        self.handle_border_cross(new_snakes[0])
        for snake in self.snakes[1:]:
            snake_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
            occupied_axis = [snake.head.position.y for snake in new_snakes]
            while snake_pos.y in occupied_axis:
                snake_pos.y = random.randrange(self.grid_size.y)
            snake.reset(snake_pos)
            new_snakes.append(snake)
            new_snakes[-1].grow_pending = True
            new_snakes[-1].move()
            self.handle_border_cross(new_snakes[-1])
        self.snakes = new_snakes
        apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        while apple_pos in [s.head.position for s in self.snakes]:
            apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        self.apple.position = apple_pos

        self.info_tracker.reset()

        self.action_frame.remove_rendering_component(self.popup)
        self.popup = None

    def unpause(self):
        self.info_tracker.unpause()
        self.action_frame.remove_rendering_component(self.popup)
        self.popup = None

    def get_current_game_state(self):
        return GameState(self.grid_size, self.apple.get_pos(), self.snakes[0], self.snakes[0].moving_direction,
                         self.info_tracker.score)

    def get_action_frame(self):
        self.action_frame = ActionFrame(
            Vector(self.grid_size.x, self.grid_size.y + 1),
            Vector(40, 40),
            [self.apple] + self.snakes + [self.info_tracker]
        )
        return self.action_frame
