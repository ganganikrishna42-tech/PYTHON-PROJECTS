from custom_modules import make_file, write_file, read_file, append_file


def handle_create():
    filename = input("Enter file name: ")
    print(make_file(filename))


def handle_write():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    print(write_file(filename, data))


def handle_read():
    filename = input("Enter file name: ")
    print("File Content:")
    print(read_file(filename))


def handle_append():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    print(append_file(filename, data))


def run_file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        pick = input("Enter your choice: ")

        if pick == "1":
            handle_create()
        elif pick == "2":
            handle_write()
        elif pick == "3":
            handle_read()
        elif pick == "4":
            handle_append()
        elif pick == "5":
            break
        else:
            print("Invalid selection, try again.")
        print("=" * 27)


if __name__ == "__main__":
    run_file_menu()
