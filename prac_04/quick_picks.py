import random

MIN_NUMBER = 1
MAX_NUMBER = 45
LINES_PER_QUICK_PICK = 6


def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER), LINES_PER_QUICK_PICK))


def display_quick_picks(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2d}" for number in quick_pick))


main()
