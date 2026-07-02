class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.goal = ""

    def set_goal(self, goal):
            self.goal = goal
    def get_goal(self):
        return self.goal
    