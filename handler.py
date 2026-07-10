class CommandHandler:

    def handle(self, command):
        commands = {
            "help": self.help_command,
            "status": self.status_command
        }

        action = commands.get(command)

        if action:
            return action()

        return "Unknown command"

    def help_command(self):
        return (
            "Available commands:\n"
            "/help\n"
            "/status"
        )

    def status_command(self):
        return "Atlas-OS is running 🚀"