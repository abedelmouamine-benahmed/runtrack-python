
montant_initial = 10000  
taux_rendement_annuel = 5  


gain_annuel = (taux_rendement_annuel / 100) * montant_initial


print(f"Le gain annuel initial est de {gain_annuel} euros.")

montant_initial += 5000
taux_rendement_annuel += 2


nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial


print(f"Après l'augmentation du capital et du taux de rendement, le nouveau gain annuel est de {nouveau_gain_annuel} euros.")


retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1


montant_final = montant_initial + nouveau_gain_annuel

print(f"Après le retrait et la diminution du rendement, le montant final de l'investissement est de {montant_final} euros.")
