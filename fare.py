# fare.py

from routes import TRAIN_PREMIUMS, TRAIN_SURCHARGES, TRAVEL_CLASSES


def calculate_slab_fare(distance):
    """
    Calculate the fare using the required distance slabs.
    """

    fare = 100

    if distance <= 100:
        fare += distance * 1.00

    elif distance <= 300:
        fare += 100 * 1.00
        fare += (distance - 100) * 0.80

    else:
        fare += 100 * 1.00
        fare += 200 * 0.80
        fare += (distance - 300) * 0.60

    return fare


def apply_senior_discount(fare, age):
    """
    Apply a 40% discount if the passenger is
    strictly above 60 years old.
    """

    if age > 60:
        return fare * 0.60

    return fare


def apply_train_premium(fare, train_type):
    """
    Apply the premium based on train type.
    """

    premium = TRAIN_PREMIUMS[train_type]

    return fare * premium


def apply_class_premium(fare, travel_class):
    """
    Apply the multiplier based on travel class.
    """

    multiplier = TRAVEL_CLASSES[travel_class]["multiplier"]

    return fare * multiplier


def calculate_excess_baggage_fee(baggage_weight, travel_class):
    """
    Calculate the excess baggage fee.

    INR 15 is charged for every kilogram
    above the free baggage allowance.
    """

    allowance = TRAVEL_CLASSES[travel_class]["baggage_allowance"]

    if baggage_weight > allowance:
        excess_weight = baggage_weight - allowance
        return excess_weight * 15

    return 0


def calculate_surcharge(train_type):
    """
    Return the flat surcharge for the selected train.
    """

    return TRAIN_SURCHARGES[train_type]


def calculate_travel_time(distance, train_speed):
    """
    Calculate travel time in hours.
    """

    return distance / train_speed


def calculate_passenger_fare(
    distance,
    age,
    train_type,
    travel_class,
    baggage_weight
):
    """
    Calculate the complete fare for one passenger
    using the six required steps in order.
    """

    # Step 1 - Slab Fare
    fare = calculate_slab_fare(distance)

    # Step 2 - Senior Citizen Discount
    fare = apply_senior_discount(fare, age)

    # Step 3 - Train Premium
    fare = apply_train_premium(fare, train_type)

    # Step 4 - Class Premium
    fare = apply_class_premium(fare, travel_class)

    # Step 5 - Excess Baggage Fee
    baggage_fee = calculate_excess_baggage_fee(
        baggage_weight,
        travel_class
    )

    fare += baggage_fee

    # Step 6 - Flat Surcharge
    surcharge = calculate_surcharge(train_type)

    fare += surcharge

    return fare


def calculate_promo_discount(subtotal, promo_code):
    """
    Calculate the discount for the selected promo code.
    """

    if promo_code == "ADG20":
        return subtotal * 0.20

    elif promo_code == "WINTER500":
        return min(500, subtotal)

    return 0


def calculate_final_total(subtotal, promo_code):
    """
    Calculate the final booking total after discount.
    """

    discount = calculate_promo_discount(
        subtotal,
        promo_code
    )

    final_total = subtotal - discount

    # Final total must never be negative
    return max(0, final_total)
