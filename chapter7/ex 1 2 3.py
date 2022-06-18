# ex 1
car=input("Quelle voiture aimeriez-vous louer?")
print(f"Laissez-moi voir si nous avons une {car}.")

# ex 2
personnes=input("Une table pour combien de personnes?")
personnes=int(personnes)
if personnes > 8:
    print("Vous devrez attendre pour une table.")
else:
    print("Nous avons une table de libre.")

# ex3
nbr=int(input("Choisissez un nombre."))
if nbr % 10 == 0 : 
    print("Multiple de 10.")
else:
    print("Votre nombre n'est pas multiple de 10.")