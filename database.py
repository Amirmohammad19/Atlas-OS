class Database:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users
    
    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def remove_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def update_username(self, user_id, new_username):
        user = self.get_user_by_id(user_id)
        if user:
            user.username = new_username
            return True
        return False