from scipy.spatial.distance import pdist, squareform
import numpy as np

item_ids = [1, 2, 3, 4, 5]

user_ids = [1, 2, 3, 4, 5, 6, 7, 8]


M = np.zeros((8, 5), dtype=bool)
for u in trange(1, 9):
    np.add.at(
        M[u-1], (item_ids[user_ids == u]) - 1,
        dataset.ratings[dataset.user_ids == u]
    )
