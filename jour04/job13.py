# Écrivez un programme qui supprime les doublons de la liste suivante :
# [10,20,30,20,10,50,60,40,80,50,40].



liste=[10,20,30,20,10,50,60,40,80,50,40]
New_liste=[]

for i in liste:
    if i not in New_liste:
        New_liste.append(i)
print(New_liste)