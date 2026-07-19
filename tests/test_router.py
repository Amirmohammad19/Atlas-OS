from core import AtlasCore
from user import User

core = AtlasCore()

user = User(1, "Amir")
core.register_user(user)

print(core.process_message(1, "/help"))

print("-----")

print(core.process_message(1, "/status"))

print("-----")

print(core.process_message(1, "Hello Atlas"))