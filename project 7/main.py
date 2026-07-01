from datetime_ops import run_datetime_menu
from math_ops import run_math_menu
from random_ops import run_random_menu
from uuid_ops import run_uuid_menu
from file_menu import run_file_menu
from explore_ops import run_explore_menu


def show_main_menu():
    print("=" * 27)
    print("Welcome to Multi-Utility Toolkit")
    print("=" * 27)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 27)


def main():
    while True:
        show_main_menu()
        pick = input("Enter your choice: ")

        if pick == "1":
            run_datetime_menu()
        elif pick == "2":
            run_math_menu()
        elif pick == "3":
            run_random_menu()
        elif pick == "4":
            run_uuid_menu()
        elif pick == "5":
            run_file_menu()
        elif pick == "6":
            run_explore_menu()
        elif pick == "7":
            print("Thank you for using the toolkit. Goodbye!")
            break
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    main()
