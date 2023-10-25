import tkinter as tk
from tkinter import messagebox as mb
import tkmacosx as tkmac
import cube_moves as cm
import numpy as np
from matplotlib.figure import Figure
from display_cube import plot_cube
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import copy
import web_solver as st
import matplotlib.animation as animation


def solve_cube(master=None):
    # master.geometry("1200x600")
    global color, pos

    color = '#ffffff'
    pos = copy.deepcopy(cm.solved_state)

    color_key = {'w': "#ffffff", 'y': "#ffff00", 'b': "#0099ff", 'g': "#66ff99", 'r': "#e60000", 'o': "#ff6600"}
    key_color = {value: key for key, value in color_key.items()}  # reverse dictionary
    buttons = np.full((9, 12), 0).tolist()

    # defining frames
    frame1 = tk.Frame(master=master, height=500, width=800, bg='#D3D3D3')
    frame1.grid(row=0, column=0, padx=10, pady=0, sticky='nsew')

    frame2 = tk.Frame(master=master, height=500, width=200, bg='#D3D3D3')
    frame2.grid(row=0, column=1, pady=0, sticky='nsew')

    frame3 = tk.Frame(master=master, height=500, width=200, bg='#D3D3D3')
    frame3.grid(row=0, column=2, padx=10, pady=0, sticky='nsew')

    # cube net
    tk.Label(master=frame1, bg='#D3D3D3', text='    ', height=2).grid(row=0, column=0)
    for i in range(9):
        for j in range(12):
            if (i < 3 or i > 5) and (j not in [3, 4, 5]):
                pass
            else:
                buttons[i][j] = tkmac.Button(master=frame1, height=50, width=50,
                                             bg=color_key[pos[i][j]], bordercolor='#000000',
                                             command=lambda row=i, column=j: changesticker(row, column))
                buttons[i][j].grid(row=i + 1, column=j + 1)

    # color chooser
    tk.Label(master=frame2, bg='#D3D3D3', text='    ', height=2).grid(row=0, column=0)
    tk.Label(master=frame2, text='COLOR PICKER', font=('Calibri', 15), bg='#D3D3D3').grid(row=1, column=1,
                                                                                          columnspan=3)
    for i in range(6):
        colors = ["#ffffff", "#ffff00", "#0099ff", "#66ff99", "#e60000", "#ff6600"]
        if i < 3:
            tkmac.Button(master=frame2, width=50, height=50, bg=colors[i],
                         command=lambda key=i: changecolor(colors[key])).grid(row=2, column=i + 1)
        else:
            tkmac.Button(master=frame2, width=50, height=50, bg=colors[i],
                         command=lambda key=i: changecolor(colors[key])).grid(row=3, column=i - 2)

    tk.Label(master=frame2, bg='#D3D3D3', text='    ', height=2).grid(row=4, column=4)
    # random scramble
    tkmac.Button(master=frame2, height=40, text='Random Scramble', bordercolor='#D3D3D3',
                 command=lambda: randscramble()).grid(row=5, column=1, columnspan=3, sticky='nsew')

    # solve cube
    tkmac.Button(master=frame2, height=40, text='Solve Cube', bordercolor='#D3D3D3',
                 command=lambda: solve()).grid(
        row=6, column=1, columnspan=3, sticky='nsew')

    # 3D cube net view
    fig = Figure(figsize=(2, 2), dpi=100)
    fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5, pady=5)
    plot_cube(pos, fig, canvas, bg='#D3D3D3')

    # creating info box
    file_handle1 = open("./utils/info.txt", 'r')
    info1 = tk.Label(master=frame3, justify='left', pady=5, wraplength=250, bg='#D3D3D3')
    info1.grid(row=0, column=0)
    text1 = ''
    while not file_handle1.readline().strip() == '--- CUBE SOLVER 1 ---':
        pass
    else:
        while True:
            line1 = file_handle1.readline()
            if line1.strip().startswith('---'):
                break
            else:
                text1 = text1 + line1
    info1.config(text=text1)
    file_handle1.close()

    def randscramble():
        global scramble, pos, scrambled_state
        scramble, scrambled_state = cm.scramble_cube()
        pos = scrambled_state
        for i in range(9):
            for j in range(12):
                if (i < 3 or i > 5) and (j not in [3, 4, 5]):
                    pass
                else:
                    buttons[i][j].config(bg=color_key[pos[i][j]])
        plot_cube(pos, fig, canvas, bg='#D3D3D3')

    def changesticker(i, j):
        if (i == 4 and j in [1, 4, 7, 10]) or (j == 4 and i in [1, 7]):
            pass
        else:
            buttons[i][j].config(bg=color)
            pos[i][j] = key_color[color]  # updating position
        plot_cube(pos, fig, canvas, bg='#D3D3D3')

    def changecolor(color1):
        global color
        color = color1

    def solve():
        global pos, scrambled_state
        scrambled_state = pos
        # checking for valid scramble
        D = {}
        text = ''
        if pos == cm.solved_state:
            text = 'Cube is already solved.'
            mb.showinfo('Info', text)

        else:
            text = 'Calculating Solution. This may take a while'
            mb.showinfo('Info', text)

            solve, solution, text = st.get_solution(pos)

            if text == '':

                for widget in frame1.winfo_children() + frame2.winfo_children() + frame3.winfo_children():
                    widget.destroy()

                fig = Figure(figsize=(5, 5), dpi=100, facecolor='#D3D3D3')
                canvas = FigureCanvasTkAgg(fig, master=frame1)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, padx=10)
                plot_cube(pos, fig, canvas)

                tk.Label(master=frame2, bg='#D3D3D3', text='    ', height=1).grid(row=0)
                tk.Label(master=frame2, text='SOLUTION', font=('Helvetica', 14), bg='#D3D3D3').grid(row=1, column=0,
                                                                                                    columnspan=3)
                output = tk.Text(master=frame2, width=30, height=len(solution.split()), yscrollcommand='True',
                                 font=('Helvetica', 14))

                output.insert(tk.END, solve.rstrip('\n'))
                output.config(spacing1=3, spacing2=4, spacing3=3, state='disabled')
                output.grid(row=2, columnspan=3)

                # creating info box
                file_handle2 = open("./utils/info.txt", 'r')
                info2 = tk.Label(master=frame3, justify='left', pady=15, wraplength=300, bg='#D3D3D3')
                info2.grid(row=0, column=0, padx=10, columnspan=2)
                text2 = ''
                while not file_handle2.readline().strip() == '--- CUBE SOLVER 2 ---':
                    pass
                else:
                    while True:
                        line2 = file_handle2.readline()
                        if line2.strip().startswith('---'):
                            break
                        else:
                            text2 = text2 + line2
                info2.config(text=text2)
                file_handle2.close()

                # animation stuff
                tk.Label(master=frame3, bg='#D3D3D3', text='    ', height=2).grid(row=1)
                animate_button = tk.Button(master=frame3, text='Animate', command=lambda: animate())
                animate_button.grid(row=2, column=0, sticky='ew')
                slider = tk.Scale(master=frame3, from_=0.25, to=2, digits=3, resolution=0.25, label='\tSpeed:',
                                  bg='#D3D3D3', orient=tk.HORIZONTAL)
                slider.grid(row=2, column=1, columnspan=1, rowspan=2)
                slider.set(1)

                back_button = tk.Button(master=frame3, text='Back', command=lambda: back())
                back_button.grid(row=3, column=0, sticky='ew')

                def back():
                    for widget in master.winfo_children():
                        widget.destroy()
                    solve_cube(master)

                def animate():
                    global pos
                    animate_button['state'] = 'disabled'
                    slider['state'] = 'disabled'
                    solution_moves = solution.split()
                    pos = scrambled_state
                    position, moves = [pos], [' ']
                    for i in solution_moves:
                        move = 'cm.' + cm.standard_moves[i]
                        pos = eval(move)
                        position.append(pos)
                        moves.append(move[3:-5])

                    def update(k):
                        pos = position[k]
                        move = moves[k]
                        if k > 1:
                            output.tag_configure('current_line', background='white')
                        if k > 0:
                            output.tag_remove("current_line", 'insert linestart', 'insert lineend+1c')
                            output.mark_set("insert", str(k) + ".0")  # changes position of insertion cursor
                            output.tag_add('current_line', 'insert linestart', 'insert lineend+1c')
                            output.tag_configure('current_line', background='light blue')

                        plot_cube(pos, fig, canvas, move)
                        k += 1
                        if k == len(position):
                            animate_button['state'] = 'normal'
                            slider['state'] = 'normal'

                    ani = animation.FuncAnimation(fig, update, frames=len(position), interval=1000 / slider.get(),
                                                  repeat=False)
                    canvas.draw()

            else:
                mb.showinfo('Error', text)


if __name__ == '__main__':
    root = tk.Tk()
    # root.configure(bg='#D3D3D3')
    solve_cube(master=root)
    root.mainloop()
