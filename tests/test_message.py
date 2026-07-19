from core import AtlasCore
from user import User

core = AtlasCore()

user = User(1, "Amir")
core.register_user(user)

response = core.process_message(1, "Hello Atlas")

print(response)

print(core.recall(1))