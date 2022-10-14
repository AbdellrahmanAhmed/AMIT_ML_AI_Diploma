#            ____  _____  ______ _      _____            _    _ __  __          _   _            _    _ __  __ ______ _____             ____  _____  ______ _      _____          _____ __  __
#      /\   |  _ \|  __ \|  ____| |    |  __ \     /\   | |  | |  \/  |   /\   | \ | |     /\   | |  | |  \/  |  ____|  __ \      /\   |  _ \|  __ \|  ____| |    |  __ \   /\   |_   _|  \/  |
#     /  \  | |_) | |  | | |__  | |    | |__) |   /  \  | |__| | \  / |  /  \  |  \| |    /  \  | |__| | \  / | |__  | |  | |    /  \  | |_) | |  | | |__  | |    | |  | | /  \    | | | \  / |
#    / /\ \ |  _ <| |  | |  __| | |    |  _  /   / /\ \ |  __  | |\/| | / /\ \ | . ` |   / /\ \ |  __  | |\/| |  __| | |  | |   / /\ \ |  _ <| |  | |  __| | |    | |  | |/ /\ \   | | | |\/| |
#   / ____ \| |_) | |__| | |____| |____| | \ \  / ____ \| |  | | |  | |/ ____ \| |\  |  / ____ \| |  | | |  | | |____| |__| |  / ____ \| |_) | |__| | |____| |____| |__| / ____ \ _| |_| |  | |
#  /_/    \_\____/|_____/|______|______|_|  \_\/_/    \_\_|  |_|_|  |_/_/    \_\_| \_| /_/    \_\_|  |_|_|  |_|______|_____/  /_/    \_\____/|_____/|______|______|_____/_/    \_\_____|_|  |_|



from Class import *

rox = Dog(dogEyeColor="Blue", dogBreed='Bread')
simba = Dog(dogEyeColor="Black", dogBreed='No Bread')

print("This dog is a", rox.breed, "and his eyes are", rox.eyeColor, "number of Dogs in class", Dog.num_dogs)
print("This dog is a", simba.breed, "and his eyes are", simba.eyeColor, "number of Dogs in class", Dog.num_dogs)

# names = ['aly','mohammed']
aly = Student(name='Aly Mohammed', age=20, numberOfEnrolled=6)
mohammed = Student(name='Mohammed Husam', age=22, numberOfEnrolled=5)

aly.sayMyName()
Dog.printNumberOfDog()
print(Student.studentList)

# for i in Student.studentList:
#     print("Student name is",i.name,"age",i.age,"number of Student is")

Student.printStudentName()
