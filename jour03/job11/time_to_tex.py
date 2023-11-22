# Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
# minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
# minutes”.

def time_to_text(min):
    if min%60==0:
        result=min/60
        print(f"{result}heures et 0 minutes")
    if min%60!=0:
        heure=min/60
        minute=min%60
        print(f"{int(heure)}heures et {minute} minutes")

time_to_text(180)