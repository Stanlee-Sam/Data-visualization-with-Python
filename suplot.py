import matplotlib.pyplot as plt
from matplotlib import style

time_hrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
temp = [20, 19, 18, 18, 17, 18, 19, 21, 24, 27, 30, 32, 33, 34, 33, 31, 29, 27, 25, 24, 22, 21, 20, 19]  # Temperature in °C
wind = [10, 12, 9, 8, 7, 6, 5, 7, 9, 12, 15, 18, 20, 19, 18, 16, 14, 13, 12, 11, 10, 9, 8, 7]  # Wind speed in km/h
humidity = [90, 92, 91, 90, 89, 88, 85, 80, 75, 70, 65, 60, 55, 50, 52, 55, 60, 65, 70, 75, 80, 85, 88, 90]  # Humidity in %
precipitation = [0, 0, 0, 0.2, 0.5, 1, 2, 1.5, 1, 0.5, 0.2, 0, 0, 0, 0, 0, 0.1, 0.3, 0.7, 1, 1.5, 1, 0.5, 0]  # Precipitation in mm

#side by side
plt.figure(figsize = (8,4))
plt.subplots_adjust(hspace= .25)

plt.subplot(1,2,1)
plt.title("Temp")
plt.plot( time_hrs, temp, color = 'b', linestyle = '-', linewidth = 1)

plt.subplot(1,2,2)
plt.title("Wind")
plt.plot(time_hrs, wind, color = 'r', linestyle = '-', linewidth = 1)

# vertical/on top of each other
plt.figure ( figsize =( 6,6))
plt.subplots_adjust(hspace= .25)

plt.subplot(2,1,1)
plt.title("Humidity")
plt.plot(time_hrs, humidity, color = 'b', linestyle = '-', linewidth = 1)

plt.subplot(2,1,2)
plt.title('Precipitation')
plt.plot(time_hrs, precipitation, color = 'r', linestyle = '-', linewidth = 1)

#four plots
plt.figure(figsize=(9,9))
plt.subplots_adjust(hspace= .3)

plt.subplot(2,2,1)
plt.title("Temp(F)")
plt.plot(time_hrs, temp, color = 'b', linestyle = '-', linewidth = 1)

plt.subplot(2,2,2)
plt.title("Wind(MPH)")
plt.plot(time_hrs, wind, color = 'r', linestyle = '-', linewidth = 1)

plt.subplot(2,2,3)
plt.title("Humidity(%)")
plt.plot(time_hrs, humidity, color = 'g', linestyle = '-', linewidth = 1)

plt.subplot(2,2,4)
plt.title("Precipitation(mm)")
plt.plot(time_hrs, precipitation, color = 'y', linestyle = '-', linewidth = 1)

plt.show()