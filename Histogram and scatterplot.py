from sklearn.datasets import load_boston

import matplotlib.pyplot as plt
from matplotlib import style

boston = load_boston()

x_axis = boston.data
y_axis = boston.target

style.use('ggplot')
plt.figure(figsize= (7, 7))
plt.hist(y_axis, bins= 50)
plt.xlabel('Price in 1000s USD')
plt.ylabel('Number of houses')
plt.show()

style.use('ggplot')
plt.figure(figsize= (7,7))
plt.scatter(boston.data[:, 5], boston.target)
plt.ylabel('Price in 1000s')
plt.xlabel('Number of houses')
plt.show()
