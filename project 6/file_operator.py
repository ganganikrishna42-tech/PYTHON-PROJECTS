import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry_text = input("Enter your journal entry: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            file = open(self.filename, "a")
            file.write("[" + timestamp + "]\n")
            file.write(entry_text + "\n\n")
            file.close()
            print("Entry added successfully!")
        except PermissionError:
            print("You do not have permission to write to this file.")
        except Exception as e:
            print("Something went wrong while adding the entry:", e)

    def view_entries(self):
        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()
            if content == "":
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("Your Journal Entries:")
                print("-----------------------------------------------------------")
                print(content)
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except PermissionError:
            print("You do not have permission to read this file.")
        except Exception as e:
            print("Something went wrong while viewing entries:", e)

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")
        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()
            entries = content.strip().split("\n\n")
            matches = []
            for entry in entries:
                if keyword in entry:
                    matches.append(entry)
            if len(matches) == 0:
                print("No entries were found for the keyword: " + keyword)
            else:
                print("Matching Entries:")
                print("-----------------------------------------------------")
                for match in matches:
                    print(match)
             
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except Exception as e:
            print("Something went wrong while searching entries:", e)

    def delete_entries(self):

        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm == "yes":
            try:
                file = open(self.filename, "w")
                file.close()
                print("All journal entries have been deleted.")
            except FileNotFoundError:
                print("No journal entries found to delete.")
            except PermissionError:
                print("You do not have permission to delete this file.")
            except Exception as e:
                print("Something went wrong while deleting entries:", e)
        else:
            print("Delete cancelled.")


def print_menu():
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")


def main():
    manager = JournalManager("journal.txt")
    while True:
        print_menu()
        choice = input("enter choice: ")

        match choice:
            case "1":
                manager.add_entry()
            case "2":
                manager.view_entries()
            case "3":
                manager.search_entry()
            case "4":
                manager.delete_entries()
            case "5":
                print("thank yoo for using the file operator ,Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()