import random
import string


def generate_random_number():
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))
    print(f"Random Number: {random.randint(low, high)}")


def generate_random_list():
    size = int(input("Enter list size: "))
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))
    values = [random.randint(low, high) for _ in range(size)]
    print(f"Random List: {values}")


def create_random_password():
    length = int(input("Enter password length: "))
    pool = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(pool) for _ in range(length))
    print(f"Generated Password: {password}")


def generate_random_otp():
    otp = "".join(random.choice(string.digits) for _ in range(6))
    print(f"Generated OTP: {otp}")


def run_random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        pick = input("Enter your choice: ")

        if pick == "1":
            generate_random_number()
        elif pick == "2":
            generate_random_list()
        elif pick == "3":
            create_random_password()
        elif pick == "4":
            generate_random_otp()
        elif pick == "5":
            break
        else:
            print("Invalid selection, try again.")
        print("=" * 27)


if __name__ == "__main__":
    run_random_menu()
