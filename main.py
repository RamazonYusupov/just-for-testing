# Function = a block of reusable code
    # place () after the function name to invoke it
def happy_birthday(name): # parametr
    print(f"Happy birthday to {name}!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Ramazon") # argument
happy_birthday("Sunnatillo")
happy_birthday("Abduqahhor")


def first_and_last_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(first_and_last_name('ramazon', 'yusupov'))