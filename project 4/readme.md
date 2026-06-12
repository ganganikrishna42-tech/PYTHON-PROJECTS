<div align="center">

# -- ! Data Analyzer & Transformer ! --
### *Interactive Console-Based Data Analysis, Statistics & Transformation Tool*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Lists](https://img.shields.io/badge/Lists-1D%20%26%202D%20Arrays-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Math](https://img.shields.io/badge/Math-Statistics%20%26%20Factorials-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Data is raw, information is structured — transform one into the other."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📥 Part A — Data Input](#-part-a--data-input)
- [📊 Part B — Data Analysis & Transformation](#-part-b--data-analysis--transformation)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Data Analyzer & Transformer** is a beginner-friendly, interactive Python console application that demonstrates core programming concepts such as **recursion**, **list comprehensions**, **lambda functions**, **higher-order functions**, and **statistical computation**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of 1D and 2D list manipulation
- Practice recursive function design with factorials
- Apply statistical logic to compute mean, median, and mode
- Demonstrate filtering, sorting, and summarizing data sets
- Use Python built-ins and user-defined functions together

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to input, analyze, filter, sort, and compute statistics on numeric datasets.

You are building a utility program for students learning Python data handling. The program must accept user choices from a menu and execute the corresponding task — ranging from data input and summary display to factorial calculation and statistical analysis.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Input | Console Input | Accepts 1D or 2D numeric lists (manual or predefined) |
| Data Summary | Analysis | Displays count, min, max, average, and sum |
| Factorial Calculator | Recursion | Computes factorial of each element using recursion |
| Threshold Filter | Transformation | Filters elements greater than a given threshold |
| Sorter | Transformation | Sorts 1D or row-wise 2D lists in ascending order |
| Statistics | Math | Calculates mean, median, and mode of the dataset |

The goal is to demonstrate **intermediate Python programming skills** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📋 **1D & 2D List Support** | All operations work on both flat and nested lists |
| 🔢 **Predefined Datasets** | Built-in sample lists for quick testing |
| 🔣 **Recursive Factorial** | User-defined recursive function for factorial computation |
| 📐 **Statistical Analysis** | Returns mean, median, and mode via a multi-return function |
| 🔽 **Threshold Filtering** | Uses `filter()` and lambda to extract values above a cutoff |
| 🗂️ **Sorting** | Sorts 1D lists or each row of a 2D list independently |
| ⚠️ **Input-Driven Flow** | Fully driven by `match-case` branching on user input |

---

## 🏗️ Project Structure

```
📦 data-analyzer-transformer/
│
├── 📄 project4.py          ← Main Python script (entry point)
│
└── 📄 README.md            ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Options 1–7
└────────────┬────────────────┘
             │
     ┌───────┼────────────────────┐
     ▼       ▼                    ▼
┌─────────┐ ┌──────────────┐  ┌───────────────┐
│Choice: 1│ │  Choice: 2–6 │  │  Choice: 7    │
│ (Input) │ │ (Operations) │  │   (Exit)      │
└────┬────┘ └──────┬───────┘  └───────────────┘
     │             │
     ▼             ▼
┌─────────────┐ ┌──────────────────────┐
│ 1D or 2D?   │ │ Analyze / Transform  │
│ Manual /    │ │ / Compute / Display  │
│ Predefined  │ └──────────┬───────────┘
└──────┬──────┘            │
       │                   ▼
       ▼        ┌──────────────────────┐
  Store in      │  Print Output to     │
  data / data2  │  Console             │
                └──────────────────────┘
                           │
                           ▼
                   Loop Back to Menu
                           │
                    (Choice: 7) Exit ✅
```

---

## 📥 Part A — Data Input

### 📝 1. What is the Data Input Module?

The input module allows users to populate a **1D list** or a **2D list** (matrix) either manually or from a predefined dataset. This data is then used by all subsequent menu operations.

---

### 🗺️ 2. Input Modes — Overview

| Mode | Type | Description |
|------|------|-------------|
| 1️⃣ | **1D List (Manual)** | User enters N elements one by one |
| 2️⃣ | **1D List (Predefined)** | Uses `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` |
| 3️⃣ | **2D List (Manual)** | User specifies rows × columns, enters each cell |
| 4️⃣ | **2D List (Predefined)** | Uses `[[1,2,3], [4,5,6], [7,8,9]]` |

---

### 🔢 3. 1D List Input

> User enters the number of elements and provides each value individually.

**Logic:**
```python
elements = int(input("Enter the number of elements in the 1D list:\n"))
data = [int(input(f"Enter element {i+1}: ")) for i in range(elements)]
```

**Sample Output:**
```
1D list created is: [3, 7, 2, 9, 5]
```

---

### 🔲 4. 2D List Input

> User specifies rows and columns; values are entered row by row using a nested list comprehension.

**Logic:**
```python
data2 = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
```

**Sample Output:**
```
2D list created is: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## 📊 Part B — Data Analysis & Transformation

### 🔍 5. Data Summary (Choice 2)

> Displays key statistics about the loaded dataset.

**Output for 1D list `[1..10]`:**
```
Number of elements: 10
Minimum value: 1
Maximum value: 10
Average value: 5.5
Sum of elements: 55
```

---

### ➗ 6. Factorial Calculator (Choice 3)

> Applies a user-defined recursive `factorial()` function to every element in the list.

**Logic:**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorials = [factorial(x) for x in data]
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔁 Recursion | Base case: `n == 0 or n == 1`; recursive case: `n * factorial(n-1)` |
| 📋 List Comprehension | Applied element-wise across the data list |
| 🔢 Nested Application | 2D lists use double list comprehension |

**Sample Output (data = `[1, 2, 3, 4, 5]`):**
```
Factorials of the 1D list: [1, 2, 6, 24, 120]
```

---

### 🔽 7. Threshold Filter (Choice 4)

> Retains only elements that exceed a user-specified threshold value.

**Logic:**
```python
threshold = int(input("Enter the threshold value: "))
filtered_data = list(filter(lambda x: x > threshold, data))
```

**Sample Output (threshold = 5, data = `[1..10]`):**
```
Filtered 1D list (values greater than 5): [6, 7, 8, 9, 10]
```

---

### 🗂️ 8. Sort Data (Choice 5)

> Sorts a 1D list in ascending order, or sorts each row of a 2D list individually.

**Logic:**
```python
sorted_data = sorted(data)                          # 1D
sorted_data_2d = [sorted(row) for row in data2]    # 2D
```

**Sample Output:**
```
Sorted 1D list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### 📐 9. Dataset Statistics (Choice 6)

> Computes mean, median, and mode using a user-defined multi-return function `mean_median_mode()`.

**Logic:**
```python
def mean_median_mode(data):
    mean = sum(data) / len(data)
    median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (
        sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2
    mode = max(set(data), key=data.count)
    return mean, median, mode
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ➗ Mean | Sum divided by count |
| 📊 Median | Middle value of sorted list; average of two midpoints if even length |
| 🔢 Mode | Most frequently occurring value using `max` + `key=data.count` |
| 📦 Multiple Return Values | Single function returns a tuple unpacked into three variables |

**Sample Output (data = `[1..10]`):**
```
Mean: 5.5, Median: 6, Mode: 1
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔂 **List Comprehension** | Built-in | Concise list construction and transformation |
| 🧮 **Arithmetic Operators** | Built-in | Sum, modulus, division for statistics |
| 🔣 **`filter()` + `lambda`** | Built-in | Functional-style threshold filtering |
| 📦 **`match-case`** | Python 3.10+ | Structural pattern matching for menu dispatch |
| 🖨️ **`print()` / `input()`** | Built-in | Console I/O and user interaction |
| 📐 **f-strings** | Python 3.6+ | Formatted string output |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Flexible Data Input** — Supports both 1D and 2D lists, manual or predefined
- 🔢 **Recursive Factorials** — Correctly computes factorials for any non-negative integer in the list
- 📊 **Full Statistics** — Accurate mean, median, and mode returned from a single function call
- 🔽 **Threshold Filtering** — Uses Python's functional `filter()` for clean element selection
- 🗂️ **Sorting** — Works element-wise for 1D and row-wise for 2D lists
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers recursion, list ops, and statistics in one project |
| 🔄 **Dual List Support** | All features handle both 1D and 2D data seamlessly |
| 📚 **Educational** | Each feature reinforces a distinct Python concept |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add new operations (standard deviation, matrix transpose, etc.) |
| 📖 **Readable Code** | Clean `match-case` and function separation makes logic easy to follow |
| 🛡️ **Predefined Fallback** | Built-in datasets let users test all features without manual input |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Gangani Krishna

[![GitHub](https://github.com/ganganikrishna42-tech/PYTHON-PROJECTS/tree/PYTHON-PROJECTS/project%204)](https://github.com/ganganikrishna42-tech)


> *"Every dataset has a story — write the code that tells it."*

**🎓 Role:Programming Enthusiast 
**📍 Location:** India\
**🛠️ Skills:** Python · Data Analysis 

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔁 [Real Python — Recursion](https://realpython.com/python-recursion/) — In-depth recursion tutorials
- 📐 [GeeksForGeeks — Statistics](https://www.geeksforgeeks.org/python-statistics-module/) — Statistical computation in Python
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 🧮 [Python f-strings Guide](https://realpython.com/python-f-strings/) — Formatted string literals
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 07 June, 2026*

</div>