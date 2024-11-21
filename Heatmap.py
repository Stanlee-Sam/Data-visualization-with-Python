import matplotlib.pyplot as plt

import seaborn as sns

flights_data = sns.load_dataset('flights')

flights_data.head()

flights_data = flights_data.pivot('month', 'year', 'passengers')

flights_data

sns.heatmap(flights_data)