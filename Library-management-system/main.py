from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        # pass
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #variables

        self.membvar=StringVar()
        self.prnvar=StringVar()
        self.idvar=StringVar()
        self.frstnmvar=StringVar()
        self.lstnmvar=StringVar()
        self.addr1var=StringVar()
        self.addr2var=StringVar()
        self.postcdvar=StringVar()
        self.moblvar=StringVar()
        self.bookidvar=StringVar()
        self.authorvar=StringVar()
        self.datebrwdvar=StringVar()
        self.dateduevar=StringVar()
        self.daysonbookvar=StringVar()
        self.latereturnvar=StringVar()
        self.dateoverduevar=StringVar()
        self.booktitlevar=StringVar()
        self.finalpricevar=StringVar()




        labeltitle=Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="green", fg="white", bd=20, relief=RIDGE, font=("times new roman", 45, "bold"), padx=2, pady=6)

        labeltitle.pack(side=TOP, fill=X)

        frame= Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="white")
        frame.place(x=0, y=130, width=1530, height=400)

        # LEFT
        DataFrameLeft= LabelFrame(frame, text="Library Memebership Information", bg="white", fg="red", bd=10, relief=RIDGE, font=("times new roman", 13, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        mem= Label(DataFrameLeft,bg="white", text="Member Type", font=("times new roman", 12, "bold"), padx=2, pady=7)
        mem.grid(row=0, column=0, sticky=W)

        comb_mem=ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.membvar , width=27, state="readonly")
        comb_mem["value"]=("Admin Staff", "Student", "Lecturer")
        comb_mem.current(0)
        comb_mem.grid(row=0, column=1)

        Prn_no=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="PRN No:", padx=2, pady=6, bg="white")
        Prn_no.grid(row=1, column=0, sticky=W)
        txtprn_no=Entry(DataFrameLeft, textvariable=self.prnvar, font=("times new roman", 13, "bold"), width=29)
        txtprn_no.grid(row=1, column=1)

        lbl_title=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="ID No:", padx=2, pady=6, bg="white")
        lbl_title.grid(row=2, column=0, sticky=W)
        txt_title=Entry(DataFrameLeft, textvariable=self.idvar, font=("times new roman", 13, "bold"), width=29)
        txt_title.grid(row=2, column=1)

        frst_nm=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="FirstName:", padx=2, pady=6, bg="white")
        frst_nm.grid(row=3, column=0, sticky=W)
        txtFrst=Entry(DataFrameLeft, textvariable=self.frstnmvar,font=("times new roman", 13, "bold"), width=29)
        txtFrst.grid(row=3, column=1)

        lst_nm=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="LastName:", padx=2, pady=6, bg="white")
        lst_nm.grid(row=4, column=0, sticky=W)
        txtlst=Entry(DataFrameLeft, textvariable=self.lstnmvar,font=("times new roman", 13, "bold"), width=29)
        txtlst.grid(row=4, column=1)

        addr1=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Address1:", padx=2, pady=6, bg="white")
        addr1.grid(row=5, column=0, sticky=W)
        txtaddr1=Entry(DataFrameLeft, textvariable=self.addr1var,font=("times new roman", 13, "bold"), width=29)
        txtaddr1.grid(row=5, column=1)

        addr2=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Address2:", padx=2,pady=6, bg="white")
        addr2.grid(row=6, column=0, sticky=W)
        txtaddr2=Entry(DataFrameLeft,  textvariable=self.addr2var,font=("times new roman", 13, "bold"), width=29)
        txtaddr2.grid(row=6, column=1)

        postal_code=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Postal Code:", padx=2,pady=6, bg="white")
        postal_code.grid(row=7, column=0, sticky=W)
        txtpst_cd=Entry(DataFrameLeft, textvariable=self.postcdvar, font=("times new roman", 13, "bold"), width=29)
        txtpst_cd.grid(row=7, column=1)

        mob_no=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Mobile:", padx=2, pady=6, bg="white")
        mob_no.grid(row=8, column=0, sticky=W)
        txtmob_no=Entry(DataFrameLeft, textvariable=self.moblvar, font=("times new roman", 13, "bold"), width=29)
        txtmob_no.grid(row=8, column=1)

        Book_id=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Book Id:", padx=2, pady=6, bg="white")
        Book_id.grid(row=0, column=2, sticky=W)
        txtbook_id=Entry(DataFrameLeft, textvariable=self.bookidvar,font=("times new roman", 13, "bold"), width=29)
        txtbook_id.grid(row=0, column=3)

        Book_nm=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Book Title:", padx=2, pady=6, bg="white")
        Book_nm.grid(row=1, column=2, sticky=W)
        txtboook_nm=Entry(DataFrameLeft, textvariable=self.booktitlevar, font=("times new roman", 13, "bold"), width=29)
        txtboook_nm.grid(row=1, column=3)

        Authr=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Author Name:", padx=2, pady=6, bg="white")
        Authr.grid(row=2, column=2, sticky=W)
        txtauthr=Entry(DataFrameLeft, textvariable=self.authorvar ,font=("times new roman", 13, "bold"), width=29)
        txtauthr.grid(row=2, column=3)


        dt_brwd=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Date Borrowed:", padx=2, pady=6, bg="white")
        dt_brwd.grid(row=3, column=2, sticky=W)
        txtdt_brwd=Entry(DataFrameLeft, textvariable=self.datebrwdvar ,font=("times new roman", 13, "bold"), width=29)
        txtdt_brwd.grid(row=3, column=3)

        dt_due=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Date Due:", padx=2, pady=6, bg="white")
        dt_due.grid(row=4, column=2, sticky=W)
        txtdt_due=Entry(DataFrameLeft, textvariable=self.dateduevar,font=("times new roman", 13, "bold"), width=29)
        txtdt_due.grid(row=4, column=3)

        dys_on_book=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Days on Book:", padx=2, pady=6, bg="white")
        dys_on_book.grid(row=5, column=2, sticky=W)
        txtdysonbook=Entry(DataFrameLeft, textvariable=self.daysonbookvar,font=("times new roman", 13, "bold"), width=29)
        txtdysonbook.grid(row=5, column=3)

        late_return=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Late Return Fine:", padx=2, pady=6, bg="white")
        late_return.grid(row=6, column=2, sticky=W)
        txtLt_return_fn=Entry(DataFrameLeft,  textvariable=self.latereturnvar,font=("times new roman", 13, "bold"), width=29)
        txtLt_return_fn.grid(row=6, column=3)

        date_overdate=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Date Over Due:", padx=2, pady=6, bg="white")
        date_overdate.grid(row=7, column=2, sticky=W)
        txtover_due=Entry(DataFrameLeft,textvariable=self.dateduevar, font=("times new roman", 13, "bold"), width=29)
        txtover_due.grid(row=7, column=3)

        Actual_price=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Actual Price:", padx=2, pady=6, bg="white")
        Actual_price.grid(row=8, column=2, sticky=W)
        txtactual_price=Entry(DataFrameLeft, textvariable=self.finalpricevar, font=("times new roman", 13, "bold"), width=29)
        txtactual_price.grid(row=8, column=3)


        #RIGHT
        DataFrameRight= LabelFrame(frame, text="Book Details", bg="white", fg="red", bd=10, relief=RIDGE, font=("times new roman", 13, "bold"))
        DataFrameRight.place(x=915, y=5, width=550, height=350)

        self.txtBox=Text(DataFrameRight, font=("times new roman", 13, "bold"), width=32, height=16,padx=2, pady=6)
        self.txtBox.grid(row=6, column=2)

        listScrollbar= Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks=["Python Crash Course", "The Waste Land", "Automate the Boring Stuff with Python", "Effective Python: 90 Specific Ways to Write Better Python", "The Sun and Her Flowers", "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Deep Learning", "Python Machine Learning", "The Waste Land",  "Data Science from Scratch: First Principles with Python", "Cracking the Coding Interview", "Clean Code: A Handbook of Agile Software Craftsmanship", "Statistics Done Wrong: The Woefully Complete Guide", "Statistics in Plain English", "The Guns of August", "SPQR: A History of Ancient Rome", "Steve Jobs",  "The Diary of a Young Girl", "Long Walk to Freedom", "Harry Potter and the Sorcerer's Stone", "Neuromancer", "The Girl with the Dragon Tattoo", "And Then There Were None", "To Kill a Mockingbird", "Pride and Prejudice", "Dune", "Sapiens: A Brief History of Humankind" ]

        def SelectBook(event=""):
            val=str(listBox.get(listBox.curselection()))
            x=val
            if (x=="Python Crash Course"):
                self.bookidvar.set("A434B23")
                self.booktitlevar.set("Python Programming")
                self.authorvar.set("Eric Matthes")

                d1= datetime.date.today()
                d2= datetime.timedelta(days=15)
                d3=d1+d2
                self.datebrwdvar.set(d1)
                self.dateduevar.set(d3)
                self.daysonbookvar.set(15)
                self.latereturnvar.set("Rs. 15")
                self.dateoverduevar.set("No")
                self.finalpricevar.set("Rs. 759")

                

        
        listBox=Listbox(DataFrameRight, font=("arial", 13, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for itm in listBooks:
            listBox.insert(END, itm)

        # BUTTONS
        Framebtn= Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="white")
        Framebtn.place(x=0, y=530, width=1530, height=55)

        btnAdd=Button(Framebtn, command=self.add_data,text="Add Data", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=0)

        btnAdd=Button(Framebtn, text="Show Data", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=1)
        
        btnAdd=Button(Framebtn, text="Update", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=2)

        btnAdd=Button(Framebtn, text="Delete", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=3)

        btnAdd=Button(Framebtn, text="Reset", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=4)

        btnAdd=Button(Framebtn, text="Exit", font=("arial", 13, "bold"), width=23, bg="blue", fg="white")
        btnAdd.grid(row=0, column=5)

        # Database details
        FrameDetl= Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="white")
        FrameDetl.place(x=0, y=600, width=1530, height=190)

        tbleframe=Frame(FrameDetl, bd=6, relief=RIDGE, bg="white")
        tbleframe.place(x=0, y=2, width=1460, height=170)

        scrollx=ttk.Scrollbar(tbleframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tbleframe,orient=VERTICAL)


        self.lib_tbl=ttk.Treeview(tbleframe, column=("membertype", "prnno", "title", "firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.lib_tbl.xview)
        scrolly.config(command=self.lib_tbl.yview)



        self.lib_tbl.heading("membertype", text="Member Type")
        self.lib_tbl.heading("prnno", text="PRN No.")
        self.lib_tbl.heading("title", text="Title")
        self.lib_tbl.heading("firstname", text="First Name")
        self.lib_tbl.heading("lastname", text="Last Name")
        self.lib_tbl.heading("address1", text="Address1")
        self.lib_tbl.heading("address2", text="Address2")
        self.lib_tbl.heading("postid", text="Post ID")
        self.lib_tbl.heading("mobile", text="Mobile Number")
        self.lib_tbl.heading("bookid", text="Book ID")
        self.lib_tbl.heading("booktitle", text="Book Title")
        self.lib_tbl.heading("author", text="Author")
        self.lib_tbl.heading("dateborrowed", text="Date of Borrowed")
        self.lib_tbl.heading("datedue", text="Date Due")
        self.lib_tbl.heading("days", text="Days on Book")
        self.lib_tbl.heading("latereturnfine", text="LateReturnFine")
        self.lib_tbl.heading("dateoverdue", text="DateOverdue")
        self.lib_tbl.heading("finalprice", text="Final Price")

        self.lib_tbl["show"]="headings"
        self.lib_tbl.pack(fill=BOTH,expand=1)

        self.lib_tbl.column("membertype", width=100)
        self.lib_tbl.column("prnno", width=100)
        self.lib_tbl.column("title", width=100)
        self.lib_tbl.column("firstname", width=100)
        self.lib_tbl.column("lastname", width=100)
        self.lib_tbl.column("address1", width=100)
        self.lib_tbl.column("address2", width=100)
        self.lib_tbl.column("postid", width=100)
        self.lib_tbl.column("mobile", width=100)
        self.lib_tbl.column("bookid", width=100)
        self.lib_tbl.column("booktitle", width=100)
        self.lib_tbl.column("author", width=100)
        self.lib_tbl.column("dateborrowed", width=100)
        self.lib_tbl.column("datedue", width=100)
        self.lib_tbl.column("days", width=100)
        self.lib_tbl.column("latereturnfine", width=100)
        self.lib_tbl.column("dateoverdue", width=100)
        self.lib_tbl.column("finalprice", width=100)



    def add_data(self):
        conct=mysql.connector.connect(host="localhost", username="root", password="Dikshu@2534#123", database="lib_data1")
        mycursor=conct.cursor()
        mycursor.execute("insert into library values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

            self.membvar.get(),
            self.prnvar.get(),
            self.idvar.get(),
            self.frstnmvar.get(),
            self.lstnmvar.get(),
            self.addr1var.get(),
            self.addr2var.get(),
            self.postcdvar.get(),
            self.moblvar.get(),
            self.bookidvar.get(),
            self.booktitlevar.get(),
            self.authorvar.get(),
            self.datebrwdvar.get(),
            self.dateduevar.get(),
            self.daysonbookvar.get(),
            self.latereturnvar.get(),
            self.dateoverduevar.get(),
            self.finalpricevar.get()

        ))
        conct.commit()
        conct.close()

        messagebox.showinfo("Success", "Member has been inserted successfully!")


if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()



    '''
    memb
    prn-no
    id
    fnm
    lstnm
    adr1
    adr2
    postid
    mob
    bookid
    author
    datebrwd
    datedue
    dateofbook
    latereturnfine
    dateoverdue
    finalprice

    '''