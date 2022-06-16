guests = ['guest1' , 'guest2' , 'guest3']
print(f"Bonjour {guests[0]}, je t'invite à manger")
print(f"Bonjour {guests[1]}, je t'invite à manger")
print(f"Malheureusement {guests[2]} ne pourra pas venir")

guests[2]='guest4'
for i in guests:
    print(f"Bonjour {i}, je t'invite à manger")
print(f"Bonne nouvelle, j'ai trouvé une table plus grande.")

guests.insert(0, 'guest5')
guests.insert(2, 'guest6')
guests.append('guest7')
for i in guests:
    print(f"Bonjour {i}, je t'invite à manger")
print(f"Vous êtes {len(guests)} invités.")
print("Oups, je ne pourrai inviter que deux personnes.")

x = 6
for x in range(1,5):
    print(f"Désolé {guests[-1]}, je ne pourrai pas t'inviter.")
    guests.pop()
    x = x-1

for i in guests:
    print(f"Bonjour {i}, tu es toujours invité à manger")

del guests[1]
del guests[0]
print(guests)