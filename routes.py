# routes.py

# Available routes and their distances in kilometres
ROUTES = {
    ("New Delhi", "Mumbai"): 1460,
    ("New Delhi", "Kolkata"): 1525,
    ("New Delhi", "Chennai"): 2200,
    ("New Delhi", "Hyderabad"): 1670,
    ("Mumbai", "Kolkata"): 1970,
    ("Mumbai", "Chennai"): 1300,
    ("Mumbai", "Hyderabad"): 711,
    ("Kolkata", "Chennai"): 1200,
    ("Kolkata", "Hyderabad"): 1600,
    ("Chennai", "Hyderabad"): 633
}


# Available train types and their average speeds
TRAIN_TYPES = {
    "Superfast": 120,
    "Express": 110,
    "Fast Passenger": 90
}


# Premium applied based on train type
TRAIN_PREMIUMS = {
    "Superfast": 1.50,
    "Express": 1.25,
    "Fast Passenger": 1.00
}


# Flat surcharge based on train type
TRAIN_SURCHARGES = {
    "Superfast": 100,
    "Express": 50,
    "Fast Passenger": 0
}


# Travel classes
TRAVEL_CLASSES = {
    "Sleeper": {
        "multiplier": 1.0,
        "baggage_allowance": 20
    },
    "AC 3-Tier": {
        "multiplier": 1.5,
        "baggage_allowance": 30
    },
    "AC 2-Tier": {
        "multiplier": 2.0,
        "baggage_allowance": 40
    }
}
