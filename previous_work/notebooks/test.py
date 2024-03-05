import numpy as np
tmp = [1.4, 3.6, 7.8, 1.2, 0.8, 5.4]
tmp = np.array(tmp)
target_item = tmp.argsort()[2]
print(target_item)