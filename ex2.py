import math

# Données
n = 500  # Taille de l'échantillon
p_hat = 220 / 500  # Proportion estimée
z_alpha = 1.96  # Valeur critique pour un niveau de confiance de 95 %

# Calcul de la marge d'erreur
margin_of_error = z_alpha * math.sqrt((p_hat * (1 - p_hat)) / n)

# Calcul des bornes de l'intervalle de confiance
lower_bound = p_hat - margin_of_error
upper_bound = p_hat + margin_of_error

# Affichage des résultats
print(f"Intervalle de confiance à 95 % : [{lower_bound:.4f}, {upper_bound:.4f}]")