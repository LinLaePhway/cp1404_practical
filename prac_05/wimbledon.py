import csv


def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    wins = count_wins(data)
    countries = get_countries(data)
    print("Wimbledon Champions:")

    for champion, count in wins.items():
        print(f"{champion} {count}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_string = ", ".join(countries)
    print(countries_string)


def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data


def count_wins(data):
    wins = {}
    for row in data:
        champion = row[2]
        if champion in wins:
            wins[champion] += 1
        else:
            wins[champion] = 1
    return wins


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


main()

