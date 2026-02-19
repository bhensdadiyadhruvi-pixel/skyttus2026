# 1.Create a base class Animal and subclasses Dog and Cat. 
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# 2.Create a class hierarchy for Vehicle → Car → ElectricCar.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is being driven")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


ecar = ElectricCar()
ecar.start()
ecar.drive()
ecar.charge()

# 3.mplement method overriding in a base and derived class. 

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.sound()
d.sound()

# 4.Demonstrate multiple inheritance with two parent classes.
class Father:
    def skill(self):
        print("Father: Driving")

class Mother:
    def talent(self):
        print("Mother : Cooking")

class Child(Father, Mother):
    def hobby(self):
        print("child: painting")
        
c = Child()
c.skill()
c.hobby()

# 5.Create a polymorphic function that works with different shapes. 
class Circle:
    def area(self):
        return 3.14 * self.radius * self.radius

    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    def area(self):
        return self.length * self.width

    def __init__(self, length, width):
        self.length = length
        self.width = width

# Polymorphic function
def print_area(shape):
    print("Area:", shape.area())


c = Circle(5)
r = Rectangle(4, 6)

print_area(c)
print_area(r)

# 6. Create a Bank system with SavingsAccount and CurrentAccount classes
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings Account Balance:", self.balance)

class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current Account Balance:", self.balance)

s = SavingsAccount(5000)
c = CurrentAccount(8000)

s.interest()
c.overdraft()

# 7.Create a class with private attributes and getter/setter methods.
class Student:
    def __init__(self, name, marks):
        self.__marks = marks   # private attribute

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks


s = Student("dhruvi", 85)

print(s.get_marks())
s.set_marks(90)
print(s.get_marks())
 
#  8. Create a Teacher and Student class to show inheritance.
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


class Student(Person):
    def study(self):
        print(self.name, "is studying")

t = Teacher("Ms.jinal Tailor ")
s = Student("Dhruvi")

t.teach()
s.study()

# 9.Create a MusicPlayer class and subclass Spotify to override play method. 
class MusicPlayer:
    def play(self):
        print("Playing Music")
        

class Spotify(MusicPlayer):
    def play(self):
        print("Playing Music on Spotify")
    

player = MusicPlayer()
spotify = Spotify()

player . play()
spotify.play()

# 10.Demonstrate the use of super() in inheritance.
class A:
    def show(self):
        print("Class A")
        
class B(A):
    def show(self):
        super().show()
        print("Class B")
    
b = B()
b.show()
