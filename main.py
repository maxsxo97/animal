class Animal:
    def __init__(self, species, age, meal, body_type):
        self.species: str = species
        self.age: int = age
        self.meal: str = meal
        self.body_type: str = body_type

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, new_species):
        if len(new_species) < 2:
            raise ValueError
        self.__species = new_species

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 4:
            raise ValueError
        self.__age = new_age

    @property
    def meal(self):
        return self.__meal

    @meal.setter
    def meal(self, new_meal):
        if len(new_meal) < 2:
            raise ValueError
        self.__meal = new_meal

    @property
    def body_type(self):
        return self.__body_type

    @body_type.setter
    def body_type(self, new_body_type):
        if len(new_body_type) < 5:
            raise ValueError
        self.__body_type = new_body_type

    def __str__(self):
        return f"Вид: {self.species}, Возраст: {self.age}, Еда: {self.meal}, Тип тела: {self.body_type}"


a = Animal("кот", 6, "корм", "4 лапый друг")
print(a)
