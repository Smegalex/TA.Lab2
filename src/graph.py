import numpy as np
import matplotlib.pyplot as plt

# Generate a range of n values
n = np.linspace(1, 1000, 100)  # Adjust the range as needed

# Calculate n log n values
# n_log_n = 200*n * np.log(n)
n_log_n = 200000000*n * np.log(n)

# x = [500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000,
#      1250000, 2500000, 5000000, 10000000, 12500000, 25000000,
#      50000000, 100000000, 125000000, 500000000]
# y_summs = [19147000,19881800,44254800,50185900,
#            181228850,299859100,1640539200,
#            3423886800,3313557200,6538551400,
#            15335817050,25634315400,40232552300,
#            72467994100,128417785500,311388590900,
#            433389040300,1725474405200]

x = [10, 100, 500, 1000]
y_5 = [19147000, 166749400, 3313557200, 9501937400]
y_10 = [19881800, 299859100, 6538551400, 25634315400]
y_50 = [44254800, 1640539200, 40232552300, 128417785500]
y_100 = [50185900, 3423886800, 72467994100, 311388590900]
y_500 = [195708300, 21169696700, 433389040300, 1725474405200]

# Plot the function
plt.plot(n, n_log_n, label='n log n')
plt.xlabel('n')
plt.ylabel('time, nanoseconds')
# plt.plot(x, y_summs, label='Merge invertion calc')
plt.plot(x, y_5, label = "5 columns")
plt.plot(x, y_10, label = "10 columns")
plt.plot(x, y_50, label = "50 columns")
plt.plot(x, y_100, label = "100 columns")
plt.plot(x, y_500, label = "500 columns")
# plt.title('Plot of n log n Complexity')
plt.grid(True)
plt.legend()
plt.show()
