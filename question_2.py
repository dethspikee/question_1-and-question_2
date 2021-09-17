from typing import Union


class Dog:

    def __init__(self, name: str, age: int, weigth: int) -> None:
        assert isinstance(age, int) == True, "Age must be int"
        assert isinstance(weigth, int) == True, "Weigth must be int"
        self.name = name
        self.age = age
        self.weight = weigth

    def bark(self) -> str:
        return "Woof!"

    def move(self) -> str:
        return "Running"

    def __str__(self) -> str:
        return self.name


class Goldendoodle(Dog):

    def __init__(self, name: str, age: int, weigth: int) -> None:
        super().__init__(name, age, weigth)

    def bark(self) -> str:
        return "WOOF WOOF!"

    def move(self) -> str:
        return "Running fast"


django = Dog("Django", 2, 6)
matty = Goldendoodle("Matty", 3, 17)


def get_oldest_dog_name(dog_1: Union[Dog, Goldendoodle], dog_2: Union[Dog, Goldendoodle]) -> str:
    """
    Return the name of the older dog. Return appropriate message
    if both are same age.
    """
    if dog_1.age == dog_2.age:
        return f"{dog_1} and {dog_2} are same age."

    return max(dog_1, dog_2, key=lambda dog: dog.age)


if __name__ == "__main__":
    print(get_oldest_dog_name(django, matty))
