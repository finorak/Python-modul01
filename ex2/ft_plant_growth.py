class Plant:

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.starting = 1
        self.growth_mesure = 6

    def grow(self) -> None:
        age = self.age()
        self.days += self.growth_mesure
        self.height += self.growth_mesure
        self.get_info()
        print(f"Growth this week: +{self.height - age + 1}cm")

    def age(self) -> int:
        temp = self.starting
        self.starting += self.growth_mesure
        return self.height + temp

    def get_info(self):
        print(f"=== Day {self.starting} ===")
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    rose.get_info()
    rose.grow()
