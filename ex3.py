# Importer les modules nécessaires
import math
from scipy.stats import norm

# Données
mu_0 = 5  # moyenne théorique (réglage de la machine)
x_bar = 5.07  # moyenne observée
sigma = 0.3  # écart-type
n = 100  # taille de l'échantillon
alpha = 0.05  # niveau de signification

# Étape 1 : Détermination de la zone d'acceptation
z_alpha = norm.ppf(1 - alpha / 2)  # valeur critique pour alpha
margin_of_error = z_alpha * (sigma / math.sqrt(n))  # marge d'erreur
interval_acceptance = (mu_0 - margin_of_error, mu_0 + margin_of_error)

# Étape 2 : Calcul de la statistique de test
z_stat = (x_bar - mu_0) / (sigma / math.sqrt(n))

# Étape 3 : Vérification si x_bar appartient à l'intervalle
if interval_acceptance[0] <= x_bar <= interval_acceptance[1]:
    decision = "Accepter H0 : la machine est bien réglée."
else:
    decision = "Rejeter H0 : la machine n'est pas bien réglée."

# Résultats
print("Intervalle d'acceptation : [", round(interval_acceptance[0], 2), ";", round(interval_acceptance[1], 2), "]")
print("Statistique de test Z : ", round(z_stat, 2))
print("Décision : ", decision)
