from taxi import Taxi


def main():
    taxi = Taxi(100)

    taxi.drive(40)

    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")
    print()

    taxi.start_fare()
    print(f"Current fare: ${taxi.get_fare():.2f} before moving any new distance")
    distance_driven = taxi.drive(100)

    print(f"After attempting to drive another 100km, the actual distance is: {distance_driven} km")
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


main()
