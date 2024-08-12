#A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

Plotting 5 cubes:
from matplotlib import pyplot as plt
 
# Define data.
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
 
# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', s=40)
# Customize plot.
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
 
# Show plot.
