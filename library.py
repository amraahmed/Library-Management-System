from tkinter import *
from tkinter import ttk
import sqlite3
import addbook
import addmember
con=sqlite3.connect('library.db')
cur=con.cursor()


class Main(object):
    def __init__(self,master):
        self.master = master

        def stat(evt):
            contbks = cur.execute("SELECT count(bookid) FROM books").fetchall()
            contmem = cur.execute("SELECT count(memberid) FROM member").fetchall()
            notav = cur.execute("SELECT count(bookid) FROM books WHERE got = lent").fetchall()
            self.bklblno.config(text='Total books in Library: '+str(contbks[0][0]))
            self.bklblno.place(x=0,y=0)
            self.memlblno.config(text='Total Members: '+str(contmem[0][0]))
            self.memlblno.place(x=0,y=70)
            self.lentno.config(text='UnAvilable books in the Library: '+str(notav[0][0]))
            self.lentno.place(x=0,y=140)

            


        def displayBooks(self):
            
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            self.lstbks.delete(0,END)
            for book in books:
                self.lstbks.insert(count,str(book[0])+"-"+str(book[1]))
                count+=1
            

            def bookInfo(evt):
                value = str(self.lstbks.get(self.lstbks.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE bookid=?",(id,))
                bookInfo=book.fetchall()
                self.lstdet.delete(0,"end")
                self.lstdet.insert(0,"Book Name:"+bookInfo[0][1])
                self.lstdet.insert(1,"Book Author:"+bookInfo[0][2])
                self.lstdet.insert(2,"Book Languge:"+bookInfo[0][3])
                self.lstdet.insert(3,"Book ISBN:"+str(bookInfo[0][4]))
                if bookInfo[0][5] <= bookInfo[0][6]:
                    self.lstdet.insert(4,"Status: Not Avilable")
                else:
                    self.lstdet.insert(4,"Status: Avilable")
                displayBooks(self)


                
            

            self.lstbks.bind('<<ListboxSelect>>',bookInfo)
            self.tbs.bind('<<NotebookTabChanged>>',stat)



            

                




        mainframe = Frame(self.master)
        mainframe.pack()
        tpframe = Frame(mainframe,width=1350,height=70,bg="#f8f8f8",padx=20,relief=SUNKEN,borderwidth=2)
        tpframe.pack(side=TOP,fill=X)
        cenframe = Frame(mainframe,width=1350,relief=RIDGE,bg="white",height=700)
        cenframe.pack(side=TOP)
        clFrame =Frame(cenframe,width=900,height=700,bg='red',bd=2,relief=SUNKEN)
        clFrame.pack(side=LEFT)
        crFrame = Frame(cenframe,width=450,height=700,bg='red',bd=2,relief=SUNKEN)
        crFrame.pack()


        srchbr = LabelFrame(crFrame,width=440,height=75,bg="#9bc9ff",text='Search Box')
        srchbr.pack(fill=BOTH)
        self.srchlbl = Label(srchbr,text='Search: ', font='arial 12 bold',bg='#9bc9ff')
        self.srchlbl.grid(row=0,column=0,padx=20,pady=10)
        self.srchent = Entry(srchbr,width=30,bd=10)
        self.srchent.grid(row=0,column=1,columnspan=3,pady=10,padx=5)
        self.srchbtn = Button(srchbr,text='Search',font='arial 12 bold', bg='#fcc324',fg='white',command=self.srchbkscmd)
        self.srchbtn.grid(row=0,column=4,padx=28,pady=10)

        lstbr = LabelFrame(crFrame,width=440,height=175,text='List Box',bg='#fcc324')
        lstbr.pack(fill=BOTH)
        lstlbl = Label(lstbr,text='Sort By:',font='times 16 bold',fg='#2488ff',bg='#fcc324')
        lstlbl.grid(row=0,column=2)


        self.lstchoe = IntVar()
        rb1 = Radiobutton(lstbr,text='All Books',var=self.lstchoe,value=1,bg='#fcc324')
        rb2 = Radiobutton(lstbr,text='In Library Books',var=self.lstchoe,value=2,bg='#fcc324')
        rb3 = Radiobutton(lstbr,text='Borrowed Books',var=self.lstchoe,value=3,bg='#fcc324')
        lstbtn = Button(lstbr,text="List Books",bg='#2488ff',fg='white',font='arial 12',command=self.lstbkscmd)
        lstbtn.grid(row=1,column=3,pady=10,padx=40)

        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)


        imgbr = Frame(crFrame,width=440,height=360)
        imgbr.pack(fill=BOTH)
        self.rtitle = Label(imgbr,text='Welcome to our Library',font='arial 15 bold')
        self.rtitle.grid(row=0)
        self.libimg = PhotoImage(file=R'C:\Users\ITECH\Music\library.png')
        self.lblimg = Label(imgbr,image=self.libimg)
        self.lblimg.grid(row=1) 







        self.icnbok = PhotoImage(file=R"C:\Users\ITECH\Music\add_book.png")
        self.btnbok = Button(tpframe,text='Add Book',compound=LEFT,font='arial 12 bold',command=self.addBookcmd)
        self.btnbok.configure(image=self.icnbok,compound=LEFT)
        self.btnbok.pack(side=LEFT,padx=10)

        self.icnadd = PhotoImage(file=R"C:\Users\ITECH\Music\users.png")
        self.addbtn = Button(tpframe,text='Add Member',compound=LEFT,font='arial 12 bold',command=self.addmembercmd)
        self.addbtn.configure(image=self.icnadd,compound=LEFT)
        self.addbtn.pack(side=LEFT,padx=10)

        self.icnlen = PhotoImage(file=R"C:\Users\ITECH\Music\givebook.png")
        self.btnlen = Button(tpframe,text='Lend Book',compound=LEFT,font='arial 12 bold')
        self.btnlen.configure(image=self.icnlen,compound=LEFT)
        self.btnlen.pack(side=LEFT,padx=10)

        self.tbs = ttk.Notebook(clFrame,width=900,height=680)
        self.tbs.pack()
        self.tb1icn = PhotoImage(file=R"C:\Users\ITECH\Music\books.png")
        self.tb2icn = PhotoImage(file=R"C:\Users\ITECH\Music\members.png")
        self.tb1 = ttk.Frame(self.tbs)
        self.tb2 = ttk.Frame(self.tbs)
        self.tbs.add(self.tb1,text='Library Management',image=self.tb1icn,compound=LEFT)
        self.tbs.add(self.tb2,text='Statistics',image=self.tb2icn,compound=LEFT)

        self.lstbks = Listbox(self.tb1,width=40,height=30,bd=5,font='times 12 bold')
        self.sb = Scrollbar(self.tb1,orient=VERTICAL)
        self.lstbks.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.lstbks.yview)
        self.lstbks.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E) 

        self.lstdet = Listbox(self.tb1,width=80,height=30,bd=5,font='times 12 bold')
        self.lstdet.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
        
        self.bklblno = Label(self.tb2,text='Avilable Books',pady=20,font='verdana 14 bold')
        self.bklblno.grid(row=0)
        self.memlblno = Label(self.tb2,text='Members',pady=20,font='verdana 14 bold')
        self.memlblno.grid(row=1,sticky=N)
        self.lentno = Label(self.tb2,text='Not Avilable Books',pady=20,font='verdana 14 bold')
        self.lentno.grid(row=2,sticky=W)

        displayBooks(self)
        stat(self)
          

    def addBookcmd(self):
            addb = addbook.AddBok()


    def addmembercmd(self):
          addm = addmember.AddMember()
    
    def srchbkscmd(self):
        value = self.srchent.get()
        srch = cur.execute("SELECT * FROM books WHERE bookname LIKE ?",('%'+value+'%',)).fetchall()
        print(srch)
        self.lstbks.delete(0,'end')
        self.lstdet.delete(0,'end')

        count = 0 
        for book in srch:
            self.lstbks.insert(count,str(book[0])+"-"+str(book[1]))
            count+=1

    def lstbkscmd(self):
        value = self.lstchoe.get()
        if value ==1:
            allbks = cur.execute("SELECT * FROM books").fetchall()
            self.lstbks.delete(0,END)
            self.lstdet.delete(0,END)
            count=0
            for books in allbks:
                self.lstbks.insert(count,str(books[0])+"-"+str(books[1]))
                count+=1

        elif value ==2:
            allbks = cur.execute("SELECT * FROM books WHERE got > lent").fetchall()
            self.lstbks.delete(0,END)
            self.lstdet.delete(0,END)
            count=0
            for books in allbks:
                self.lstbks.insert(count,str(books[0])+"-"+str(books[1]))
                count+=1  
        elif value ==3:
            allbks = cur.execute("SELECT * FROM books WHERE got = lent").fetchall()
            self.lstbks.delete(0,END)
            self.lstdet.delete(0,END)
            count=0
            for books in allbks:
                self.lstbks.insert(count,str(books[0])+"-"+str(books[1]))
                count+=1    

        

                  










def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x700")
    root.mainloop()

if __name__ =='__main__':
    main()