MINIMUM_NUM_OF_PASSWORD = 1


def main():
    password = get_password()
    print_password_stars(password)


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_NUM_OF_PASSWORD:
        print(f"Invalid input")
        password = input("Please enter your password: ")
    return password


def print_password_stars(password):
    print('*' * len(password))


main()
