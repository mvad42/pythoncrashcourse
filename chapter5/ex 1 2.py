objet = 'bidule'
print("V/F")
print(objet == 'bidule')

jetob = 'dulebi'
print("V/F")
print(jetob == 'dulbi')

print("\ntitle/lower:")
print(jetob.title() == 'dulebi')
print(objet.title() == 'bidule')
print(jetob.lower() == 'dulebi')
print(objet.lower() == 'bidule')

print("\nnombres:")
print(6==6)
print(6<7)
print(7<6)

# listes
print("\nlistes:")
nombres=[]
for i in range(1,21):
    nombres.append(i)
x=21
print('x' in nombres)
y=20
print('y' in nombres)
print(x>20 or y>21)
print(x>20 and y>21)