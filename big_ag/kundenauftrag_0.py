import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(range(1000))

plt.gcf()
plt.savefig('Kundenauftrag0.png',dpi=30)
plt.show()