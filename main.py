'''
FOFANA Adama
STEPHANE Pieraly
LAWANI Imran
MYSSIE Mondestin
NDANDJI Franck
DE SOUZA Yvann

'''
# Compter l'occurrence de chaque lettre dans la chaîne 'm'
m = "Mississippi"
s = {e: m.count(e) for e in m}
print(s)

# Trouver la lettre la plus fréquente
max_freq = max(s.values())
most_frequent_letters = [letter for letter, freq in s.items() if freq == max_freq]
print(most_frequent_letters, "et leur fréquence d'apparition est", max_freq)

# Remplacer les lettres les plus fréquentes par 'e'
m_modifiee = m
for lettre in most_frequent_letters:
    m_modifiee = m_modifiee.replace(lettre, 'e')
print(m_modifiee)

# Analyser un texte plus long (à remplacer par votre texte)
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

# Fonction pour nettoyer le texte et le diviser en mots
def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("l'", "l' ")
    return text.split(" ")

my_text_cleaned = clean_text(texte)

# Compter le nombre de 'le' suivant un pronom
mesPronoms = ['je', "tu", 'il', "nous", "vous", 'ils']
compteur_le = 0
for i in range(1, len(my_text_cleaned)):
    if my_text_cleaned[i] == "le" and my_text_cleaned[i - 1].lower() in mesPronoms:
        compteur_le += 1
print("Le nombre 'le' est :", compteur_le)

# Compter le nombre de 'e' dans le texte
nbr_e = texte.count("e")
print("le nombre de 'e' est :", nbr_e)

# Remplacer tous les 'e' par des espaces
texte_sans_e = texte.replace("e", " ")
print(texte_sans_e)

# Trouver les mots les plus fréquents dans le texte
import re
from collections import Counter

texte_list = re.sub(r'[^\w\s]', '', texte.lower()).split()
temp = {mot: texte_list.count(mot) for mot in texte_list}
most_frequent_letters = [letter for letter, freq in temp.items() if freq == max(temp.values())]
print(most_frequent_letters, "et leur nombre d'apparition est de :", max(temp.values()))

# Compter le nombre de pronoms dans le texte
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'le', 'la', 'les', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
mots = re.findall(r'\b\w+\b', texte.lower())
mots_non_pronoms = [mot for mot in mots if mot not in pronoms]
mot_plus_utilise_non_pronom = Counter(mots_non_pronoms).most_common(1)
print("le mot le plus utilisé sans pronoms est :", mot_plus_utilise_non_pronom)

# Compter le nombre d'articles et de pronoms dans le texte
articles = ['le',"la", 'les',"l'"]
mesPronoms = ['je',"tu", 'il', "nous", "vous", "ils"]
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
compteur_pronoms = 0

for i in range(1, len(my_text_cleaned)):
    if my_text_cleaned[i] in articles and my_text_cleaned[i - 1].lower() in mesPronoms:
        compteur_pronoms += 1
    elif my_text_cleaned[i] in pronoms:
        compteur_pronoms += 1
print("Le nombre de pronoms: ", compteur_pronoms)

# Écrire les résultats dans un fichier JSON
import json

data = {"nbr_pronom_le": compteur_le, "nbr_e": nbr_e, "nbr_total_pronoms": compteur_pronoms}
path = "rapport.json"  # Chemin du fichier JSON
with open(path, 'w') as file:
    json.dump(data, file)
