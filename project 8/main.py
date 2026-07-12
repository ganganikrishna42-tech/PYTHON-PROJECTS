import numpy as np
from data_analytics import DataAnalytics

current_data = None


def print_header():
    print("Welcome to the NumPy Analyzer!")
    print("=" * 40)


def main_menu():
    print("Choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    return input("Enter your choice: ").strip()


def create_array():
    global current_data
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        size = int(input("Enter the number of elements: "))
        values = list(map(int, input(f"Enter {size} elements for the array separated by space: ").split()))
        arr = np.array(values)

    elif choice == "2":
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        total = rows * cols
        values = list(map(int, input(f"Enter {total} elements for the array separated by space: ").split()))
        arr = np.array(values).reshape(rows, cols)

    elif choice == "3":
        depth = int(input("Enter the depth: "))
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        total = depth * rows * cols
        values = list(map(int, input(f"Enter {total} elements for the array separated by space: ").split()))
        arr = np.array(values).reshape(depth, rows, cols)

    else:
        print("Invalid choice, returning to main menu.")
        return

    current_data = DataAnalytics(arr)
    print("\nArray created successfully:")
    print(current_data.array)

    array_submenu()


def array_submenu():
    while True:
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            idx = input("Enter the index (comma separated for multi-dim, e.g. 0,1): ")
            index = tuple(int(i) for i in idx.split(",")) if "," in idx else int(idx)
            print(f"\nElement at index {idx}: {current_data.get_element(index)}")

        elif choice == "2":
            if current_data.array.ndim == 1:
                row_range = tuple(map(int, input("Enter the range (start:end): ").split(":")))
                result = current_data.get_slice(row_range)
            else:
                row_range = tuple(map(int, input("Enter the row range (start:end): ").split(":")))
                col_range = tuple(map(int, input("Enter the column range (start:end): ").split(":")))
                result = current_data.get_slice(row_range, col_range)
            print("\nSliced Array:")
            print(result)

        elif choice == "3":
            return

        else:
            print("Invalid choice, please try again.")


def math_operations():
    if current_data is None:
        print("\nNo array created yet. Please create one first.")
        return

    print("\nChoose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Dot Product")
    print("6. Matrix Multiplication")
    choice = input("Enter your choice: ").strip()

    size = current_data.array.size
    shape = current_data.array.shape

    if choice in ("1", "2", "3", "4"):
        values = list(map(float, input(f"Enter the same-size array elements ({size} elements separated by space): ").split()))
        other = np.array(values).reshape(shape)

        print("\nOriginal Array:")
        print(current_data.array)
        print("\nSecond Array:")
        print(other)

        if choice == "1":
            result = current_data.add(other)
            label = "Addition"
        elif choice == "2":
            result = current_data.subtract(other)
            label = "Subtraction"
        elif choice == "3":
            result = current_data.multiply(other)
            label = "Multiplication"
        else:
            result = current_data.divide(other)
            label = "Division"

        print(f"\nResult of {label}:")
        print(result)

    elif choice == "5":
        values = list(map(float, input("Enter the second array elements separated by space: ").split()))
        cols = shape[-1]
        other = np.array(values).reshape(cols, -1)
        print("\nDot Product:")
        print(current_data.dot_product(other))

    elif choice == "6":
        values = list(map(float, input("Enter the second array elements separated by space: ").split()))
        cols = shape[-1]
        other = np.array(values).reshape(cols, -1)
        print("\nMatrix Multiplication Result:")
        print(current_data.matrix_multiply(other))

    else:
        print("Invalid choice, please try again.")


def combine_split_menu():
    if current_data is None:
        print("\nNo array created yet. Please create one first.")
        return

    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        size = current_data.array.size
        values = list(map(int, input(f"Enter the elements of another array to combine ({size} elements separated by space): ").split()))
        other = np.array(values).reshape(current_data.array.shape)

        print("\nOriginal Array:")
        print(current_data.array)
        print("\nSecond Array:")
        print(other)

        combined = current_data.combine(other)
        print("\nCombined Array (Vertical Stack):")
        print(combined)

    elif choice == "2":
        sections = int(input("Enter the number of sections to split into: "))
        print("\nOriginal Array:")
        print(current_data.array)
        try:
            parts = current_data.split(sections)
            print("\nSplit Arrays:")
            for i, part in enumerate(parts):
                print(f"Part {i + 1}:")
                print(part)
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice, please try again.")


def search_sort_filter_menu():
    if current_data is None:
        print("\nNo array created yet. Please create one first.")
        return

    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")
    choice = input("Enter your choice: ").strip()

    print("\nOriginal Array:")
    print(current_data.array)

    if choice == "1":
        value = float(input("Enter the value to search for: "))
        result = current_data.search(value)
        print(f"\nIndices where {value} was found:")
        print(result)

    elif choice == "2":
        order = input("Sort in ascending or descending order? (a/d): ").strip().lower()
        result = current_data.sort(ascending=(order != "d"))
        print("\nSorted Array:")
        print(result)
        print("(Sorting applied row-wise.)")

    elif choice == "3":
        condition_str = input("Enter a condition using 'x' (e.g. x > 20): ")
        condition = eval(f"lambda x: {condition_str}")
        result = current_data.filter(condition)
        print("\nFiltered Array:")
        print(result)

    else:
        print("Invalid choice, please try again.")


def aggregates_menu():
    if current_data is None:
        print("\nNo array created yet. Please create one first.")
        return

    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")
    print("6. Minimum")
    print("7. Maximum")
    print("8. Percentile")
    print("9. Correlation with another array")
    choice = input("Enter your choice: ").strip()

    print("\nOriginal Array:")
    print(current_data.array)

    if choice == "1":
        print(f"\nSum of Array: {current_data.sum()}")
    elif choice == "2":
        print(f"\nMean of Array: {current_data.mean()}")
    elif choice == "3":
        print(f"\nMedian of Array: {current_data.median()}")
    elif choice == "4":
        print(f"\nStandard Deviation of Array: {current_data.std_dev()}")
    elif choice == "5":
        print(f"\nVariance of Array: {current_data.variance()}")
    elif choice == "6":
        print(f"\nMinimum value: {current_data.minimum()}")
    elif choice == "7":
        print(f"\nMaximum value: {current_data.maximum()}")
    elif choice == "8":
        q = float(input("Enter the percentile to calculate (0-100): "))
        print(f"\n{q}th Percentile: {current_data.percentile(q)}")
    elif choice == "9":
        size = current_data.array.size
        values = list(map(float, input(f"Enter {size} elements for the second array: ").split()))
        other = np.array(values)
        print(f"\nCorrelation Coefficient: {current_data.correlation(other)}")
    else:
        print("Invalid choice, please try again.")


def run():
    print_header()
    while True:
        choice = main_menu()

        if choice == "1":
            create_array()
        elif choice == "2":
            math_operations()
        elif choice == "3":
            combine_split_menu()
        elif choice == "4":
            search_sort_filter_menu()
        elif choice == "5":
            aggregates_menu()
        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    run()
