class Employee:
    def __init__(self):
        self.__name=""
        self.__salary=1.0
        self.__age=0
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_salary(self,salary):
        if salary >0.0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0")
    def get_salary(self):
        return self.__salary
    def set_age(self,age):
        if 18<=age<=100:
            self.__age=age
        else:
            print("Error: Age should be between 18 and 100")
    def get_age(self):
        return self.__age
m=Employee()
m.set_name("John Doe")
m.set_salary(50000.0)
m.set_age(30)
print("Employee Name : ",m.get_name())
print("Employee Marks : ",m.get_salary())
print("Employee age : ",m.get_age())
m.set_salary(150)
print("Error: Salary must be greater than 0.")





