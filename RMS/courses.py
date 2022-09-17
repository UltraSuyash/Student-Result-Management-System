import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
class CourseClass:
    def __init__(self,w):
        self.w=w
        self.w.title("Student Result Management System")
        self.w.geometry('1050x450+20+80')
        self.w.config(bg="white")
        self.w.focus_force()
#===============Title===============
        title = Label(self.w, text="Manage Course Details", padx=10,
                      font=("New Roman", 15, "bold"), bg="#0b5377", fg="white").place(x=10, y=15,relwidth=1, height=30)

#===============Variables================
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

#===============Widgets===================
        lbl_cousename=Label(self.w,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.w,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.w,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.w,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

#===============Entry Fields===============
        self.txt_course=Entry(self.w,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_course.place(x=150,y=60,width=200)
        txt_duration=Entry(self.w,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_duration.place(x=150,y=100,width=200)
        txt_charges=Entry(self.w,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_charges.place(x=150,y=140,width=200)
        self.txt_description=Text(self.w,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=470,height=80)

#===============Button===================
        self.btn_add=Button(self.w,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.save)
        self.btn_add.place(x=150,y=300,width=110,height=40)
        self.btn_update = Button(self.w, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=300, width=110, height=40)
        self.btn_delete = Button(self.w, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=300, width=110, height=40)
        self.btn_clear = Button(self.w, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=300, width=110, height=40)

#===============Search Panel===============
        self.var_search=StringVar()
        lbl_search_course =Label(self.w, text="Course Name",font=("goudy old style", 15, "bold"),bg="White")
        lbl_search_course.place(x=595, y=60, width=200)
        txt_search_course = Entry(self.w,textvariable=self.var_search,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=760, y=60, width=180)
        btn_search = Button(self.w, text="Search", font=("goudy old style", 15, "bold"),bg="#2196f4", fg="white",cursor="hand2",command=self.search).place(x=960, y=60, width=80, height=28)

#===============Content===============
        self.c_frame=Frame(self.w,bd=2,relief=RIDGE)
        self.c_frame.place(x=640,y=100,width=400,height=300)
        scrollx = Scrollbar(self.c_frame, orient=HORIZONTAL)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        self.course_table=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)
        self.course_table.heading("cid",text="Course Id")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("charges",text="Charges")
        self.course_table.heading("description",text="Description")
        self.course_table["show"]='headings'
        self.course_table.column("cid", width=40)
        self.course_table.column("name", width=50)
        self.course_table.column("duration",width=50 )
        self.course_table.column("charges", width=50)
        self.course_table.column("description",width=100)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#===================Footer Area=======================

        footer=Label(self.w,text="SRMS-Student Result Management System\Contact Us For Any Technical Issue:+919690402370",font=("goudy old Style",12,"bold"),bg="blue",fg="white").pack(side=BOTTOM,fill=X)

    #===============Function Buttons================

#===============Clear Button====================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)
        self.txt_course.config(state=NORMAL)

#===============Delete Button===================
    def delete(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Should Be Required",parent=self.w)
            else:
                 cur.execute("select * from course where name=?",(self.var_course.get(),))
                 row=cur.fetchone()
                 if row==None:
                    messagebox.showerror("Error","Please Select Course From The List First",parent=self.w)
                 else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.w)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course Deleted Successfully",parent=self.w)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#===============Get Data Function===============
    def get_data(self,x):
        self.txt_course.config(state="readonly")
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.var_.set(row[4])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])

#===============Save Button=====================
    def save(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Should Be Required",parent=self.w)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name Already Present",parent=self.w)
                else:
                    cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfuly",parent=self.w)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#===============Update Button===================
    def update(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name Should Be Required",parent=self.w)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from List",parent=self.w)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Update Successfuly",parent=self.w)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#==========Description Text=====================
    def show(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
                cur.execute("select * from course")
                rows=cur.fetchall()
                self.course_table.delete(*self.course_table.get_children())
                for row in rows:
                    self.course_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#==========Search Button========================
    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

if __name__ == '__main__':
    w=Tk()
    obj=CourseClass(w)
    w.mainloop()