from datetime import datetime
from unittest.mock import patch


def get_food_period(database, species):
    return


def feed_animal(database, name, when):
    return


def go_round(database, species):
    now = datetime.datetime.utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1

    return fed


def get_animals():
    print("wwwww")


print("Outside patch: ", get_animals)

with patch("__main__.get_animals"):
    print("inside agein: ", get_animals)

print("Outside agein: ", get_animals)
