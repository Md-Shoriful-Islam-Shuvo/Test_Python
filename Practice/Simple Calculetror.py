#Simple Calculetror
class Calculator:
    result = 0
    def add(self, number):
        self.result += number
        return self.result
    def subtract(self, number):
        self.result -= number
        return self.result
    def multiply(self, number):
        self.result *= number
        return self.result  
    def divide(self, number):
        if number == 0:
            raise ValueError("Error: Division by zero")
        self.result /= number
        return self.result
    def clear(self):
        self.result = 0
        return self.result
    def get_result(self):
        return self.result
    
#Example usage
number= input("Enter a number: ")
calc = Calculator()
calc.result = float(number)
i=1
while i!=0:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Get Result")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        number = float(input("Enter a number to add: "))
        result = calc.add(number)
        print(f"Result: {result}")
    elif choice == 2:
        number = float(input("Enter a number to subtract: "))
        result = calc.subtract(number)
        print(f"Result: {result}")
    elif choice == 3:
        number = float(input("Enter a number to multiply: "))
        result = calc.multiply(number)
        print(f"Result: {result}")
    elif choice == 4:
        number = float(input("Enter a number to divide: "))
        try:
            result = calc.divide(number)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)
    elif choice == 5:
        result = calc.clear()
        print(f"Calculator cleared. Result: {result}")
    elif choice == 6:
        result = calc.get_result()
        print(f"Current Result: {result}")
    elif choice == 7:
        break
    else:
        print("Invalid choice, please try again.")
    i = int(input("Enter 1 to continue or 0 to exit: "))