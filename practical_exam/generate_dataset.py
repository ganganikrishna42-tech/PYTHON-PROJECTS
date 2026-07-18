"""
generate_dataset.py
--------------------
Generates a realistic synthetic dataset: library_transactions.csv
This simulates an e-library's book borrowing transaction log.

Columns:
    Transaction ID, Date, User ID, Book Title, Genre, Borrowing Duration (Days)

Note: A small amount of intentional messiness (missing values, duplicate
rows) is injected so the dashboard's data-cleaning logic has something
real to demonstrate.
"""

import random
import csv
from datetime import datetime, timedelta

random.seed(42)

# ---- Reference data pools -------------------------------------------------

BOOKS_BY_GENRE = {
    "Fiction": [
        "The Silent Orchard", "Whispers of the Tide", "A Thousand Quiet Rooms",
        "The Cartographer's Daughter", "Midnight in Avalon"
    ],
    "Science Fiction": [
        "Echoes of Andromeda", "The Last Colony Ship", "Neon Horizon",
        "Quantum Drift", "Beyond the Event Horizon"
    ],
    "Mystery": [
        "The Vanishing Hour", "Case of the Broken Compass", "Shadows on Elm Street",
        "The Locked Library", "Detective Rao's Final Case"
    ],
    "Fantasy": [
        "The Dragon's Ledger", "Kingdom of Ash and Ember", "The Sorcerer's Apprentice",
        "Crown of Thorned Vines", "The Last Rune Keeper"
    ],
    "Biography": [
        "An Ordinary Genius", "Life in the Margins", "The Long Road Home",
        "Notes from a Quiet Life", "Rising: A Memoir"
    ],
    "Self-Help": [
        "Atomic Focus", "The Discipline of Small Wins", "Rewire Your Mornings",
        "The Art of Deep Rest", "Habits That Stick"
    ],
    "History": [
        "Empires of Sand", "The Forgotten Treaty", "Revolutions of the Mind",
        "A Century of Silence", "The Merchant Kingdoms"
    ],
}

ALL_BOOKS = [(title, genre) for genre, titles in BOOKS_BY_GENRE.items() for title in titles]

# Skew popularity so some books are borrowed far more often than others
BOOK_WEIGHTS = [random.uniform(0.5, 5.0) for _ in ALL_BOOKS]

NUM_USERS = 120
NUM_TRANSACTIONS = 1500
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

def random_date():
    delta_days = (END_DATE - START_DATE).days
    d = START_DATE + timedelta(days=random.randint(0, delta_days))
    return d

def random_duration():
    # Most loans 3-21 days, occasional long overdue outliers
    if random.random() < 0.05:
        return random.randint(30, 60)
    return int(max(1, random.gauss(12, 6)))

rows = []
for i in range(1, NUM_TRANSACTIONS + 1):
    title, genre = random.choices(ALL_BOOKS, weights=BOOK_WEIGHTS, k=1)[0]
    user_id = f"U{random.randint(1, NUM_USERS):04d}"
    date = random_date().strftime("%Y-%m-%d")
    duration = random_duration()

    rows.append({
        "Transaction ID": f"T{i:05d}",
        "Date": date,
        "User ID": user_id,
        "Book Title": title,
        "Genre": genre,
        "Borrowing Duration (Days)": duration
    })

# ---- Inject realistic messiness --------------------------------------------

# 1. Missing values (~2% of rows have a blank field)
for _ in range(int(NUM_TRANSACTIONS * 0.02)):
    row = random.choice(rows)
    field = random.choice(["Book Title", "Genre", "Borrowing Duration (Days)", "Date"])
    row[field] = ""

# 2. Duplicate rows (~1.5% duplicated)
duplicates = [dict(r) for r in random.sample(rows, int(NUM_TRANSACTIONS * 0.015))]
rows.extend(duplicates)

# 3. A few inconsistent/invalid duration entries (negative or non-numeric-looking)
for _ in range(5):
    row = random.choice(rows)
    row["Borrowing Duration (Days)"] = random.choice([-3, "N/A", ""])

random.shuffle(rows)

# ---- Write CSV --------------------------------------------------------------

fieldnames = ["Transaction ID", "Date", "User ID", "Book Title", "Genre", "Borrowing Duration (Days)"]
with open("library_transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated library_transactions.csv with {len(rows)} rows (including injected messiness).")
