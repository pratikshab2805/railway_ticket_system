# fare.py

from routes import TRAIN_PREMIUMS, TRAIN_SURCHARGES, TRAVEL_CLASSES


def calculate_slab_fare(distance):
    """
    Calculate the base fare using distance slabs.
    """

    fare = 100

    # First 100 km
    if distance <= 100:
        fare += distance * 1.00

    # 101 km to 300 km
    elif distance <= 300:
        fare += 100 * 1.00
        fare += (distance - 100) * 0.80

    # Beyond 300 km
    else:
        fare += 100 * 1.00
        fare += 200 * 0.80
        fare += (distance - 300) * 0.60

    return fare


def apply_senior_discount(fare, age):
    """
    Apply 40% senior citizen discount
    if age is strictly greater than 60.
    """

    if age > 60:
        return fare * 0.60

    return fare


def apply_train_premium(fare, train_type):
    """
    Apply the premium associated with the selected train type.
    """

    premium = TRAIN_PREMIUMS[train_type]

    return fare * premium


def apply_class_premium(fare, travel_class):
    """
    Apply the multiplier associated with the selected travel class.
    """

    multiplier = TRAVEL_CLASSES[travel_class]["multiplier"]

    return fare * multiplier


def calculate_excess_baggage_fee(baggage_weight, travel_class):
    """
    Calculate baggage penalty.

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
    Return the flat surcharge for the selected train type.
    """

    return TRAIN_SURCHARGES[train_type]


def calculate_passenger_fare(
    distance,
    age,
    train_type,
    travel_class,
    baggage_weight
):
    """
    Calculate the complete fare for one passenger.
    """

    # Step 1: Slab Fare
    fare = calculate_slab_fare(distance)

    # Step 2: Senior Citizen Discount
    fare = apply_senior_discount(fare, age)

    # Step 3: Train Premium
    fare = apply_train_premium(fare, train_type)

    # Step 4: Class Premium
    fare = apply_class_premium(fare, travel_class)

    # Step 5: Excess Baggage Fee
    baggage_fee = calculate_excess_baggage_fee(
        baggage_weight,
        travel_class
    )

    fare += baggage_fee

    # Step 6: Flat Surcharge
    surcharge = calculate_surcharge(train_type)

    fare += surcharge

    return fare


def calculate_promo_discount(subtotal, promo_code):
    """
    Calculate discount based on the promotional code.
    """

    if promo_code == "ADG20":
        return subtotal * 0.20

    elif promo_code == "WINTER500":
        return min(500, subtotal)

    return 0


def calculate_final_total(subtotal, promo_code):
    """
    Calculate the final amount after applying promo discount.
    """

    discount = calculate_promo_discount(
        subtotal,
        promo_code
    )

    final_total = subtotal - discount

    # Total should never be negative
    return max(0, final_total)
