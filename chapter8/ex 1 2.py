def display_message():
    """Afficher un message."""
    print("J'apprends les fonctions en Python.")

print(display_message())

# ex 2
def favorite_book(livre):
    """Afficher le livre préféré de quelqu'un."""
    print(f"Ton livre préféré est {livre.title()}.")

favorite_book('gatsby le magnifique')