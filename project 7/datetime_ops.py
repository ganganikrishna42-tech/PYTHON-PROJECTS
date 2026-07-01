import datetime
import time


def show_current_datetime():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def date_difference():
    first = input("Enter the first date (YYYY-MM-DD): ")
    second = input("Enter the second date (YYYY-MM-DD): ")
    d1 = datetime.datetime.strptime(first, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(second, "%Y-%m-%d")
    gap = abs((d2 - d1).days)
    print(f"Difference: {gap} days")


def custom_format_date():
    raw = input("Enter a date (YYYY-MM-DD): ")
    pattern = input("Enter desired format (e.g. %d/%m/%Y): ")
    parsed = datetime.datetime.strptime(raw, "%Y-%m-%d")
    print(f"Formatted Date: {parsed.strftime(pattern)}")


def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter again to stop the stopwatch...")
    end = time.time()
    elapsed = end - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")


def countdown_timer():
    seconds = int(input("Enter countdown duration (in seconds): "))
    while seconds > 0:
        print(seconds, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")


def run_datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        pick = input("Enter your choice: ")

        if pick == "1":
            show_current_datetime()
        elif pick == "2":
            date_difference()
        elif pick == "3":
            custom_format_date()
        elif pick == "4":
            stopwatch()
        elif pick == "5":
            countdown_timer()
        elif pick == "6":
            break
        else:
            print("Invalid selection, try again.")
        print("=" * 27)


if __name__ == "__main__":
    run_datetime_menu()
