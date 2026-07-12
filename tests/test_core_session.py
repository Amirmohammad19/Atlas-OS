import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core import AtlasCore

core = AtlasCore()

core.set_session(1, "mode", "chat")

print(core.get_session(1, "mode"))

core.clear_session(1)

print(core.get_session(1, "mode"))