from Class import *


rox = Dog(dogEyeColor="Blue",dogBreed='Bread')
simba = Dog(dogEyeColor="Black",dogBreed='No Bread')

print("This dog is a",rox.breed,"and his eyes are",rox.eyeColor,"number of Dogs in class",Dog.num_dogs)
print("This dog is a",simba.breed,"and his eyes are",simba.eyeColor,"number of Dogs in class",Dog.num_dogs)

# names = ['aly','mohammed']
aly = Student(name='Aly Mohammed',age=20,numberOfEnrolled=6)
mohammed = Student(name='Mohammed Husam',age=22,numberOfEnrolled=5)

# for i in names:
#     print("Student name is",i.name,"age",i.age,"number of Student is")