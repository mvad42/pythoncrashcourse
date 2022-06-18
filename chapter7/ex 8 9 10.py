# ex 8 et 9
sandwich_orders = ['thon','jambon-beurre','pastrami','pastrami','pastrami','épinards']
sandwich_faits = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"En train de faire {current_sandwich}")
    sandwich_faits.append(current_sandwich)

print("\n Ces sandwichs ont été faits:")
for i in sandwich_faits:
    print(f"\t{i}")

# ex 10

reponses={}
quest1="Comment vous appelez-vous?"
quest2="Quel endroit aimeriez-vous visiter?"
quest3="Quelqu'un d'autre aimerait-il répondre? (y/n)"
sondage=True
while sondage:
    name=input(quest1)
    reponse=input(quest2)
    reponses[name]=reponse
    suite=input(quest3)
    if suite == 'n':
        print("Merci de votre participation.")
        sondage=False

print("Résultats du sondage:\n")
for reponse in reponses:
    print(f"{reponse} aimerait visiter {reponses[name]}")