class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 arg")
        elif a and b:
            print("2 arg")
        elif a:
            print("1 arg")
        else:
            print("no arg")
a=Demo()
a.show()
a.show(1,2,3)
a.show(1,2)
a.show(1)