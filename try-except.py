# ==============================================================================
#                                   Chapter 10                        
#                              Files and Exceptions
# ==============================================================================

## ---- Exercise 10-6 ----------------------------------------------------------

### A simple programme that requests user's input for processing ----
while True:
    try:
        value = int(input("Kindly tell us your age: "))
    except ValueError:
        print("Sorry, that is not a number. Please try again")
    else: 
        x = value * 4
        print(f"You are {x}")
        break

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
