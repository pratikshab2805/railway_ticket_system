# main.py

from routes import ROUTES, TRAIN_TYPES, TRAVEL_CLASSES
from fare import calculate_passenger_fare, calculate_final_total


def get_positive_integer(prompt):
    """
    Get a positive integer from the user.
    """

    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a value greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_age(prompt):
    """
    Get a valid age from the user.
    """

    while True:
        try:
            age = int(input(prompt))

            if age <= 0:
                print("Age must be greater than zero.")

            elif age > 120:
                print("Please enter a realistic age.")

            else:
                return age

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_baggage_weight(prompt):
    """
    Get a valid baggage weight.
    """

    while True:
        try:
            weight = float(input(prompt))

            if weight <= 0:
                print("Baggage weight must be greater than zero.")
            else:
                return weight

        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_route():
    """
    Display available routes and allow the user to choose one.
    """

    route_list = list(ROUTES.keys())

    print("\nAvailable Routes:")

    for index, route in enumerate(route_list, start=1):
        source, destination = route
        distance = ROUTES[route]

        print(
            f"{index}. {source} -> {destination} "
            f"({distance} km)"
        )

    while True:
        try:
            choice = int(input("Select route: "))

            if 1 <= choice <= len(route_list):
                return route_list[choice - 1]

            print("Invalid route selection.")

        except ValueError:
            print("Please enter a valid number.")


def choose_train():
    """
    Display available train types and get user selection.
    """

    train_list = list(TRAIN_TYPES.keys())

    print("\nTrain Types:")

    for index, train in enumerate(train_list, start=1):
        speed = TRAIN_TYPES[train]

        print(
            f"{index}. {train} "
            f"(Average Speed: {speed} km/hr)"
        )

    while True:
        try:
            choice = int(input("Select train type: "))

            if 1 <= choice <= len(train_list):
                return train_list[choice - 1]

            print("Invalid train selection.")

        except ValueError:
            print("Please enter a valid number.")


def choose_class():
    """
    Display available travel classes and get user selection.
    """

    class_list = list(TRAVEL_CLASSES.keys())

    print("\nTravel Classes:")

    for index, travel_class in enumerate(class_list, start=1):

        multiplier = TRAVEL_CLASSES[travel_class]["multiplier"]

        allowance = TRAVEL_CLASSES[travel_class]["baggage_allowance"]

        print(
            f"{index}. {travel_class} "
            f"(Multiplier: {multiplier}x, "
            f"Free Baggage: {allowance} kg)"
        )

    while True:
        try:
            choice = int(input("Select travel class: "))

            if 1 <= choice <= len(class_list):
                return class_list[choice - 1]

            print("Invalid class selection.")

        except ValueError:
            print("Please enter a valid number.")


def get_passenger_details(passenger_number):
    """
    Collect all details for one passenger.
    """

    print(f"\n--- Passenger {passenger_number} ---")

    name = input("Enter passenger name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter passenger name: ").strip()

    age = get_age("Enter age: ")

    baggage_weight = get_baggage_weight(
        "Enter baggage weight (kg): "
    )

    return {
        "name": name,
        "age": age,
        "baggage_weight": baggage_weight
    }


def main():
    """
    Main program coordinator.
    """

    print("=" * 50)
    print("      RAILWAY TICKET BOOKING SYSTEM")
    print("=" * 50)

    # Select route
    source, destination = choose_route()

    distance = ROUTES[(source, destination)]

    # Select train
    train_type = choose_train()

    # Calculate travel time
    speed = TRAIN_TYPES[train_type]

    travel_time = distance / speed

    # Select class
    travel_class = choose_class()

    # Number of passengers
    number_of_passengers = get_positive_integer(
        "\nEnter number of passengers: "
    )

    passengers = []

    subtotal = 0

    # Collect passenger information
    for passenger_number in range(1, number_of_passengers + 1):

        passenger = get_passenger_details(
            passenger_number
        )

        fare = calculate_passenger_fare(
            distance,
            passenger["age"],
            train_type,
            travel_class,
            passenger["baggage_weight"]
        )

        passenger["fare"] = fare

        passengers.append(passenger)

        subtotal += fare

    # Promo code
    print("\nPromo Code")
    print("Available codes:")
    print("ADG20")
    print("WINTER500")

    promo_code = input(
        "Enter promo code (press Enter to skip): "
    ).strip().upper()

    if promo_code not in ("", "ADG20", "WINTER500"):

        print("Invalid promo code. No discount applied.")

        promo_code = ""

    # Final total
    final_total = calculate_final_total(
        subtotal,
        promo_code
    )

    discount = subtotal - final_total

    # Final booking summary
    print("\n")
    print("=" * 50)
    print("          BOOKING SUMMARY")
    print("=" * 50)

    print(f"Route        : {source} -> {destination}")
    print(f"Distance     : {distance} km")
    print(f"Train        : {train_type}")
    print(f"Travel Class : {travel_class}")
    print(f"Travel Time  : {travel_time:.2f} hours")

    print("\nPassengers:")

    for index, passenger in enumerate(passengers, start=1):

        print(
            f"{index}. {passenger['name']} | "
            f"Age: {passenger['age']} | "
            f"Baggage: {passenger['baggage_weight']:.2f} kg | "
            f"Fare: INR {passenger['fare']:.2f}"
        )

    print("\n" + "-" * 50)

    print(f"Subtotal     : INR {subtotal:.2f}")
    print(f"Promo Code   : {promo_code if promo_code else 'None'}")
    print(f"Discount     : INR {discount:.2f}")
    print(f"Final Total  : INR {final_total:.2f}")

    print("=" * 50)
    print("       Thank you for using our system!")
    print("=" * 50)


if __name__ == "__main__":
    main()
