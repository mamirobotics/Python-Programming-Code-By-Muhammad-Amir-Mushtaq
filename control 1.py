import numpy as np
import matplotlib.pyplot as plt

x = np.array([12, 14, 16, 18])
y = np.array([2, 4, 6, 8])
plt.scatter(x, y)
plt.xlabel('Horizontal axis value')
plt.ylabel('Vertical axis values')
plt.title('Our first plot')
plt.show()
