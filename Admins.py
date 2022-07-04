from tkinter import *
from tkinter import ttk, messagebox
import qrcode
from PIL import ImageTk
from tkcalendar import Calendar, DateEntry
import pymysql


class Admins:

    def __init__(self, root):
        self.root = root

        self.root.title("Home")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="f.jpg")
        self.lbl = Label(self.root, image=self.bg).place(x=0, y=0)

        self.id = IntVar()
        self.nm = StringVar()
        self.ln = StringVar()
        self.em = StringVar()
        self.phn = StringVar()

        self.homeicon = ImageTk.PhotoImage(file="icons.png")
        self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
        self.backicon = ImageTk.PhotoImage(file="backcon.png")
        self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")

        self.admin = ImageTk.PhotoImage(file="admin1.jpg")
       # self.usr = ImageTk.PhotoImage(file="user.png")
        #self.wlt = ImageTk.PhotoImage(file="wallet2.jpg")
        self.hw = ImageTk.PhotoImage(file="howto.jpg")

        framex = Frame(self.root, bg="#0b0205", relief=RIDGE)
        framex.place(x=0, y=0, width=1500, height=50)
        self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Lato", 15), bg="#0b0205",
                           fg="white", command=self.gotoHome).place(x=600, y=2)
        self.admins = Button(framex, text="admins", image=self.adminicon, compound=LEFT, font=("Lato", 15),
                             bg="#0b0205",
                             fg="white").place(x=1100, y=2)
        self.backcon = Button(framex, text="Back", image=self.backicon, compound=LEFT,
                              font=("Andalus", 15), bg="#0b0205", fg="white").place(x=100, y=2)
        self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Lato", 15),
                             bg="#0b0205", fg="white", command=self.gotoclnt).place(x=300, y=2)
        self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Lato", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)


        newframe = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        newframe.place(x=500, y=590, width=330)

        btn = Button(newframe, text="Add", font=("Lato", 15, "bold"), width=6, command=self.addpopup).grid(
            row=0, column=0, padx=10,
            pady=10)
        btn1 = Button(newframe, text="Update", font=("Lato", 15, "bold"), width=6,
                      command=self.updateadmin).grid(row=0, column=1,
                                                    padx=10, pady=10)
        btn2 = Button(newframe, text="Delete", font=("Lato", 15, "bold"), width=6,
                      command=self.deletedata).grid(row=0, column=2,
                                                    padx=10, pady=10)

        sideframe = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        sideframe.place(x=300, y=80, width=800, height=500)

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
        frame2.place(x=10, y=70, width=760, height=400)
        scrollx = Scrollbar(frame2, orient=HORIZONTAL)
        scrolly = Scrollbar(frame2, orient=VERTICAL)
        self.table = ttk.Treeview(frame2, columns=("id", "Name", "ln", "email", "phone"), xscrollcommand=scrollx.set,
                                  yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        self.table.heading("id", text="Id")
        self.table.heading("Name", text="Name")
        self.table.heading("ln", text="Last name")
        self.table.heading("email", text="email")
        self.table.heading("phone", text="Phone Number")
        self.table['show'] = "headings"
        self.table.column("id", width=50)
        self.table.column("Name", width=100)
        self.table.column("ln", width=100)
        self.table.column("email", width=150)
        self.table.column("phone", width=100)
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease-1>", self.getcur)
        self.fetchdata()
    def updateadmin(self):

        frame1 = Toplevel()
        frame1.geometry("500x500+550+250")
        frame1.config(bg="#0b0205")
        frame1.focus_force()
        frame1.grab_set()
        title = Label(frame1, text="Admin", font=("Lato", 20, "bold"), bg="#0b0205", fg="white")
        title.grid(row=0, columnspan=2, pady=20)
        idcl = Label(frame1, text="Name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        idcl.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        idtxt = Entry(frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.nm)
        idtxt.grid(row=1, column=1, pady=10, padx=20, sticky="w")


        ln = Label(frame1, text="Last name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        ln.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        lntxt = Entry(frame1, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.ln)
        lntxt.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        email = Label(frame1, text="Email", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        mailtxt = Entry(frame1, font=("Lato", 15, "bold"), textvariable=self.em, bd=5, relief=GROOVE)
        mailtxt.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        phn = Label(frame1, text="Phone number", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        phn.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        phnttxt = Entry(frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.phn)
        phnttxt.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        bt=Button(frame1, text="Done", command=self.updateuser).place(x=200, y=400, width=100)

    def fetchdata(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())

            for row in rows:
                self.table.insert('', END, values=row)
                """"
                qr = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                qr.add_data(row)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                img.save('qrcode001.png')
                """
            conn.commit()
        conn.close()

    def getcur(self, ev):
        cursorow = self.table.focus()
        contents = self.table.item(cursorow)
        row = contents['values']
        self.id.set(row[0])
        self.nm.set(row[1])
        self.ln.set(row[2])
        self.em.set(row[3])
        self.phn.set(row[4])

    def updateuser(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        cur.execute("update admin set firstname=%s, lastname=%s, email=%s, phonenum=%s where id=%s", (

            self.nm.get(),
            self.ln.get(),
            self.em.get(),
            self.phn.get(),
            self.id.get()

        ))
        conn.commit()
        self.fetchdata()
        conn.close()

    def deletedata(self):
        cnx = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = cnx.cursor()
        cur.execute("delete from admin where id=%s", self.id.get())
        cnx.commit()
        self.fetchdata()
        cnx.delete()

    def addpopup(self):
        self.frame1 = Toplevel()
        self.frame1.geometry("500x500+550+250")
        self.frame1.config(bg="#0b0205")
        # frame1.focus_force()
        self.frame1.grab_set()
        title = Label(self.frame1, text="Add Admin", font=("Lato", 20, "bold"), bg="#0b0205", fg="white")
        title.grid(row=0, columnspan=2, pady=20)
        nm = Label(self.frame1, text="Name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        nm.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.nmtxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.nmtxt.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        self.ln = Label(self.frame1, text="Last name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        self.ln.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.lntxt = Entry(self.frame1, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.lntxt.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        email = Label(self.frame1, text="Email", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.mailtxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.mailtxt.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        phn = Label(self.frame1, text="Phone number", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        phn.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        self.phnttxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.phnttxt.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        bd = Label(self.frame1, text="Birthdate", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        bd.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        # self.bdtxt = Entry(frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        # self.bdtxt.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # c = Calendar(frame1, font="Arial 14", selectmode='day', cursor="hand1", year=2020, month=2, day=5).grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.cal = DateEntry(self.frame1, width=12, background='darkblue', fg='white', bd=2, year=2010)
        self.cal.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        pw = Label(self.frame1, text="Password", font=("Lato", 15, "bold"), bg="#0b0205", fg="white")
        pw.grid(row=11, column=0, pady=10, padx=20, sticky="w")
        self.pwtxt = Entry(self.frame1, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.pwtxt.grid(row=11, column=1, pady=10, padx=20, sticky="w")
        bt = Button(self.frame1, text="Done", command=self.addadmin).grid(row=12, column=1, pady=10, padx=20,
                                                                          sticky="w")

    def addadmin(self):



        if self.nmtxt.get()=="" or self.lntxt.get()=="" or self.mailtxt.get()=="" or self.phnttxt.get()=="" or self.pwtxt.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:


             try:
                 con=pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                 cur=con.cursor()
                 cur.execute("SELECT * FROM admin WHERE email=%s",self.mailtxt.get())
                 row= cur.fetchone()
                 print(row)
                 if row!=None:
                     messagebox.showerror("Error", "User already exists, please try with another email")

                 else:

                     cur.execute("insert into admin (firstname, lastname, email, phonenum, password, bd) values(%s, %s,%s,%s,%s, %s)", (self.nmtxt.get(), self.lntxt.get(),self.mailtxt.get(), self.phnttxt.get(), "22", self.cal.get_date()))
                     con.commit()
                     self.fetchdata()
                     con.close()
                     self.frame1.destroy()
                     messagebox.showinfo("Success", "Admin added succussfully")



             except Exception as es:
                 messagebox.showerror("Error", f"error due to:{str(es)}")

    def gotoclnt(self):
        self.root.destroy()
        import Clients

    def gotoHome(self):
        self.root.destroy()

        import Home


    def searchdata(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        if self.search.get() == "Id":
            cur.execute("SELECT * FROM admin WHERE id=%s", str(self.txtsearch.get()))
        elif self.search.get() == "Name":
            cur.execute("SELECT * FROM admin WHERE firstname=%s", str(self.txtsearch.get()))
        elif self.search.get() == "email":
            cur.execute("SELECT * FROM admin WHERE email=%s", str(self.txtsearch.get()))

        rows = cur.fetchall()

        if len(rows) != 0:
            self.table.delete(*self.table.get_children())

            for row in rows:
                self.table.insert('', END, values=row)
            conn.commit()

        else:
            messagebox.showerror("Error", "Admin doesn't exist")
        conn.close()

root = Tk()
obj = Admins(root)
root.mainloop()

