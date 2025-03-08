"""
Expérimenter les types dynamiques
Déclarez une variable avec un nombre, changez-la ensuite en texte et affichez son type à chaque étape.

"""
# Déclaration initiale avec un entier
variable = 50
print("Valeur : " + str(variable) + ", Type : " + str(type(variable)))

# Changement du type en chaîne de caractères
variable = "Python"
print("Valeur : " + variable + ", Type : " + str(type(variable)))
