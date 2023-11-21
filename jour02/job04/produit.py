# Créer un programme qui affiche en console les
# tables de multiplication de 1 à N. N étant un
# entier supérieur à zéro saisi par l’utilisateur.
# N'oubliez pas de vérifier tout ce qui est
# nécessaire pour assurer la fiabilité de votre
# programme.

entier=input("entrez un entier (N*): " )

print(f"voici la table de {entier}")

for i in range (1,11):
      
    result=int(entier) * int(i)
    
    print(f"{entier}*{i}={result}")
  

