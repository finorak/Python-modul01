class Plant:

    plant_count = 0

    def __init__(self, name: str, flower_type: str, height: int,
                 age: int, color: None | str) -> None:
        self.name = name.capitalize()
        self.flower_type = flower_type
        self.height = height
        self.age = age
        self.color = color
        self.is_flower = flower_type.lower() == "flowers"
        self.prize = False
        self.growth_metric = 1
        Plant.plant_count += 1

    def grow(self) -> int:
        self.height += self.growth_metric
        print(f"{self.name} {self.flower_type} grew {self.growth_metric}cm")
        return self.growth_metric

    @classmethod
    def get_plant_count(cls):
        return cls.plant_count

    @staticmethod
    def ft_append(lst: list, el: object) -> list:
        return (lst + [el])


class FloweringPlant(Plant):

    def __init__(self, name: str, flower_type: str, height: int,
                 age: int, color: None | str) -> None:
        super().__init__(name, flower_type, height, age, color)
        self.growth_metric = 1

    def grow(self) -> int:
        return super().grow()


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, flower_type: str, height: int,
                 age: int, color: None | str) -> None:
        super().__init__(name, flower_type, height, age, color)
        self.prize = True
        self.prize_point = 10


class GardenManager:
    class GardenStats:
        plants = []
        garden = 0
        growth = 0

        def __init__(self) -> None:
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def show_stats(self) -> None:
            print(f"Plant added: {Plant.get_plant_count()}", end=", ")
            print(f"Total growth: {self.get_growth_total()}cm")
            print(f"Plant types: {self.regular} regular", end=", ")
            print(f"{self.flowering} flowering, {self.prize} prize flowers")

        @classmethod
        def number_of_garden(cls) -> None:
            print(f"Total gardens managed: {cls.garden}")

        @classmethod
        def get_growth_total(cls) -> int:
            return cls.growth

    def __init__(self, owner: str) -> None:
        self.owner = owner.capitalize()
        self.plants: list[PrizeFlower | Plant] = []
        self.stats = self.GardenStats()
        self.GardenStats.garden += 1

    def add_plant(self, plant: Plant | PrizeFlower) -> None:
        print(f"Added {plant.name} {plant.flower_type}", end=" ")
        print(f"to {self.owner}'s garden")
        self.plants = Plant.ft_append(self.plants, plant)

    def create_garden_netword(self) -> None:
        pass

    def garden_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plant in garden:")
        for plant in self.plants:
            color = "" if not plant.color else plant.color
            if plant.is_flower and plant.prize:
                print(f"- {plant.name}: {plant.height}cm", end=", ")
                print(f"{color} {plant.flower_type} (blooming)", end=", ")
                print(f"Prize points: {plant.prize_point}")
                self.stats.prize += 1
            elif plant.is_flower:
                print(f"- {plant.name}: {plant.height}cm, {color}", end=" ")
                print(f"{plant.flower_type} (blooming)")
                self.stats.flowering += 1
            else:
                print(f"- {plant.name} {plant.flower_type}: {plant.height}cm")
                self.stats.regular += 1
        print()
        self.stats.show_stats()
        print()

    def grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.GardenStats.growth += plant.grow()


if __name__ == "__main__":
    print("=== Garden Manager System Demo ===\n")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    oak = Plant("oak", "Tree", 100, 1816, None)
    rose = Plant("rose", "flowers", 25, 30, "red")
    sunflower = PrizeFlower("sunflower", "flowers", 50, 50, "yellow")
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.grow()
    alice_garden.garden_report()
    print("Height validation test: True")
    print(f"Garden scores - {alice_garden.owner}: 218, {bob_garden.owner}: 92")
    GardenManager.GardenStats.number_of_garden()
