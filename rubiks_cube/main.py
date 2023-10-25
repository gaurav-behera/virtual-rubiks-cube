import tkinter as tk
import tkinter.ttk as ttk
import virtual_cube
import cube_solver
import cube_timer
import db


root = tk.Tk()
root.title("Rubik's Cube")
root.configure(bg='#D3D3D3')

# root.geometry("1400x570")
db.sql_credentials()

notebook = ttk.Notebook(master=root)
notebook.pack()
frame1 = tk.Frame(notebook, bg='#D3D3D3')
frame2 = tk.Frame(notebook, bg='#D3D3D3')
frame3 = tk.Frame(notebook, bg='#D3D3D3')
notebook.add(frame1, text='Cube Solver')
notebook.add(frame2, text='Virtual Cube')
notebook.add(frame3, text='Cube Timer')

cube_solver.solve_cube(master=frame1)
virtual_cube.virtual_cube(master=frame2)
cube_timer.cube_timer(master=frame3, root=root)

root.mainloop()
