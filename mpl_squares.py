import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(input_values, squares, c=input_values, cmap=plt.cm.magma, s=100)

ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

ax.tick_params(axis="both", labelsize=14)

plt.show()

print(plt.style.available)
