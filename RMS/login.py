import os
import sqlite3
from tkinter import*
from datetime import*
from math import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from PIL import ImageDraw
from getpass import getpass
class Login:
    def __init__(self,w):
        self.w=w
        self.w.title("Login System")
        self.w.geometry('1350x700+0+0')
        self.w.config(bg="#021e2f")
        # ============left Bg Color===========
        left_lbl=Label(self.w,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=550)
        # ============Right Bg Color===========
        right_lbl=Label(self.w,bg="#031F3C",bd=0)
        right_lbl.place(x=550,y=0,relheight=1,relwidth=1)
        # =============Login Frames==================
        login_frame=Frame(self.w,bg="white")
        login_frame.place(x=441,y=80,width=550,height=400)

        title=Label(login_frame,text="Student Result Management System\nLogin Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=10)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="#08A3d2").place(x=50,y=100)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=130,width=350,height=30)
        
        password=Label(login_frame,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="#08A3d2").place(x=50,y=200)
        

        self.txt_password=Entry(login_frame,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=225,width=350,height=30)


        btn_register=Button(login_frame,text="Register New Account?",font=("times new roman",15),bd=0,fg="#DF005E",cursor="hand2",command=self.register_window).place(x=50,y=280)
        btn_forget=Button(login_frame,text="Forget Password",font=("times new roman",15),bg="white",bd=0,fg="#DF005E",cursor="hand2",command=self.forget_password_window).place(x=260,y=280)

        btn_login=Button(login_frame,text="Login",font=("times new roman",18,"bold"),bg="#DF005E",fg="white",bd=0,cursor="hand2",command=self.login).place(x=50,y=320,width=180,height=30)

    # =========== Clock Frame=============
        self.lbl=Label(self.w,bg="white",text="\nTime",font=("Book Antiqua",20,"bold"),fg="blue",compound=BOTTOM,bd=0)
        self.lbl.place(x=90,y=80,height=400,width=350)
        # self.clock_img()
        self.working()

    def reset(self):
        self.cmb_question.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_password.delete(0,END)

    def forget_password(self):
        if self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.w1)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select The Correct Security Question / Enter Answer",parent=self.w1)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(),(self.txt_email.get()),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been successfuly Reset,Please Login With New Password",parent=self.w1)
                    self.reset()
                    self.w1.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due To {str(ex)}",parent=self.w)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter Email Address To Reset Your Password",parent=self.w)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter Valid Email Address To Reset Your Password",parent=self.w)

                else:
                    con.close()
                    self.w1=Toplevel()
                    self.w1.title("Forget Password")
                    self.w1.geometry("350x400+442+110")
                    self.w1.config(bg="white")
                    self.w1.focus_force()
                    self.w1.grab_set()
                    t=Label(self.w1,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    question=Label(self.w1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                    self.cmb_question=ttk.Combobox(self.w1,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best friend Name")
                    self.cmb_question.place(x=50,y=130,width=200)
                    self.cmb_question.current(0)

                    answer=Label(self.w1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.w1,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=200)

                    new_password=Label(self.w1,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_password=Entry(self.w1,font=("times new roman",15),bg="lightgray")
                    self.txt_new_password.place(x=50,y=290,width=200)
                    btn_change_password=Button(self.w1,text="Reset Password",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.forget_password).place(x=80,y=340,height=30)

            except Exception as ex:
                messagebox.showerror("Error",f"Error Due To {str(ex)}",parent=self.w)

    def register_window(self):
        self.w.destroy()
        os.system("python register.py")

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.w)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),(self.txt_password.get()),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=self.w)

                else:
                    messagebox.showinfo("Success",f"Welcome:{self.txt_email.get()}",parent=self.w)
                    self.w.destroy()
                    os.system("python dashboard.py")
                con.commit()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due To {str(ex)}",parent=self.w)

    def clock_img(self,hr,min_,sec):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        origin=200,200
        # ========Hours line===============
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        # ========min line=================
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        # =========sec line==================
        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="orange")

        clock.save("images/myclock.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        self.clock_img(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="images/myclock.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

w=Tk()
obj=Login(w)
w.mainloop()