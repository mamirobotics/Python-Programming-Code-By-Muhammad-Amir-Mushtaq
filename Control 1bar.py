import numpy as np
import matplotlib.pyplot as plt

fruits = ['Mango', 'Apple', 'Banana']
price = [50, 80, 40]
plt.bar(fruits, price)
plt.xlabel('Fruits')
plt.ylabel('Price')
plt.title('Fruit Price Chart')
plt.show()
