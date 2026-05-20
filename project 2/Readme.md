# Pattern Generator and Number Analyzer

## Overview
This Python project is a simple command-line application that allows users to:

1. Generate different star (`*`) patterns
2. Analyze numbers within a given range

The program runs continuously in a loop until the user chooses to exit.

---

## Features

### Pattern Generator
Users can generate:
- Right Triangle Pattern
- Left Triangle Pattern
- Pyramid Pattern

### Number Analyzer
The program:
- Identifies whether numbers in a range are even or odd
- Calculates the sum of numbers within the selected range

---

## Requirements

- Python 3.x

---

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run the program using:

```bash
python project_2.py
```

---

## Menu Options

### Main Menu
```text
1. Generate a pattern
2. Analyze a number
3. Exit
```

---

## Pattern Options

### Right Triangle
Example:
```text
*
**
***
****
```

### Left Triangle
Example:
```text
   *
  **
 ***
****
```

### Pyramid
Example:
```text
   *
  ***
 *****
*******
```

---

## Number Analyzer Example

Input:
```text
Start: 1
End: 5
```

Output:
```text
1 is an odd number.
2 is an even number.
3 is an odd number.
4 is an even number.
5 is an odd number.
```

---

## File Structure

```text
project_2.py   # Main Python program
README.md      # Project documentation
```

---

## Notes

- The program uses loops and conditional statements extensively.
- Input validation is limited, so users should enter valid numeric values.
- The sum calculation logic may need improvement for accuracy in all cases.

---

## Author

Created for learning Python basics including:
- Loops
- Conditional statements
- User input
- Pattern printing
- Number analysis
