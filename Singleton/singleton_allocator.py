import random


class Database:
    _instance = None

    def __init__(self) -> None:
        id = random.randint(1, 101)
        print(id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


d1 = Database()
d2 = Database()
print(d1 == d2)
