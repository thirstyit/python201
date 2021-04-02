def greet(greeting=None, name=None):  # parameters
    return greeting, name

print(greet("Hi", "Sadie"))
# print(greet(name="Martin", greeting="Hello"))  # arguments


def greet(greeting="Hi", name="User"):  # Adding defaults
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet())
print(greet(name="Fievel", greeting="Hello"))