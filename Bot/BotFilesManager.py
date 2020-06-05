import os

import jsonpickle as jsonpickle


class BotFilesManager:
    bot_resources_file_name = "saved-bot.json"

    @staticmethod
    def check_for_saved_bot():
        if os.path.exists(BotFilesManager.bot_resources_file_name):
            file = open(BotFilesManager.bot_resources_file_name)
            data = file.read()
            file.close()
            return jsonpickle.loads(data)
        else:
            return None

    @staticmethod
    def save_bot(network_weights):
        data = jsonpickle.dumps(network_weights)
        file = open(BotFilesManager.bot_resources_file_name, mode="w")
        file.write(data)
        file.close()
