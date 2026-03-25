# 🐍 Python Beginner Level Tasks

A collection of beginner-level Python programming tasks covering core concepts such as variables, OOP, dictionaries, loops, and lists.

---

## 📁 Project Structure

```
Beginner Level/
│
├── Task 1 - Variables/
│   └── variables.py
│
├── Task 2 - Classes and Objects/
│   └── avengers.py
│
├── Task 3 - Dictionary/
│   └── dictionary.py
│
├── Task 4 - For Loop/
│   └── for_loop.py
│
├── Task 5 - List/
│   └── justice_league.py
│
└── README.md
```

---

## 📌 Task 1 — Variables

**File:** `variables.py`

### What it covers:
- Creating and storing variables
- Understanding data types using `type()`
- Python reserved keywords
- Simple arithmetic with variables

### Problems Solved:
| # | Task | Concept |
|---|------|---------|
| 1 | Store `22/7` in variable `pi` and check its data type | `float`, `type()` |
| 2 | Try to create a variable named `for` and understand the error | Reserved Keywords, `SyntaxError` |
| 3 | Calculate Simple Interest using `P`, `R`, `T` variables | Arithmetic operators |

### Formula Used:
```
Simple Interest = P × R × T / 100
```

### Key Concept — Reserved Keywords:
`for` is a Python keyword used in loops and **cannot** be used as a variable name.
Other reserved keywords: `if`, `while`, `class`, `return`, `True`, `False`, `break`, `import`, etc.

---

## 📌 Task 2 — Classes and Objects

**File:** `avengers.py`

### What it covers:
- Defining a `class` with `__init__()` constructor
- Creating multiple objects (instances)
- Instance variables vs class variables
- Defining and calling methods
- `is_leader()` method using conditional logic

### The Avengers Team:
| Hero | Super Power | Weapon | Leader? |
|------|-------------|--------|---------|
| Captain America | Super Strength | Shield | ✅ Yes |
| Iron Man | Technology | Armor | ❌ No |
| Black Widow | Superhuman Agility | Batons | ❌ No |
| Hulk | Unlimited Strength | No Weapon | ❌ No |
| Thor | Super Energy | Mjölnir | ❌ No |
| Hawkeye | Fighting Skills | Bow and Arrows | ❌ No |

### Class Properties:
```python
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        ...
    def get_info(self):      # Displays hero profile
        ...
    def is_leader(self):     # Returns True/False
        ...
```

---

## 📌 Task 3 — Dictionary

**File:** `dictionary.py`

### What it covers:
- Creating lists and lists of tuples
- List comprehension
- Creating and accessing dictionaries
- `sum()`, `max()`, `abs()` built-in functions
- Iterating over dictionary keys and values

### Problems Solved:

#### Part 1 — Friends List & Tuples:
- Create a list of 5+ friend names
- Generate list of tuples: `(name, len(name))`
- Example: `('Aditya', 6)`

#### Part 2 — Trip Expense Tracker:
| Category | Your Expenses | Partner's Expenses |
|----------|--------------|-------------------|
| Hotel | ₹1200 | ₹1000 |
| Food | ₹800 | ₹900 |
| Transportation | ₹500 | ₹600 |
| Attractions | ₹300 | ₹400 |
| Miscellaneous | ₹200 | ₹150 |

- Calculate total for each person
- Determine who spent more
- Find the category with the biggest spending difference

---

## 📌 Task 4 — For Loop

**File:** `for_loop.py`

### What it covers:
- `for` loop with `range()`
- `random` module — `random.randint()`
- `break` statement
- `input()` for user interaction
- String methods: `.strip()`, `.lower()`
- Counters and conditional logic

### Problems Solved:

#### Part 1 — Dice Rolling Simulator:
- Roll a 6-sided die 20 times using `random.randint(1, 6)`
- Track and print:
  - How many times **6** was rolled
  - How many times **1** was rolled
  - How many times **two 6s appeared in a row**

#### Part 2 — Jumping Jacks Workout:
- Loop through 10 sets of 10 jumping jacks (total = 100)
- After each set, ask: *"Are you tired?"*
  - `yes` → Ask to skip remaining sets
    - `yes` → Break and print total completed
    - `no`  → Continue workout
  - `no`  → Show remaining count and continue

```
Workout Flow:
Set 1 (10 jacks) → Tired? → yes → Skip? → yes → STOP
                                         → no  → Continue
                          → no  → Show remaining → Next Set
...
Set 10 (100 jacks) → Congratulations!
```

---

## 📌 Task 5 — List

**File:** `justice_league.py`

### What it covers:
- List creation, indexing, and length
- `.append()`, `.insert()`, `.remove()`, `.index()`, `.clear()`, `.sort()`
- Traversing lists with `enumerate()`
- Dynamic position calculation

### Starting List:
```python
justice_league = ["Superman", "Batman", "Wonder Woman",
                  "Flash", "Aquaman", "Green Lantern"]
```

### Operations Performed:
| Step | Operation | Method Used |
|------|-----------|-------------|
| 1 | Count total members | `len()` |
| 2 | Add Batgirl & Nightwing | `.append()` |
| 3 | Make Wonder Woman leader (move to index 0) | `.remove()` + `.insert(0, ...)` |
| 4 | Place Superman between Aquaman & Flash | `.index()` + `.remove()` + `.insert()` |
| 5 | Replace list with new team | `.clear()` + reassignment |
| 6 | Sort alphabetically | `.sort()` |

### 🏆 Bonus — New Leader After Sorting:
After replacing with: `["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]`
and sorting alphabetically:

```
[0] Cyborg          👑 NEW LEADER
[1] Green Arrow
[2] Hawkgirl
[3] Martian Manhunter
[4] Shazam
```
**Cyborg** becomes the new leader because **"C"** comes first alphabetically!

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required (only `random` from standard library)

---

## ▶️ How to Run

```bash
# Run any task file directly
python variables.py
python avengers.py
python dictionary.py
python for_loop.py
python justice_league.py
```

Or run from your IDE (Spyder, VS Code, PyCharm) using the Run button.

---

## 🧠 Concepts Covered

| Concept | Task |
|---------|------|
| Variables & Data Types | Task 1 |
| Reserved Keywords | Task 1 |
| Classes & Objects | Task 2 |
| Instance & Class Variables | Task 2 |
| Methods & Constructors | Task 2 |
| Lists & Tuples | Task 3 |
| Dictionaries | Task 3 |
| For Loops | Task 4 |
| Break Statement | Task 4 |
| Random Module | Task 4 |
| User Input Handling | Task 4 |
| List Methods | Task 5 |
| Sorting & Indexing | Task 5 |

---

## 👨‍💻 Author

**Rajveer**
Beginner Python Learning Journey 🚀

---
