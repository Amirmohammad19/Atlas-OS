class Database:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if self.user_exists(user.user_id):
            return False

        self.users.append(user)
        return True

    def _find_user_index(self, user_id):
        return next(
            (i for i, u in enumerate(self.users) if u.user_id == user_id),
            -1
        )

    def get_users(self):
        return self.users.copy()

    def get_user_by_id(self, user_id):
        return next(
            (u for u in self.users if u.user_id == user_id),
            None
        )

    def get_user_by_username(self, username):
        return next(
            (u for u in self.users if u.username == username),
            None
        )

    def remove_user(self, user_id):
        index = self._find_user_index(user_id)

        if index == -1:
            return False

        self.users.pop(index)
        return True

    def update_username(self, user_id, new_username):
        existing = self.get_user_by_username(new_username)

        if existing and existing.user_id != user_id:
            return False

        user = self.get_user_by_id(user_id)

        if not user:
            return False

        user.username = new_username
        return True

    def user_exists(self, user_id):
        return self._find_user_index(user_id) != -1

    def get_user_count(self):
        return len(self.users)

    def clear_users(self):
        self.users.clear()