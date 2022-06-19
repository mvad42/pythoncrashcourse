def make_sandwich(*ingredients):
    print("Il y a dans ce sandwich:")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

make_sandwich('tomate')
make_sandwich('tomate','salami')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Vadim', 'X',
                            location='sainté',
                            field='fieldent')
print(user_profile)

def make_car(marque, couleur, **user_info):
    user_info['marque'] = marque
    user_info['couleur'] = couleur
    return user_info

car = make_car('bmw','noire',type='berline',fuel='diesel')
print(car)