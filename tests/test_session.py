from session import SessionManager

session = SessionManager()

session.set(1, "mode", "chat")

print(session.get(1, "mode"))

session.clear(1)

print(session.get(1, "mode"))