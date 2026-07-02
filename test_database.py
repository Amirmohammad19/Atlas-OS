from database import Database
from user import User

db = Database()

user1 = User(1, "Amir")
user2 = User(2, "Sara")

db.add_user(user1)
db.add_user(user2)

db.update_username(2, "Sarah")

for user in db.get_users():
    print(user)