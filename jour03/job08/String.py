# Créer une fonction qui prend 2 paramètres :
# - Le premier reçoit un String nommé “type”
# - Le second reçoit un String nommé “saison”
# Si la valeur de “type” est égale à “fruits” et que celle de saison est égale à “hiver”,
# affichez “orange, mandarine et kiwi”
# Si la valeur de “type” est égale à “fruits” et que celle de saison est égale à “ete”, affichez
# “Poire, fraise, cassis”
# Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “hiver”,
# affichez “carotte, topinambour, endive”
# Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “ete”,
# affichez “artichaut, aubergine,navet”

def String(type,saison):
    if str(type)==str("fruit") and str(saison)==str("hiver"):
        print("orange, mandarine et kiwi")
    elif str(type)==str("fruit") and str(saison)==str("ete"):
        print("Poire, fraise, cassis")
    elif str(type)==str("legume") and str(saison)==str("hiver"):
        print("carotte, topinambour, endive")
    elif str(type)==str("legume") and str(saison)==str("ete"):
        print("artichaut, aubergine, navet")

String("fruit","ete")

