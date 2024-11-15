import matplotlib.pyplot as plt
from matplotlib import style

web_customers = [123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80]
time_hrs = [7,8,9,10,11,12,13,14,15,16,17]

style.use('ggplot')

#alpha value to set the transparency
plt.plot(time_hrs, web_customers, alpha = .4)

plt.xlabel('Hrs')
plt.ylabel('Number of users')

plt.title('Website traffic')

plt.annotate('Max', ha = 'center', va = 'bottom', xytext=(8,1500), xy=(11,1630), arrowprops= {'facecolor' : 'green'})

plt.show()