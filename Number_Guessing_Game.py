
# Number Guessing Game Using Python
import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number , highest_number ) # To get Random Number
guesses = 0
is_running = True # While Loop Continue


print("\n\t\t\t------ NUMBER GUESSING GAME ------\n")
print(f"\t\t\t(Guess A Number Between {lowest_number} And {highest_number})\n")

while is_running:

    guess = input("Enter Your Guess :")

    if guess.isdigit(): 
        guess = int(guess)
        guesses += 1 # Increse The Guesses By 1 Each Time Guess


        if guess < lowest_number or guess > highest_number:
            print("Your Guess Is Out Of Range!")
            print(f"Please Guess A Number Between {lowest_number} And {highest_number}\n")

        elif guess < answer:
            print("Guess Is To Low!")
        
        elif guess > answer:
            print("Guess Is To High!")
        
        else:
            print("\nCongratulations! You guessed correctly!")
            print(f"The number was {answer}")
            print(f"You guessed it in {guesses} attempts\n")
            is_running = False

    else:
        print(f"*{guess}* Is A Invaild Guess!")
        print(f"Please Guess A Number Between {lowest_number} And {highest_number}\n")


