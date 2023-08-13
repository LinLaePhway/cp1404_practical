def main():
    user_data = {}
    email = input("Email: ")

    while email != "":
        name_guess = extract_name(email)
        confirmation = input(f"Is your name {name_guess}? (Y/n) ").lower()

        if confirmation == '' or confirmation == 'y':
            name = name_guess
        else:
            name = input("Name: ").title()

        user_data[email] = name
        email = input("Email: ")

    print("\nUser Data:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def extract_name(email):
    return email.split('@')[0].title()


main()
