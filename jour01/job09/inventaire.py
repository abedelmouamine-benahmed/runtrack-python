nom,prix_produit,stock_produit="sac_de_riz",30,6

produit=int(input(" cb ?\n"))

if produit <= stock_produit:
      stock_produit=stock_produit-produit  
else :
    print("il y'en a pas assez!")

 
prix_produit= prix_produit * (1 + 10 / 100)


print(f"information produit:\nproduit: {nom}\nprix: {prix_produit}\nstock: {stock_produit}\n")

