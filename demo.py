import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# NumPy test
print(np.array([1,2,3]) + 5)

# Pandas test
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df)

# Matplotlib test (plot a line)
plt.plot([1,2,3],[4,5,6])
plt.show()

# scikit-learn test
knn = KNeighborsClassifier(n_neighbors=3)
print("KNN model created:", knn)
