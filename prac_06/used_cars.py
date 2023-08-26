"""
CP1404 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from cars import Car


def main():
    my_car = Car(180, "My Car")
    limo = Car(100, "Limo")

    limo.add_fuel(20)
    limo.drive(115)

    print(my_car)
    print(limo)


main()
