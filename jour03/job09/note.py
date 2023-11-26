print("saisir trois notes")
note1=input("note1= ")
note2=input("note2= ")
note3=input("note3= ")
def moyenne():
    
    moyenne_etudiant=(note1+note2+note3)/3  
    
    if moyenne_etudiant>=15:
        return print(f"{moyenne_etudiant}, Très bon élève" )
    
    elif moyenne_etudiant<15 and moyenne_etudiant>10:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
   
    elif moyenne_etudiant>=10 and moyenne_etudiant>8:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
    else:
        return print(f"{moyenne_etudiant}, Élève devant faire des efforts")   
    
moyenne()



