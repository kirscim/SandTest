import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = [0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6, 8, 11, 16, 22, 32]

ax = plt.subplot()
ax.set_xscale('log')
plt.grid(True, which='both')
ax.set_xticks([0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6, 8, 11, 16, 22, 32, 45])
ax.set_yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
formatter = FuncFormatter(lambda x, _: '{:.16g}'.format(x))
ax.get_xaxis().set_major_formatter(formatter)
plt.show()
