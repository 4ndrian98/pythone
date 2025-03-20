import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

# Make data
X, Y, Z = axes3d.get_test_data(0.01)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()