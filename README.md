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

# My Python Learning Portfolio

A solid collection of scripts demonstrating my daily coding progress as I prepare for a Junior Python Developer career in the US and target my dream job at Apple.

## Project 1: Advanced Loop & List Showcase (Walmart Edition)

A clean script showcasing automated loop structures and data filtering using standard English naming conventions.

### Features
- **Collection Iteration**: Uses a `for` loop to seamlessly iterate through a dynamic list (`walmart_shelf`) without manual counters.
- **Data Filtering**: Implements conditional `if/else` checks to detect specific items (like `"Creamy Coconut"`) and flag them as `"out of stock"`.
- **Automated Ranges**: Utilizes the `range(3)` generator to automatically repeat actions exactly 3 times without risk of infinite loops.

### Code Preview
```python
walmart_shelf = ["Grape", "Cream-Soda", "Creamy Coconut", "Strawberries-Cream"]

for soda in walmart_shelf:
    if soda == "Creamy Coconut":
        print("out of stock")
    else:
        print(soda)

for i in range(3):
    print("Took a delicious sip of Strawberries & Cream while watching DangerLyoha")
```

---

## Project 2: Interactive Wallet & Balance Manager

A clean script designed to simulate financial transactions, multiplier events, and budget deductions. This code demonstrates variable overriding and fundamental arithmetic operations in Python.

### Features
- **Variable Overriding**: Modifies the same variable (`my_balance`) over multiple steps to track state changes.
- **Arithmetic Logic**: Implements multiplication (`*`) for double-balance events and subtraction (`-`) for purchase tracking.
- **Console Feedback**: Uses sequence-based `print()` logs to output step-by-step wallet balance changes.
