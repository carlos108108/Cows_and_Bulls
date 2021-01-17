import random
import time

def main():
    total_time = game_counter = all_counter = 0
    x = None
    while x != 'q':  # hru ukončujeme příkazem 'q'
        print('''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n''')
        while True:  # smyčka generující i 4digit čísla začínající 0
            number = random.randrange(0, 9876)
            if len(str(number)) < 3:
                continue
            if len(str(number)) == 3:
                number = str('0') + str(number)
            x = set(str(number))
            if len(x) == 4:
                break

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
            print(f'no pain, no gain: {counter} attempts')
        print(f'This game took {round((end - start), 2)} seconds')
        x = input('if you don\'t want to play enter \'q\'')
        print()
        game_counter += 1
        total_time += (end - start)
        all_counter += counter
    my_statistic(game_counter, total_time, all_counter)

def get_num():
    while True:
        num = input(f'Enter a 4-digits number: ')
        if len(str(num)) == 4 and num.isnumeric():
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
        print(f'there was {cows} cow in your number\n')
    else:
        print(f'there were {cows} cows in your number\n')

def my_statistic(game_counter, total_time, all_counter):
    if game_counter == 1:
        print(f'thank you for your {game_counter} game')
    else:
        print(f'thank you for your {game_counter} games')
    print(f'all games took {round(total_time, 2)} seconds')
    print(f'each game took {round(total_time / game_counter, 2)} seconds on average')
    print(f'you needed {round(all_counter / game_counter, 2)} attemps on average for each game')

main()
print()
