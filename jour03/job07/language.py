# Créer une fonction qui prend en paramètre une String nommée “langage”.
# Si la valeur de “langage” est égale à “JavaScript” affichez “tu es un développeur web”
# Sinon si la valeur de “langage” est égale à “python” affichez “tu es un développeur IA”
# Sinon si la valeur de “langage” est égale à “java” affichez “tu es un développeur logiciel”
# Sinon si la valeur de “langage” est égale à “reactjs” affichez “tu es un developpeur mobile”
# Sinon, affichez “un jour, je serai le meilleur développeur... ”

def Langue(language):
    if str(language)==str("javaScript"):
        print("tu es un développeur web")
    elif str(language)==str("python"):
        print("tu es un développeur IA")
    elif str(language)==str("java"):
        print("tu es un développeur logiciel")
    elif str(language)==str("reactjs"):
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur..." )

Langue("java")