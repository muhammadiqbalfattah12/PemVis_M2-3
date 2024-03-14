import numpy as np
import matplotlib.pyplot as plt

# Koordinat titik
x = 2
y = 3

# Plot titik
plt.scatter(x, y, color='red')

# Penyesuaian batas sumbu
plt.xlim(0, 5)
plt.ylim(0, 5)

# Label sumbu dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Titik')

# Tampilkan plot
plt.grid(True)
plt.show()
