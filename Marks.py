class Marks:
    def __init__(self,marks):
        self.__math_marks=0
        self.set_marks(marks)
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__math_marks = marks
    def get_marks(self):
        print(self.__math_marks)
m=Marks(marks=100)
print(m.get_marks())
m.set_marks(85)
print(m.get_marks())
