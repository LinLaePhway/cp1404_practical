import csv
from guitar import Guitar


def main():
    guitars = load_guitars()

    while True:
        name = input("Enter the guitar's name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year_input = input("Enter the year it was made: ")
        if not year_input.isdigit():
            print("Invalid year. Please enter a valid year.")
            continue
        year = int(year_input)
        cost_input = input("Enter the cost of the guitar: ")
        if not cost_input.replace('.', '', 1).isdigit():
            print("Invalid cost. Please enter a valid cost.")
            continue
        cost = float(cost_input)
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{name} ({year}) - ${cost:.2f} added to your collection.")

    save_guitars(guitars)

    print("\nAll Guitars in guitars.csv:")
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year}) - ${guitar.cost:.2f}")


def load_guitars():
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
        print("No existing data file found.")
    return guitars


def save_guitars(guitars):
    with open('guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
