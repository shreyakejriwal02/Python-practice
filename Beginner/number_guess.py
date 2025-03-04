import random

###
# Goal: Create a program that generates a random number between two bounds and the user has to guess the number within 7 tries.
###

# Opening banner
print("Welcome to the Number Guessing Game!")

# Retrieve a number from the users
while True:
    try:
        lower_input = input("Enter a lower bound: ")
        lower = int(lower_input)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        
while True:
    try:
        upper_input = input("Enter an upper bound: ")
        upper = int(upper_input)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Generate a random number between the lower and upper bounds
guess_number = random.randint(int(lower_input), int(upper_input))
print("I have generated a random number between " + lower_input + " and " + upper_input + ".")
print("You will have 7 tries to guess the number. Good Luck!")

# Loop through 7 tries
for i in range(7):
    # Ask the user to enter a guess
    while True:
        try:
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Check if the guess is correct
    if guess == guess_number:
        print("Congratulations! You have guessed the correct number.")
        # Inform the user how many tries it took if they guessed the number
        print("You have guessed the correct number in " + str(i + 1) + " tries.")
        break
    elif guess < guess_number:
        print("The number is higher. Try again.")
        lower = guess
    else:
        print("The number is lower. Try again.")
        upper = guess
    
    # Inform the user if number of tries are over
    if i == 6:
        print("You have run out of tries. The correct number was " + str(guess_number) + ".")
