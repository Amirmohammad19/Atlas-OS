class Memory:
    def __init__(self):
        self.messages = {}

    def save(self, user_id, message):
        if user_id not in self.messages:
            self.messages[user_id] = []

        self.messages[user_id].append(message)

    def get(self, user_id):
        return self.messages.get(user_id, [])

    def clear(self, user_id):
        if user_id in self.messages:
            self.messages[user_id].clear()

    def clear_all(self):
        self.messages.clear()