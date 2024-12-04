import scipy.stats as stats
import numpy as np

# Données
n = 200  # Taille de l'échantillon
x_bar = 168  # Moyenne échantillonnale
sigma = 1  # Écart-type (connu)
alpha = 0.05  # Niveau de signification

# Calcul de z_alpha/2 pour un intervalle de confiance à 95%
z_alpha_div_2 = stats.norm.ppf(1 - alpha / 2)

# Calcul des bornes de l'intervalle de confiance
margin_of_error = z_alpha_div_2 * (sigma / np.sqrt(n))
lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

# Affichage des bornes de l'intervalle de confiance
print(f"Intervalle de confiance à 95% : [{lower_bound}, {upper_bound}]")