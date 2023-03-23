import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 2*np.cos(x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0, color="red")

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(-4, 4), yticks=np.arange(-4, 4))

plt.gcf()
plt.savefig('Kundenauftrag5.png',dpi=30)
plt.show()