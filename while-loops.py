# ==============================================================================
#                                   Chapter 7                        
#                           User input and while loops
# ==============================================================================

## ---- User input -------------------------------------------------------------

### Getting a user imput
message = input("Hei Hillow, what is your surname?")
print(f"Nice to meet you, {message}. Let's keep in touch")

### Long prompt messages ----
prompt = "Olá, bem vindo ao mundo Python 😎"
prompt += "\nComo te chamas? 🧐"
prompt += "Onde será que vives?"

name = input(prompt)
print(f"Prazer em conhecê-lo, {name}!")

### Getting numerical inputs ----
prompt2 = "Quantos anos tens?"
idade = input(prompt2)
print(idade)

## ---- While loops ------------------------------------------------------------

message = ""
while message != "quit":
    message = input(prompt2)
    print(message)

### Use a flag to stop a while loop ----
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

### Use a flag to stop a while loop ----
active = True
while active:
    message = input(prompt)

    if message == "quit":
        break
    else:
        print(message)

### Moving items from one list to another ----
unconfirmed_invitees = ["Tomás", "José", "Luis", "João"]
confirmed = []

while unconfirmed_invitees:
    for invitee in unconfirmed_invitees:
        check = input(f"Hey, {invitee}, Are you coming to the party?")
        if check == "yes":
            confirmed.append(invitee)
    break
print(f"All confirmed users: {confirmed}")

### Remove all instances of specific values from a list ----
pets = ["dogs", "cats", "goldfish", "rabbit", "cats", "cats", "dogs"]

while "cats" in pets: 
    pets.remove("cats")
print(pets)