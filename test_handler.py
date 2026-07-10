from handler import CommandHandler

handler = CommandHandler()

print(handler.handle("help"))

print("---")

print(handler.handle("status"))

print("---")

print(handler.handle("test"))