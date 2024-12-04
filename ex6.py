import math

# Données
mu_0 = 250  # Moyenne théorique
sigma = 20  # Écart-type
n = 100  # Taille de l'échantillon
alpha = 0.05  # Niveau de signification

# Étape 1 : Calcul de Z critique
z_critical = 1.645  # Valeur critique pour P(Z < z) = 0.95, trouvée dans la table

# Étape 2 : Calcul de la moyenne seuil critique
margin_of_error = z_critical * (sigma / math.sqrt(n))
mu_critical = mu_0 - margin_of_error

# Affichage des résultats
print("Résolution avec méthode du test unilatéral :")
print(f"Valeur critique Z : {z_critical:.3f}")
print(f"Moyenne seuil critique : {mu_critical:.2f}")
print("Décision :")
print(f"Si la moyenne observée est < {mu_critical:.2f}, rejeter H0 : le sachet ne correspond pas à la norme.")
print(f"Si la moyenne observée est >= {mu_critical:.2f}, accepter H0 : le sachet correspond à la norme.")

