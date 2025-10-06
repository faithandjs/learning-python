import random

count = 0
max = 10


def get_number_of_di():
    return input(f'How many di do you want to roll? (max {max}): ')


while True:
    proceed = input('Roll the dice? (y/n): ').lower()
    if proceed == 'y':
        retry_input_count = 0
        num = get_number_of_di()

        while not num.isdigit() or int(num) > max:
            if retry_input_count < 3:
                print('Invalid input')
                retry_input_count += 1
                num = get_number_of_di()
            else:
                num = '1'

        value = int(num)
        count += value
        for number in range(value):
            v1 = random.randint(1, 6)
            v2 = random.randint(1, 6)
            print(f'Dice {number+1}: ({v1},{v2})')
    elif proceed == 'n':
        if count > 0:
            print(
                f"You rolled the dice {count} time{'' if count == 1 else 's' }!")
        print('Thanks for playing!')

        break
    else:
        print('Invalid choice')
