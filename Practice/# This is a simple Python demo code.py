# This is a simple Python demo code

def greet(name):
    """
    Function to greet a user by name.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    Function to add two numbers.
    """
    return a + b

if __name__ == "__main__":
    # Greet the user
    name = input("Enter your name: ")
    print(greet(name))

    # Add two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {add_numbers(num1, num2)}.")