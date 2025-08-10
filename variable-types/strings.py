# ==============================================================================
#               Getting acquainted with Strings in Python
# ==============================================================================

## ---- Changing case in a string with Methods ---------------------------------

text = "my name is tomas zaba"
text.title()
text.lower()
text.upper()
text.capitalize() # Capitalise the first letter

## ---- Using variables in strings ---------------------------------------------

text1 = "Tomás"
text2 = "Niquisse"
full_name = f"{text1} {text2}"
message = f"Hello people, I go by {full_name.title()}"

## ---- Adding whitespaces to strings with tabs or newlines --------------------

### Whitespace: non-printing character - spaces, tabs, and end-of-line symbols.

### Add a tab (indentation) ----
print(f"\t{full_name}")
print("Indented names:" f"\t{text1} \t{text2}")

### Add a new line ----
print("Names:" f"\n{text1} \n{text2}")

### Tabs and new lines in a single string ----
print("Names:" f"\t{text1} \n{text2}")

### Stripping whitespace ----
new_language = "python "
new_language.rstrip()
new_language2 = "  python"
new_language2.lstrip()

## ---- Removing prefixes ------------------------------------------------------

tx = "Dr. John Doe"
tx.removeprefix("Dr.").lstrip()
tx.removesuffix("Doe").rstrip()
tx.swapcase()

## ---- Exercises --------------------------------------------------------------

### Exercise 2.3 ----
person_name = "Musdafa"
message = f"Hello {person_name}, \nwould you like to learn some Python today"

### Exercise 2.4 ----
author = "Tobler"
quote = "'Everything is related to everything, but closer things are more related than distant things'."
quote_author = f"{author} once said: {quote.lower()}"

### Exercise 2.5 ----
print(f"{author}: \t{quote}")
print(f"{author} once said: \n{quote}")
