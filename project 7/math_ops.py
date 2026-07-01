import math


def calculate_factorial():
    num = int(input("Enter a number: "))
    print(f"Factorial: {math.factorial(num)}")


def compound_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (in %): "))
    years = float(input("Enter time (in years): "))
    amount = principal * math.pow((1 + rate / 100), years)
    print(f"Compound Interest: {amount:.2f}")


def trig_calculations():
    angle = float(input("Enter an angle (in degrees): "))
    radians = math.radians(angle)
    print(f"sin: {math.sin(radians):.4f}")
    print(f"cos: {math.cos(radians):.4f}")
    print(f"tan: {math.tan(radians):.4f}")


def shape_area():
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    shape = input("Choose a shape: ")

    if shape == "1":
        radius = float(input("Enter radius: "))
        print(f"Area: {math.pi * radius ** 2:.2f}")
    elif shape == "2":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        print(f"Area: {length * breadth:.2f}")
    elif shape == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area: {0.5 * base * height:.2f}")
    else:
        print("Invalid shape selection.")


def run_math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        pick = input("Enter your choice: ")

        if pick == "1":
            calculate_factorial()
        elif pick == "2":
            compound_interest()
        elif pick == "3":
            trig_calculations()
        elif pick == "4":
            shape_area()
        elif pick == "5":
            break
        else:
            print("Invalid selection, try again.")
        print("=" * 27)


if __name__ == "__main__":
    run_math_menu()
