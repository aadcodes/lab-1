#q1 
class person:
    def __init__(self,name,age) :
       self.name=name
       self.age=age
    def display(self):
        print(f"Name:{self.name},Age:{self.age}")

class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    def show_details(self):
        self.display()
        print(f"Student ID:{self.student_id}")
student1=student("Alice",20,"S12345")
student1.show_details()

#q2
 class vehicle:
     def into(self):
         print("this is a vehicle")
 class car(vehicle):
     def car_info(self):
         print("this is a car")
 class electriccar(car):
     def battery_info(self):
         print("this car has a battery")

 electric_car=electric()
 electric_car.info()
 electric_car.car_info()
 electric_car.battery_info()

# #q3
class teacher:
  def description(self):
        print("this is a teacher")
class author:
    def description(self):
         print("this is a author")
class tutorauthor(teacher,author):
     def description(self):
        super().description()
        author.description(self)
 tutor_author=tutorauthor()
 tutor_autro.description()

 #q4
class animal:
     def sound(self):
         print("Animals make sound")
 class Dog(animal):
     def sound(self):
         print("Dog barks")
 class Cat(Animal):
     def sound(self):
         print("cat meows")
 dog=Dog()
 cat=Cat()
 dog.sound()
 cat.sound
