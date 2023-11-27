# Écrire un programme qui affiche dans la console un triangle avec des ‘_’, des
# ‘\’ et des ‘/’ en fonction de l’input entré, qui représentera la hauteur.
# Exemple si l’input entré est 5 :
def triangle(height):
    for i in range(height):
        if i==0:
            print(' '*(height-(i+1))+'/''\\')
        elif i!=0 and i!=height-1:
            print(' '*(height-(i+1))+'/'+'  '*(i),end='')
            print('\\')
        else:
            print('/'+'__'*(height-1)+"\\")


triangle(7)