from database import Database
from memory import Memory


class AtlasCore:
    def __init__(self):
        self.database = Database()
        self.memory = Memory()

    def register_user(self, user):
        return self.database.add_user(user)

    def remember(self, user_id, message):
        self.memory.save(user_id, message)

    def recall(self, user_id):
        return self.memory.get(user_id)

    def clear_memory(self, user_id):
        self.memory.clear(user_id)

    def process_message(self, user_id, message):
        self.remember(user_id, message)

        return f"You said: {message}"