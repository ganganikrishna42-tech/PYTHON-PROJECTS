
emp_dic = {}

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
        print("Department  :", self.department)


while True:

    
    print(" Employee Management System:\n")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Show All Employees")
    print("4. Check Inheritence")
    print("5. Exit")

    choice = int(input("Enter your choice:"))
    match choice:
        case 1:

            name = input("Enter your Name: ")
            age = int(input("Enter the Age: "))
            salary = int(input("Enter the Salary: "))
            emp_id = input("Enter your Employee ID: ")

            emp = Employee(name, age, salary, emp_id)
            emp_dic[name] = emp

            print("\nEmploy Created Successfully!")
        case 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            emp_id = input("Enter Employ ID: ")
            dept = input("Enter Department: ")

            mgr = Manager(name, age, salary, emp_id, dept)
            emp_dic[name] = mgr

            print("\nManager Created Successfully!")
        case 3:
            if not emp_dic:
                print("\nNot  Records Found.")
            else:
                for obj in emp_dic.values():
                    obj.display()
        case 4:
            print("\nInheritance Check")
            print("Manager is subclass of Employ :", issubclass(Manager, Employee))       
        case 5:
            print("\nThank You for Using Employee Management System.")
            break

        