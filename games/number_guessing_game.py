import random

number = random.randint(1, 100)

while True:
    try:
        value = int(input('Guess the number between 1 and 100: '))
        if int(value) > number:
            print("Too high!")
        elif int(value) < number:
            print("Too low!")
        else:
            print('Congratulations! You guessed he number.')
            break
    except ValueError:
        print("Please enter a valid number")
