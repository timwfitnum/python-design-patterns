import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.population = {}
        f = open("capitals.txt", "r")
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i + 1].strip())
        f.close()
        pass


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population.get(c, 0)
        return result


class ConfigurableRecordFinder:
    def __init__(self, db) -> None:
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population.get(c, 0)
        return result


class DummyDatabase:
    population = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    def get_population(self, name):
        return self.get_population[name]


class SingletonTest(unittest.TestCase):

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(["A", "B"]))

    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = [""]  # insert from your file here
        tp = rf.total_population(names)
        self.assertEqual(0, 0)  # use tp and your population expected sum here
