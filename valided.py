m = "Mississippi"

compteurs = {char: 0 for char in set(m)} 

for lettre in m:
    if lettre in compteurs:
        compteurs[lettre] += 1

for char in sorted(compteurs):  # Parcours des clés triées du dictionnaire
    print(f"Le nombre de '{char}' dans la chaîne est : {compteurs[char]}")
