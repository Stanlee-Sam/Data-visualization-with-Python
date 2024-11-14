import matplotlib.pyplot as plt
from matplotlib import style

web_customers = [123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80]
time_hrs = [7,8,9,10,11,12,13,14,15,16,17]

style.use('ggplot')

plt.plot( time_hrs, web_customers)

plt.xlabel('Hrs')
plt.ylabel('Number of users')

plt.title('Website Traffic')

plt.show()