# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def write_letter(name, text):
    print(greet("Hello", name) + "\n")
    print(text + "\n")
    print(f"Goodbye {name}")




def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

write_letter("Jonno", "THis is my very long letter")