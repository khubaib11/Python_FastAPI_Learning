# s = "abc"
# print(id(s))

# s = s + "d"
# print(id(s))



# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color
#         self.model = model

#     def drive(self):
#         print(f"{self.model} is driving")

#     def stop(self):
#         print(f"{self.model} stopped")
    
#     def display(self):
#         print(f"{self.model} is {self.color}")


# myCar=Car("blue","Mehran")
# myCar.drive()
# myCar.stop()
# myCar.display()
# print(myCar.color)



#Encapsulation

# class Car:
#     def __init__(self, speed, name, color):
#         self.__speed = speed  # private
#         self.name = name      # public
#         self._color=color     #protected

#     def get_speed(self):
#         return self.__speed

#     def set_speed(self, value):
#         self.__speed = value

#     def display(self):
#         print(f"{self.name} has speed {self.__speed} which color is {self._color}")


# myCar = Car(120, "Toyota","orange")

# print(myCar.name)        # ✅ public, works
# print(myCar.get_speed()) # ✅ private via getter
# # print(myCar.__speed)   # ❌ private, will fail
# print(myCar._Car__speed) # it will works but not recommended
# print(myCar._color)      #this will print but not recoomended 
# myCar.display()          # ✅ works



#Inheritance

# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Bike(Vehicle):  # Bike inherits Vehicle
#     def wheelie(self):
#         print("Bike is doing a wheelie")

# b = Bike()
# b.start()   # Vehicle started
# b.wheelie() # Bike is doing a wheelie


# class Engine:
#     def start(self):
#         print("Engine starts")
#     def display(self):
#         print("conflict function 1")

# class Radio:
#     def play_music(self):
#         print("Playing music 🎵")
    
#     def display(self):
#         print("conflict function 2")

# class Car(Engine, Radio):
#     def drive(self):
#         print("Car is driving 🚗")

# c = Car()
# c.start()       # from Engine
# c.play_music()  # from Radio
# c.drive()       # Car's own

# c.display()

# print(Car.__mro__)


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()

# d = D()
# d.show()
# print(D.__mro__)
# print(B.__mro__)
# print(C.__mro__)
# print(A.__mro__)


# -----------------------
# ##Polymorphism
# -----------------------

## We can achive polymorphism by diferent ways


# 1 Method Overriding (Inheritance Polymorphism / Runtime Polymorphism)
# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     def speak(self):  # overrides parent method
#         print("Dog barks")

# a = Animal()
# d = Dog()

# a.speak()  # Animal sound
# d.speak()  # Dog barks


#2 Duck Typing (Polymorphism without inheritance)
# Simply Create a function that can call the other class method by passing class as arguments
# class Cat:
#     def speak(self):
#         print("Meow!")

# class Dog:
#     def speak(self):
#         print("Woof!")

# def make_sound(animal):
#     animal.speak()  # works as long as 'speak' exists

# make_sound(Cat())  # Meow!
# make_sound(Dog())  # Woof!



#3 Operator Overloading (Polymorphism with Operators)
# same operators work diferently using dunder method
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(1,2)
# p2 = Point(3,4)
# print(p1 + p2)  # (4, 6)
# print(1+3,2+4)

#4 Function/Method Overloading (Simulated)
# we cannot do function overloading directly in python so we used same func it will overwrite or else we can achive using defalt arguments, **kwargs
# class Calculator:
#     def add(self, a, b=0, c=0):  # default values simulate overloading
#         return a + b + c

# calc = Calculator()
# print(calc.add(2,3))    # 5
# print(calc.add(2,3,4))  # 9


#5 Abstract Base Classes / Interfaces (Formal Polymorphism)
# This is abs and abstr decorators are way to create abstract func 
# The same func area can implement using child classes 

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r ** 2

# class Square(Shape):
#     def __init__(self, s):
#         self.s = s
#     def area(self):
#         return self.s ** 2

# shapes = [Circle(5), Square(4)]
# for s in shapes:
#     print(s.area())





