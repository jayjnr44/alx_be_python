import random

secret_number=random.randint(1, 10) 
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?: "))

match guess:
    case _ if guess == secret_number:
        print("Congratulations! You guessed the secret number!") 
    case _ if guess < secret_number:
        print("Oops your guess was too low! Try again")
    case _ if guess > secret_number:
        print("Nope, your guess was too high. Give it another shot.")
    case _:
        print("Invalid guess. Please enter a number between 1 and 10.")

print(f"The secret number was: {secret_number}")
int(input("I'm thinking of a number between 1 and 10. Can you guess it?:"))

match guess:
    case _ if guess == secret_number:
        print("Congratulations! You guessed the secret number!") 
    case _ if guess < secret_number:
        print("Oops your guess was too low! Try again")
    case _ if guess > secret_number:
        print("Nope, your guess was too high. Give it another shot.")
    case _:
        print("Invalid guess. Please enter a number between 1 and 10.")
print ("thank you for playing!")
