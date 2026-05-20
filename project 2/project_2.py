while True:


    print("Welcome to the Pattern Generator and Number Analyzer!!")

    print("\nSelect an option from the menu below:")
    print("1. Generate a pattern")
    print("2. Analyze a number")
    print("3. Exit")

    option = int(input("\nEnter your choice (1, 2, or 3): "))

    if option == 1:

        print("\nYou have selected to generate a pattern.")
        print("select the pattern you want to generate:")
        print("1. Right Triangle")
        print("2. Left Triangle")
        print("3. Pyramid")
        

        pattern_option = int(input("Enter your choice (1, 2, or 3): "))
        rows = int(input("Enter the number of rows for the pattern: "))

        if pattern_option == 1:
            print("\nGenerating a Right Triangle pattern:")
            for i in range(1, rows + 1):
                print("*" * i)
        elif pattern_option == 2:
            print("\nGenerating a Left Triangle pattern:")
            for i in range(1, rows + 1):
                print(" " * (rows - i) + "*" * i)
        elif pattern_option == 3:
            print("\nGenerating a Pyramid pattern:")
            for i in range(1, rows + 1):
                print(" " * (rows - i) + "*" * (2 * i - 1)) 
        else:
            print("\nInvalid pattern choice. Please enter 1, 2, or 3.")        
    elif option == 2:

        print("\nYou have selected to analyze a number.")
        start = int(input("Enter the start number of range: "))
        end = int(input("Enter the end number of range: "))
        print(f"\nAnalyzing numbers from {start} to {end}:")
        for n in range(start, end + 1):
            if n % 2 == 0:
                print(f"{n} is an even number.")
            else:
                print(f"{n} is an odd number.")
        print("the sum of the numbers for this range is :",start/2*(start+end))

    elif option == 3:
        print("\nThank you for using the Pattern Generator and Number Analyzer!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")