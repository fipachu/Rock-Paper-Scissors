# todo:
#  1) implement some optimal strategy shenanigans,
#  statistics, and a better scoring system
#  2) update rating.txt after !exit
# https://www.youtube.com/watch?v=-1GDMXoMdaY
# https://www.youtube.com/watch?v=rudzYPHuewc
# test #6 protects against that, but it could be easily fooled
# beats_user could be precomputed for all moves, but whatever
# users that make len(moves) don't deserve Christmas gifts
from random import choice

username = input("Enter your name: ")
print(f"Hello, {username}")

with open('rating.txt') as rating_file:
    ratings: dict[str:int] = \
        {line.split(' ')[0]: eval(line.split(' ')[1]) for line in rating_file}
score: int = 0
if username in ratings:
    score = ratings[username]

moves: list[str] = input().split(',')
if len(moves) < 3:  # or len(moves) % 2,
    moves = ['rock', 'paper', 'scissors']
# here we coooouuuuld randomize division for even len(moves):
beats_number: int = (len(moves) - 1) // 2
beats_master = moves + moves[:beats_number]

print("Okay, let's start!")

while True:
    users_move: str = input()
    if users_move == '!exit':
        print('Bye!')
        break
    elif users_move == '!rating':
        print(f"Your rating: {score}")
        continue
    elif users_move not in moves:
        print('Invalid input')
        continue

    elif users_move in moves:
        next_index: int = moves.index(users_move) + 1
        beats_user: list[str] = beats_master[next_index: next_index + beats_number]

        computers_move = choice(moves)
        if computers_move in beats_user:
            print(f"Sorry, but the computer chose {computers_move}")
        elif computers_move == users_move:
            print(f"There is a draw ({computers_move})")
            score += 50
        elif users_move not in beats_user:
            score += 100
            print(f"Well done. The computer chose {computers_move} and failed")
