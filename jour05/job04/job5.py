# Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
# messages. Sa méthode était assez simple : il décalait les lettres de trois rangs dans
# l'alphabet.
# Créer une fonction à laquelle on donne un message et un décalage, et la fonction
# renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
# décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z').
import string

def crypt(message):
    
    t=ord(message)
    print(t)
    # for i in message:
    #     print (i)

   
   
   
    # x=message.upper()
    # crypt=x.split(" ")
    
    # d=string.ascii_uppercase
    # e=list(d)
    # for i in crypt:
    #     for b in range(len(i)):
    #         c=i[b]
    #         print(c)
            # for lettre in e:
            #    print(lettre) 
                # if c==lettre:
                #     print(c)
                


crypt('hey tout le monde ')