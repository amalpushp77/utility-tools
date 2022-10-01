import math

import pandas as pd
# import random
import numpy as np
import matplotlib.pyplot as plt

n = 5
p = ['a', 'b', 'c', 'd', "e"]

x = np.random.randint(1, 10, size=5)
y = np.random.randint(1, 10, size=5)
w = np.random.randint(1, 7, size=5)
h = np.random.randint(1, 3, size=5)

print(x)
print(y)
print(w)
print(h)
plt.scatter(x, -1 * y, color='green')
plt.grid()

for i, label in enumerate(p):
    plt.annotate(label, (x[i], -1 * y[i]))

m = {"a": [np.nan, np.nan, np.nan, np.nan, np.nan],
     "b": [np.nan, np.nan, np.nan, np.nan, np.nan],
     "c": [np.nan, np.nan, np.nan, np.nan, np.nan],
     "d": [np.nan, np.nan, np.nan, np.nan, np.nan],
     "e": [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(m, columns=p, index=p)

for i in range(n - 1):
    for j in range(i + 1, n):
        # print(c[i][0], c[j][0])
        dx = abs(x[i] - x[j])
        dy = abs(y[i] - y[j])
        theta = math.degrees(dx) if dx == 0 else math.degrees(math.atan(dy / dx))
        dr = (w[i] + w[j]) * math.cos(theta) + (h[i] + h[j]) * math.sin(theta)
        man_dist = abs((dx + dy) / dr)
        df.at[p[i], p[j]] = man_dist
        df.at[p[j], p[i]] = man_dist
print(df)
plt.show()
