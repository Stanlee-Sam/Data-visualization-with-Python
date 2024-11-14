import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

random_number = np.random.rand(100)

print(random_number)

style.use('ggplot')

plt.plot(random_number, 'g', label = 'line one' , linewidth = 2)

plt.xlabel('Range')
plt.ylabel('Numbers')
plt.title('Random Numbers')

plt.legend()
plt.show()




























