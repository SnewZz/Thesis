import numpy as np
from scipy.stats import rankdata

# Example array
preds = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

preds2 = -preds

# Assign ranks using rankdata
rk_data = rankdata(preds2, method='ordinal')

argsort = preds2.argsort()

# Display the results
print("Original array:", preds)
print("Original negative array:", -preds)
print("Ranks:", rk_data)
print("argsort:", argsort)
