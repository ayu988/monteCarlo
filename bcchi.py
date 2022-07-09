from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
from matplotlib import rcParams

# In Windows the next line should provide the full path to convert.exe
# since convert is a Windows command
#rcParams['animation.convert_path'] = "C:\Program Files\ImageMagick-6.9.3\convert.exe"
rcParams['mathtext.fontset'] = 'cm'
rcParams['font.size'] = 14


red = "#e41a1c"
blue = "#377eb8"
gray = "#eeeeee"


def update(n):
    ax.cla()
    pts = np.random.uniform(low=0, high=1, size=(2, n))
    circ = pts[:, pts[0, :]**2 + pts[1, :]**2 <= 1]
    out_circ = pts[:, pts[0, :]**2 + pts[1, :]**2 > 1]
    pi_approx = 4*circ.shape[1]/n
    circle = mpatches.Wedge((0, 0), 1, 0, 90,  color=gray)
    ax.add_artist(circle)
    plt.plot(circ[0, :], circ[1, :], marker='.', markersize=1,
             linewidth=0, color=red)
    plt.plot(out_circ[0, :], out_circ[1, :], marker='.',markersize=1,
             linewidth=0, color=blue)
    plt.title(r"$n = {}, \pi \approx {:.4f}$".format(n, pi_approx))
    plt.axis("square")
    plt.xlim(0, 1)
    plt.ylim(0, 1)


nvec = np.round(np.logspace(2, 5, 10))
nvec = [3000, 4000, 5000, 6500, 8500, 10000, 15000, 18000, 24000, 30000]
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, update, frames=nvec, blit=False)
ani.save("monte_carlo_pi.gif", writer='imagemagick',
         savefig_kwargs={'delay': 6})