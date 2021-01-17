import random
import time

print('''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.''')
while True:
    number = random.randrange(1234, 9876)
    if len(str(number)) < 3:
        continue
    if len(str(number)) == 3:
        number = str('0') + str(number)
    x = set(str(number))
    if len(x) == 4:
        print(number)
        break


def main():
    start = time.time()
    counter = 0
    num = None
    while str(num) != str(number):
        num = get_num()
        match(num, number)
        counter += 1
    end = time.time()
    if counter == 1:
        print(f'1 attemp? congrats, you\'ve hacked my game :) ')
    elif counter < 6:
        print(f'amazing!!! {counter} attempts')
    elif counter < 12:
        print(f'good job: {counter} attempts')
    elif counter < 21:
        print(f'not great, not terrible: {counter} attempts')
    else:
        print(f'no pain no gain, sorry looser: {counter} attempts')
    print(f'This game took {int(end - start)} seconds')


def get_num():
    while True:
        num = input(f'Enter a 4-digits number: ')
        if len(str(num)) == 4:
            return num


def match(num, number):
    bulls = cows = 0
    for i in range(4):
        if str(number)[i] in set(str(num)):
            cows += 1
        if str(number)[i] == str(num)[i]:
            bulls += 1
            cows -= 1
    if bulls == 1:
        print(f'there was {bulls} bull in your number')
    else:
        print(f'there were {bulls} bulls in your number')
    if cows == 1:
        print(f'there was {cows} cow in your number')
    else:
        print(f'there were {cows} cows in your number')


main()
print()
