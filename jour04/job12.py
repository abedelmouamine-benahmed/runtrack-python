# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.

# def taille(a):
#     total=0
#     for i in a:
#         total+=1
#     return print(total)
a=["78","8","9"]



i=0
for i in a:
    if i>(a[1]):
        a.append(a[0])
        del a[0]
    else:
        a.append(a[1])
        del a[1]

print(a)         


   
    