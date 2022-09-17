import os
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Register:
    def __init__(self,w):
        self.w=w
        self.w.title("Registeration Window")
        self.w.geometry('1350x700+0+0')
        self.w.config(bg="white")
        #============ BG Image===================
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.w,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #============ Left Image===================
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.w,image=self.left).place(x=50,y=40,width=400,height=470)
        #============ Register Label===================
        fram1=Frame(self.w,bg="white")
        fram1.place(x=450,y=40,width=600,height=470)

        title=Label(fram1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # self.var_fname=StringVar()
        fname=Label(fram1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=200)

        lname=Label(fram1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=330,y=100)
        self.txt_lname=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=330,y=130,width=200)

        contact=Label(fram1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=200)

        email=Label(fram1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=330,y=170)
        self.txt_email=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=330,y=200,width=200)

        question=Label(fram1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(fram1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best friend Name")
        self.cmb_question.place(x=50,y=270,width=200)
        self.cmb_question.current(0)

        answer=Label(fram1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=330,y=240)
        self.txt_answer=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=330,y=270,width=200)

        pasword=Label(fram1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(fram1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=200)

        cpassword=Label(fram1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=330,y=310)
        self.txt_cpassword=Entry(fram1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=330,y=340,width=200)
        self.var_chk=IntVar()
        chk=Checkbutton(fram1,text="I Agree The Terms & Condition",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="images/register.png")

        btn_register=Button(fram1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_sign=Button(self.w,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=150,y=380,width=180)

    def login_window(self):
        self.w.destroy()
        # os.system("login")
        import login

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.current(0)

    def register_data(self):
            if self.txt_fname.get()=="" or \
               self.txt_contact.get()=="" or \
               self.txt_email.get()=="" or \
               self.cmb_question.get()=="Select" or\
               self.txt_answer.get()=="" or \
               self.txt_password.get()=="" or \
               self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.w)
            elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Password & confirm Password Should be Same",parent=self.w)
            elif self.var_chk.get()==0:
                messagebox.showerror("Error","Please Agree Our Terms & Condition",parent=self.w)

            else:
                try:
                    con=sqlite3.connect(database="srms.db")
                    cur=con.cursor()
                    cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","User Already Exits,Please try with another emaqil",parent=self.w)
                    else:
                        cur.execute("insert into employee (fname,lname,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.cmb_question.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                        ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Register Successfuly",parent=self.w)

                        self.clear()
                        self.login_window()
                except Exception as ex:
                     messagebox.showerror("Error",f"Error Due To {str(ex)}")

if __name__ == '__main__':
    w=Tk()
    obj=Register(w)
    w.mainloop()