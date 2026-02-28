class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.type = "Flower"
        self.get_info()

    def get_info(self) -> None:
        print(f"{self.name} (self.type): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.type = "Tree"
        self.get_info()

    def produce_shade(self) -> None:
        print(f"{self.name} provides {78} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} ({self.type}): {self.height}cm, {self.age} days, {self.trunk_diameter} diameter")

class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.type = "Vegetable"
        self.get_info()

    def get_info(self) -> None:
        print(f"{self.name} ({self.type}): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

    def benefice(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("flower", 25, 30, "red")
    rose.bloom()
    peace_lily = Flower("peace lily", 2, 15, "violet")
    peace_lily.bloom()
    print()
    oak = Tree("oak", 500, 1825, 50)
    oak.produce_shade()
    baobab = Tree("Baobab", 10000, 30000, 100)
    baobab.produce_shade()
    print()
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamine c")
    tomato.benefice()
    letuce = Vegetable("letuce", 80, 90, "moon", "vitamine e")
    letuce.benefice()
