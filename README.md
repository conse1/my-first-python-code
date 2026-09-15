# Simple Inventory Filter System (Python)

A beginner-friendly Python script designed to manage an inventory with a built-in verification check. This project is part of my daily coding routine as I prepare for a Junior Python Developer career in the US.

## Features
- **Loop Control**: Uses a `while` loop to manage a 3-step item entry system.
- **Dynamic Input**: Interactively requests item names from the user.
- **Data Validation & Anti-Scam Filter**: Implements an `if/else` condition to screen inputs. If an item matches `"dota"`, it flags it as a `"scam"` and blocks it from entering the storage.
- **List Management**: Safely appends verified items into the main inventory list (`lux_inventory`) and outputs the final collection.

## Code Preview
```python
lux_inventory = []
step = 0

while step < 3:
    item = input("Enter item name: ")
    if item == "dota":
        print("scam")
    else:
        lux_inventory.append(item)
        print("approved")
        
    step = step + 1

print(lux_inventory)
```

## Goals
- Mastering core Python logic (loops, lists, and conditions).
- Next step: Refactoring this project using `for` loops and `range()`.



---

## Project 2: Interactive Wallet & Balance Manager (Python)

A clean and simple script designed to simulate financial transactions, multiplier events, and budget deductions. This code demonstrates variable overriding and fundamental arithmetic operations in Python.

### Features
- **Variable Overriding**: Modifies the same variable (`my_balance`) over multiple steps to track state changes.
- **Arithmetic Logic**: Implements multiplication (`*`) for double-balance events and subtraction (`-`) for purchase tracking.
- **Console Feedback**: Uses sequence-based `print()` logs to output step-by-step wallet balance changes.

### Future Improvement
- Refactoring with compound assignment operators (`*= 2` and `-= 1500`) to match professional clean code practices.
