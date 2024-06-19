import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Using predefined styles from matplotlib
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=32)
ax.plot(input_values, squares, linewidth = 1)

# Set the chart title and label axes
ax.set_title("Sqaure Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()