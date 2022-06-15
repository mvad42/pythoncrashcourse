# Chapitre 2
# 15/06/2022

msg="Blabla, blablabla, blablabla"
print(msg)

nom="michel hernandez"
print(nom.title())
print(nom.upper())
print(nom.lower())

citation='Qui sème le vent récolte la tempête'
print(f"\t{nom.title()} a dit: '{citation}'")

citation='Qui sème le vent récolte la tempête'
truc=f"{nom.title()} a dit:\n '{citation}'"
print(truc)

nom2=" michel hernandez "
print(nom2.strip())