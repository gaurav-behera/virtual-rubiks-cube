# import mysql.connector
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


def sql_credentials():
    global databasePath
    databasePath = './utils/cube_db.sqlite'
    # global HOST_NAME, USER_NAME, PASSWORD
    # with open('./utils/db_credentials.txt', 'r') as handle:
    #     credentials = dict()
    #     for line in handle.readlines():
    #         credentials[line.partition('=')[0].strip()] = line.partition('=')[2].strip()
    #     HOST_NAME, USER_NAME, PASSWORD = credentials['host'], credentials['user'], credentials['passwd']
    # if PASSWORD == "":
    #     sql_window = tk.Tk()
    #     sql_window.title('MYSQL CONNECTION')
    #     sql_frame = tk.Frame(master=sql_window)
    #     sql_frame.pack()
    #     e1 = tk.Entry(master=sql_frame)
    #     e1.insert(tk.END, 'localhost')
    #     e2 = tk.Entry(master=sql_frame)
    #     e2.insert(tk.END, 'root')
    #     e3 = tk.Entry(master=sql_frame)
    #     tk.Label(sql_frame, text='Host : ').grid(row=0, column=0)
    #     e1.grid(row=0, column=1)
    #     tk.Label(sql_frame, text='User : ').grid(row=1, column=0)
    #     e2.grid(row=1, column=1)
    #     tk.Label(sql_frame, text='Passwd : ').grid(row=2, column=0)
    #     e3.grid(row=2, column=1)
    #     sql_window.wait_visibility()
    #     sql_window.grab_set()
    #     tk.Button(master=sql_frame, text='Apply', command=lambda: apply()).grid(row=3)

    #     def apply():
    #         HOST_NAME, USER_NAME, PASSWORD = e1.get(), e2.get(), e3.get()
    #         sql_window.destroy()
    #         with open('./utils/db_credentials.txt', 'w') as handle:
    #             handle.write('host=' + HOST_NAME + '\n')
    #             handle.write('user=' + USER_NAME + '\n')
    #             handle.write('passwd=' + PASSWORD)


def initialise_connection():
    global HOST_NAME, USER_NAME, PASSWORD

    # con = mysql.connector.connect(host=HOST_NAME, user=USER_NAME, passwd=PASSWORD)
    con = sqlite3.connect(databasePath)
    cursor = con.cursor()

    # creating database and tables
    # cursor.execute("CREATE DATABASE IF NOT EXISTS cube_db")
    # cursor.execute("USE cube_db")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS times(Session_Name varchar(20), Date_Time datetime, Average_Time varchar(10), "
        "Fastest_Solve varchar(10), Worst_Solve varchar(10), Solves_Count integer);")
    con.commit()
    return con, cursor


def add_session(name, times):
    con, cursor = initialise_connection()
    best = worst = avg = 0.0
    if len(times) != 0:
        avg = "{:.2f}".format(sum(times) / len(times))
        best, worst = min(times), max(times)
    query = "INSERT INTO times VALUES ('{}', datetime('now'), '{}', '{}', '{}', {})".format(name, str(avg), str(best), str(worst),
                                                                                  len(times))
    cursor.execute(query)
    con.commit()


def display_sessions(master=None, root=None):
    con, cursor = initialise_connection()
    cursor.execute("SELECT * FROM times ORDER BY Date_Time desc;")
    items = cursor.fetchall()

    style = ttk.Style()
    style.theme_use('aqua')
    style.map('Treeview', background=[('selected', '#99ccff')], foreground=[('selected', 'black')])
    style.configure("Treeview", font=(None, 15), rowheight=30, background='#D3D3D3', fieldbackground='#D3D3D3')

    table = ttk.Treeview(master=master, columns=('Name', 'Time', 'Avg', 'Min', 'Max', 'Num'), height='15',
                         show='tree', selectmode='browse')

    table.column('#0', width='0', anchor='center')
    table.column('Name', width='170', anchor='center')
    table.column('Time', width='220', anchor='center')
    table.column('Avg', width='160', anchor='center')
    table.column('Min', width='160', anchor='center')
    table.column('Max', width='160', anchor='center')
    table.column('Num', width='206', anchor='center')

    headings = tk.Label(master=master, bg='#D3D3D3')
    headings.grid(row=0, column=1, columnspan=7, pady=6)
    headings.config(text='SESSION NAME\t\tTIMESTAMP\t\tAVERAGE TIME\tBEST SOLVE\tWORST SOLVE\tNUMBER OF SOLVES\t\t')

    table.grid(row=1, column=0, padx=40, columnspan=8)
    count = 0
    for item in items:
        table.insert(parent='', index='end', iid=count, values=item)
        count += 1

    def delete():
        if table.item(table.focus(), 'values'):
            cursor.execute("DELETE FROM times WHERE Date_Time = '{}'".format(table.item(table.focus(), 'values')[1]))
            con.commit()
            table.delete(table.selection())

    def edit():
        if table.item(table.focus(), 'values'):
            edit_window = tk.Tk()
            edit_window.title('EDIT SESSION')
            e = [0, 0, 0, 0, 0, 0]
            edit_frame = tk.Frame(master=edit_window)
            edit_frame.pack()
            for i in range(6):
                e[i] = tk.Entry(master=edit_frame)
                e[i].insert(tk.END, table.item(table.focus(), 'values')[i])
            tk.Label(edit_frame, text='Session Name : ').grid(row=0, column=0)
            e[0].grid(row=0, column=1)
            tk.Label(edit_frame, text='Timestamp : ').grid(row=1, column=0)
            e[1].grid(row=1, column=1)
            tk.Label(edit_frame, text='Average Time : ').grid(row=2, column=0)
            e[2].grid(row=2, column=1)
            tk.Label(edit_frame, text='Best Solve : ').grid(row=3, column=0)
            e[3].grid(row=3, column=1)
            tk.Label(edit_frame, text='Worst Solve : ').grid(row=4, column=0)
            e[4].grid(row=4, column=1)
            tk.Label(edit_frame, text='Number of solves : ').grid(row=5, column=0)
            e[5].grid(row=5, column=1)

            def save():
                delete()
                cursor.execute("INSERT INTO times VALUES ('{}', CAST('{}' AS DATETIME), '{}', '{}', '{}', {})".format(
                    e[0].get(), e[1].get(), e[2].get(), e[3].get(), e[4].get(), int(e[5].get())))
                con.commit()
                edit_window.destroy()
                display_sessions(master)

            tk.Button(master=edit_frame, text='Save', command=lambda: save()).grid(row=6, column=1)
            tk.Button(master=edit_frame, text='Cancel', command=lambda: edit_window.destroy()).grid(row=6, column=0)
            edit_window.wait_visibility()
            edit_window.grab_set()

    def back():
        from cube_timer import cube_timer
        for widget in master.winfo_children():
            widget.destroy()
        cube_timer(master=master, root=root)

    edit_button = tk.Button(master=master, text='EDIT', bg='#D3D3D3', command=lambda: edit(), width=10)
    delete_button = tk.Button(master=master, text='DELETE', bg='#D3D3D3', command=lambda: delete(), width=10)
    back_button = tk.Button(master=master, text='BACK', bg='#D3D3D3', command=lambda: back(), width=10)
    edit_button.grid(row=2, column=6, sticky='E', pady=5)
    delete_button.grid(row=2, column=7, sticky='W')
    back_button.grid(row=2, column=1, sticky='W', padx=30)
