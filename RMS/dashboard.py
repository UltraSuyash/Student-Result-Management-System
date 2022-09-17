from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from courses import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import ttk,messagebox
import os
import sqlite3
from datetime import*
from math import*
from PIL import Image,ImageTk
from PIL import ImageDraw
class RMS:
    def __init__(self,w):
        self.w=w
        self.w.title("Student Result Management System")
        self.w.geometry('1350x700+0+0')
        self.w.config(bg="white")
#===================icon====================
        self.logo_dash=PhotoImage(file="images/logo_p.png")

#===================Title====================
        title=Label(self.w,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("New Roman",20,"bold"),bg="#0b5377",fg="white").place(x=0,y=0,relwidth=1,height=50)

#=================Main Menu===================
        m_frame=LabelFrame(self.w,text="Menus",font=("times new roman",15),bg="white")
        m_frame.place(x=10,y=70,width=1067,height=80)

#=================Button=======================
        btn_course=Button(m_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=155,height=40)
        btn_student=Button(m_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=195,y=5,width=155,height=40)
        btn_result=Button(m_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=375,y=5,width=155,height=40)
        btn_view=Button(m_frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=555,y=5,width=155,height=40)
        btn_logout=Button(m_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.Logout).place(x=735,y=5,width=155,height=40)
        btn_exit=Button(m_frame,text="Exit",font=("goudy old sty1001"
                                                  "le",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.Exit).place(x=910,y=5,width=150,height=40)

#==================Content Window===============
        filename="images/bg.png"
        self.bg_img=Image.open(filename)
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl=Label(self.w,image=self.bg_img).place(x=320,y=150,width=750,height=300)

#===================Update label==================
        self.lbl_course=Label(self.w,text="Total Course\n[0]",font=("gudy old style",15),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=460,width=200,height=75)
        self.lbl_student = Label(self.w, text="Total Students\n[0]", font=("gudy old style", 15), bd=10, relief=RIDGE,bg="#0676ad", fg="white")
        self.lbl_student.place(x=610, y=460, width=200, height=75)
        self.lbl_result = Label(self.w, text="Total Results\n[0]",font=("gudy old style", 15), bd=10, relief=RIDGE,bg="#038074", fg="white")
        self.lbl_result.place(x=820, y=460, width=200, height=75)
        # =========== Clock Frame=============
        self.lbl=Label(self.w,bg="white",font=("Book Antiqua",20,"bold"),fg="blue",compound=BOTTOM,bd=0)
        self.lbl.place(x=8,y=150,height=385,width=308)
        # self.clock_img()
        self.working()


        #=====================Footer Area==================
        footer=Label(self.w,text="SRMS-Student Result Management System\Contact Us For Any Technical Issue:+919690402370",font=("goudy old Style",12,"bold"),bg="blue",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#=========================================
    def update_details(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            # self.lbl_student.after(200,self.update_details)

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            # self.lbl_result.after(200,self.update_details)


        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        self.clock_img(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="myclock.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

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
        clock.save("myclock.png")

    def add_course(self):
        self.new_win=Toplevel(self.w)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.w)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.w)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.w)
        self.new_obj=ReportClass(self.new_win)

    def Logout(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Logout?",parent=self.w)
        if op==True:
            self.w.destroy()
            import login

    def Exit(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Exit?",parent=self.w)
        if op==True:
            self.w.destroy()

if __name__ == '__main__':
    w=Tk()
    obj=RMS(w)
    w.mainloop()
