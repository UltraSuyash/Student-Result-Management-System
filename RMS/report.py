import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk

class ReportClass:
    def __init__(self,w):
        self.w=w
        self.w.title("Add Student Results Management System")
        self.w.geometry('1050x450+20+80')
        self.w.config(bg="white")
        self.w.focus_force()
        #===============Title===============
        title = Label(self.w, text="View Student Result", padx=10,
                      font=("New Roman", 15, "bold"), bg="orange", fg="#222626").place(x=10, y=15,relwidth=1, height=30)
        #=====================Footer Area===================
        footer=Label(self.w,text="SRMS-Student Result Management System\Contact Us For Any Technical Issue:+919690402370",font=("goudy old Style",12,"bold"),bg="blue",fg="white").pack(side=BOTTOM,fill=X)
#==================Search==================
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.w,text="Search By Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=350,y=100)
        txt_search=Entry(self.w,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow").place(x=520,y=100,width=150,height=30)
        btn_search=Button(self.w,text="Search",font=("times new roman",15),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=30)
        btn_clear=Button(self.w,text="Clear",font=("times new roman",15),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=30)

#=========================Result label============================
        lbl_roll=Label(self.w,text="Roll No.",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=130,height=40)
        lbl_name=Label(self.w,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=280,y=230,width=130,height=40)
        lbl_course=Label(self.w,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=410,y=230,width=130,height=40)
        lbl_marks_ob=Label(self.w,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=540,y=230,width=150,height=40)
        lbl_total_marks=Label(self.w,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=690,y=230,width=130,height=40)
        lbl_par=Label(self.w,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=820,y=230,width=130,height=40)
#=========================Show Results================================

        self.roll=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=270,width=130,height=40)

        self.name=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=280,y=270,width=130,height=40)

        self.course=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=410,y=270,width=130,height=40)

        self.marks_ob=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_ob.place(x=540,y=270,width=150,height=40)

        self.total_marks=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.total_marks.place(x=690,y=270,width=130,height=40)

        self.par=Label(self.w,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.par.place(x=820,y=270,width=130,height=40)
#=================================Delete Button=========================
        btn_delete=Button(self.w,text="Delete",font=("times new roman",15),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=480,y=330,width=150,height=30)
#==================Function===================
    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll Number Should Be Required",parent=self.w)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks_ob.config(text=row[4])
                    self.total_marks.config(text=row[5])
                    self.par.config(text=row[6])
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.w)
        except Exception as ex:
            messagebox.showerror("Error","Error Due To {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.total_marks.config(text="")
        self.par.config(text="")
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.w)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid  Student Result",parent=self.w)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.w)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result Deleted Successfully",parent=self.w)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")


if __name__ == '__main__':
    w=Tk()
    obj=ReportClass(w)
    w.mainloop()