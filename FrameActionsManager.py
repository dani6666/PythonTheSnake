import asyncio
import time
from multiprocessing.dummy import Process

from Rendering.RenderingManager import RenderingManager


class FrameActionsManager:
    def __init__(self, rendering_enabled, bot_input_provider, player_input_provider):
        self.rendering_enabled = rendering_enabled
        self.bot_input_provider = bot_input_provider
        self.player_input_provider = player_input_provider
        # self.event_loop = asyncio.get_event_loop()

    async def carry_frame_actions(self, game_state):
        if self.bot_input_provider:
            # thread = Process(target=self.bot_input_provider.start_thinking, args=game_state)
            # thread.start()
            thinking_task = asyncio.create_task(self.bot_input_provider.start_thinking(game_state))
                # self.event_loop.run_in_executor(None, , 0))

        if self.rendering_enabled:
            time.sleep(8)
            RenderingManager.render()

        if self.player_input_provider:
            return self.player_input_provider.retrieve_input()

        if self.bot_input_provider:
            # thread.join()
            await thinking_task
            return self.bot_input_provider.retrieve_input()
