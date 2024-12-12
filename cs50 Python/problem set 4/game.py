import random
import sys

while True:
    level = input("Level: ")
    if level.isdigit() and int(level) > 0:
        rand_num = random.randint(1, int(level))
        while True:
            guess = input("Guess: ")
            if guess.isdigit():
                if int(guess) < rand_num:
                    print("Too small!")
                elif int(guess) > rand_num:
                    print("Too large!")
                else:
                    sys.exit("Just right!")
