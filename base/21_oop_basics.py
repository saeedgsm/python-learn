# کلاس‌ها، اشیا، متدها و وراثت

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, I am {self.name}"

class Student(Person):
    def __init__(self, name: str, age: int, sid: str):
        super().__init__(name, age)
        self.sid = sid

    def info(self) -> str:
        return f"{self.name} ({self.sid})"

p = Person("Ali", 30)
s = Student("Sara", 21, "S1001")
print(p.greet())
print(s.greet())
print(s.info())


"""
class 
oop -> object oriented programming
-> attributes  صفات یا ویژگی ها
-> methods   روش ها یا توابع


"""
# from playsound import playsound

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def drive(self):
#         print(f"Driving {self.make} {self.model} {self.year}")
#     def horn(self):
#         playsound('/assets/')
#         print("Horn")

    
