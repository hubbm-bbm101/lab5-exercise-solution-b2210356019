import random

print("You should find the right answer in 10 guess!")
print("Guess a number between 1 and 100!")
number = random.randint(1, 100)
guess = 0
number_of_guesses = 0

while number_of_guesses < 10 and guess != number:
    guess = int(input("Please enter a number: "))
    number_of_guesses = number_of_guesses + 1
    print("Remaining guesses: " + str(10 - number_of_guesses))
    if guess == number:
        print("You win!!")
    elif number_of_guesses == 10:
        print("You lose!!")
    elif guess < number:
        print("Increase your number!")
    else:
        print("Decrease your number!")
