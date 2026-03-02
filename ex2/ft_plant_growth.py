class Plant:

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.old_height = self.height
        self.starting = 1
        self.growth_mesure = 6

    def grow(self) -> None:
        self.old_height = self.height
        self.height += self.growth_mesure
        self.get_info()

    def age(self) -> None:
        self.days += self.growth_mesure
        self.starting += 6
        self.get_info()
        self.get_growth()

    def get_growth(self):
        growth = self.height - self.old_height
        print(f"Growth this weak: +{growth}")
        self.old_height = self.height

    def get_info(self):
        print(f"=== Day {self.starting} ===")
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    rose.grow()
    rose.age()
    rose.age()
    rose.grow()
    rose.age()
