class SecurePlant:

    PLANT_ADDED = []

    def __init__(self, name: str, height: str, age: str) -> None:
        self.name = name.capitalize()
        self.__height = ""
        self.__age = ""
        self.plant_creation(height, age)

    def strlen(self, element: str) -> int:
        counter = 0
        for _ in element:
            counter += 1
        return counter

    def is_digit(self, element: str) -> bool:
        digits = "0123456789"
        index = 0
        length = self.strlen(element)
        if element[0] == '-' or element[0] == '+':
            index += 1
        while index < length:
            if element[index] not in digits:
                print("Attempted to insert non valid value [REJECTED]")
                return False
            index += 1
        return True

    def is_valid(self, element: str, representation: str) -> bool:
        metric = "cm" if representation == "height" else " days"
        if element[0] == '-':
            print("\nInvalid operation attempted: height ", end="")
            print(f"{element}{metric} [REJECTED]")
            print(f"Security: Negative {element} [REJECTED]\n")
            return False
        return True

    def plant_creation(self, height: str, age: str) -> None:
        if not self.is_digit(height) or not self.is_digit(age):
            return
        if not self.is_valid(height, "height") \
                or not self.is_valid(age, "age"):
            return
        self.__height = height
        self.__age = age
        self.content = f"{self.name} ({self.__height}cm, {self.__age} days)"
        self.PLANT_ADDED += [self.content]
        print(f"Plant created: {self.name}")
        print(f"Height updated: {self.__height}cm [OK]")
        print(f"Age updated: {self.__age} days [OK]")

    def update_age(self, age: str):
        if self.is_digit(age) and self.is_valid(age, "age"):
            self.age = age
            return

    def get_info(self):
        print(self.content)

    def get_plants(self) -> None:
        for plant in self.PLANT_ADDED:
            print(plant)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", "25", "30")
    invalid = SecurePlant("invalid", "-25", "36")
    rose.get_plants()
