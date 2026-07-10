from command import CommandParser

parser = CommandParser()

print(parser.is_command("/help"))
print(parser.is_command("Hello Atlas"))

print(parser.get_command("/help"))
print(parser.get_command("/start hello"))