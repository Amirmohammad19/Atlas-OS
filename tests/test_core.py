from core import AtlasCore
from user import User

core = AtlasCore()

user = User(1, "Amir")

print(core.register_user(user))

core.remember(1, "Hello Atlas")
core.remember(1, "Second message")

print(core.recall(1))

core.clear_memory(1)

print(core.recall(1))