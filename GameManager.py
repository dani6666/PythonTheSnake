import random

import Util
from Model.GameState import GameState
from GameObjects.Snake import Snake
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
        snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        self.snakes = []
        self.snakes.append(Snake(snake_pos))
        for i in range(amount_of_players - 1):
            snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
            while snake_pos in [s.head.position for s in self.snakes]:
                snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
            self.snakes.append(Snake(snake_pos, snd=True))
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
        place_new_apple = False
        for i, snake in enumerate(self.snakes):
            action = actions[i]
            if action and not Util.is_opposite(snake.moving_direction, action):
                snake.moving_direction = action

            snake.move()

            self.handle_border_cross(snake)

            # eating apple
            if snake.head.get_pos() == self.apple.get_pos():
                snake.grow_pending = True

                self.info_tracker.increment_score()
                if self.info_tracker.score == self.grid_size.x * self.grid_size.y - 1:
                    self.determine_winner_apple()
                    return True

                place_new_apple = True

        if place_new_apple:
            self.place_new_apple()

        self.info_tracker.update_time()

        # check if there are any collisions; if there are - determine the winner
        return self.handle_winner_determining()

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
            self.call_popup(Reason.game_won)
        else:
            if self.snakes[0].get_size() > self.snakes[1].get_size():
                self.call_popup(Reason.p1_wins)
            elif self.snakes[0].get_size() < self.snakes[1].get_size():
                self.call_popup(Reason.p2_wins)
            else:
                self.call_popup(Reason.tie)

    def place_new_apple(self):
        potential_apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        slots_occupied_by_snakes = [a for s in self.snakes for a in s.get_slots_occupied_by_snake()]
        while potential_apple_pos in slots_occupied_by_snakes:
            potential_apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        self.apple.change_pos(potential_apple_pos)

    def handle_winner_determining(self):
        if not self.is_multi:
            if self.snakes[0].check_collision():
                self.call_popup(Reason.game_lost)
                return True
        else:
            one_collide = self.snakes[0].check_collision() or \
                self.snakes[0].head.position in self.snakes[1].get_slots_occupied_by_snake()
            two_collide = self.snakes[1].check_collision() or \
                self.snakes[1].head.position in self.snakes[0].get_slots_occupied_by_snake()
            if one_collide and two_collide:
                self.call_popup(Reason.tie)
                return True
            elif two_collide:
                self.call_popup(Reason.p1_wins)
                return True
            elif one_collide:
                self.call_popup(Reason.p2_wins)
                return True
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
        for snake in self.snakes[1:]:
            snake_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
            while snake_pos in [s.head.position for s in new_snakes]:
                snake_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
            snake.reset(snake_pos)
            new_snakes.append(snake)
        self.snakes = new_snakes
        apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        while apple_pos in [s.head.position for s in self.snakes]:
            apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))
        self.apple.position = apple_pos

        self.info_tracker.reset()

        self.action_frame.remove_rendering_component(self.popup)
        self.popup = None

    def get_current_game_state(self):
        return GameState(self.grid_size, self.apple.get_pos(), self.snakes[0], self.snakes[0].moving_direction)

    def get_action_frame(self):
        self.action_frame = ActionFrame(
            Vector(self.grid_size.x, self.grid_size.y + 1),
            Vector(40, 40),
            [self.apple] + self.snakes + [self.info_tracker]
        )
        return self.action_frame
