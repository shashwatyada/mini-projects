import random
secret_number = random.randint(1, 100)
attemts_left =5
print("Welcome to the guessing game!")
print("You have 5 attempts to guess the secret number between 1 and 100.")

while attemts_left > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    attemts_left -= 1
    print(f"You have {attemts_left} attempts left.")
if attemts_left == 0:
    print(f"Game over! The secret number was {secret_number}. Better luck next time!")
