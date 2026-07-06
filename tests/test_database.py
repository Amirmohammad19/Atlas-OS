from database import Database
from user import User

db = Database()

user1 = User(1, "Amir")
user2 = User(2, "Sarah")

db.add_user(user1)
db.add_user(user2)

db.clear_users()

print(db.get_user_count())