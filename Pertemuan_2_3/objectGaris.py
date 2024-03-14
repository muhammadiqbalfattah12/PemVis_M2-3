import numpy as np
import matplotlib.pyplot as plt

# PROGRAM UNTUK TITIK DAN GARIS
print("\033c")  # Untuk membersihkan layar konsol

row, col = int(500), int(500)

# Parameter titik
pd = int(5)  # Diameter titik
point_color = [0, 0, 220]  # Warna titik
lw = int(5)  # Lebar garis
line_color = [0, 0, 220]  # Warna garis

def buat_garis(Gambar, y1, x1, y2, x2, pd, lw, point_color, line_color):
    pr, pg, pb = point_color
    lr, lg, lb = line_color
    hd = int(pd / 2)  # Menghitung separuh diameter titik
    hw = int(lw / 2)  # Menghitung separuh lebar garis
    dy = y2 - y1
    dx = x2 - x1

    # Menggambar titik pertama
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                Gambar[j, i, :] = [pr, pg, pb]

    # Menggambar titik kedua
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                Gambar[j, i, :] = [pr, pg, pb]

    # Menggambar garis (untuk garis yang cenderung horisontal)
    if abs(dy) <= abs(dx):
        my = dy / dx
        if x2 < x1:
            y1, y2 = y2, y1
            x1, x2 = x2, x1
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            x, y = i, j
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Gambar[j, i, :] = [lr, lg, lb]

    # Menggambar garis (untuk garis yang cenderung vertikal)
    if abs(dy) > abs(dx):
        mx = dx / dy
        if y2 < y1:
            y1, y2 = y2, y1
            x1, x2 = x2, x1
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x, y = i, j
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Gambar[j, i, :] = [lr, lg, lb]

    return Gambar

print('col, row =', col, ',', row)
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)  # Persiapan kanvas hitam

x1, y1 = 400, 400
x2, y2 = 400, 100

hasil = buat_garis(Gambar, y1, x1, y2, x2, pd, lw, point_color, line_color)

plt.figure('Rotasi')
plt.imshow(hasil)
plt.show()
