from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicous")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicous")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water," f" pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water," f" pour {amount}ml, enjoy!")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialised = False

    def __init__(self) -> None:
        if not self.initialised:
            self.initialised = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Avaliable drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (1-{len(self.factories)}): ")
        idx = int(s) - 1
        s = input("Specify amount: ")
        amount = int(s)
        return self.factories[idx - 1][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.make_drink()
