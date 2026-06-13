emp_dic = {}
manager = {}
develop = {}


class Employee:

    def __init__(self, name="", age=0, salary=0, employee_id=""):
        self.name = name
        self.age = age
        self.__salary = salary
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID:", self.get_employee_id())
        print("Name :", self.name)
        print("Age:", self.age)
        print("Salary:", self.get_salary())


class Manager(Employee):

    def __init__(self, name, age, salary, employee_id, department):
        super().__init__(name, age, salary, employee_id)
        self.department = department

    def display(self):
        super().display()
        print("Department :", self.department)


class Developer(Manager):

    def __init__(self, name, age, salary, employee_id, department, language):
        super().__init__(name, age, salary, employee_id, department)
        self.language = language

    def display(self):
        super().display()
        print("Language :", self.language)


while True:

    print("\nEmployee Management System:\n")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show All Employees")
    print("5. Check Inheritance")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            emp_id = input("Enter Employee ID: ")

            emp = Employee(name, age, salary, emp_id)
            emp_dic[name] = emp

            print("\nEmployee Created Successfully!")

        case 2:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            emp_id = input("Enter Employee ID: ")
            dept = input("Enter Department: ")

            mgr = Manager(name, age, salary, emp_id, dept)
            manager[name] = mgr

            print("\nManager Created Successfully!")

        case 3:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            emp_id = input("Enter Employee ID: ")
            dept = input("Enter Department: ")
            lang = input("Enter Programming Language: ")

            dev = Developer(name, age, salary, emp_id, dept, lang)
            develop[name] = dev

            print("\nDeveloper Created Successfully!")

        case 4:

            if not emp_dic and not manager and not develop:
                print("\nNo Records Found.")
            else:
                for obj in emp_dic.values():
                    obj.display()

                for obj in manager.values():
                    obj.display()

                for obj in develop.values():
                    obj.display()

        case 5:

            print("\nInheritance Check")
            print("Manager is subclass of Employee :", issubclass(Manager, Employee))
            print("Developer is subclass of Employee :", issubclass(Developer, Employee))
            print("Developer is subclass of Manager :", issubclass(Developer, Manager))

        case 6:

            print("\nThank You for Using Employee Management System.")
            break

        case _:

            print("\nInvalid Choice.")