import os
import shutil
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import pymysql
import pyqrcode
import cv2
import io
import qrcode
import base64
import png
from tkcalendar import DateEntry
from datetime import datetime


class Rgstr:

    def __init__(self, root):

        self.root = root
        self.r = IntVar()

        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="f.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="c.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        self.bln = False

        self.homeicon = ImageTk.PhotoImage(file="icons.png")
        self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
        self.backicon = ImageTk.PhotoImage(file="backcon.png")
        self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")

        framex = Frame(self.root, bg="#0b0205", relief=RIDGE)
        framex.place(x=0, y=0, width=1500, height=50)
        self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Andalus", 15), bg="#0b0205",
                           fg="white", command=self.gotohome).place(x=600, y=2)
        self.admins = Button(framex, text="admins", image=self.adminicon, command=self.gotoadmins, compound=LEFT,
                             font=("Andalus", 15),
                             bg="#0b0205",
                             fg="white").place(x=1100, y=2)
        self.backcon = Button(framex, text="Back", image=self.backicon, compound=LEFT,
                              font=("Lato", 15), bg="#0b0205", fg="white").place(x=100, y=2)
        self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Lato", 15),
                             bg="#0b0205", fg="white", command=self.gotoclients).place(x=300, y=2)
        self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Lato", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)

        frame1 = Frame(self.root, bg="#0b0205")
        frame1.place(x=480, y=100, width=700, height=500)
        tite = Label(frame1, text="Register here", font=("Lato", 20, "bold"), bg="#0b0205", fg="light blue").place(
            x=50, y=30)

        self.name = Label(frame1, text="First name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=50, y=100)
        self.txtFname = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray")
        self.txtFname.place(x=50, y=130, width=250)

        self.Lastname = Label(frame1, text="Last name", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=370, y=100)
        self.lntxt = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray")
        self.lntxt.place(x=370, y=130, width=250)

        self.email = Label(frame1, text="Email", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=50, y=170)
        self.mailtxt = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray")
        self.mailtxt.place(x=50, y=200, width=250)

        self.Phone = Label(frame1, text="Phone number", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=370, y=170)
        self.phntxt = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray")
        self.phntxt.place(x=370, y=200, width=250)

        self.bd = Label(frame1, text="Birth date", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=370, y=320)
        self.cal = DateEntry(frame1, width=12, background='darkblue', fg='white', bd=2, year=2010)
        self.cal.place(x=500, y=320)

        self.varcheck = IntVar()

        self.radio_v = StringVar()
        self.radio_v.set('Female')
        self.gndr = Label(frame1, text="Gender", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=370, y=270)
        r1 = Radiobutton(frame1, text='Male', variable=self.radio_v, value='Male')
        r1.place(x=540, y=270, width=80)

        r2 = Radiobutton(frame1, text='Female', variable=self.radio_v, value='Female')
        r2.place(x=460, y=270, width=80)

        self.btnfile = Button(frame1, text="Or Upload file", font=("Lato", 10), bd=0, cursor="hand2", bg="white",
                          command=self.fileDailog).place(x=160, y=250 , width=90)

        self.btn = Button(frame1, text="REGISTER", font=("Lato", 10), bd=0, cursor="hand2", bg="light green",
                          command=self.regdata).place(x=370, y=440)
        self.btn = Button(frame1, text="Next", font=("Lato", 10), bd=0, cursor="hand2", bg="light green",
                          command=self.activity).place(x=470, y=440)
        self.btnlgn = Button(frame1, text="Save picture", font=("Lato", 10), bd=0, cursor="hand2",
                             command=self.takepic).place(x=50, y=250, width=100)
        self.lblpic = Label(frame1, bd=2)
        self.lblpic.place(x=50, y=270, width=240, height=190)

    def clear(self):
        self.txtFname.delete(0, END)
        self.lntxt.delete(0, END)
        self.mailtxt.delete(0, END)

    def takepic(self):
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while (result):
            ret, frame = videoCaptureObject.read()
            cv2.imwrite("faces/" + self.txtFname.get() + " " + self.lntxt.get() + ".jpg", frame)

            result = False

        videoCaptureObject.release()
        self.bln = True
        j = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        j = cv2.cvtColor(j, cv2.COLOR_BGR2RGB)

        if ret:  # frame captured without any errors
            # cv2.namedWindow("cam-test", cv2.CV_WINDOW_AUTOSIZE)
            # j=cv2.imshow("cam-test", frame)
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            img1 = img.resize((250, 190), Image.ANTIALIAS)
            self.h = ImageTk.PhotoImage(img1)

            self.lblpic.config(image=self.h)

        # cv2.waitKey(0)
        # destroyWindow("cam-test")
        # imwrite("filename.jpg", img)  # save image

    def regdata(self):
        if self.bln == True:
            with open("faces/" + self.txtFname.get() + " " + self.lntxt.get() + ".jpg", 'rb') as file:
                self.binaryData = file.read()

        # file = self.convertToBinaryData(biodataFile)

        if self.txtFname.get() == "" or self.lntxt.get() == "" or self.phntxt.get() == "":
            messagebox.showerror("Error", "Those fields are required", parent=self.root)

        elif self.varcheck.get() == 0:
            messagebox.showerror("Error", "Please agree on out terms and conditions of use", parent=self.root)
        elif self.bln == False:
            messagebox.showerror("Error", "Please Take a pic first", parent=self.root)

        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE email=%s", self.mailtxt.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User already exists, please try with another email",
                                         parent=self.root)

                else:
                    cur.execute(
                        "insert into user (firstname,lastname, email, phone ,  img,gender, dateinsc, bd) values(%s, %s,%s,%s, %s, %s, %s, %s)",
                        (self.txtFname.get(),
                         self.lntxt.get(),
                         self.mailtxt.get(),
                         self.phntxt.get(),
                         # self.pwtxtFramw.get(),
                         # self.pwcnftxtFramw.get(),
                         self.binaryData,
                         self.radio_v.get(),
                         datetime.now(),
                         self.cal.get_date()
                         )

                    )

                    self.r = cur.lastrowid
                    print(self.r)

                    con.commit()

                    con.close()
                    print("fuck")
                    #self.activity()

                    messagebox.showinfo("Success", "User register succussfully")
                    #self.Nxt()

                    #self.root.destroy()

                    #import Act

            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}")

            # , self.lntxt.get(), self.mailtxt.get(), self.Phntxt.get(), self.cmd_quest.get())

    def gotoclients(self):

        self.root.destroy()

        import Clients

    def fileDailog(self):
        self.bln=True
        self.fileName = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")))

        img = Image.open(self.fileName)
        img1 = img.resize((200, 200), Image.ANTIALIAS)
        imm = ImageTk.PhotoImage(img1)

        self.lblpic.config(image=imm)



    def gotoadmins(self):
        self.root.destroy()

        import Admins

    def gotohome(self):
        self.root.destroy()

        import Home

    def getid(self):
        return self.r

    def Nxt(self):
        cnx = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = cnx.cursor()
        # cur.execute("select userid from user where userid=5")
        s = cur.execute("select userid from user where email=%s", self.mailtxt.get())
        url = pyqrcode.create(s)

        # url.png_as_base64_str(self.root)

        url.svg("client.svg", scale=8)
        url.png('client.png', scale=6)
        # pyqrcode.QRCode.show(self.root)
        url.show(self.root)

        cnx.commit()
        # self.root.destroy()
        # Import NextReg

    def activity(self):
        self.actframe = Toplevel()
        self.actframe.geometry("1350x700+0+0")
        self.actframe.config(bg="#0b0205")
        # frame1.focus_force()
        self.actframe.grab_set()

        self.pay = DoubleVar()

        self.actframe.title("Client activity window")
        self.actframe.geometry("1350x700+0+0")
        self.actframe.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="f.jpg")
        bg = Label(self.actframe, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="c.jpg")
        left = Label(self.actframe, image=self.left).place(x=80, y=100, width=400, height=500)

        self.bln = False

        self.homeicon = ImageTk.PhotoImage(file="icons.png")
        self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
        self.backicon = ImageTk.PhotoImage(file="backcon.png")
        self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")

        framex = Frame(self.actframe, bg="#0b0205", relief=RIDGE)
        framex.place(x=0, y=0, width=1500, height=50)
        self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Andalus", 15), bg="#0b0205",
                           fg="white").place(x=600, y=2)
        self.admins = Button(framex, text="admins", image=self.adminicon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205",
                             fg="white").place(x=1100, y=2)
        self.backcon = Button(framex, text="Back", image=self.backicon, compound=LEFT,
                              font=("Andalus", 15), bg="#0b0205", fg="white").place(x=100, y=2)
        self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205", fg="white").place(x=300, y=2)
        self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Andalus", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)

        frame1 = Frame(self.actframe, bg="#0b0205")
        frame1.place(x=480, y=100, width=700, height=500)
        tite = Label(frame1, text="Register here", font=("Lato", 20, "bold"), bg="#0b0205", fg="light blue").place(
            x=50, y=30)

        self.py = Label(frame1, text="Payment", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=370, y=240)
        self.pytxt = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray", textvariable=self.pay)
        self.pytxt.place(x=370, y=270, width=250)

        self.days = Label(frame1, text="Days number", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=370,
                                                                                                                 y=170)
        self.daystxt = Entry(frame1, font=("Lato", 15), bg="lightgray", fg="gray")
        self.daystxt.place(x=370, y=200, width=250)

        self.Pay = Label(frame1, text="Duration", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=50,
                                                                                                             y=170)

        self.cmdquest = ttk.Combobox(frame1, font=("Lato", 13), state='readonly', justify=CENTER)
        self.cmdquest['values'] = ("Select", "Daily", "weekly", "monthly")
        self.cmdquest.place(x=50, y=200, width=250)
        self.cmdquest.current(0)

        Payment = Label(frame1, text="Activity", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
            x=50, y=240)
        self.cmd_quest = ttk.Combobox(frame1, font=("Lato", 13), state='readonly', justify=CENTER)
        self.cmd_quest['values'] = (
            "Select", "Aerobic", "weightlifting ", "musculation", "sona", "Aerobic sona", "musculation sona",
            "Racewalking, jogging, or running.", "losing weight activity", "Bicycling")
        self.cmd_quest.place(x=50, y=270, width=250)
        self.cmd_quest.current(0)



        self.check = Checkbutton(frame1, text="Payed", variable=self.varcheck, onvalue=1,
                                 offvalue=0, bg="white",
                                 font=("Lato", 12)).place(x=50, y=370)


        btn = Button(frame1, text="Submit", font=("Lato", 10), bd=0, cursor="hand2", bg="light green",
                     command=self.addact).place(x=240, y=370, width=150)

    def addact(self):
        if self.pytxt.get() == "" or self.daystxt.get() == "" or self.cmd_quest.get() == "Select" or self.cmdquest.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.actframe)



        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                cur = con.cursor()
                now = datetime.now()
                hr = now.time()

                cur.execute(
                    "insert into activity (name, price, duration, nbrdays, datepay, hr, usrid) values(%s, %s, %s, %s, %s, %s, %s)",
                    (self.cmd_quest.get(),
                     self.pytxt.get(),

                     self.cmdquest.get(),

                     self.daystxt.get(),
                     now,
                     str(hr),
                     self.r
                     ))
                h = cur.lastrowid





                print(hr)
                #cur.execute("update user set act=%s where userid=%s", (h, self.r))
               # cur.execute("insert into payment (iduser, idact, datepay, paymentamount )  values (%s, %s, %s, %s )",
                #           (self.r, h,now, self.pytxt ))
                con.commit()

                con.close()
                self.actframe.destroy()
                self.root.destroy()
                import Clients



            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}")


root = Tk()
obj = Rgstr(root)
root.mainloop()















