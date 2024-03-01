from matplotlib import pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64]

fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)

plt.show()