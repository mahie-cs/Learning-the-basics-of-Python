# doing some tests related to matplotlib and graphs

import matplotlib.pyplot as plt

x = [0, 0.5, 1, 1.5, 2]
y = [4, 5, 7, 18, 6]

plt.plot(x, y, marker='o')
plt.title("Success! Matplotlib + UV are working!")
plt.show()
