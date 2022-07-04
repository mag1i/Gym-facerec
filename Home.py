from tkinter import *
from tkinter import ttk, messagebox
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, time
from PIL import Image, ImageTk
import pymysql

# import pyserial
import serial

from tkcalendar import DateEntry
from time import sleep
import sys


# from mfrc522 import SimpleMFRC522
# reader = SimpleMFRC522()


class Home:
    def __init__(self, root):

        self.root = root

        self.dtString=datetime.today()

        self.root.title("Home")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bl=BooleanVar()
        self.bg = ImageTk.PhotoImage(file="f.jpg")
        self.lbl = Label(self.root, image=self.bg).place(x=0, y=0)

        self.homeicon = ImageTk.PhotoImage(file="icons.png")
        self.adminicon = ImageTk.PhotoImage(file="i2.jpg")
        self.backicon = ImageTk.PhotoImage(file="backcon.png")
        self.payments = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.clientiscon = ImageTk.PhotoImage(file="i3.jpg")
        img = Image.open("done.png")
        img1 = img.resize((180, 180), Image.ANTIALIAS)
        self.usr = ImageTk.PhotoImage(img1)

        img = Image.open("admin-settings-male.png")
        img1 = img.resize((180, 180), Image.ANTIALIAS)
        self.admin = ImageTk.PhotoImage(img1)

        self.wlt = ImageTk.PhotoImage(file="i3 - Copy.jpg")
        self.hw = ImageTk.PhotoImage(file="howto.jpg")

        framex = Frame(self.root, bg="#0b0205", relief=RIDGE)
        framex.place(x=0, y=0, width=1500, height=50)
        self.home = Button(framex, text="Home", image=self.homeicon, compound=LEFT, font=("Andalus", 15), bg="#0b0205",
                           fg="white").place(x=600, y=2)
        self.admins = Button(framex, text="admins", image=self.adminicon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205",
                             fg="white", command=self.gotoadmins).place(x=1100, y=2)
        self.backcon = Button(framex, text="Back", image=self.backicon, compound=LEFT,
                              font=("Andalus", 15), bg="#0b0205", fg="white").place(x=100, y=2)
        self.clntts = Button(framex, text="Clients", image=self.clientiscon, compound=LEFT, font=("Andalus", 15),
                             bg="#0b0205", fg="white", command=self.gotoclient).place(x=300, y=2)
        self.money = Button(framex, text="Walet", image=self.payments, compound=LEFT, font=("Andalus", 15),
                            bg="#0b0205", fg="white").place(x=900, y=2)

        lbrhr = Label(self.root, text="HOUR", font=("Andalus", 15), bg="#0b0205", fg="light blue")
        lbrhr.place(x=200, y=140, width=100, height=20)
        self.lbrhrd = Label(self.root, text="HOUR", font=("Andalus", 30), bg="#0b0205", fg="light blue")
        self.lbrhrd.place(x=200, y=65, width=100, height=70)
        lbrmin = Label(self.root, text="MINUT", font=("Andalus", 15), bg="#0b0205", fg="light blue")
        lbrmin.place(x=310, y=140, width=100, height=20)
        self.lbrmind = Label(self.root, text="MINUT", font=("Andalus", 30), bg="#0b0205", fg="light blue")
        self.lbrmind.place(x=310, y=65, width=100, height=70)
        lbrsec = Label(self.root, text="SECOND", font=("Andalus", 15), bg="#0b0205", fg="light blue")
        lbrsec.place(x=420, y=140, width=100, height=20)
        self.lbrsecd = Label(self.root, text="SECOND", font=("Andalus", 30), bg="#0b0205", fg="light blue")
        self.lbrsecd.place(x=420, y=65, width=100, height=70)
        lbrnn = Label(self.root, text="NOON", font=("Andalus", 15), bg="#0b0205", fg="light blue")
        lbrnn.place(x=540, y=140, width=100, height=20)
        self.lbrnnd = Label(self.root, text="AM", font=("Andalus", 30), bg="#0b0205", fg="light blue")
        self.lbrnnd.place(x=540, y=65, width=100, height=70)

        bbtn = Button(self.root, text="WECLOM TO GYM", font=("Andalus", 50), bg="#0b0205", fg="light blue")
        bbtn.place(x=650, y=65, width=680, heigh=70)

        frame0 = Frame(self.root, bg="#0b0205", bd=4, relief=RIDGE)
        frame0.place(x=300, y=170, width=390, height=500)
        # tite = Label(frame0, text="Home", font=("times new roman", 20, "bold"), bg="#0b0205",  fg="white").place(  x=50, y=30)

        self.one = Button(frame0, text="User", image=self.usr, font=("Andalus", 15), bd=0, bg="#0b0205", fg="#0b0205",
                          command=self.gotoclient).place(x=40, y=50, width=150, height=150)
        lblbone = Label(frame0, text="Client", font=("Andalus", 15), bd=0, bg="#0b0205", fg="white").place(x=80, y=210)
        self.two = Button(frame0, text="Admin", image=self.admin, font=("Andalus", 15), bd=0, bg="#0b0205",
                          fg="#0b0205", command=self.gotoadmins).place(x=230, y=50, width=150, height=150)
        lblbtwo = Label(frame0, text="Admins", font=("Andalus", 15), bd=0, bg="#0b0205", fg="white").place(x=280, y=210)

        self.three = Button(frame0, text="face rec", font=("Andalus", 15), bg="#0b0205", fg="white",
                            command=self.facerec).place(x=100, y=350, width=200, height=30)
        self.foor = Button(frame0, text="stop", font=("Andalus", 15), bg="#0b0205", fg="white",
                           command=self.stop).place(x=100, y=400, width=200, height=30)
        self.five = Button(frame0, text="Show in big screen", font=("Andalus", 15), bg="#0b0205", fg="white").place(
            x=100, y=300, width=200, height=30)

        sideframe = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        sideframe.place(x=700, y=170, width=650, height=500)

        searchbar = Label(sideframe, text="Search by", bg="#0b0205", fg="white", font=("Lato", 15, "bold"))
        searchbar.grid(row=0, column=0, pady=10, padx=5, sticky="w")

        self.search = ttk.Combobox(sideframe, width=10, font=("Lato", 10, "bold"), state="readonly")
        self.search['values'] = ("Id", "Name", "email")
        self.search.grid(row=0, column=1, padx=5, pady=10)

        self.txtsearch = Entry(sideframe, font=("Lato", 15, "bold"), bd=5, relief=GROOVE)
        self.txtsearch.grid(row=0, column=2, pady=15, padx=5, sticky="w")
        searchbtn = Button(sideframe, text="Search", width=10).grid(row=0, column=3, padx=5, pady=10)



        showallbtn = Button(sideframe, text="Show all", width=10).grid(row=0, column=4, padx=5, pady=10)

        frame2 = Frame(sideframe, bd=4, relief=RIDGE, bg="#0b0205")
        frame2.place(x=10, y=70, width=620, height=400)
        scrollx = Scrollbar(frame2, orient=HORIZONTAL)
        scrolly = Scrollbar(frame2, orient=VERTICAL)
        self.table = ttk.Treeview(frame2, columns=("id", "Name", "ln", "email", "phn", "gender", "bd"),
                                  xscrollcommand=scrollx.set,
                                  yscrollcommand=scrolly.set)

        # style = ttk.Style(master)
        # style.configure('Treeview', rowheight=50)
        # style.map('')
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
        self.table.heading("bd", text="Last activity")
        self.table['show'] = "headings"
        self.table.column("id", width=50)
        self.table.column("Name", width=100)
        self.table.column("ln", width=100)
        self.table.column("email", width=150)
        self.table.column("phn", width=100)
        self.table.column("gender", width=100)

        self.p = self.table.column("bd", width=100)
        self.table.pack(fill=BOTH, expand=1)
        # .table.bind("<ButtonRelease-1>", self.getcur)
        g = ImageTk.PhotoImage(file="smtg.png")

        frm = Frame(self.root, bd=4, relief=RIDGE, bg="#0b0205")
        frm.place(x=10, y=170, width=280, height=500)

        f = Frame(frm, bd=4, relief=RIDGE, bg="#0b0205")
        f.place(x=10, y=70, width=250, height=400)
        scrllx = Scrollbar(f, orient=HORIZONTAL)
        scrlly = Scrollbar(f, orient=VERTICAL)
        self.tb = ttk.Treeview(f, columns=("nm", "date", "hour"),
                               xscrollcommand=scrollx.set,
                               yscrollcommand=scrolly.set)

        # style = ttk.Style(master)
        # style.configure('Treeview', rowheight=50)
        # style.map('')
        scrllx.pack(side=BOTTOM, fill=X)
        scrlly.pack(side=RIGHT, fill=Y)
        scrllx.config(command=self.tb.xview)
        scrlly.config(command=self.tb.yview)
        self.tb.heading("nm", text="Name")

        self.tb.heading("hour", text="Hour")
        self.tb.heading("date", text="Date")

        self.tb['show'] = "headings"
        self.tb.column("nm", width=150)
        self.tb.column("hour", width=100)
        self.tb.column("date", width=100)

        self.tb.pack(fill=BOTH, expand=1)

        searchbar = Label(frm, text="Attending history", bg="#0b0205", fg="white", font=("Lato", 15, "bold"))
        searchbar.grid(row=0, column=2, pady=10, padx=5, sticky="w")

        #self.cal = DateEntry(frame2, width=12, background='darkblue', fg='white', bd=2, year=2010, day=30)
        #self.cal.place(x=500, y=320)
        #l = self.cal.get_date()

        #print(self.calculate_days(l))



        print(datetime.today().day)
        self.clock()

    def clock(self):
        n = datetime.now()
        h = str(n.strftime("%H"))
        m = str(n.strftime("%M"))
        s = str(n.strftime("%S"))
        if int(h) > 12 and int(m) > 0:
            self.lbrnnd.config(text="PM")
        if int(h) > 12:
            h = str((int(h)) - 12)

        self.lbrhrd.config(text=h)
        self.lbrmind.config(text=m)
        self.lbrsecd.config(text=s)
        self.lbrhrd.after(200, self.clock)

    def findEncodings(self, images):
        encodeList = []
        for img in images:
            try:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                print(encode)

                encodeList.append(encode)
            except Exception as e:
                print(e)

        return encodeList

    def markAttendance(self, name):

        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                td = datetime.today()
                self.dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{self.dtString}')
                self.tb.insert('', END, values=(name,td,  self.dtString))


    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr
    def facerec(self):
        self.bl = True
        messagebox._show("Click q to quit this window")
        path = 'faces'
        self.images = []
        self.classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        print(self.classNames)

        encodeListKnown = self.findEncodings(self.images)
        print('Encoding Complete')
        cap = cv2.VideoCapture(0)

        while self.bl:
            try:


                success, img = cap.read()
                if not success: break
                j = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                j = cv2.cvtColor(j, cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(j)
                encodesCurFrame = face_recognition.face_encodings(j, facesCurFrame)

                for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    # print(faceDis)
                    matchIndex = np.argmin(faceDis)

                    if faceDis[matchIndex] < 0.50:
                        name = self.classNames[matchIndex].upper()
                        self.markAttendance(name)
                    else:
                        name = 'Unknown'
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                cv2.imshow('Webcam', img)

                if cv2.waitKey(25) & 0xFF == ord('q'):

                    break
                    self.bl=False

            #cv2.waitKey(1)
            except Exception as e:
                print(e)




    def gotoadmins(self):
        self.root.destroy()

        import Admins

    def gotoclient(self):
        self.root.destroy()

        import Clients

    def stop(self):


        self.bl = False
        cv2.destroyAllWindows()

    def calculate_days(self, signdate):
        today = datetime.today()

        return signdate.day - today.day


    def getdays(self):
        conn = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE userid=%s", str(self.txtsearch.get()))

    """"
   def rfid(self):

      try:
          while True:
              print("Hold a tag near the reader")
              id, text = reader.read()
              print("ID: %s\nText: %s" % (id, text))
              sleep(5)
      except KeyboardInterrupt:
          GPIO.cleanup()
          raise
   """


root = Tk()
obj = Home(root)
root.mainloop()

