# Écrire un programme qui affiche dans la console un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :

# draw_rectangle(10, 3)
# def tiret(width):
#     for i in range(width):
#         print("-")

def draw_rectangle(width,height):
    for i in range(height):
        
        if i==0 or i==height-1:
            print('|'+'-'*(width-2)+'|')
            
        else:
            print("|"+' '*(width-2)+'|') 
           


draw_rectangle(10,3)
