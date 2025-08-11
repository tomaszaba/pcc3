# ==============================================================================
#               Getting acquainted with Strings in Python
# ==============================================================================

## ---- Create a dictionary ----------------------------------------------------

hana = {
    "nationality": "lander",
    "Sex": "female",
    "age": "26",
    "first_name": "Hana",
    "last_name": "Kasim",
    "city": "Hargeisa"
}

### Loop over ----
for iv, i in hana.items():
    print(f"\nKey: {iv}")
    print(f"\tValue: {i}")

for val in hana.values():
    print(f"{val}")

for val in sorted(hana.values()):
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
dics = [hana, rivers_in_moz]