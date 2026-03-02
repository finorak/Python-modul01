class Plant:

    number_of_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_start = age
        Plant.number_of_plants += 1
        self.get_info()

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age_start} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25, 30)
    oak = Plant("oak", 200, 365)
    cactus = Plant("cactus", 5, 90)
    sunflower = Plant("sunflower", 80, 45)
    fern = Plant("fern", 15, 120)
    print(f"Total plants created: {Plant.number_of_plants}")
