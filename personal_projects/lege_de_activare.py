import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Cod pentru legea de activare (laborator particule)

x = np.array([])
y = np.array([])

with open("lege_de_activare.csv") as csvfile:
    heading = next(csvfile)  # ignores the title columns
    entire_data = csv.reader(csvfile)
    for row in entire_data:
        x = np.append(x, [float(row[0])])
        y = np.append(y, [float(row[1])])

# def predict_y(x_value):
#     return 1 - math.e ** (x_value * 60 * 0.00502 * (-1))

y_pred = 1 - math.e ** (x * 60 * 0.00502 * (-1))

print(f"predicted response:\n{y_pred}")

x_new = np.linspace(1, 20, 100)
bspline = interpolate.make_interp_spline(x, y_pred)
y_new = bspline(x_new)


plt.xlabel("$t_{a} (min)$")
plt.ylabel("$N/N_{max}$")
plt.scatter(x, y, marker="^", color="red")
plt.plot(x_new, y_new, color="black", linewidth=1)
plt.show()

# also an useful link:
# https://www.tutorialspoint.com/how-to-write-text-in-subscript-in-the-axis-labels-and-the-legend-using-matplotlib
