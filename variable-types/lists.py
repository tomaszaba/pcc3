# ==============================================================================
#               Getting acquainted with lists in Python
#
#         What lists area and how to start with the elements in a list
# ==============================================================================

## --- Accessing elements in a list --------------------------------------------

names = ["Carlos", "André", "John", "Doe"]
print(f"My friend's name is {names[1].upper()}")

### Modifying it (replace through its index ----
names[0] = "Don Carlos"

### Adding elements to a list ----
names.append("Don Júlio")

### Insert elements into a list ----
names.insert(0, "Don Tomé")

### Remove using del: useful if I know the position ----
del names[-1]

### Remove using pop() method and let use the poped element ----
names.pop()
names.pop(0)

### Remove item by value ----
names.remove("André")

## ---- Looping over a list ----------------------------------------------------

for name in names:
    print(f"Hey there! My name is {name}")
print("Very nice to meet you all")

### Slicing the list ----
for name in names[ :2]:
    print(name)