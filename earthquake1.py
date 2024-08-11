import matplotlib.pyplot as plt
magnitudes = [5,2, 6.3, 6.8, 4.8, 4.4, 5.1, 4.9, 5.7, 6.2, 7.4, 6.4, 7.1, 6.6] 
# magnitudes from the past month from the GeoJSON Summary

plt.figure(figsize=(10, 5))
plt.plot(magnitudes, marker='o', linestyle='-', color='b')
plt.title("Earthquake Magnitudes - how2matplotlib.com")
plt.xlabel("Earthquake Events")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
