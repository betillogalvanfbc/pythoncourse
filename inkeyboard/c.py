number = 8
#user_input = input("Enter 'y' if you would like to play:").lower()
user_input = input("Enter 'y' if you would like to play:").lower()

# if user_input in ("y","Y"):

if user_input == "y":
    user_number = int(input("Guess our number:"))
    if user_number == number:
        print("You guessed correclty!")
    elif abs(number - user_number) == 1:
        print("You we are off by one.")
    else:
        print("Sorry, it's wrong!")
