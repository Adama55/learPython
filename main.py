'''
FOFANA Adama
STEPHANE Pieraly
LAWANI Imran
MYSSIE Mondestin
NDANDJI Franck
DE SOUZA Yvann

'''
m = "Mississippi"
# 2 afficher la fréquence d'apparition de chaque lettre
s = {e: m.count(e) for e in m}
print(s)

#1-a Trouver la lettre la plus fréquente et sa fréquence

max_freq = max(s.values())
most_frequent_letters = [letter for letter, freq in s.items() if freq == max_freq]
print(most_frequent_letters, "et leur fréquence d'apparition est", max_freq)

#1-b Remplacer les lettres avec la fréquence maximale par "e"
m_modifiee = m
for lettre in most_frequent_letters:
    m_modifiee = m_modifiee.replace(lettre, 'e')

print(m_modifiee)

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

# 3-a calcul du nombre du pronom "le"
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

#3-b compter le nombre de e
nbr_e = texte.count("e")
print("le nombre de 'e' est :", nbr_e)

# 3-c retirer tous les "e"
texte_sans_e = texte.replace("e", " ")
#print(texte_sans_e)

##4 ecrire le rapport dans le fichier json
import json

data ={ "nbr_pronom_le": compteur, "nbr_e":nbr_e}
path = "rapport.json" #D:/ESTIAM/python_expert/tp_cours/rapport.json
with open(path,'w') as file:
    json.dump(data, file)

## 5 trouver le mot le plus utilisé
import re
from collections import Counter
mots = re.findall(r'\b\w+\b', texte.lower())
mot_plus_utilise = Counter(mots).most_common(1)
print("le mot le plus utilisé est :", mot_plus_utilise)

######### trouver le mot le plus utilisé sans pronoms
print("#########")
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'le', 'la', 'les', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
mots = re.findall(r'\b\w+\b', texte.lower())
mots_non_pronoms = [mot for mot in mots if mot not in pronoms]
mot_plus_utilise_non_pronom = Counter(mots_non_pronoms).most_common(1)
print("le mot le plus utilisé sans pronoms est :", mot_plus_utilise_non_pronom)