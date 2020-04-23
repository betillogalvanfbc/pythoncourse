number = 8
# while user_input != "n":
while True:
    user_input = input("Would you like to play? (Y/n)?\n").lower()

    if user_input == "n":
        break

    user_number = int(input("Guess our number:"))
    if user_number == number:
        print("You guessed correclty!")
    elif abs(number - user_number) == 1:
        print("You we are off by one.")
    else:
        print("Sorry, it's wrong!")
