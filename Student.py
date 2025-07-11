class Student:
    def __init__(self):
        self.__name=""
        self.__marks=0
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Error: Marks should be between 0 and 100")
    def get_marks(self):
        return self.__marks
m=Student()
m.set_name("Alice")
m.set_marks(85)
print("Student Name : ",m.get_name())
print("Student Marks : ",m.get_marks())
m.set_marks(150)
print("Student Marks (after invalid input):", m.get_marks())