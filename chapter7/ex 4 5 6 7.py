# ex 4
start = "Bienvenue à la pizzeria."
start2 = "Que voulez-vous sur votre pizza? Entrez 'quit' pour quitter."

print(start)
while True :
    topping = input(start2)
    if topping == 'quit':
        print(f"Au revoir.")
        break
    else:
        print(f"Nous ajoutons {topping} à votre pizza.")

# ex 5
start = "Bienvenue au cinéma."
start2 = "Quel âge avez-vous?"
print(start)
age =  int(input(start2))
if age < 3 :
    print("Ticket gratuit.")
elif age < 12:
    print("10 euros")
elif age < 18:
    print("15 euros")

# ex 7
while True:
    print(input())