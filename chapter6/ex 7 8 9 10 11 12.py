# ex 7
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721


personne1 = {'first_name': 'Michel','last_name': 'Hernandez', 'city': 'Lyon'}
personne2 = {'first_name': 'Michelle','last_name': 'Hernandez', 'city': 'Lyon'}
personne3 = {'first_name': 'Miguel','last_name': 'Hernandez', 'city': 'Lyon'}

personnes = [personne1, personne2, personne3]
for personne in personnes:
    print(personne)

# ex 8

anim1 = {'espece': 'chat1','owner': 'owner1'}
anim2 = {'espece': 'chat2','owner': 'owner2'}
anim3 = {'espece': 'chat3','owner': 'owner3'}
anims = [anim1, anim2, anim3]
for anim in anims:
    print(anim)

# ex 9
endroits = {'individu1': 'vosges','individu2':'jura','individu3':'alpes'}
for name, lieux in endroits.items():
    print(f"\n L'endroit préféré de {name.title()} est:")
    print(f"\t{lieux.title()}")

# ex 10
couleurs = {
    'michel':['bleu','saphir'],
    'truc': ['rouge','cramoisi'],
    'machin': ['vert','sapin'],
    'bidule': ['jaune','moutarde'],
    'mec': ['violet','magenta'],
    }
for i in couleurs:
    print(f"La couleur préférée de {i.title()} est {couleurs[i]}")
