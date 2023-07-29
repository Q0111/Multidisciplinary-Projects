import matplotlib.pyplot as plt
days = ['week 1', 'week 2', 'week 3', 'week 4 ', 'week 5', 'week6']
mean_value=['10', '10.3', '10.3', '12.3', '9.7', '53.3']
median_value = ['10', '10', '11', '12', '12', '51']
standard_deviation = ['2.29', '1.50', '2.15', '1.96', '2.18', '36.01']
plt.plot(days,mean_value,label="Mean value")
plt.plot(days,median_value,label='Median value')
plt.plot(days,standard_deviation,label='STD')
plt.ylabel("Kg")
plt.title("Weekly Tracking")
plt.legend()
plt.show()



