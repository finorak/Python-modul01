class SecurePlant:

    plant_added = []

    def __init__(self, name: str, height: str, age: str) -> None:
        self.__name = name.capitalize()
        self.__height = "0"
        self.__age = "0"
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
        if not element:
            return False
        if element[0] == '-' or element[0] == '+':
            index += 1
        if self.strlen(element) <= 1:
            print("Attempted to insert non valid value [REJECTED]")
            return False
        while index < length:
            if element[index] not in digits:
                print("Attempted to insert non valid value [REJECTED]")
                return False
            index += 1
        return True

    def is_valid(self, element: str, representation: str) -> bool:
        metric = "cm" if representation == "height" else " days"
        if not element:
            return False
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
        self.content = f"{self.__name} ({self.__height}cm, {self.__age} days)"
        self.plant_added += [self.content]
        print(f"Plant created: {self.__name}")
        print(f"Height updated: {self.__height}cm [OK]")
        print(f"Age updated: {self.__age} days [OK]\n")

    def update_age(self, age: str) -> None:
        if self.is_digit(age) and self.is_valid(age, "age"):
            self.__age = age
            self.content = f"{self.__name} ({self.__height}cm, {self.__age} days)"
            print("Age updated succesfully!")
    
    def update_height(self, height: str) -> None:
        if self.is_digit(height) and self.is_valid(height, "height"):
            self.__height = height
            self.content = f"{self.__name} ({self.__height}cm, {self.__age} days)"
            print("Height updated succesfully!")
    
    def get_info(self) -> None:
        print(self.content)

    def get_plants(self) -> None:
        print("Current Plant: ")
        for plant in SecurePlant.plant_added:
            print(plant)

    def get_age(self) -> str:
        return self.__age

    def get_height(self) -> str:
        return self.__height


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", "12", "60")
    rose.update_age("61")
    rose_age = rose.get_age()
    print(f"rose age: {rose_age}")
