from datetime import datetime, timedelta
from unittest.mock import Mock


class ZooDatabase:
    def get_animals(self, species):
        return

    def get_food_period(self, species):
        return

    def feed_animal(self, name, when):
        return


def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utctime()
    feeding_timedelta = database.get_food_period(species)
    animals = database.get_animals(species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) >= feeding_timedelta:
            database.feed_animal(name, now)
            fed += 1

    return fed


database = Mock(spec=ZooDatabase)

now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2019, 6, 5, 15, 45)
breakpoint()

database.get_food_period.assert_called_once_with("Meerkat")
database.get_animals.assert_called_once_with("Meerkat")
database.feed_animal.assert_has_calls(
    [call("Spot", now_func.return_value), call("Fluffy", now_func.return_value)],
    any_order=True,
)
