# Créez une fonction nommée "moyenne" qui prend en paramètre trois notes et retourne la moyenne de ces notes.

# Demandez à l'utilisateur de saisir trois notes, puis enregistrez le résultat de la fonction "moyenne"
# dans une variable appelée "moyenne_etudiant".

# Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
# ➔ Très bon élève si la moyenne est comprise entre 20 et 15.

# ➔ Bon élève si la moyenne est comprise entre 14 et 11.
# ➔ Élève moyen si la moyenne est comprise entre 10 et 8.
# ➔ Élève devant faire des efforts si la moyenne est comprise entre 0 et 7.
print("saisir trois notes" )
note1=int(input("note1= "))
note2=int(input("note2= "))
note3=int(input("note3= "))
def moyenne():
    
    moyenne_etudiant=(note1+note2+note3)/3
    if moyenne_etudiant>=15:
        return print(f"{moyenne_etudiant}, Très bon élève" )
    
    elif moyenne_etudiant<15 and moyenne_etudiant>10:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
   
    elif moyenne_etudiant>=10 and moyenne_etudiant>8:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
    else:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
    
moyenne()