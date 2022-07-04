import base64
import os
import tkinter
import io
from io import BytesIO
from tkinter import *
from tkinter import ttk, messagebox
import cv2
from rawkit import raw
import qrcode
from PIL import Image, ImageTk
import pymysql


class Cients:

    def __init__(self, master):
        self.SortDir = True;
        self.root = root

        self.root.title("Home")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="f.jpg")
        self.lbl = Label(self.root, image=self.bg).place(x=0, y=0)

        self.id = IntVar()
        self.em = StringVar()
        self.phn = StringVar()
        self.activ = StringVar()
        self.duration = StringVar()

        self.homeicon = ImageTk.PhotoImage(file="icons.png")
        self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
        self.backicon = ImageTk.PhotoImage(file="backcon.png")
        self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")

        self.admin = ImageTk.PhotoImage(file="admin1.jpg")
        # self.usr = ImageTk.PhotoImage(file="user.png")
        # self.wlt = ImageTk.PhotoImage(file="user.png")
        self.hw = ImageTk.PhotoImage(file="howto.jpg")

        framex = Frame(self.root, bg="#0b0205", relief=RIDGE)
        framex.place(x=0, y=0, width=1500, height=50)
        self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Lato", 15), bg="#0b0205",
                           fg="white", command=self.gotoHome).place(x=600, y=2)
        self.admins = Button(framex, text="admins", image=self.adminicon, compound=LEFT, font=("Lato", 15),bg="#0b0205",fg="white", command=self.gotoadmins).place(x=1100, y=2)


        self.backcon = Button(framex, text="Back", image=self.backicon, compound=LEFT,
                              font=("Lato", 15), bg="#0b0205", fg="white").place(x=100, y=2)
        self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Lato", 15),
                             bg="#0b0205", fg="white").place(x=300, y=2)
        self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Lato", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)
        self.frame1 = Frame(self.root, bg="#0b0205", relief=RIDGE)
        self.frame1.place(x=20, y=100, width=450, height=560)
        self.title = Label(self.frame1, text="Clients", font=("Lato", 20, "bold"), bg="#0b0205", fg="white")
        self.title.grid(row=0, columnspan=2, pady=50)
        idcl = Label(self.frame1, text="ID", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        idcl.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        idtxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.id)
        idtxt.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        namecl = Label(self.frame1, text="Email", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        namecl.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        nametxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.em)
        nametxt.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        ln = Label(self.frame1, text="Phone number", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        ln.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        lntxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.phn)
        lntxt.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        email = Label(self.frame1, text="Last activity", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        mailtxt = Entry(self.frame1, font=("Lato", 15, "bold"), textvariable=self.activ, bd=5, relief=GROOVE)
        mailtxt.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        last = Label(self.frame1, text="Duration", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        last.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        lasttxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.duration)
        lasttxt.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        newframe = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        newframe.place(x=30, y=550, width=430)

        btn = Button(newframe, text="Add", font=("Lato", 15, "bold"), width=6, command=self.addclient).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10)
        btn1 = Button(newframe, text="Update", font=("Lato", 15, "bold"), width=6, command=self.updateuser).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10)
        btn2 = Button(newframe, text="Delete", font=("Lato", 15, "bold"), width=6, command=self.deletedata).grid(row=0,
                                                                                                                 column=2,
                                                                                                                 padx=10,
                                                                                                                 pady=10)
        btn3 = Button(newframe, text="Details", font=("Lato", 15, "bold"), width=6, command=self.details).grid(row=0,
                                                                                                               column=3,
                                                                                                               padx=10,
                                                                                                               pady=10)

        sideframe = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        sideframe.place(x=500, y=100, width=800, height=650)

        searchbar = Label(sideframe, text="Search by", bg="#0b0205", fg="white", font=("Lato", 15, "bold"))
        searchbar.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.search = ttk.Combobox(sideframe, width=10, font=("Lato", 10, "bold"), state="readonly")
        self.search['values'] = ("Id", "Name", "email")
        self.search.grid(row=0, column=1, padx=20, pady=10)

        self.txtsearch = Entry(sideframe, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.txtsearch.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        searchbtn = Button(sideframe, text="Search", width=10, command=self.searchdata).grid(row=0, column=3, padx=10,
                                                                                             pady=10)
        showallbtn = Button(sideframe, text="Show all", width=10, command=self.fetchdata).grid(row=0, column=4, padx=10,
                                                                                               pady=10)
        frame2 = Frame(sideframe, bd=4, relief=RIDGE, bg="#0b0205")
        frame2.place(x=10, y=70, width=760, height=500)
        scrollx = Scrollbar(frame2, orient=HORIZONTAL)
        scrolly = Scrollbar(frame2, orient=VERTICAL)
        self.table = ttk.Treeview(frame2, columns=("id", "Name", "ln", "email", "phn", "gender", "bd"),
                                  xscrollcommand=scrollx.set,
                                  yscrollcommand=scrolly.set)

        style = ttk.Style(master)
        style.configure('Treeview', rowheight=50)
        style.map('')
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        self.table.heading("id", text="Id")
        self.table.heading("Name", text="Name")
        self.table.heading("ln", text="Last name")
        self.table.heading("email", text="email")
        self.table.heading("phn", text="Phone number")
        self.table.heading("gender", text="Gender")
        self.table.heading("bd", text="Birth date")
        self.table['show'] = "headings"
        self.table.column("id", width=50)
        self.table.column("Name", width=100)
        self.table.column("ln", width=100)
        self.table.column("email", width=150)
        self.table.column("phn", width=100)
        self.table.column("gender", width=100)

        self.p = self.table.column("bd", width=100)
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease-1>", self.getcur)
        img = Image.open("smtg.png")
        img1 = img.resize((130, 130), Image.ANTIALIAS)
        g = ImageTk.PhotoImage(img1)


        #img = Image.open(g)
        #ggg = img.resize((130, 130), Image.ANTIALIAS)
        self.h = Label(self.frame1, image=g)
        self.h.place(x=5, y=5, width=130, height=130)
        self.fetchdata()

    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def fetchdata(self):
        self.photo_list = []
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()

        cur.execute("SELECT * FROM user")
        """"
        crsr=conn.cursor()
        crsr.execute("SELECT img FROM user")
        data2 = crsr.fetchall()
        p=[]
        s=100
        k=0

        for r in data2:

            file_like2 = io.BytesIO(data2[0][0])
            o=ImageTk.PhotoImage(file_like2)
            img1 = Image.open(file_like2, mode='r').convert('RGB')
            for i in p:
                 pp=Label(self.table, image=img1).place(x=0, y=100+k,width=100, height=100)
                 p.append(pp)
                 k=k+s
                 """

        rows = cur.fetchall()

        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                # create another cursoor here and continue

                # print(row[1])
                # iii=row[5]
                # hg=self.write_file(row[6],"faces/"+row[1]+" "+row[2]+".jpg" )
                # print(image)
                # img = Image.open(BytesIO(rows))
                # im=base64.b64decode(row[6]).decode(encoding="utf-8")
                # Image.open(im)
                # img = Image.open(BytesIO(iii))
                # self.ph = ImageTk.PhotoImage(img)

                # img1 = img.resize((50, 100), Image.ANTIALIAS)
                # my_img = ImageTk.PhotoImage(img1)
                # my_img = Label(image=my_img)

                # self.table.insert('', END, values=row)
                self.table.insert('', END, values=(row[0], row[1], row[2], row[3], row[4], row[7], row[8]))
            conn.commit()
        conn.close()

    def getcur(self, ev):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
            cur = conn.cursor()
            cursorow = self.table.focus()
            contents = self.table.item(cursorow)
            row = contents['values']
            b = cur.execute("SELECT img FROM user where userid=%s", row[0])
            data2 = cur.fetchone()

            img = Image.open(BytesIO(data2[0]))
            img1 = img.resize((180, 130), Image.ANTIALIAS)


            cur.execute("select name from activity where usrid=%s", row[0])
            nameact = cur.fetchone()

            cur.execute("select duration from activity where usrid=%s", row[0])
            dur = cur.fetchone()

            # my_img = ImageTk.PhotoImage(img1)
            self.phh = ImageTk.PhotoImage(img1)
            self.id.set(str(row[0]))
            self.em.set(row[3])
            self.phn.set(row[4])
            self.title.config(text=row[1] + " " + row[2])
            self.activ.set(nameact)
            self.duration.set(dur)
            self.h.config(image=self.phh)
        except Exception as es:
            messagebox.showerror("Error", f"error due to:{str(es)}")

        """"
    def Showdetals(self):
        frm=topLevel()
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()

        cur.execute("Select date time from user where id=%s",self.id (
        """

    def updateuser(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()

        cur.execute("update user set email=%s, phone=%s where userid=%s", (
            self.em.get(),
            self.phn.get(),
            self.id.get()
        ))
        cur.execute("update activity set name=%s, duration=%s where usrid=%s", (
            self.activ.get(),
            self.duration.get(),

            self.id.get()

        ))
        conn.commit()
        self.fetchdata()
        conn.close()

    def deletedata(self):
        cnx = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = cnx.cursor()

        #cur.execute("ALTER TABLE activity ADD CONSTRAINT fk1 FOREIGN KEY (usrid) REFERENCES user (userid) ON DELETE CASCADE")
        cur.execute(" delete from user where userid=%s", self.id.get())





        cnx.commit()
        self.fetchdata()
        cnx.delete()

    def addclient(self):
        self.root.destroy()
        import Register

    def searchdata(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        if self.search.get() == "Id":
            cur.execute("SELECT * FROM user WHERE userid=%s", str(self.txtsearch.get()))
        elif self.search.get() == "Name":
            cur.execute("SELECT * FROM user WHERE firstname=%s", str(self.txtsearch.get()))
        elif self.search.get() == "email":
            cur.execute("SELECT * FROM user WHERE email=%s", str(self.txtsearch.get()))

        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
            conn.commit()
        else:
            messagebox.showerror("Error", "User doesn't exist, please enter valid user")
        conn.close()

    def details(self):
        self.fr = Toplevel()
        self.fr.geometry("500x500+550+250")
        self.fr.config(bg="#0b0205")
        # frame1.focus_force()
        self.fr.grab_set()
        #title = Label(self.fr, text="Details", font=("Lato", 20, "bold"), bg="#0b0205", fg="white")
        scrollx = Scrollbar(self.fr, orient=HORIZONTAL)
        scrolly = Scrollbar(self.fr, orient=VERTICAL)
        #title.grid(row=0, columnspan=2, pady=20)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.tb = ttk.Treeview(self.fr, columns=("name", "ln", "activity", "duration","nbrdays", "payed", "date", "hour"),
                               xscrollcommand=scrollx.set,
                               yscrollcommand=scrolly.set)

        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        self.tb.heading("name", text="Name")
        self.tb.heading("ln", text="Last name")
        self.tb.heading("activity", text="Activity")
        self.tb.heading("duration", text="Duration")
        self.tb.heading("nbrdays", text="Nbr days")
        self.tb.heading("payed", text="Payed")
        self.tb.heading("date", text="Date")
        self.tb.heading("hour", text="Hour")
        self.tb['show'] = "headings"
        self.tb.column("name", width=50)
        self.tb.column("ln", width=100)
        self.tb.column("activity", width=100)
        self.tb.column("duration", width=150)
        self.tb.column("nbrdays", width=150)
        self.tb.column("payed", width=100)
        self.tb.column("date", width=100)
        self.tb.column("hour", width=100)
        self.tb.pack(fill=BOTH, expand=1)
       # self.tb.bind("<ButtonRelease-1>", self.getcur)


        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()



        cur.execute("SELECT * FROM activity")
        rows = cur.fetchall()

        if len(rows) != 0:
            #self.tb.delete(*self.table.get_children())
            for row in rows:
                h= str(row[7])

                cur.execute("select firstname from user where userid=%s",h)
                nm=cur.fetchone()
                cur.execute("select lastname from user where userid=%s", h)
                ln = cur.fetchone()

                self.tb.insert('', END, values=(nm, ln, row[1], row[3],row[4], row[2], row[5], row[6]))
            conn.commit()
        conn.close()

    def gotoadmins(self):
        self.root.destroy()

        import Admins

    def gotoHome(self):
        self.root.destroy()

        import Home



root = Tk()
obj = Cients(root)
root.mainloop()

