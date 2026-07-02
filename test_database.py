from  database import Database
from user import User

db = Database()

user1 = User(1, "Amir")
user2 = User(2, "Sara")

db.add_user(user1)
db.add_user(user2)

found_user = db.get_user_by_id(2)

print(found_user)