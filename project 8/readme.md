<div align="center">

# -- ! NumPy Analyzer ! --
### *Interactive Console-Based NumPy Array Creation & Analysis Toolkit*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Design-Object%20Oriented-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"An array is just numbers until you know how to ask it questions."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Part A — The `DataAnalytics` Class](#-part-a--the-dataanalytics-class)
- [🖥️ Part B — The Interactive Menu (`main.py`)](#️-part-b--the-interactive-menu-mainpy)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [⚠️ Known Limitations](#️-known-limitations)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **NumPy Analyzer** is a menu-driven Python console application that wraps common **NumPy array operations** behind a friendly, interactive command-line interface. It separates concerns cleanly into two files:

- `data_analytics.py` — a `DataAnalytics` class that encapsulates array creation, indexing, arithmetic, statistics, and more.
- `main.py` — a text-based menu system that drives the class, collects user input, and prints results.

This project is designed to:
- Demonstrate **object-oriented design** applied to a numerical computing library
- Practice building **menu-driven CLI programs** with nested submenus
- Wrap NumPy's array creation, math, and statistics functions behind simple prompts
- Provide a hands-on sandbox for exploring 1D, 2D, and 3D array behavior

---

## 🎯 Problem Statement

> **Objective:** Build a console-based tool that lets a user create NumPy arrays of any dimension and interactively explore operations on them — without writing a single line of code.

The program should let a user:
1. Create a 1D, 2D, or 3D array from typed-in values
2. Index and slice that array
3. Run element-wise math against a second array
4. Combine or split arrays
5. Search, sort, and filter values
6. Compute aggregate statistics (sum, mean, median, std dev, variance, percentile, correlation)

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Array Creation | Input Handling | Builds 1D/2D/3D arrays from user-entered values |
| Indexing & Slicing | Access | Retrieve single elements or sub-ranges |
| Math Operations | Arithmetic | Element-wise add/subtract/multiply/divide, dot & matrix product |
| Combine/Split | Restructuring | Concatenate or `array_split` an array |
| Search/Sort/Filter | Analysis | Locate values, sort, or filter by condition |
| Aggregates & Stats | Statistics | Sum, mean, median, std dev, variance, min/max, percentile, correlation |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Persistent Menu Loop** | Main menu runs until the user selects Exit |
| 🧊 **1D / 2D / 3D Array Support** | Create arrays of any of the three dimensionalities |
| 🎯 **Indexing & Slicing Submenu** | Dedicated submenu for exploring a created array |
| ➕ **Full Arithmetic Suite** | Add, subtract, multiply, divide, dot product, matrix multiplication |
| 🔗 **Combine & Split** | Concatenate two arrays or split one into sections |
| 🔍 **Search, Sort & Filter** | Find values, sort ascending/descending, filter with a custom condition |
| 📊 **Statistics Suite** | Sum, mean, median, std dev, variance, min, max, percentile, correlation |
| 🧩 **Class-Based Design** | All array logic lives in a reusable `DataAnalytics` class |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 main.py               ← Entry point — menu system & user interaction
├── 📄 data_analytics.py     ← DataAnalytics class — core NumPy operations
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│      Display Main Menu      │  ← 1-6 options
└────────────┬────────────────┘
             │
   ┌────┬────┼────┬────┬────┐
   ▼    ▼    ▼    ▼    ▼    ▼
  Create Math Combine Search Stats Exit
  Array  Ops   /Split /Sort/  Menu   ✅
   │           Filter
   ▼
┌──────────────────┐
│ Choose 1D/2D/3D   │
│ Enter values      │
└────────┬──────────┘
         ▼
┌──────────────────┐
│ Indexing/Slicing  │
│ Submenu           │
└────────┬──────────┘
         │
         ▼
   Loop Back to Menu
```

---

## 🧱 Part A — The `DataAnalytics` Class

### 📝 1. What It Does

`DataAnalytics` (in `data_analytics.py`) wraps a single NumPy array and exposes a set of methods for working with it, so `main.py` never has to call `numpy` functions directly.

```python
class DataAnalytics:
    def __init__(self, array=None):
        self.array = array
```

### 🗺️ 2. Method Overview

| Category | Methods | Notes |
|----------|---------|-------|
| **Construction** | `from_input(dimensions, shape, values)` | Class method — builds an array from a flat list and target shape |
| **Access** | `get_element(index)`, `get_slice(row_range, col_range)` | Handles both 1D and N-D access |
| **Restructuring** | `combine(other, axis)`, `split(sections, axis)` | Uses `np.concatenate` / `np.array_split` |
| **Arithmetic** | `add`, `subtract`, `multiply`, `divide` | Validated with `_validate_same_shape` before running |
| **Linear Algebra** | `dot_product(other)`, `matrix_multiply(other)` | Wraps `np.dot` / `np.matmul` |
| **Search/Sort/Filter** | `search(value)`, `sort(ascending)`, `filter(condition)` | `filter` accepts any callable condition |
| **Statistics** | `sum`, `mean`, `median`, `std_dev`, `variance`, `minimum`, `maximum`, `percentile(q)`, `correlation(other)` | Thin wrappers around NumPy's aggregate functions |
| **Display** | `__repr__` | Pretty-prints the wrapped array |

### 🔺 3. Example: Shape Validation Before Arithmetic

```python
@staticmethod
def _validate_same_shape(arr1, arr2):
    if arr1.shape != arr2.shape:
        raise ValueError("Arrays must be the same shape for this operation.")

def add(self, other):
    self._validate_same_shape(self.array, other)
    return self.array + other
```

Every element-wise operation (`add`, `subtract`, `multiply`, `divide`) checks shape compatibility first and raises a clear `ValueError` if the arrays don't match.

---

## 🖥️ Part B — The Interactive Menu (`main.py`)

### 🔍 4. Main Menu

```
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

### 🔢 5. Array Creation Flow

The user first picks a dimensionality, then types the shape and flat values, which are reshaped into a NumPy array:

```python
elif choice == "2":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    total = rows * cols
    values = list(map(int, input(f"Enter {total} elements ...").split()))
    arr = np.array(values).reshape(rows, cols)
```

Immediately after creation, the user is dropped into an **Indexing & Slicing submenu** to explore the new array.

**Sample interaction (2D array):**
```
Enter the number of rows: 2
Enter the number of columns: 3
Enter 6 elements for the array separated by space: 1 2 3 4 5 6

Array created successfully:
[[1 2 3]
 [4 5 6]]
```

### 🧮 6. Key Concepts Used

| Concept | Detail |
|---------|--------|
| 🧊 `reshape(shape)` | Converts flat user input into N-dimensional arrays |
| 🎯 Tuple Indexing | Comma-separated input parsed into multi-dimensional index tuples |
| ➗ Shape Validation | Arithmetic operations reject mismatched shapes with a clear error |
| 🧠 `eval()` for Filters | Custom filter conditions (e.g. `x > 20`) are compiled into lambdas at runtime |
| 📊 NumPy Aggregates | Sum, mean, median, std dev, variance, percentile, correlation via one-line calls |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🔢 **NumPy** | Latest | Array creation, reshaping, math, and statistics |
| 🧩 **Classes & Class Methods** | Built-in | Encapsulates array logic in `DataAnalytics` |
| 🔁 **While Loop** | Built-in | Persistent main menu control |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |
| 📐 **f-strings** | Python 3.6+ | Formatted console output |

---

## 🚀 Getting Started

```bash
# 1. Install the only dependency
pip install numpy

# 2. Run the analyzer
python main.py
```

---

## ⚠️ Known Limitations

| Limitation | Detail |
|------------|--------|
| 🧪 **`eval()` in Filters** | The filter submenu uses `eval()` to build conditions from raw input — only run this on trusted input |
| 🔢 **No Input Validation on Counts** | Entering the wrong number of elements for a given shape will raise a `ValueError` from `reshape` |
| 📐 **Dot/Matrix Product Shape Guessing** | `main.py` infers the second array's shape as `(cols, -1)`, which assumes compatible dimensions |
| 🧮 **Sort is Row-Wise** | `sort()` sorts along the last axis, so multi-dimensional arrays are sorted per-row, not flattened |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Great for Learning NumPy** | Exposes core array operations without writing any code |
| 🧩 **Clean Separation of Concerns** | Logic (`DataAnalytics`) is fully decoupled from I/O (`main.py`) |
| 🔄 **Reusable Class** | `DataAnalytics` can be imported and used outside the CLI entirely |
| 🖥️ **No Extra Dependencies** | Only requires NumPy — no other third-party packages |
| 🧪 **Extensible** | Easy to add new statistical or array methods to the class |
| 🛡️ **Guarded Arithmetic** | Shape mismatches are caught early with descriptive errors |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 🙏 Acknowledgements

Special thanks to the following resources that made this project possible:

- 📚 [NumPy Official Documentation](https://numpy.org/doc/stable/) — Reference for array operations and statistics functions
- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🖥️ [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp) — Beginner-friendly NumPy reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with 🐍 and NumPy*

</div>
