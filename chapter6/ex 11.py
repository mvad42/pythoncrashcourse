# ex 11
villes = {
    'saint-etienne': {
        'pays':'france',
        'habitants':'170 000',
        'fait':"s'appelait armeville"
        },
    'roanne': {
        'pays':'france',
        'habitants':'35 000',
        'fait':"j'y suis né"
        },
    'firminy': {
        'pays':'france',
        'habitants':'17 000',
        'fait':'ville la plus moche du monde'
        },
    }
for ville, ville_infos in villes.items():
    print(f"\nVille : {ville}")
    pays = ville_infos['pays']
    habitants = ville_infos['habitants']
    fait = ville_infos['fait']
    print(f"\tPays: {pays}")
    print(f"\tHabitants: {habitants}")
    print(f"\tFait: {fait}")
