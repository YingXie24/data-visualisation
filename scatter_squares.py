import matplotlib.pyplot as plt

x_values =  range(1,1001)
y_values = [x_value**2 for x_value in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Turn off scientific notation in the axis.
ax.ticklabel_format(style="plain")
# Set the range for each axis. 
ax.axis([0, 1100, 0, 1100000])

plt.show()