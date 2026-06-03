# Playing with a bunch of graphs.
# Today I learned about Histograms.

from matplotlib import pyplot as plt

x = [8, 14, 20, 15, 25]

plt.hist(x)
plt.title("Test")

plt.savefig('my_hist.png')
print("Histogram saved as my_hist.png")
