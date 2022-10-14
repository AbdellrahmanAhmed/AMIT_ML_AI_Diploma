#            ____  _____  ______ _      _____            _    _ __  __          _   _            _    _ __  __ ______ _____             ____  _____  ______ _      _____          _____ __  __
#      /\   |  _ \|  __ \|  ____| |    |  __ \     /\   | |  | |  \/  |   /\   | \ | |     /\   | |  | |  \/  |  ____|  __ \      /\   |  _ \|  __ \|  ____| |    |  __ \   /\   |_   _|  \/  |
#     /  \  | |_) | |  | | |__  | |    | |__) |   /  \  | |__| | \  / |  /  \  |  \| |    /  \  | |__| | \  / | |__  | |  | |    /  \  | |_) | |  | | |__  | |    | |  | | /  \    | | | \  / |
#    / /\ \ |  _ <| |  | |  __| | |    |  _  /   / /\ \ |  __  | |\/| | / /\ \ | . ` |   / /\ \ |  __  | |\/| |  __| | |  | |   / /\ \ |  _ <| |  | |  __| | |    | |  | |/ /\ \   | | | |\/| |
#   / ____ \| |_) | |__| | |____| |____| | \ \  / ____ \| |  | | |  | |/ ____ \| |\  |  / ____ \| |  | | |  | | |____| |__| |  / ____ \| |_) | |__| | |____| |____| |__| / ____ \ _| |_| |  | |
#  /_/    \_\____/|_____/|______|______|_|  \_\/_/    \_\_|  |_|_|  |_/_/    \_\_| \_| /_/    \_\_|  |_|_|  |_|______|_____/  /_/    \_\____/|_____/|______|______|_____/_/    \_\_____|_|  |_|



class Dog:
    num_dogs = 0

    def __init__(self, dogBreed, dogEyeColor):
        Dog.num_dogs += 1
        self.breed = dogBreed
        self.eyeColor = dogEyeColor

    # Class Method
    @classmethod
    def printNumberOfDog(cls):
        print(Dog.num_dogs)


class Student:
    num_student = 0
    studentList = []

    def __init__(self, name, age, numberOfEnrolled):
        Student.num_student += 1
        self.name = str(name)
        self.age = age
        self.numberOfEnrolled = numberOfEnrolled
        # studentList = studentList.append(self.name)
        Student.studentList.append(self.name)

    # Instance Method
    def sayMyName(self):
        print(self.name)

    # Static Method
    @staticmethod
    def printStudentName():
        for i in Student.studentList:
            print(i)
