class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30).get_info()
    sunflower = Plant("sunflower", 80, 45).get_info()
    cactus = Plant("cactus", 15, 120).get_info()
