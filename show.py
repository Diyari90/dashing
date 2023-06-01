import numpy as np
import matplotlib.pyplot as plt

# X-axis values
x = [21.75, 23.90, 25.69, 28.10, 29.73, 31.26, 32.81, 34.42]

# Y-axis values
y = [117, 610, 1250, 2608, 5181, 10500, 21100, 42300]

# Function to plot
plt.plot(x, y)

# Function add a legend
plt.legend(['single element'])

# function to show the plot
plt.show()