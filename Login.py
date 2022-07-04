from tkinter import *
from tkinter import ttk, messagebox


from PIL import ImageTk
import pymysql


class Lgn:


      def __init__(self,root):

         self.root=root


         self.root.title("Login window")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="white")

         self.bg = ImageTk.PhotoImage(file="f.jpg")
         self.lbl = Label(self.root, image=self.bg).place(x=0, y=0)

         self.left = ImageTk.PhotoImage(file="c.jpg")
         left = Label(self.root, image=self.left).place(x=250, y=90, width=400, height=500)


         frame2 = Frame(self.root, bg="#0b0205", relief=RIDGE)
         frame2.place(x=650, y=90, width=350, height=500)
         tite = Label(frame2, text="Login here", font=("Elephant", 30, "bold"), bg="#0b0205", fg="white").place(x=0, y=30, relwidth=1)
         self.usermail=StringVar()
         self.userpwvar=StringVar()
         self.userlbl=Label(frame2, text="email", font=("Andalus", 15), bg="#0b0205", fg="white").place(x=50, y=100)
         txtuserm=Entry(frame2, font=("times new roman", 15), bg="gray",textvariable=self.usermail).place(x=50, y=140, width=250)

         self.userpwlbl = Label(frame2, text="password", font=("Andalus", 15), bg = "#0b0205", fg = "white").place(x=50, y=190)
         txtpwuser = Entry(frame2,show="*", font=("times new roman", 15), bg = "gray", textvariable=self.userpwvar).place(x=50, y=230, width=250)

         btnlgn= Button(frame2,command=self.login, text="Log In", font=("Arial Rounded MT Bold", 15), bg="light blue", activebackground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)
         ht=Label(frame2, bg="lightgray" ).place(x=50, y=370, width=250, height=2)
         or_=Label(frame2,text="OR", bg="#0b0205",fg="lightgray", font=("times new roman",15, "bold")).place(x=150, y=350)
         frgt=Button(frame2,text="Forgot password?", font=("Arial Rounded MT Bold", 13), bg="#0b0205", fg="light gray", bd=0, command=self.forgotpw ).place(x=100, y=400 )
      def login(self):


          if self.usermail.get()=="" or self.userpwvar.get()=="":
               messagebox.showerror("Error", "No field should be empty", parent= self.root)

          else:
              try:
                  con= pymysql.connect(host="localhost", user="root" ,password="1234", database="Gym")
                  cur= con.cursor()
                  cur.execute("SELECT* FROM admin WHERE email=%s AND password=%s", (self.usermail.get(), self.userpwvar.get()))
                  row= cur.fetchone()
                  if row==None:
                      messagebox.showerror("Error", "Invalid username or password \n try again with valid information",parent=self.root)

                  else:
                      messagebox.showinfo("Success", "Welcome admin", parent=self.root)
                  con.close()


              except EXCEPTION as es:
                  messagebox.showerror("Error", f"Error due to: {str(es)}")




      def goto(self):
          self.root.destroy()
          import Register



      def forgotpw(self):


          if self.usermail.get()=="":
              messagebox.showerror("Error","Please enter a valid email to reset your password", parent= self.root )
          else:
              try:
                  con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                  cur = con.cursor()
                  cur.execute("SELECT* FROM admin WHERE email=%s", (self.usermail.get()))
                  row = cur.fetchone()
                  if row == None:
                      messagebox.showerror("Error","Please enter a valid email to reset your password", parent= self.root )


                  else:
                      self.root2 = Toplevel()
                      self.root2.title("forgot password")
                      self.root2.geometry("400x400+450+150")
                      self.root2.config(bg="white")
                      self.root2.focus_force()
                      self.root2.grab_set()
                      t = Label(self.root2, text="Forgot password", font=("Lato", 20, "bold"), bg="white",
                                fg="red").place(x=0, y=10, relwidth=1)

                      self.seccode = StringVar()
                      self.newpw = StringVar()
                      sec = Label(self.root2, text="Secutity code", font=("Andalus", 15), bg="white",fg="#0b0205").place(x=50, y=100)

                      self.txtcoodesec = Entry(self.root2, font=("times new roman", 15), bg="gray", textvariable=self.seccode).place(x=50, y=140, width=250)

                      self.new = Label(self.root2, text="set new password", font=("Andalus", 15), bg="white",
                                         fg="#0b0205").place(x=50, y=190)
                      txtnewpw = Entry(self.root2, show="*", font=("times new roman", 15), bg="gray", textvariable=self.newpw ).place(x=50, y=230, width=250)

                      btnsetnewpw = Button(self.root2, text="Reset password", font=("Arial Rounded MT Bold", 15),
                                           bg="light blue", activebackground="white", cursor="hand2", command=self.resetpw).place(x=50, y=300,  width=250, height=35)




                  con.close()


              except EXCEPTION as es:
                  messagebox.showerror("Error", f"Error due to: {str(es)}")

      def resetpw(self):
          if self.seccode.get()=="" or self.newpw.get()=="":
              messagebox.showerror("Error", "Please fill the required fields", parent=self.root2)
          else:
              try:
                  if self.seccode.get()!="1234":
                      messagebox.showerror("Error", "Please enter a correct security code", parent=self.root2)
                  else:
                      con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
                      cur = con.cursor()
                      #cur.execute("SELECT * FROM admin WHERE email=%s", (self.usermail.get()))
                      #row = cur.fetchone()
                      cur.execute("update admin set password=%s WHERE email=%s", (self.newpw.get(), self.usermail.get()))
                      con.commit()
                      con.close()
                      self.root2.destroy()
                      messagebox.showinfo("Success", "Your password has been reset, Please log in with the new password")



              except EXCEPTION as es:
                  messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root2)


root = Tk()
obj = Lgn(root)
root.mainloop()

