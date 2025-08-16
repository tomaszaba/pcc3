# ==============================================================================
#                                   Chapter 10                        
#                              Files and Exceptions
# ==============================================================================

## ---- Exercise 10-6 ----------------------------------------------------------

### A simple programme that requests user's input for processing ----
def ask_for_number(prompt):
    """Keep asking until user provides a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Sorry, that's not a number. Please try again 💪")

# Use the helper function
print("Hello, welcome to `mwana` library website.")

age = ask_for_number("👉 Kindly tell us your age: ")
work_years = ask_for_number("👉 How many years of work experience do you have? ")

print(f"\n✅ Thanks! You entered: Age = {age}, Work years = {work_years}")

### Handle errors silently ----
try:
    value = int(input("Age: "))
except ValueError:
    pass
else:
    try:
        value / 0
    except ZeroDivisionError:
        print("Sorry")

## ---- Exercise 10-8 ----------------------------------------------------------

### Manage FileNotFound error ----
from pathlib import Path

try: 
    path = Path("catx.txt")
    text = path.read_text().splitlines()
except:
    print("😄")
else:
    ## Count the approximate number of words in the file ----
    x = [len(line.split()) for line in text]

## ---- Exercise 10-10 ---------------------------------------------------------

### Count the number of times the word "IDP" appears per line ----
[line.count("IDP") for line in text]
