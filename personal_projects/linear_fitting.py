import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.array([])
y = np.array([])

with open("plot_data.csv") as csvfile:
    heading = next(csvfile)     # ignores the column titles
    entire_data = csv.reader(csvfile)
    for row in entire_data:
        x = np.append(x, [float(row[0])])
        y = np.append(y, [float(row[1])])

x = x.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x, y, marker="^", color="red")
plt.plot(x, y_pred, color="black", linewidth=1)
plt.show()

# also an useful link:
# https://www.tutorialspoint.com/how-to-write-text-in-subscript-in-the-axis-labels-and-the-legend-using-matplotlib
