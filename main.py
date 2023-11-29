texte =""" 
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux
"""

#calcul du nombre du pronom "le"
def clean_text(text):
    text = text.replace("\n", " ")
    return text.split(" ")

my_text_cleaned = clean_text(texte)


mesPronoms = ['je',"tu", 'il', "nous", "vous", "ils"]

compteur = 0

# Parcourez le tableau de mots pour trouver "le"
for i in range(1, len(my_text_cleaned)):
    if my_text_cleaned[i] == "le" and  my_text_cleaned[i - 1].lower() in mesPronoms:
        compteur += 1

# Affichez le résultat
print("Le nombre 'le' est :", compteur)

#compter le nombre de e
nbr_e = texte.count("e")
print("le nombre de 'e' est :", nbr_e)

#retirer tous les "e"
texte_sans_e = texte.replace("e", " ")
#print(texte_sans_e)

import json

data ={ "nbr_pronom_le": compteur, "nbr_e":nbr_e}
path = "rapport.json" #D:/ESTIAM/python_expert/tp_cours/rapport.json
with open(path,'w') as file:
    json.dump(data, file)

import re
from collections import Counter
texte_sans_ponctuation = re.sub(r'[^\w\s]', '', texte)
text_list = texte_sans_ponctuation.split()
#print(text_list)
mots = re.findall(r'\b\w+\b', texte.lower())
mot_plus_utilise = Counter(mots).most_common(1)
print("le mot le plus utilisé est :", mot_plus_utilise)

########################"
print("#########")
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'le', 'la', 'les', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
mots = re.findall(r'\b\w+\b', texte.lower())
mots_non_pronoms = [mot for mot in mots if mot not in pronoms]
mot_plus_utilise_non_pronom = Counter(mots_non_pronoms).most_common(1)
print("le mot le plus utilisé non pronoms est :", mot_plus_utilise_non_pronom)