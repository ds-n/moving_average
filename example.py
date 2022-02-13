import matplotlib.pyplot as plt
import numpy as np
from mma import sma

fig, ax = plt.subplots()
size = 100
r = np.random.uniform(size=size)
x = range(1, size+1)

s = sma(r)
s5 = sma(r, k=5)
s15 = sma(r, k=15)
ax.plot(x, r)
ax.plot(x, s5)
ax.plot(x, s15)
plt.show()
