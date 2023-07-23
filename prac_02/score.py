import random


def main():
    user_score = float(input("Enter score: "))
    result = get_result(user_score)
    print(result)

    random_score = random.randint(0, 200)
    result = get_result(random_score)
    print(f"Random {random_score} score is {result}")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
