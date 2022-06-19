def make_shirt(shirt_size='L', shirt_text='I love Python'):
    """faire un t-shirt"""
    print(f"\nTaille du t-shirt : {shirt_size}")
    print(f"Imprimé du t-shirt : {shirt_text}")

make_shirt()
make_shirt(shirt_size='M')
make_shirt(shirt_size='L', shirt_text='2')

def describe_city(name, country):
    """Afficher le nom d'une ville et son pays"""
    print(f"\n{name} se situe en {country}.")

describe_city(name='villea', country='paysa')
describe_city(name='villeb', country='paysa')
describe_city(name='villec', country='paysb')
