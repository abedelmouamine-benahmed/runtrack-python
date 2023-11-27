# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
# ligne/n+1 colonne traversé par une diagonale.

def tapis(n):
    print('+'+'-'*(n+1)+'+')
    for i in range(n+1):
        if i==0:
            print('|'+"#"*(n)+' '+'|')
        elif i==n:
            print('|'+' '+"#"*(n)+'|')
        else:
            print('|'+"#"*(n-i)+' '+"#"*(i)+'|')
        
    print('+'+'-'*(n+1)+'+')


tapis(9)
