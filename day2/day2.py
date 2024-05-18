import re

#Part 1

treshold = {'red': 12, 'green': 13, 'blue': 14}
total = 0

with open ('input.txt') as input:

    games = input.read().strip().split('\n')

    for id, game in enumerate(games, start=1):

        for num, color in re.findall('(\d+) (red|green|blue)', game):
            if int(num) > treshold[color]:
                break
        else:
            total += id

print(total)

#Part 2
