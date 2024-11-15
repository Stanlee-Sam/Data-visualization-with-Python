import matplotlib.pyplot as plt
from matplotlib import style

web_monday = [123,645,950,1290,1630,1450,1034,1295,465,205,80]
web_tuesday = [95,680,889,1145,1670,1323,1119,1265,510,310,110]
web_wednesday = [105, 630, 700, 1006, 1520, 1124, 1239, 1380, 580, 610, 230]
time_hrs = [7, 8, 9, 10,11,12,13,14,15,16,17]

style.use('ggplot')

plt.plot(time_hrs, web_monday, 'r', label = 'Monday', linewidth = 1)
plt.plot(time_hrs, web_tuesday,'g', label = 'Tuesday', linewidth = 1.5)
plt.plot(time_hrs, web_wednesday, 'b', label = 'Wednesday', linewidth = 2)
plt.axis([6.5,17.5,50,2000])

plt.xlabel('Hrs')
plt.ylabel('Number of Users')

plt.title('Network traffic')

plt.show()