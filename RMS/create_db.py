import sqlite3
def create_db():
    con=sqlite3.connect(database="srms.db")

    cur=con.cursor()
    cur=con.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,duration TEXT,charges TEXT,description TEXT)")
    con.commit()
    cur=con.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,dob TEXT,contact TEXT,admission TEXT,course TEXT,state TEXT,city TEXT,pin TEXT,address TEXT)")
    con.commit()
    cur=con.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text ,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()
    cur=con.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,fname text ,lname text,contact text,email text,question text,answer text,password text)")
    con.commit()
    con.close()
create_db()

