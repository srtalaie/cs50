import random


def main():
    level = get_level()
    i = 0
    score = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} ="
        tries = 1
        while True:
            answer = input(problem + " ")
            if tries != 3:
                if not answer.isdigit():
                    print("EEE")
                    tries += 1
                elif answer.isdigit() and (int(answer) == (x + y)) and tries < 3:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            elif tries == 3:
                print(f"EEE\n{problem} {int(x + y)}")
                break

        i += 1
    print(f"Score: {score}")


def get_level():
    num = 0
    while True:
        level = input()
        if level.isdigit():
            if int(level) in range(1, 4):
                num = int(level)
                break
    return num


def generate_integer(level):
    if 1 <= level <= 3:
        if int(level) == 1:
            return random.randint(0, 9)
        elif int(level) == 2:
            return random.randint(10, 99)
        elif int(level) == 3:
            return random.randint(100, 999)
    else:
        raise ValueError("Level is not in range from 1 to 3")


if __name__ == "__main__":
    main()
