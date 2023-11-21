# Créer un programme qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88

for i in range(101):
    if i not in (26,37,88):
        print(i)