import numpy as np


def plot_cube(pos, fig, canvas, move=' ', bg=''):
    ax = fig.gca(projection='3d')
    ax.clear()
    ax.set_axis_off()
    if bg != '':
        ax.set_facecolor(bg)
    ax.set_xlim3d(-0.5, 3.5)
    ax.set_ylim3d(-0.5, 3.5)
    ax.set_zlim3d(-0.5, 3.5)

    color = {'w': "#ffffff", 'y': "#ffff00", 'b': "#0099ff", 'g': "#66ff99", 'r': "#e60000", 'o': "#ff6600"}

    # defining and plotting surfaces
    for i in range(9):
        for j in range(12):
            if i == 0 or i == 1 or i == 2:  # yellow centre
                zz = np.full((2, 2), 3)
                if j == 3 or j == 4 or j == 5:
                    xx, yy = np.meshgrid(np.linspace(j - 3, j - 2, 2), np.linspace(2 - i, 3 - i, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=1, linewidth=2, shade=False)
            if i == 3 or i == 4 or i == 5:
                if j == 0 or j == 1 or j == 2:  # red centre
                    xx = np.full((2, 2), 0)
                    yy, zz = np.meshgrid(np.linspace(2 - j, 3 - j, 2), np.linspace(5 - i, 6 - i, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=60, linewidth=2, shade=False)
                if j == 3 or j == 4 or j == 5:  # green centre
                    yy = np.full((2, 2), 0)
                    xx, zz = np.meshgrid(np.linspace(j - 3, j - 2, 2), np.linspace(5 - i, 6 - i, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=10, linewidth=2, shade=False)
                if j == 6 or j == 7 or j == 8:  # orange centre
                    xx = np.full((2, 2), 3)
                    yy, zz = np.meshgrid(np.linspace(j - 6, j - 5, 2), np.linspace(5 - i, 6 - i, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=0, linewidth=2, shade=False)
                if j == 9 or j == 10 or j == 11:  # blue centre
                    yy = np.full((2, 2), 3)
                    xx, zz = np.meshgrid(np.linspace(12 - j, 11 - j, 2), np.linspace(6 - i, 5 - i, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=0, linewidth=2, shade=False)
            if i == 6 or i == 7 or i == 8:  # white centre
                zz = np.full((2, 2), 0)
                if j == 3 or j == 4 or j == 5:
                    xx, yy = np.meshgrid(np.linspace(j - 3, j - 2, 2), np.linspace(i - 6, i - 5, 2))
                    ax.plot_surface(xx, yy, zz, color=color[pos[i][j]], edgecolor='black', zorder=0, linewidth=2, shade=False)
    if move != ' ':
        #  arc
        r1, u1, h1 = 0.5, np.linspace(-np.pi, 0.5 * np.pi, 10), 0
        if move[0] in 'ybo':
            h1 = 3.5
        if move[0] in 'wgr':
            h1 = -0.5
        x1, y1 = 1.5 + r1 * np.outer(np.ones(np.size(u1)), np.cos(u1)), 1.5 + r1 * np.outer(np.ones(np.size(u1)),
                                                                                            np.sin(u1))
        z1 = h1 * np.outer(np.ones(np.size(u1)), np.ones(np.size(u1)))
        if move[0] in 'yw':
            ax.plot_surface(x1, y1, z1, edgecolor='black', alpha=0, shade=False, linewidth=3)  # yellow/white
        if move[0] in 'bg':
            ax.plot_surface(x1, z1, y1, edgecolor='black', alpha=0, shade=False, linewidth=3)  # blue/green
        if move[0] in 'or':
            ax.plot_surface(z1, x1, y1, edgecolor='black', alpha=0, shade=False, linewidth=3)  # orange/red

        # cone
        u2, r2 = np.linspace(0, 2 * np.pi, 10), np.linspace(-0.1, 0, 10)
        t2, r2 = np.meshgrid(u2, r2)
        fixed = variable = height = a = b = c = 0

        if move.endswith('acw'):
            if move[0] in 'bwr':
                variable, fixed, height = r2 * np.sin(t2), r2 * 5, r2 * np.cos(t2)
            if move[0] in 'yog':
                variable, fixed, height = r2 * np.sin(t2), -r2 * 5, r2 * np.cos(t2)
        elif move.endswith('cw') or move.endswith('x2'):
            fixed, variable, height = r2 * np.sin(t2), r2 * 5, r2 * np.cos(t2)
        if move[0] == 'y':
            a, b, c = fixed + 1, variable + 2, height + 3.5
        if move[0] == 'w':
            a, b, c = -variable + 1, fixed + 2, height - 0.5
        if move[0] == 'g':
            a, b, c = fixed + 1, height - 0.5, variable + 2
        if move[0] == 'b':
            a, b, c = -variable + 1, height + 3.5, fixed + 2
        if move[0] == 'o':
            a, b, c = height + 3.5, fixed + 1, variable + 2
        if move[0] == 'r':
            a, b, c = height - 0.5, -variable + 1, fixed + 2
        ax.plot_surface(a, b, c, color="black")
    # ax.text(1.5, 1.5, 3.5, 'x2', size=20, zorder=50)
    canvas.draw()
