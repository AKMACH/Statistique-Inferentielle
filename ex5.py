import math
from scipy.stats import norm

# Données pour le test Z
mu_0 = 1.5  # Moyenne théorique
x_bar = 1.495  # Moyenne observée
s_corrected = 0.01  # Écart-type corrigé
n = 100  # Taille de l'échantillon
alpha = 0.05  # Niveau de signification

# Étape 1 : Calcul de la statistique Z
z_stat = (x_bar - mu_0) / (s_corrected / math.sqrt(n))

# Étape 2 : Valeur critique Zσ
z_critical = norm.ppf(1 - alpha / 2)  # Valeur critique bilatérale

# Étape 3 : Prendre la valeur absolue de Z et comparer
z_stat_abs = abs(z_stat)

# Étape 4 : Décision
if z_stat_abs > z_critical:
    decision = "Rejeter H0 : La machine n'est pas bien réglée."
else:
    decision = "Accepter H0 : La machine est bien réglée."

# Affichage des résultats
print("Résolution avec méthode du test Z :")
print(f"Statistique Z calculée : {z_stat:.2f}")
print(f"Valeur absolue de Z : {z_stat_abs:.2f}")
print(f"Valeur critique Zσ : {z_critical:.2f}")
print(f"Décision : {decision}")

