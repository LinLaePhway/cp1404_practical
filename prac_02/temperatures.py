MENU = "C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"
print(MENU)


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = calculate_celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = calculate_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def calculate_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
