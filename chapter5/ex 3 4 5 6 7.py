# ex 5-3

alien_color = 'blue'
if alien_color == 'blue':
    print("Vous avez gagné 5 points.")

# ex 5-4
print("\n ex 5-4:")

alien_color == 'blue'
if alien_color == 'blue':
    print("Vous avez gagné 5 points.")
else:
    print("Vous avez gagné 10 points.")
# fait pour le else:
alien_color == 'blue'
if alien_color == 'green':
    print("Vous avez gagné 5 points.")
else:
    print("Vous avez gagné 10 points.")

# ex 5-5
print("\n ex 5-5:")

alien_color='red'
if alien_color == 'green':
    points=5
elif alien_color == 'yellow':
    points=10
elif alien_color == 'red':
    points=15
print(f"Vous avez gagné {points} points.")

# ex 5-6
print("\n ex 5-6:")

age=int(input())
if age<2:
    print("bébé")
elif age<4:
    print("petit enfant")
elif age<13:
    print("enfant")
elif age<20:
    print("ado")
elif age<65:
    print("adulte")
elif age>=65:
    print("personne âgée")

# ex 5-7
print("\n ex 5-7:")

favorite_fruits=[1,2,3,4,5]
for i in range(1,20):
    if i in favorite_fruits:
        print(f"Tu aimes les {i}")
    else:
        print(f"Tu n'aimes pas les {i}")