class Dog:
    num_dogs = 0

    def __init__(self, dogBreed, dogEyeColor):
        Dog.num_dogs += 1
        self.breed = dogBreed
        self.eyeColor = dogEyeColor


class Student:
    num_student = 0

    def __init__(self, name, age, numberOfEnrolled):
        self.name = name
        self.age = age
        self.numberOfEnrolled = numberOfEnrolled
