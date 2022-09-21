from tkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('library.db')
cur=con.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.resizable(False,False)

        self.tpframe = Frame(self,height=150,bg='white')
        self.tpframe.pack(fill=X)

        self.btnframe = Frame(self,height=600,bg='#fcc324')
        self.btnframe.pack(fill=X)

        self.tpimg = PhotoImage(file=R'C:\Users\ITECH\Music\addbook.png')
        tpimglbl = Label(self.tpframe,image=self.tpimg,bg='white')
        tpimglbl.place(x=120,y=10)
        head = Label(self.tpframe,text='Add Book',font='arial 22 bold',fg='#003f8a',bg='white')
        head.place(x=290,y=60)



        self.namelbl = Label(self.btnframe,bg='#fcc324',text='Member Name')
        self.namelbl.place(x=40,y=40)
        self.nameent = Entry(self.btnframe,width=30,bd=4)
        self.nameent.insert(0,'Please enter the member name')
        self.nameent.place(x=150,y=45)

        self.phonelbl = Label(self.btnframe,text='Member Phone',bg='#fcc324')
        self.phonelbl.place(x=40,y=80)
        self.phoneent = Entry(self.btnframe,width=30,bd=4)
        self.phoneent.insert(0,'Please enter a phone number')
        self.phoneent.place(x=150,y=85)

        self.addbtn = Button(self.btnframe,text="Add Member",command=self.addmembercmd)
        self.addbtn.place(x=270,y=200)


    def addmembercmd(self):
        name = self.nameent.get()
        phone = self.phoneent.get()

        if (name and phone != ""):
            try:
                query = "INSERT INTO 'member'(membername,memberphone) Values(?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                messagebox.showinfo("Success","Successfuly added")
            except:
                messagebox.showerror("Error","Can't be added to database")

        else:
            messagebox.showerror('Error','Fields cannot be empty')