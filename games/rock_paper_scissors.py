import random

icon = ['🪨', '📃', '✂️']
my_score = 0
comp_score = 0


def calculate(num):
    global my_score, comp_score

    comp = random.randint(0, 2)

    if (num == 0 and comp == 1) or (num == 2 and comp == 0) or (num == 1 and comp == 2):
        msg = 'Computer wins'
        comp_score += 1
    elif (num == 1 and comp == 0) or (num == 0 and comp == 2) or (num == 2 and comp == 1):
        msg = 'You win'
        my_score += 1
    else:
        msg = "It's a draw"

    print(f"""
    You chose {icon[num]}    
    Computer chose {icon[comp]}
    {msg}!

    Computer {comp_score} - {my_score} You
    """)


while True:
    val = input('Rock, paper, or scissors? (r/p/s/quit): ').lower()

    if val == 'quit':
        break
    elif val == 'r':
        calculate(1)
    elif val == 'p':
        calculate(1)
    elif val == 's':
        calculate(2)
    else:
        print('Invalid input!')
        continue

    # proceed = input('Continue? (y/n): ').lower()
    # if proceed != 'y':
    #     break
