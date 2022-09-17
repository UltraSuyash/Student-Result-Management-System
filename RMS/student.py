import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
class StudentClass:
    def __init__(self,w):
        self.w=w
        self.w.title("Student Result Management System")
        self.w.geometry('1050x450+20+80')
        self.w.config(bg="white")
        self.w.focus_force()
#===============Title===============
        title = Label(self.w, text="Student Admission Form ", padx=10,
                      font=("New Roman", 15, "bold"), bg="#0b5377", fg="white").place(x=10, y=15,relwidth=1, height=30)

#===============Variables================
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

#===============Widgets===================

#================Column 1=================
        lbl_roll=Label(self.w,text="Roll No",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.w,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email=Label(self.w,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.w,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_state=Label(self.w,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        txt_state=Entry(self.w,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=100,y=220,width=150)
        lbl_city=Label(self.w,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=220)
        txt_city=Entry(self.w,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=300,y=220,width=120)
        lbl_pin=Label(self.w,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=425,y=220)
        txt_pin=Entry(self.w,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=460,y=220,width=130)

        lbl_address=Label(self.w,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=300)
#===============Entry Fields===============
        self.txt_roll=Entry(self.w,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=100,y=60,width=150)
        txt_name=Entry(self.w,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_name.place(x=100,y=100,width=150)
        txt_email=Entry(self.w,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_email.place(x=100,y=140,width=150)
        self.txt_gender=ttk.Combobox(self.w,textvariable=self.var_gender,values=("SELECT","Male","Female","Other"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=100,y=180,width=150)
        self.txt_gender.current(0)

#==================Column2======================
        lbl_dob=Label(self.w,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=60)
        lbl_contact=Label(self.w,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=100)
        lbl_addmision=Label(self.w,text="Addmission Date",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=140)
        lbl_course=Label(self.w,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=260,y=180)
        #===============Entry Fields===============
        self.course_list=[]
        #=========Function_Call To Update==========
        self.fetch_course()
        txt_dob=Entry(self.w,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_dob.place(x=420,y=60,width=170)
        txt_contact=Entry(self.w,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_contact.place(x=420,y=100,width=170)
        txt_addmision=Entry(self.w,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_addmision.place(x=420,y=140,width=170)
        self.txt_course=ttk.Combobox(self.w,textvariable=self.var_course,values=(self.course_list),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=420,y=180,width=170)
        self.txt_course.set("SELECT")

#==================Address=======================
        self.txt_address=Text(self.w,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=290,width=470,height=50)

#===============Button===================
        self.btn_add=Button(self.w,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.save)
        self.btn_add.place(x=150,y=360,width=110,height=40)
        self.btn_update = Button(self.w, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=360, width=110, height=40)
        self.btn_delete = Button(self.w, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=360, width=110, height=40)
        self.btn_clear = Button(self.w, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=360, width=110, height=40)

#===============Search Panel===============
        self.var_search=StringVar()
        lbl_search_roll =Label(self.w, text="Roll No.",font=("goudy old style", 15, "bold"),bg="White")
        lbl_search_roll.place(x=600, y=60, width=200)
        txt_search_course = Entry(self.w,textvariable=self.var_search,font=("goudy old style", 15, "bold"),bg="lightyellow").place(x=740, y=60, width=150)
        btn_search= Button(self.w, text="Search", font=("goudy old style", 15, "bold"),bg="#2196f4", fg="white",cursor="hand2",command=self.search).place(x=910, y=60, width=130, height=28)

#===============Content===============
        self.c_frame=Frame(self.w,bd=2,relief=RIDGE)
        self.c_frame.place(x=640,y=100,width=400,height=300)
        scrollx = Scrollbar(self.c_frame, orient=HORIZONTAL)
        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        self.course_table=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)
        self.course_table.heading("roll",text="Roll No.")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("email",text="Email")
        self.course_table.heading("gender",text="Gender")
        self.course_table.heading("dob",text="D.O.B")
        self.course_table.heading("contact",text="Contact")
        self.course_table.heading("admission",text="Admission")
        self.course_table.heading("course",text="Course")
        self.course_table.heading("state",text="State")
        self.course_table.heading("city",text="City")
        self.course_table.heading("pin",text="Pin")
        self.course_table.heading("address",text="Address")
        self.course_table["show"]='headings'
        self.course_table.column("roll", width=100)
        self.course_table.column("name", width=100)
        self.course_table.column("email",width=150 )
        self.course_table.column("gender", width=100)
        self.course_table.column("dob",width=100)
        self.course_table.column("contact",width=100)
        self.course_table.column("admission",width=100)
        self.course_table.column("course",width=100)
        self.course_table.column("state",width=100)
        self.course_table.column("city",width=100)
        self.course_table.column("pin",width=100)
        self.course_table.column("address",width=100)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#===================Footer Area=======================

        footer=Label(self.w,text="SRMS-Student Result Management System\Contact Us For Any Technical Issue:+919690402370",font=("goudy old Style",12,"bold"),bg="blue",fg="white").pack(side=BOTTOM,fill=X)

#===============Function Buttons================

#===============Clear Button====================
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("SELECT"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("SELECT"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END),
        self.txt_roll.config(state=NORMAL),
        self.var_search.set("")

#===============Delete Button===================
    def delete(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number Should Be Required",parent=self.w)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select Student From The List First",parent=self.w)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete",parent=self.w)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.w)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#===============Get Data Function===============
    def get_data(self,x):
        self.txt_roll.config(state="readonly")
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[11])

#===============Save Button=====================
    def save(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number Should Be Required",parent=self.w)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number Already Present",parent=self.w)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfuly",parent=self.w)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#===============Update Button===================
    def update(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number Should Be Required",parent=self.w)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from List",parent=self.w)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(

                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfuly",parent=self.w)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#==========Description Text=====================
    def show(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#===========Fetch Course========================
    def fetch_course(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

#==========Search Button========================
    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert("",END,values=row)
            else:
                messagebox.showerror("Error","No Record Found",parent=self.w)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due To {str(ex)}")

if __name__ == '__main__':
    w=Tk()
    obj=StudentClass(w)
    w.mainloop()