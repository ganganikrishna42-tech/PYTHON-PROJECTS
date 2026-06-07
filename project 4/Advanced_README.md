# 🚀 Data Analyzer & Transformer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

<p align="center">
  <b>A Menu-Driven Python Application for Data Analysis, Transformation, and Statistical Computation</b>
</p>

---

# 📖 Table of Contents

- Overview
- Features
- Learning Outcomes
- Tech Stack
- Project Architecture
- Getting Started
- Usage Guide
- Function Documentation
- Docstrings & Code Documentation
- Sample Output
- Testing
- Future Enhancements
- Contributing
- License

---

# 🎯 Overview

Data Analyzer & Transformer is an interactive command-line application that allows users to create, analyze, and transform both 1D and 2D numerical datasets.

The project demonstrates core Python programming concepts including:

- Recursion
- List Comprehensions
- Lambda Functions
- Pattern Matching (`match-case`)
- Statistical Analysis
- User-Defined Functions
- Dynamic Documentation

---

# ✨ Features

## Dataset Management

✅ Create custom 1D lists

✅ Create custom 2D lists

✅ Use predefined sample datasets

✅ Display dataset summaries

## Data Analysis

📊 Mean Calculation

📈 Median Calculation

📉 Mode Calculation

📋 Dataset Statistics

## Data Transformation

🔍 Threshold-Based Filtering

🔢 Factorial Computation

📑 Sorting Operations

## Programming Concepts Demonstrated

- Recursive Functions
- Nested Lists
- Lambda Expressions
- List Comprehensions
- Pattern Matching
- Dynamic Variables
- Function Documentation

---

# 🎓 Learning Outcomes

This project helps learners understand:

| Concept | Demonstrated |
|----------|-------------|
| Functions | ✅ |
| Recursion | ✅ |
| Statistics | ✅ |
| Data Structures | ✅ |
| Lists & Nested Lists | ✅ |
| Lambda Functions | ✅ |
| Pattern Matching | ✅ |
| Docstrings | ✅ |
| Menu-Driven Programs | ✅ |

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core Language |
| Built-in Functions | Data Processing |
| Match-Case | Menu Navigation |
| Lambda Functions | Filtering |
| Recursion | Factorial Calculation |

No third-party dependencies are required.

---

# 🏗 Project Architecture

```text
┌──────────────────────┐
│      Main Menu       │
└──────────┬───────────┘
           │
           ▼
 ┌─────────────────────┐
 │ Dataset Selection   │
 └──────────┬──────────┘
            │
            ▼
 ┌─────────────────────┐
 │ Data Operations     │
 ├─────────────────────┤
 │ Summary             │
 │ Factorial           │
 │ Filtering           │
 │ Sorting             │
 │ Statistics          │
 └─────────────────────┘
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.10 or later
- Terminal / Command Prompt
- Optional Virtual Environment

## Installation

```bash
git clone https://github.com/your-username/data-analyzer-transformer.git

cd data-analyzer-transformer

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

Run the program:

```bash
python project4.py
```

---

# ▶ Usage Guide

## Main Menu

```text
1. Input data
2. Display data summary
3. Calculate factorial of the list
4. Filter data by threshold
5. Sort data
6. Display dataset statistics
7. Exit Program
```

## Example Workflow

```python
Input Dataset:
[10, 20, 30, 40, 50]

Summary:
Elements: 5
Minimum: 10
Maximum: 50
Average: 30.0

Statistics:
Mean: 30.0
Median: 30
Mode: 10
```

---

# 📚 Function Documentation

## factorial(n)

Recursively calculates the factorial of a number.

```python
def factorial(n):
    '''Calculate the factorial of a number n recursively.'''
```

Example:

```python
factorial(5)
# 120
```

### Complexity

| Metric | Value |
|---------|--------|
| Time | O(n) |
| Space | O(n) |

---

## mean_median_mode(data)

Returns multiple statistical values.

```python
def mean_median_mode(data):
    '''Calculate the mean, median, and mode of a list of numbers.'''
```

Returns:

```python
mean, median, mode
```

---

# 📝 Docstrings & Code Documentation

The project contains documented functions using Python docstrings.

### Function-Level Docstrings

```python
'''Calculate the factorial of a number n recursively.'''
```

```python
'''Calculate the mean, median, and mode of a list of numbers.'''
```

### Dynamic Documentation

The program also modifies the special `__doc__` variable during execution:

```python
__doc__ = "Predefined 1D list with 10 elements"
__doc__ = "User-defined 1D list"
__doc__ = "Predefined 2D list"
__doc__ = "User-defined 2D list"
```

This demonstrates how Python documentation metadata can be updated dynamically.

---

# 📸 Sample Output

```text
Welcome to the Data Analyzer and Transformer Program

1. Input data
2. Display data summary
3. Calculate factorial
4. Filter data
5. Sort data
6. Statistics
7. Exit

Please select an option:
```

---

# 🧪 Testing

Run tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov
```

---

# 🔮 Future Enhancements

- CSV Import/Export
- Data Visualization
- Pandas Integration
- Error Handling
- Input Validation
- GUI Version (Tkinter)
- Logging System
- Dataset Persistence

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push updates
5. Open a Pull Request

---

# 📄 License

Licensed under the MIT License.

---

# ⭐ Support

If you found this project helpful:

- Star the repository
- Share with fellow developers
- Submit feature requests
- Contribute improvements

Happy Coding! 🚀
