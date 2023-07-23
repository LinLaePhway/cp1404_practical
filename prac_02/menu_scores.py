import random
MENU = "(P)rint result \n(S)how stars \n(R)andom score and result \n(Q)uit"


def main():
    user_score = get_valid_score()

    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "P":
            print_result(user_score)
        elif choice == "S":
            show_stars(user_score)
        elif choice == "R":
            random_score = generate_random_score()
            print(f"Random score: {random_score}")
            print_result(random_score)
        else:
            print("Invalid choice. Please try again.")

        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell!")


def get_valid_score():
    score = float(input("Enter the score between 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter the score between 0-100: "))
    return score


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    result = get_result(score)
    print(result)


def show_stars(score):
    stars = '*' * int(score)
    print(stars)


def generate_random_score():
    return random.randint(0, 100)


main()
