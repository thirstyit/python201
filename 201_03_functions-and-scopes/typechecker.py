def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet("Hello", "World"))
print(greet([1, 2, 3], 42))
print(greet(True, False))
