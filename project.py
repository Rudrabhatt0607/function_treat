# -------------------------------
# Employee Management System
# Demonstrates:
# Constructor
# Destructor
# Encapsulation
# Getter & Setter
# Inheritance
# Method Overriding
# Method Overloading
# super()
# issubclass()
# Menu Driven Program
# -------------------------------


class Employee:

    # Constructor Overloading using default arguments
    def __init__(self, employee_id=None, name=None, age=None, salary=0):

        self.__employee_id = employee_id    # private
        self.name = name
        self.age = age
        self.__salary = salary              # private

    # Destructor
    def __del__(self):
        print(f"Employee object {self.name} deleted.")

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):

        if salary >= 0:
            self.__salary = salary

        else:
            print("Salary cannot be negative")

    # Display Method
    def display(self):

        print("\n------ Employee Details ------")

        print("Employee ID :", self.__employee_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self.__salary)


# -------------------------------------
# Manager Class
# -------------------------------------

class Manager(Employee):

    def __init__(self,
                 employee_id,
                 name,
                 age,
                 salary,
                 department):

        super().__init__(
            employee_id,
            name,
            age,
            salary
        )

        self.department = department

    # Method Overriding
    def display(self):

        super().display()

        print("Department  :", self.department)


# -------------------------------------
# Developer Class
# -------------------------------------

class Developer(Employee):

    def __init__(self,
                 employee_id,
                 name,
                 age,
                 salary,
                 programming_language):

        super().__init__(
            employee_id,
            name,
            age,
            salary
        )

        self.programming_language = programming_language

    # Method Overriding
    def display(self):

        super().display()

        print("Language    :", self.programming_language)


# -------------------------------------
# Main Program
# -------------------------------------

employee = None
manager = None
developer = None

while True:

    print("\n")
    print("==== Employee Management System ====")

    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Employee Details")
    print("5. Show Manager Details")
    print("6. Show Developer Details")
    print("7. Check issubclass()")
    print("8. Exit")

    choice = int(input("\nEnter your choice : "))

    # --------------------------------
    # Create Employee
    # --------------------------------

    if choice == 1:

        emp_id = input("Enter Employee ID : ")

        name = input("Enter Name : ")

        age = int(input("Enter Age : "))

        salary = float(input("Enter Salary : "))

        employee = Employee(
            emp_id,
            name,
            age,
            salary
        )

        print("\nEmployee Created Successfully")


    # --------------------------------
    # Create Manager
    # --------------------------------

    elif choice == 2:

        emp_id = input("Enter Employee ID : ")

        name = input("Enter Name : ")

        age = int(input("Enter Age : "))

        salary = float(input("Enter Salary : "))

        department = input("Enter Department : ")

        manager = Manager(
            emp_id,
            name,
            age,
            salary,
            department
        )

        print("\nManager Created Successfully")


    # --------------------------------
    # Create Developer
    # --------------------------------

    elif choice == 3:

        emp_id = input("Enter Employee ID : ")

        name = input("Enter Name : ")

        age = int(input("Enter Age : "))

        salary = float(input("Enter Salary : "))

        language = input("Enter Programming Language : ")

        developer = Developer(
            emp_id,
            name,
            age,
            salary,
            language
        )

        print("\nDeveloper Created Successfully")


    # --------------------------------
    # Show Employee Details
    # --------------------------------

    elif choice == 4:

        if employee:

            employee.display()

        else:

            print("\nNo Employee Found")


    # --------------------------------
    # Show Manager Details
    # --------------------------------

    elif choice == 5:

        if manager:

            manager.display()

        else:

            print("\nNo Manager Found")


    # --------------------------------
    # Show Developer Details
    # --------------------------------

    elif choice == 6:

        if developer:

            developer.display()

        else:

            print("\nNo Developer Found")


    # --------------------------------
    # issubclass()
    # --------------------------------

    elif choice == 7:

        print()

        print(
            "Is Manager subclass of Employee ?",
            issubclass(Manager, Employee)
        )

        print(
            "Is Developer subclass of Employee ?",
            issubclass(Developer, Employee)
        )


    # --------------------------------
    # Exit
    # --------------------------------

    elif choice == 8:

        print("\nExiting Program...")
        break

    else:

        print("\nInvalid Choice")