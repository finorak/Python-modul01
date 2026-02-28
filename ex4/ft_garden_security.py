class SecurePlant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.plant_creation()

    def is_valid(self) -> bool:
        if self.height < 0:
            print(f"Invalid operation attempted: height {self.height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        if self.age < 0:
            print(f"Invalid operation attempted: age -{self.age} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        return True

    def plant_creation(self) -> None:
        if not self.is_valid():
            return
        print(f"Plant created: {self.name}")
        print(f"Height updated: {self.height}cm [OK]")
        print(f"Age updated: {self.age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", 25, 30)
    print()
    invalid = SecurePlant("rose", -5, 30)
    print()
    print(f"Current plant: {rose.name} ({rose.height}cm, {rose.age} days)")
    
