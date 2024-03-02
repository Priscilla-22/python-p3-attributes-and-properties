class Human:
    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    # compiled bt the property function and prints smth when age is accessed through the dot notation or an attr() function
    def get_age(self):
        print("Retriving age.")
        return self._age

    # this function is compiled by the property() function and prints something when the human age is changed
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to {age}.")
            self._age = age
        else:
            print("Age must be a number between 0 and 120.")

    # this property function compiles together the getter and setter and calls them whenever anyone accesses the human age
    age = property(get_age, set_age)


guido = Human(age=67)

guido.age = 66
print(guido.age)
