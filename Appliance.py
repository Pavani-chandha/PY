from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
            pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is now ON.")
class Fridge(Appliance):
    def turn_on(self):
        print("Fridge is now ON.")
wm = WashingMachine()
wm.turn_on()
f = Fridge()
f.turn_on()
