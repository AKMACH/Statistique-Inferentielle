import math
from scipy.stats import norm

# Données
mu_0 = 1.5  # Moyenne théorique (norme)
x_bar = 1.495  # Moyenne observée
sigma_corrected = 0.01  # Écart type corrigé
n = 100  # Taille de l'échantillon
alpha = 0.05  # Niveau de signification

# Étape 1 : Déterminer les valeurs critiques (loi normale)
z_alpha = norm.ppf(1 - alpha / 2)  # Valeur critique bilatérale pour alpha
margin_of_error = z_alpha * (sigma_corrected / math.sqrt(n))

# Intervalle de confiance
lower_bound = mu_0 - margin_of_error
upper_bound = mu_0 + margin_of_error

# Étape 2 : Vérification si la moyenne observée est dans l'intervalle
if lower_bound <= x_bar <= upper_bound:
    decision = "Accepter H0 : La machine est bien réglée."
else:
    decision = "Rejeter H0 : La machine n'est pas bien réglée."

# Affichage des résultats
print("Résultats de l'exercice :")
print(f"Intervalle de confiance : [{lower_bound:.5f} ; {upper_bound:.5f}]")
print(f"Moyenne observée : {x_bar:.5f}")
print("Décision :", decision)

