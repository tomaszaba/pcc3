# ==============================================================================
#               Getting acquainted with Strings in Python
# ==============================================================================

## ---- Create a dictionary ----------------------------------------------------

person = {
    "nationality": "Moz",
    "Sex": "female",
    "age": "16",
    "first_name": "John",
    "last_name": "Doe",
    "city": "Molocue"
}

### Loop over ----
for iv, i in person.items():
    print(f"\nKey: {iv}")
    print(f"\tValue: {i}")

for val in person.values():
    print(f"{val}")

for val in sorted(person.values()):
    print(val)

## ---- Exercise ---------------------------------------------------------------
rivers_in_moz = {
    "limpopo": "South Africa",
    "Zambeze": "mozambique",
    "lake malawi": "Malawi"
}

for river, country in rivers_in_moz.items():
    print(f"The river {river.title()} is located in {country.title()}")

### Exercise 6.5 - print each river ----
for river in rivers_in_moz.keys():
    print(river.title())

for country in rivers_in_moz.values():
    print(country.title()) 

## ---- List of dictionaries ---------------------------------------------------
dics = [person, rivers_in_moz]