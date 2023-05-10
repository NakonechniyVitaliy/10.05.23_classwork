class Human:
    race = "Людина"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Builder(Human):
    def build_house(self):
        return (f"{self.name} {self.surname}побудував будинок")

class Sailor(Human):
    def sea(self):
        return (f"{self.name} {self.surname}вийшов у відкритий океан")

class Pilot(Human):
    def sky(self):
        return (f"{self.name} {self.surname}полетів у рейс")


first_human = Builder("Виталий", "Наконечний ")
print(first_human.build_house(), "\nРасса -", f"{first_human.race}")

second_human = Sailor("Роман", "Титаренко ")
print(second_human.sea(), "\nРасса -", f"{second_human.race}")

thirth_human = Pilot("Ростислав", "Гончаренко ")
print(thirth_human.sky(), "\nРасса -", f"{thirth_human.race}")

####################################################################################

class Animals:
    rase = "Animal"
    def __init__(self, name, weigh, height):
        self.name = name
        self.weigh = weigh
        self.height = height

class Kenguru(Animals):
    kind = "Кенгуру"
    def kenguru_def(self):
       None

class Krokodile(Animals):
    kind = "Крокодил"
    def krokodile_def(self):
        None

class Tiger(Animals):
    kind = "Тигр"
    def tiger_def(self):
        None


first_kenguru = Kenguru("Ігор", "100", "180")
first_krokodile = Krokodile("Володя", "80", "40")
first_tiger = Tiger("Ілля", "200", "70")

print(first_kenguru.kind, first_kenguru.name, first_kenguru.weigh, first_kenguru.height)
print(first_krokodile.kind, first_krokodile.name, first_krokodile.weigh, first_krokodile.height)
print(first_tiger.kind, first_tiger.name, first_tiger.weigh, first_tiger.height)

