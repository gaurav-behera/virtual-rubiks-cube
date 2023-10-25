import tkinter as tk
import tkmacosx as tkmac
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from display_cube import plot_cube
import cube_moves as cm
import time
import copy


def virtual_cube(master=None):
    """
    Provides a virtual interface for cube solving.
    :param master: obj, tkinter root object
    :return: None
    """
    global pos, started, finished, scrambled, stopped
    pos = copy.deepcopy(cm.solved_state)
    started = finished = scrambled = stopped = False

    # defining frames
    frame1 = tk.Frame(master=master, height=500, width=500, bg='#D3D3D3')
    frame1.grid(row=0, column=0, padx=5, pady=5)

    frame2 = tk.Frame(master=master, height=500, width=300, bg='#D3D3D3')
    frame2.grid(row=0, column=6, padx=5, pady=10)

    frame3 = tk.Frame(master=master, height=500, width=300, bg='light blue')
    frame3.grid(row=0, column=12, padx=5, pady=5)

    # defining canvas for frame1
    fig = Figure(figsize=(5, 5), dpi=100, facecolor='#D3D3D3')
    # fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=6, columnspan=6)

    # defining buttons for cube moves
    tk.Label(master=frame2, bg='#D3D3D3', height=1).grid(row=0)
    tkmac.Button(master=frame2, text="White CW", command=lambda: update(pos, 'cm.white_cw(pos1)'), height=60).grid(
        row=1, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="Yellow CW", command=lambda: update(pos, 'cm.yellow_cw(pos1)'), height=60).grid(
        row=2, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="Blue CW", command=lambda: update(pos, 'cm.blue_cw(pos1)'), height=60).grid(
        row=3, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="Green CW", command=lambda: update(pos, 'cm.green_cw(pos1)'), height=60).grid(
        row=4, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="Red CW", command=lambda: update(pos, 'cm.red_cw(pos1)'), height=60).grid(
        row=5, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="Orange CW", command=lambda: update(pos, 'cm.orange_cw(pos1)'), height=60).grid(
        row=6, column=0, sticky='nsew')
    tkmac.Button(master=frame2, text="White ACW", command=lambda: update(pos, 'cm.white_acw(pos1)'), height=60).grid(
        row=1, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="Yellow ACW", command=lambda: update(pos, 'cm.yellow_acw(pos1)'), height=60).grid(
        row=2, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="Blue ACW", command=lambda: update(pos, 'cm.blue_acw(pos1)'), height=60).grid(
        row=3, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="Green ACW", command=lambda: update(pos, 'cm.green_acw(pos1)'), height=60).grid(
        row=4, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="Red ACW", command=lambda: update(pos, 'cm.red_acw(pos1)'), height=60).grid(
        row=5, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="Orange ACW", command=lambda: update(pos, 'cm.orange_acw(pos1)'), height=60).grid(
        row=6, column=1, sticky='nsew')
    tkmac.Button(master=frame2, text="White x2", command=lambda: update(pos, 'cm.white_x2(pos1)'), height=60).grid(
        row=1, column=2, sticky='nsew')
    tkmac.Button(master=frame2, text="Yellow x2", command=lambda: update(pos, 'cm.yellow_x2(pos1)'), height=60).grid(
        row=2, column=2, sticky='nsew')
    tkmac.Button(master=frame2, text="Blue x2", command=lambda: update(pos, 'cm.blue_x2(pos1)'), height=60).grid(
        row=3, column=2, sticky='nsew')
    tkmac.Button(master=frame2, text="Green x2", command=lambda: update(pos, 'cm.green_x2(pos1)'), height=60).grid(
        row=4, column=2, sticky='nsew')
    tkmac.Button(master=frame2, text="Red x2", command=lambda: update(pos, 'cm.red_x2(pos1)'), height=60).grid(
        row=5, column=2, sticky='nsew')
    tkmac.Button(master=frame2, text="Orange x2", command=lambda: update(pos, 'cm.orange_x2(pos1)'), height=60).grid(
        row=6, column=2, sticky='nsew')

    # creating info box
    file_handle = open("./utils/info.txt", 'r')
    info = tk.Label(master=frame3, justify='left', padx=5, pady=5, wraplength=250, bg='#D3D3D3')
    info.grid(row=0, column=0)
    text = ''
    while not file_handle.readline().strip() == '--- VIRTUAL CUBE ---':
        pass
    else:
        while True:
            line = file_handle.readline()
            if line.strip().startswith('---'):
                break
            else:
                text = text + line
    info.config(text=text)
    file_handle.close()

    # adding timer
    tk.Label(master=frame2, bg='#D3D3D3').grid(row=7)
    clock = tk.Label(master=frame2, text='00:00.00', font=('DIN Alternate', 40), bg='#D3D3D3')
    clock.grid(row=8, column=0, columnspan=3)

    # scrambler
    scramble_button = tk.Button(master=frame2, text='Scramble Cube', command=lambda: scramble(), height=2)
    scramble_button.grid(row=9, column=0, columnspan=2)

    stop_button = tk.Button(master=frame2, text='Stop Timer', height=2, state='disabled', command=lambda: stop())
    stop_button.grid(row=9, column=2)

    # creating initial position
    plot_cube(cm.solved_state, fig, canvas)

    scrambled_state = copy.deepcopy(cm.solved_state)

    def scramble():
        global pos, scrambled_state, scrambled
        shuffle, pos = cm.scramble_cube()
        plot_cube(pos, fig, canvas)
        scrambled_state = copy.deepcopy(pos)
        scrambled = True

    def stop():
        global stopped
        stopped = True

    def timer():
        global started, finished, scrambled, stopped
        if scrambled and not started:
            started = True
            scramble_button['state'] = 'disabled'
            stop_button['state'] = 'normal'
            now = time.time()
            while not finished and not stopped:
                time.sleep(0.01)
                value = time.time() - now
                min = int(value // 60)
                sec = round(value - min * 60, 2)
                if min < 10:
                    min = '0' + str(min)
                else:
                    min = str(min)
                if sec < 10:
                    sec = '0' + str(sec)
                else:
                    sec = str(sec)
                if int(sec[3:]) < 10:
                    sec = sec[:3] + '0' + sec[-1]
                clock.config(text=min + ':' + sec)
                master.update()

        if pos == cm.solved_state:
            finished = True

    def update(pos1, move):
        global pos
        pos = eval(move)
        plot_cube(pos, fig, canvas)
        timer()


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg='#D3D3D3')
    virtual_cube(master=root)
    root.mainloop()
