def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country('santiago','chile')
city_country('amsterdam','netherlands')
city_country('hanover','germany')

def make_album(album_name, album_artist):
    album = { 'nomalbum': album_name, 'artistealbum': album_artist }
    return album

creation = True
while creation:
    print("Rentrez le nom de l'album puis l'artiste:")
    stop="Si vous ne voulez plus rentrer d'album, tapez 'quit' pour une des deux valeurs."
    valeur1=input()
    valeur2=input()
    if valeur1 == 'quit' or valeur2 == 'quit':
        creation = False
        print("Merci d'avoir rentré les informations.")
    else: 
        album = make_album(valeur1, valeur2)
        print(album)