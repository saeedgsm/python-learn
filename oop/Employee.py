class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def display(self):
        print(self.first, self.last, self.pay)

first = Employee('saeed','ghasemi',3000)
second = Employee('john','doe',7000)

first.display()
second.display()