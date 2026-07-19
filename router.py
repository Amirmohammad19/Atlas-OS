from core import AtlasCore


class MessageRouter:

    def __init__(self):
        self.core = AtlasCore()


    def process(self, user_id, message):
        return self.core.process_message(
            user_id,
            message
        )