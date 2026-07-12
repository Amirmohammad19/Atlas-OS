class SessionManager:
    def __init__(self):
        self.sessions = {}

    def set(self, user_id, key, value):
        if user_id not in self.sessions:
            self.sessions[user_id] = {}

        self.sessions[user_id][key] = value

    def get(self, user_id, key):
        return self.sessions.get(user_id, {}).get(key)

    def clear(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]