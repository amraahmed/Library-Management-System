from tkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('library.db')
cur=con.cursor()


class AddBok(Toplevel):
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



        self.namelbl = Label(self.btnframe,bg='#fcc324',text='Book Name')
        self.namelbl.place(x=40,y=40)
        self.nameent = Entry(self.btnframe,width=30,bd=4)
        self.nameent.insert(0,'Please enter the book name')
        self.nameent.place(x=150,y=45)

        self.authlbl = Label(self.btnframe,text='Book Author',bg='#fcc324')
        self.authlbl.place(x=40,y=80)
        self.authent = Entry(self.btnframe,width=30,bd=4)
        self.authent.insert(0,'Please enter the book author')
        self.authent.place(x=150,y=85)

        self.langlbl = Label(self.btnframe,text='Book Languge',bg='#fcc324')
        self.langlbl.place(x=40,y=120)
        self.langent = Entry(self.btnframe,width=30,bd=4)
        self.langent.insert(0,'Please enter the book languge')
        self.langent.place(x=150,y=125)

        self.ISBNlbl = Label(self.btnframe,text='Book ISBN',bg='#fcc324')
        self.ISBNlbl.place(x=40,y=160)
        self.ISBNent = Entry(self.btnframe,width=30,bd=4)
        self.ISBNent.insert(0,'Please enter the book ISBN')
        self.ISBNent.place(x=150,y=165)

        self.addbtn = Button(self.btnframe,text="Add Book",command=self.addbook)
        self.addbtn.place(x=270,y=200)


    def addbook(self):
        bookname = self.nameent.get()
        author = self.authent.get()
        lang = self.langent.get()
        isbn = self.ISBNent.get()

        if (bookname and author and lang and isbn != ""):
            try:
                query = "INSERT INTO 'books'(bookname,author,lang,isbn) Values(?,?,?,?)"
                cur.execute(query,(bookname,author,lang,isbn))
                con.commit()
                messagebox.showinfo("Success","Successfuly added")
            except:
                messagebox.showerror("Error","Can't be added to database")

        else:
            messagebox.showerror('Error','Fields cannot be empty')
                