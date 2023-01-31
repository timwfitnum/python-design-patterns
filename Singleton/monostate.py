class CEO:
    __shared_state = {"name": "Steve", "age": 55}

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}"


cfo1 = CFO()
cfo1.name = "Sheryl"
cfo1.money_managed = 1
print(cfo1)
cfo2 = CFO()
cfo2.name = "Ruth"
cfo2.money_managed = 10

print(cfo1)
print(cfo2)
