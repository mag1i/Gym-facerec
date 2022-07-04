import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import pyqrcode
import cv2
import io
import qrcode
import base64
import png
from tkcalendar import DateEntry

class Activty:


    def __init__(self,root):
         self.pay = DoubleVar()


         self.root=root

         self.root.title("Client activity0 window")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="white")


         self.bg = ImageTk.PhotoImage(file="f.jpg")
         bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

         self.left = ImageTk.PhotoImage(file="c.jpg")
         left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

         self.bln=False

         self.homeicon = ImageTk.PhotoImage(file="icons.png")
         self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
         self.backicon = ImageTk.PhotoImage(file="backcon.png")
         self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
         self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")

         framex = Frame(self.root, bg="#0b0205", relief=RIDGE)
         framex.place(x=0, y=0, width=1500, height=50)
         self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Andalus", 15), bg="#0b0205",
                           fg="white").place(x=600, y=2)
         self.admins = Button(framex, text="admins", image=self.adminicon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205", fg="white", command=self.gotoadmins).place(x=1100, y=2)

         self.backcon = Button(framex, text="Back", image=self.backicon,  compound=LEFT,
                               font=("Andalus", 15), bg="#0b0205", fg="white").place(x=100, y=2)
         self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205", fg="white",command= self.gotoclients).place(x=300, y=2)
         self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Andalus", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)

         frame1 = Frame(self.root, bg="#0b0205")
         frame1.place(x=480, y=100, width=700, height=500)
         tite = Label(frame1, text="Register here", font=("Lato", 20, "bold"), bg="#0b0205", fg="light blue").place(
             x=50, y=30)

         self.py = Label(frame1, text="Payment", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=370,
                                                                                                            y=240)
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

         btn = Button(frame1, text="Submit", font=("Lato", 10), bd=0, cursor="hand2", bg="light green",
                      command=self.addact).place(x=240, y=370, width=150)

    def gotoclients(self):
        self.root.destroy()

        import Clients

    def gotoadmins(self):
        self.root.destroy()

        import Admins

    def addact(self):
        if self.pytxt.get() == "" or self.daystxt.get() == "" or self.cmd_quest.get() == "Select" or self.cmdquest.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)



        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                cur = con.cursor()
                cur.execute("SELECT  MAX(userid) from user")
                g = cur.fetchone()
                print(g)

                cur.execute(
                    "insert into activity (name, price, duration, nbrdays) values(%s, %s, %s, %s)",
                    (
                     self.cmd_quest.get(),


                     self.pytxt.get(),
                     self.cmdquest.get(),

                     self.daystxt.get(),
                     ))
                h = cur.lastrowid
                cur.execute("update user set act=%s where userid=%s",(h, g))



                con.commit()

                con.close()
                messagebox.showinfo("Success", "User register succussfully")


            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}")


root = Tk()
obj = Activty(root)
root.mainloop()






