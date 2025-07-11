class Employee:
    def work(self):
        print("Work")
class Manager(Employee):
    def manage(self):
        print("manage")
m=Manager()
m.work()
m.manage()