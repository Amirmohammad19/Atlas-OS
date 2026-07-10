from memory import Memory

memory = Memory()

memory.save(1, "Hello")
memory.save(1, "How are you?")

print(memory.get(1))

memory.clear(1)

print(memory.get(1))