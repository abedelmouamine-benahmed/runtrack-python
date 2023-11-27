# Créer un programme contenant une fonction nommée “my_long_word”. Cette fonction
# doit prendre deux paramètres, un chiffre entier et une chaîne de caractère.
# Cette fonction doit retourner les mots plus long que le chiffre passé en paramètre.

# Exemple :
# my_long_word(3,“ La peur est le chemin vers le côté obscur, la peur mène à la colère, la
# colère mène à la haine, la haine mène à la souffrance”)

# Output : “peur chemin vers côté obscur peur mène colère colère mène haine haine mène souffrance”
def Taille(a):
    total=0
    for i in a:
        total+=1
    return total
        
New_liste=[]
liste2=[]

def my_long_word(nombre,chaine):
    liste=chaine.split()
    print(liste)
    for i in liste:
        if i!= ",": 
            liste2.append(i)
    for i in liste2:
        print(i)
        if Taille(i) > nombre:
            New_liste.append(i)
            
        
             
    print(New_liste)


my_long_word(3,"La peur est le chemin vers le côté obscur , la peur mène à la colère , la colère mène à la haine , la haine mène à la souffrance")
