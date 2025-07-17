#Employee Management System whit Hierarchy class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 12

    def introduce(self):
        return f"{super().introduce()} I work with employee ID {self.employee_id}."

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
    
    def calculate_paycheck(self):
        return super().calculate_paycheck() + super().calculate_paycheck()*0.2

    def manage_team(self):
        return f"Managing the {self.department} department."

class Engineer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language
    
    def code(self):
        return f"Coding in {self.programming_language}."

class TechnicalManager(Manager, Engineer):
    def __init__(self, name, age, employee_id, salary, department, programming_language):
        Employee.__init__(self, name, age, employee_id, salary)
        self.department = department
        self.programming_language = programming_language


def show_hierarchy(cls):
    print(f"Class Hierarchy for {cls.__name__}:")
    print(f"  {cls.__name__}")
    for base in cls.__mro__:
        print(f"  {base.__name__}")


# Test your implementation - DO NOT MODIFY THIS TEST CODE
# Create instances
person = Person("John Smith", 30)
employee = Employee("Alice Johnson", 35, "E12345", 60000)
manager = Manager("Bob Williams", 45, "M54321", 85000, "Marketing")
engineer = Engineer("Carol Davis", 28, "E98765", 75000, "Python")
tech_mgr = TechnicalManager("Dave Wilson", 40, "TM24680", 90000, "R&D", "Java")

# Test basic methods
print(person.introduce())
print(employee.introduce())
print(f"Monthly pay: ${employee.calculate_paycheck():.2f}")
print(manager.manage_team())
print(engineer.code())

# Test inheritance hierarchies
print("\nHierarchy demonstrations:")
show_hierarchy(TechnicalManager)

# Test method resolution in multiple inheritance
print("\nTechnical Manager tests:")
print(tech_mgr.introduce())
print(f"Monthly pay: ${tech_mgr.calculate_paycheck():.2f}")
print(tech_mgr.manage_team())
print(tech_mgr.code())
