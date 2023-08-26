from guitar import Guitar


def test_get_age():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    expected_age1 = 100
    expected_age2 = 9

    actual_age1 = guitar1.get_age(2022)
    actual_age2 = guitar2.get_age(2022)

    print(f"Gibson L-5 CES get_age() - Expected {expected_age1}. Got {actual_age1}")
    print(f"Another Guitar get_age() - Expected {expected_age2}. Got {actual_age2}")


def test_is_vintage():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    expected_vintage1 = True
    expected_vintage2 = False

    actual_vintage1 = guitar1.is_vintage(2022)
    actual_vintage2 = guitar2.is_vintage(2022)

    print(f"Gibson L-5 CES is_vintage() - Expected {expected_vintage1}. Got {actual_vintage1}")
    print(f"Another Guitar is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")


test_get_age()
test_is_vintage()
