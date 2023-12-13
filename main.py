# Déclaration des noms
noms = [
    'FOFANA Adama',
    'STEPHANE Pieraly',
    'LAWANI Imran',
    'MYSSIE Mondestin',
    'NDANDJI Franck',
    'DE SOUZA Yvann'
]

# Compter l'occurrence de chaque lettre dans la chaîne 'm'
mot_test = "Mississippi"
occurrences_lettres = {lettre: mot_test.count(lettre) for lettre in mot_test}
print(occurrences_lettres)

# Trouver la lettre la plus fréquente
max_occurrence = max(occurrences_lettres.values())
lettres_plus_frequentes = [lettre for lettre, occ in occurrences_lettres.items() if occ == max_occurrence]
print(lettres_plus_frequentes, "et leur fréquence d'apparition est", max_occurrence)

# Remplacer les lettres les plus fréquentes par 'e'
mot_modifie = mot_test
lettre_a_remplacer = 'e'
for lettre in lettres_plus_frequentes:
    mot_modifie = mot_modifie.replace(lettre, lettre_a_remplacer)
print(mot_modifie)

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
def nettoyer_et_diviser_texte(texte, ancien="l'", nouveau="l' "):
    texte = texte.replace("\n", " ")
    texte = texte.replace(ancien, nouveau)
    return texte.split(" ")

texte_nettoye = nettoyer_et_diviser_texte(texte)

# Compter le nombre de 'le' suivant un pronom
pronoms_personnels = ['je', "tu", 'il', "nous", "vous", 'ils']
compteur_le = 0
for i in range(1, len(texte_nettoye)):
    if texte_nettoye[i] == "le" and texte_nettoye[i - 1].lower() in pronoms_personnels:
        compteur_le += 1
print("Le nombre 'le' est :", compteur_le)

# Compter le nombre de 'e' dans le texte
lettre_a_compter = "e"
nbr_e = texte.count(lettre_a_compter)
print(f"Le nombre de {lettre_a_compter} est :", nbr_e)

# Remplacer tous les 'e' par des espaces
texte_sans_e = texte.replace(lettre_a_remplacer, " ")
print(texte_sans_e)

# Trouver les mots les plus fréquents dans le texte
import re
from collections import Counter

texte_liste_mots = re.sub(r'[^\w\s]', '', texte.lower()).split()
occurrences_mots = {mot: texte_liste_mots.count(mot) for mot in texte_liste_mots}
mots_plus_frequents = [mot for mot, freq in occurrences_mots.items() if freq == max(occurrences_mots.values())]
print(mots_plus_frequents, "et leur nombre d'apparition est de :", max(occurrences_mots.values()))

# Compter le nombre de pronoms dans le texte
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'le', 'la', 'les', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
mots_non_pronoms = [mot for mot in texte_liste_mots if mot not in pronoms]
mot_plus_utilise_non_pronom = Counter(mots_non_pronoms).most_common(1)
print("Le mot le plus utilisé sans pronoms est :", mot_plus_utilise_non_pronom)

# Compter le nombre d'articles et de pronoms dans le texte
articles = ['le', "la", 'les', "l'"]
pronoms_personnels = ['je', "tu", 'il', "nous", "vous", 'ils']
pronoms = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'me', 'te', 'se', 'lui', 'leur', 'eux', 'y', 'en', 'moi', 'toi', 'soi', 'toi-même']
compteur_pronoms = 0

for i in range(1, len(texte_nettoye)):
    if texte_nettoye[i] in articles and texte_nettoye[i - 1].lower() in pronoms_personnels:
        compteur_pronoms += 1
    elif texte_nettoye[i] in pronoms:
        compteur_pronoms += 1
print("Le nombre de pronoms: ", compteur_pronoms)

# Écrire les résultats dans un fichier JSON
import json

donnees = {"nbr_pronom_le": compteur_le, "nbr_e": nbr_e, "nbr_total_pronoms": compteur_pronoms}
chemin_fichier_json = "rapport.json"  # Chemin du fichier JSON
with open(chemin_fichier_json, 'w') as fichier_json:
    json.dump(donnees, fichier_json)

# Partie 2

print("\t\t Partie 2")
elements = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e']

# Création de couples d'éléments consécutifs
couples_elements = [(elements[i], elements[i + 1]) for i in range(0, len(elements) - 1, 2)]



print(couples_elements)
