import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Try a higher number.")
    elif guess > secret_number:
        print("Try a lower number.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break   
