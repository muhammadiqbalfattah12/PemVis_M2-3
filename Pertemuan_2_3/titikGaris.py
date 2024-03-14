import numpy as np
import matplotlib.pyplot as plt

# Koordinat titik
x_point = 2
y_point = 3

# Koordinat titik awal dan akhir garis
x1_line = 1
y1_line = 1
x2_line = 4
y2_line = 5

# Plot titik
plt.scatter(x_point, y_point, color='red', label='Titik')

# Plot garis
plt.plot([x1_line, x2_line], [y1_line, y2_line], color='blue', label='Garis')

# Penyesuaian batas sumbu
plt.xlim(0, 6)
plt.ylim(0, 6)

# Label sumbu dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Titik dan Garis')

# Tampilkan legenda
plt.legend()

# Tampilkan plot
plt.grid(True)
plt.show()
