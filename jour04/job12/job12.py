# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.
# len
def Taille(a):
    total=0
    for i in a:
        total+=1
    return total
# minimum
def mini(a):
    Min,cpt=a[0],0
    R=0
    for i in a: 
        cpt=cpt+1
        if i < Min:
            Min=i
            R=cpt-1
           # print(rg)
    return Min, R
# programme
New_liste=[]
t=[3, 1, 0, 45, 8, 9, 7]
# Taille(t)
for i in range(7):

    Min, R=mini(t)
    print(Min)
    New_liste.append(Min)
    # print(R)
    t.pop(R)
    #t.remove(rg)
    print(t)
print(New_liste)
   
    
    














   
    