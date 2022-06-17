# ex 8 et 9
print("ex 8 et 9:")

usernames=['admin','jean','michel','truc','bidule']
if usernames:
    for username in usernames:
        if username=='admin':
            print(f"message spécial {username}")
        else:
            print(f"message normal {username}")
else: 
    print("liste d'utilisateurs vide\n")
print("\n")
# ex 10

current_users=['user1','user2','user3','user4','user5']
new_users=['user3','uSer1','user6','user7','user8']
for new_user in new_users:
    if new_user.lower() not in current_users:
        print("nom d'utilisateur disponible")
    elif new_user.lower() in current_users:
        print("Nom d'utilisateur indisponible")

# ex 11
print("\n")

ordinaux=[]
for i in range(1,10):
    ordinaux.append(i)
print(ordinaux)
for i in ordinaux:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")