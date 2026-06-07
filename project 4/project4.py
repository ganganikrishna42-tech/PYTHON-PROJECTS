
def factorial(n):
    '''Calculate the factorial of a number n recursively.'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

def mean_median_mode(data):
    '''Calculate the mean, median, and mode of a list of numbers.'''
    mean = sum(data) / len(data)
    median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2
    mode = max(set(data), key=data.count)
    return mean, median, mode    
    
    

data = []
data2 = [[]]
predefined_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
predefined_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
while True:

    print("----------------------------------------------------------------")
    print("\nWelcome to the Data analyzer and transformer program!\n")
    print("\nMain Menu:\n")
    print("1.Input data\n")#ask user to input data either as 1d or 2d list, and store it in a variable called data
    print("2.Display data summary\n")
    print("3.Calculate factorial of the list\n")
    print("4.Filter data by threshold\n")
    print("5.Sort data\n")
    print("6.Display dataset statistics(return multiple values)\n")
    print("7.Exit Program\n")
    
    choice = int(input("Please select an option (1-7):\n"))

    match choice:
        case 1:
            options = int(input("Please select the type of data you want to input:\n1.1D list\n2.2D list\n"))
            match options:
                case 1:
                    use_predefined = input("Do you want to use the predefined list of 10 elements? (yes/no): ").lower() == 'yes'
                    if use_predefined:
                        data = predefined_list1.copy()
                        print("\n\nPredefined list used is:", predefined_list1  )
                        __doc__ = "Predefined 1D list with 10 elements"
                    else:
                        elements = int(input("Enter the number of elements in the 1D list:\n"))
                        data = [int(input(f"Enter the element to be stored in list {i+1}: ")) for i in range(elements)]#enter data separated by space, and store it in a list called data
                        print("\n\n1D list created is:", data)
                        __doc__ = "User-defined 1D list"

                case 2:
                    use_predefined = input("Do you want to use the predefined 2D list? (yes/no): ").lower() == 'yes'
                    if use_predefined:
                        data2 = predefined_list2.copy()
                        print("\n\nPredefined 2D list used is:", predefined_list2)
                        __doc__ = "Predefined 2D list"
                    else:
                        rows = int(input("Enter the number of rows in the 2D list:\n"))
                        cols = int(input("Enter the number of columns in the 2D list:\n"))
                        data2 = [[int(input(f"Enter the element to be stored in list [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
                        __doc__ = "User-defined 2D list"
                        print("\n\n2D list created is:", data2)     
        case 2:
            if data:
                print("Data Summary for 1D list:")
                print(f"Number of elements: {len(data)}")
                print(f"Minimum value: {min(data)}")
                print(f"Maximum value: {max(data)}")
                print(f"Average value: {sum(data) / len(data)}")
                print(f"Sum of elements: {sum(data)}")
            elif data2:
                print("Data Summary for 2D list:")
                total_elements = sum(len(row) for row in data2)
                min_value = min(min(row) for row in data2)
                max_value = max(max(row) for row in data2)
                average_value = sum(sum(row) for row in data2) / total_elements
                print(f"Number of elements: {total_elements}")
                print(f"Minimum value: {min_value}")
                print(f"Maximum value: {max_value}")
                print(f"Average value: {average_value}")
                print(f"Sum of elements: {sum(sum(row) for row in data2)}")
            else:
                print("No data available. Please input data first.")
        case 3:#use user defined function to calculate factorial of the list, and display the result
                if data:
                    factorials = [factorial(x) for x in data]
                    print("Factorials of the 1D list:", factorials)
                elif data2:
                    factorials_2d = [[factorial(x) for x in row] for row in data2]
                    print("Factorials of the 2D list:", factorials_2d)
        case 4:
            threshold = int(input("Enter the threshold value to filter the data:\n"))
            if data:
                filtered_data = list(filter(lambda x: x > threshold, data))
                print(f"Filtered 1D list (values greater than {threshold}):", filtered_data)
            elif data2:
                filtered_data_2d = [[x for x in row if x > threshold] for row in data2]
                print(f"Filtered 2D list (values greater than {threshold}):", filtered_data_2d)
        case 5:
            if data:
                sorted_data = sorted(data)
                print("Sorted 1D list:", sorted_data)
            elif data2:
                sorted_data_2d = [sorted(row) for row in data2]
                print("Sorted 2D list:", sorted_data_2d)
        case 6:               
            if data:
                mean, median, mode = mean_median_mode(data)
                print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
            elif data2:
                flat_data = [x for row in data2 for x in row]
                mean, median, mode = mean_median_mode(flat_data)
                print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
            
        case 7:
            print("Thank you for using the Data analyzer and transformer program. Goodbye!")
            break
