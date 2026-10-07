class Employee:
    def __init__(self,name,salary):
        print('execute attributes')
        self.name=name
        self.salary=salary

    def travel(self,destination):
        print('the travel class execution')
        self.destination=destination
        print(f"Employee is travelling {destination}")
emp=Employee("John",50000,)
print(emp.name)
print(emp.salary)
emp.travel('Knp')
