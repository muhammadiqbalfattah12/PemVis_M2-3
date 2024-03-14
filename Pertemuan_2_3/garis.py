import numpy as np
import matplotlib.pyplot as plt

# Membuat titik-titik untuk garis
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

# Membuat plot garis
plt.plot(x, y)

# Menampilkan plot
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Plot Garis')
plt.grid(True)
plt.show()
