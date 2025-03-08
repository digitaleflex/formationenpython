"""
Manipuler les types
Convertissez un entier en chaîne et inversement.
"""

# Conversion d'un entier en chaîne

nombre = 25
nombre_str = str(nombre)
# print(f"Nombre : {nombre} ({type(nombre)})")
# print(f"Nombre_str : {nombre_str} ({type(nombre_str)})")

# Affichage des valeurs avec la concaténation
print ('conversion en chaine : ' + nombre_str + ' ' + str(type(nombre_str)))  


# Conversion d'une chaîne en entier

texte = "100"
texte_int = int(texte)
# print(f"Texte : {texte} ({type(texte)})")
# print(f"Texte_int : {texte_int} ({type(texte_int)})")

print ('conversion en entier : ' + str(texte_int) + ' ' + str(type(texte_int)))
