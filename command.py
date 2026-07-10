class CommandParser:

    def is_command(self, message):
        return message.startswith("/")

    def get_command(self, message):
        if self.is_command(message):
            return message[1:].split()[0]

        return None