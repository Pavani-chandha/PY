class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            return a / b
calc = Calculator()
print("Addition (10 + 5):", calc.add(10, 5))
print("Subtraction (10 - 5):", calc.subtract(10, 5))
print("Multiplication (10 * 5):", calc.multiply(10, 5))
print("Division (10 / 5):", calc.divide(10, 5))
print("Division (10 / 0):", calc.divide(10, 0))
