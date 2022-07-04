import qrcode
from MyQR import myqr
import base64
import os

from tkinter import *
from tkinter import ttk, messagebox

from PIL import ImageTk
import pymysql


class Getqr:

    def __init__(self, root):
        self.root = root

        self.root.title("Home")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="f.jpg")
        self.lbl = Label(self.root, image=self.bg).place(x=0, y=0)
        self.table = ttk.Treeview(self.root, columns=("id", "Name", "ln", "email", "act"))

        self.table.heading("id", text="Id")
        self.table.heading("Name", text="Name")
        self.table.heading("ln", text="Last name")
        self.table.heading("email", text="email")
        self.table.heading("act", text="Last acivity")
        self.table['show'] = "headings"
        self.table.column("id", width=50)
        self.table.column("Name", width=100)
        self.table.column("ln", width=100)
        self.table.column("email", width=150)
        self.table.column("act", width=100)
        self.table.pack(fill=BOTH, expand=1)
        self.qrr()


    def qrr(self):

        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)

            lines=rows

            for i in range(0,len(lines)):
                data=self.email.get().encode()
                name= base64.b64encode(data)

                version, level, qrname=myqr.run(
                str(name),
                level='H',
                version=1,
                picture='howto.jpg',
                colorized=True,
                contrast=1.0,
                brightness=1.0,
                save_name=str(lines[i],'.bmp'),
                save_dir=os.getcwd()
            )


        conn.commit()
        conn.close()

root = Tk()
obj = Getqr(root)
root.mainloop()

