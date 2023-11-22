# Créer une fonction qui prend en paramètre un nombre nommé “nombre”.
# Afficher “positif” si le nombre est supérieur à 0
# Afficher “negatif” si le nombre est inférieur à 0
# Appeler cette fonction plusieurs fois en y passant des paramètres différents pour
# afficher ces résultats.

def Nombre(nombre):
    if int(nombre)>0:
        print("positif")
    elif int(nombre)<0:
        print("negatif")
Nombre(-3)
Nombre(1)
