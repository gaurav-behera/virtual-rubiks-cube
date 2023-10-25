import tkinter as tk
import tkmacosx as tkmac
from tkinter import ttk
from tkinter import simpledialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cube_moves as cm
import time
from db import add_session, display_sessions


def cube_timer(master=None, root=None):
    frame1 = tk.Frame(master=master, height=400, width=700, bg='#D3D3D3')
    frame1.grid(row=0, column=0, padx=10)

    frame2 = tk.Frame(master=master, height=500, width=200, bg='#D3D3D3')
    frame2.grid(row=0, column=1, padx=5, pady=5, rowspan=2)

    frame3 = tk.Frame(master=master, height=10, width=700, bg='#D3D3D3')
    frame3.grid(row=1, column=0, padx=10)

    # timer, scramble
    tk.Label(master=frame1, bg='#D3D3D3', width=85, height=5).grid(row=0, columnspan=2)
    scramble_label = tk.Label(master=frame1, text=' ' * 30, font=('DIN Alternate', 30), bg='#D3D3D3')
    scramble_label.grid(row=1, columnspan=2)
    clock = tk.Label(master=frame1, text='00:00.00', font=('DIN Alternate', 100), bg='#D3D3D3')
    clock.grid(row=2, columnspan=2)

    show_scramble = tk.IntVar()
    tk.Checkbutton(master=frame1, text='Show Scramble', command=lambda: check(), bg='#D3D3D3').grid(row=3, columnspan=2)
    tk.Label(master=frame1, bg='#D3D3D3', height=4).grid(row=4, columnspan=2)

    def check():
        if show_scramble.get() == 1:
            show_scramble.set(0)
            scramble_label.config(text='\t' * 6)
        elif show_scramble.get() == 0:
            show_scramble.set(1)
            scramble_label.config(text=cm.scramble_cube()[0])

    # creating info box
    file_handle = open("./utils/info.txt", 'r')
    info1 = tk.Label(master=frame3, justify='left', pady=5, wraplength=400, bg='#D3D3D3')
    info2 = tk.Label(master=frame3, justify='left', pady=5, wraplength=400, bg='#D3D3D3')
    info1.grid(row=0, column=0)
    info2.grid(row=0, column=1)
    text = ''
    while not file_handle.readline().strip() == '--- CUBE TIMER ---':
        pass
    else:
        while True:
            line = file_handle.readline()
            if line.strip().startswith('---'):
                break
            else:
                text = text + line
    info1.config(text=text)
    file_handle.seek(0, 0)
    text = ''
    while not file_handle.readline().strip() == '--- DETAILS ---':
        pass
    else:
        while True:
            line = file_handle.readline()
            if line.strip().startswith('---'):
                break
            else:
                text = text + line
    info2.config(text=text)
    file_handle.close()

    # details
    tabs = ttk.Notebook(master=frame2, height=450, width=300)
    tabs.grid(row=0, column=0)

    sessions = [tk.Frame(master=tabs)]
    session_times = [[]]

    def define_session(session):
        session_times.append([])
        text_box1 = tk.Text(master=session, height=5, width=10, font=('', 15))
        text_box1.grid(row=0, column=0, padx=5)
        text_box2 = tk.Text(master=session, height=3, width=20, font=('', 15))
        text_box2.grid(row=0, column=1)

        times = ''
        count = 0
        for i in session_times[sessions.index(session)]:
            times = times + str(count + 1) + '. ' + str(i) + ' sec' + '\n'
            count += 1
        text_box1.insert(tk.END, times.rstrip('\n'))
        text_box1.see(tk.END)
        text_box1.config(spacing1=3, spacing2=3, spacing3=3, state='disabled')

        fastest = slowest = average = 0.00
        if count != 0:
            fastest = min(session_times[sessions.index(session)])
            slowest = max(session_times[sessions.index(session)])
            average = "{:.2f}".format(sum(session_times[sessions.index(session)]) / count)

        details = 'Fastest solve: ' + str(fastest) + ' sec\n' + 'Slowest solve: ' + str(
            slowest) + ' sec\n' + 'Average time: ' + str(average)[:] + ' sec'
        text_box2.insert(tk.END, details)
        text_box2.config(spacing1=3, spacing2=3, spacing3=3, state='disabled')
        fig = Figure(figsize=(3, 3), dpi=100)
        # fig.subplots_adjust(bottom=1, top=2, left=1, right=2)
        plot = fig.add_subplot()
        plot.plot(session_times[sessions.index(session)])
        canvas = FigureCanvasTkAgg(fig, master=session)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

        def save():
            session_name = tk.simpledialog.askstring("Save Session", 'Enter Session Name:')
            add_session(session_name, session_times[sessions.index(session)])
            root.grab_set()

        def show():
            frame1.grid_remove()
            frame2.grid_remove()
            frame3.grid_remove()
            display_sessions(master=master, root=root)

        save_button = tkmac.Button(master=session, text='Save Session', command=lambda: save())
        save_button.grid(row=2, column=0)
        show_button = tkmac.Button(master=session, text='Show Saved Sessions', command=lambda: show())
        show_button.grid(row=2, column=1)

    tabs.add(sessions[0], text='Session 1')
    define_session(sessions[0])
    session_add = tk.Frame(master=tabs, height=450, width=200)
    tabs.add(session_add, text='+')
    tk.Label(master=session_add, text='Session name :').grid(row=0, column=0)
    name = tk.Entry(master=session_add)
    name.grid(row=0, column=1, pady=20)
    add = tk.Button(master=session_add, text='Add Session', command=lambda: add(name.get()))
    add.grid(row=1, column=0, columnspan=2, pady=10)

    def add(name):
        # tabs.hide(len(sessions))
        tabs.forget(session_add)
        sessions.append(tk.Frame(master=tabs))
        if name == '':
            tabs.add(sessions[-1], text='Session ' + str(len(sessions)))
        else:
            tabs.add(sessions[-1], text=name)
        tabs.add(session_add, text='+')
        define_session(sessions[-1])

    timer_control = 0
    root.bind('<space>', lambda event: keybind(event))

    def next_solve():
        if show_scramble.get() == 1:
            scramble_label.config(text=cm.scramble_cube()[0])
        time_str = clock.cget('text')
        if time_str.startswith('00:'):
            time_taken = float(time_str[3:])
        else:
            time_taken = float(time_str[:2]) * 60 + float(time_str[3:])

        session_times[tabs.index('current')] += [time_taken]
        define_session(sessions[tabs.index('current')])

    def keybind(event):
        nonlocal timer_control
        if timer_control == 0:  # reset timer
            clock.config(text='00:00.00')
            clock.config(fg='red')
            timer_control = 1
        elif timer_control == 1:  # start timer
            # scramble_label.config(text='')
            clock.config(fg='green')
            timer_control = 2
            timer()
        elif timer_control == 2:  # stop timer
            clock.config(fg='black')
            timer_control = 0
            next_solve()

    def timer():
        nonlocal timer_control
        now = time.time()
        while timer_control == 2:
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


if __name__ == '__main__':
    master = tk.Tk()
    master.configure(bg='#D3D3D3')
    # cube_timer(master=master)
    cube_timer(master=master, root=master)
    master.mainloop()
