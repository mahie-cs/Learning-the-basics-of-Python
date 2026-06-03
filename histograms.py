# Playing with a bunch of graphs.
# Today I learned about Histograms.
import numpy as np
from matplotlib import pyplot as plt

x = np.random.uniform(40.0, 100.0, 50)

plt.hist(x)

plt.savefig('my_hist.png')
print("Histogram saved as my_hist.png")
