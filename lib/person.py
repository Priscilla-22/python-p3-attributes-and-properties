#!/usr/bin/env python3


"""class Human:
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
"""
#################### MAIN TASK #########################
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing",
]


class Person:

    def __init__(self, name="George", job="Marketing"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, value):
        if  isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()

        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)


person1 = Person("john doe", "Sales")
print(person1.name) 
print(person1.job) 

person2 = Person(
    "jane smith", "Accounting"
)  
person3 = Person(
    "adam", "ITC Department"
) 
person4 = Person(12345, "Human Resources")  
