def greet_many(greeting, *args):
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
    return greetings

print(greet_many("Hello", "Martin", "Sadie", "Martin", "Martin", "Martin", "Martin"))
print(greet_many("Hello", "Thais", "Fievel"))

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

user_tuple = ("Hello", "Waheed")
print(greet(*user_tuple))