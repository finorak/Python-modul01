class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)


if __name__ == "__main__":
    pass
