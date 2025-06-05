from tkinter import*
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from tkinter import messagebox as mb
import mysql.connector as ms
import math
from twilio.rest import Client
import math
import random
import datetime
from tkinter import ttk
def Lonin_normal():
    b1.configure(state=NORMAL, background='white')
    b2.configure(state=NORMAL, background='white')
    b3.configure(state=NORMAL, background='white')
    e1.configure(state=NORMAL, background='white')
    e2.configure(state=NORMAL, background='white')
#NORMAL-------------------------------------------------------
def unable_me():
    m1.configure(state=NORMAL, background='#E6E6FA')
    m2.configure(state=NORMAL, background='#E6E6FA')
    m3.configure(state=NORMAL, background='#E6E6FA')
    m4.configure(state=NORMAL, background='#E6E6FA')
    m5.configure(state=NORMAL, background='#E6E6FA')
    m6.configure(state=NORMAL, background='#E6E6FA')
    m7.configure(state=NORMAL, background='#E6E6FA')
    m8.configure(state=NORMAL, background='#E6E6FA')
#DISABLED-----------------------------------------------------
def Disable_me():
    m1.configure(state=DISABLED, background='#FFFAF0')
    m2.configure(state=DISABLED, background='#FFFAF0')
    m3.configure(state=DISABLED, background='#FFFAF0')
    m4.configure(state=DISABLED, background='#FFFAF0')
    m5.configure(state=DISABLED, background='#FFFAF0')
    m6.configure(state=DISABLED, background='#FFFAF0')
    m7.configure(state=DISABLED, background='#FFFAF0')
    m8.configure(state=DISABLED, background='#FFFAF0')
#-------------------------------------------------------------
def graph1():
    mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
    cur = mydb.cursor()
    list1=["Current","Saving"]
    list2=[]
    x=[0,1]
    for i in range(0,len(list1)):
                   cur.execute("select count(AccountType)from bank where AccountType=%s",(list1[i],))
                   myrecords=cur.fetchone()
                   list2.append(myrecords[0])
    plt.bar(x,list2,color='cyan')
    plt.xticks(x,list1)
    plt.show()          
    
#-------------------------------------------------------------
def Statement():
    account_state=accountnumber.get()
    if account_state=='':
        mb.showerror(screen1,"insert status", "AccountNO required",parent=screen9)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select *from transation where AccountNo=%s",(account_state,))
        row=cur.fetchall()
        frm = Frame(st)
        frm.place(x=20,y=140)
        tv = ttk.Treeview(frm)
        tv["columns"]=("column1","column2","column3","column4","column5","column6","column7")
        tv.column("#0",width=0,minwidth=0)
        tv.column("column1",width=100,minwidth=25)
        tv.column("column2",width=100,minwidth=25)
        tv.column("column3",width=100,minwidth=25)
        tv.column("column4",width=100,minwidth=25)
        tv.column("column5",width=100,minwidth=25)
        tv.column("column6",width=100,minwidth=25)
        tv.pack()
        tv.heading(0,text="Date")
        tv.heading(1,text="Time")
        tv.heading(2,text="AccountNO")
        tv.heading(3,text="Operation")
        tv.heading(4,text="TransationAc")
        tv.heading(5,text="AmountPluse")
        tv.heading(6,text="AmountMinuse")
        for i in row:
            tv.insert('', 'end',values=i)
        Button(st,text="< Go Back",font=("Arial",15),command=lambda:[unable_me(),st.destroy()]).place(x=20,y=400)
def statement_show():
    global st
    st=LabelFrame(screen,text="STATEMENT",font=("Arial",25),width=1000,height=550,bg="white")
    st.place(x=350,y=220)
    Label(st,text="ACCOUNT NUMBER  :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Label(st,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(st,text="STATMENT",width=10,height=1,font=("Arial",15),command=lambda:[Statement()]).place(x=120,y=80)
    Button(st,text="GRAPH",width=10,height=1,font=("Arial",15),command=lambda:[st.destroy(),graph1()]).place(x=280,y=80)
#-------------------------------------------------------------
def et_NOr():
    g1.configure(state=NORMAL, background='#B0E0E6')
    g2.configure(state=NORMAL, background='#B0E0E6')
    g3.configure(state=NORMAL, background='#B0E0E6')
    g4.configure(state=NORMAL, background='#B0E0E6')
def et_dis():
    g1.configure(state=DISABLED, background='#E6E6FA')
    g2.configure(state=DISABLED, background='#E6E6FA')
    g3.configure(state=DISABLED, background='#E6E6FA')
    g4.configure(state=DISABLED, background='#E6E6FA')
#-------------------------------------------------------------   
def new_address():
    address_info=address1.get()
    account_info=accountnumber.get()
    if (address_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("update bank set Address=%s where AccountNo=%s",(address_info,account_info,))
        mydb.commit()
        mb.showinfo("Update","Address Change Successful")
def address():
    global Address
    global address1
    address1=StringVar()
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        result=cur.fetchall()
        for x in result:
            Address=x[8]
        z1=Label(et,text="CURRENT ADDRESS :",font=("Arial",15),fg="black",height=2,bg="white")
        z1.place(x=250,y=280)
        z2=Label(et,text=Address,font=("Arial",15),bg="white")
        z2.place(x=500,y=290)

        z3=Label(et,text="NEW ADDRESS :",font=("Arial",15),fg="black",height=2,bg="white")
        z3.place(x=250,y=340)
        z4=Entry(et,textvariable=address1,font=("Arial",15))
        z4.place(x=500,y=350)
        z5=Button(et,text="CHANGE",font=("Arial",15),command=new_address)
        z5.place(x=320,y=400)
        z6=Button(et,text="< GO BACK",font=("Arial",15),command=lambda:[et_NOr(),Type(),z1.destroy(),z1.destroy(),z2.destroy(),z3.destroy(),z4.destroy(),z5.destroy(),z6.destroy()])
        z6.place(x=450,y=400)
def new_type():
    Accounty_info=Act1
    account_info=accountnumber.get()
    if (Accounty_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("update bank set AccountType=%s where AccountNo=%s",(Accounty_info,account_info,))
        mydb.commit()
        mb.showinfo("Update","Account Type Edited successful")
def type1():
    global Actype
    global Act1
    Act1=StringVar()
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("Update", "All fields are required",parent=screen0)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        result=cur.fetchall()
        for x in result:
            Actype=x[5]
        a1=Label(et,text="CURRENT ACCOUNT TYPE :",font=("Arial",15),fg="black",bg="white",height=2)
        a1.place(x=250,y=280)
        a2=Label(et,text=Actype,font=("Arial",15),bg="white")
        a2.place(x=530,y=290)

        if Actype=='Saving':
            Act1=('Current')
        else:
            Actype=='Current'
            Act1=('Saving')

        a3=Label(et,text="NEW ACCOUNT TYPE :",font=("Arial",15),fg="black",bg="white",height=2)
        a3.place(x=250,y=340)
        a4=Label(et,text=Act1,font=("Arial",15),bg="white")
        a4.place(x=530,y=350)
        a5=Button(et,text="CHANGE",font=("Arial",15),command=lambda:[new_type()])
        a5.place(x=320,y=400)
        a6=Button(et,text="< GO BACK ",font=("Arial",15),command=lambda:[et_NOr(),Type(),a1.destroy(),a1.destroy(),a2.destroy(),a3.destroy(),a4.destroy(),a5.destroy(),a6.destroy()])
        a6.place(x=450,y=400)
def new_contact():
    contact_info=con1.get()
    account_info=accountnumber.get()
    if (contact_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("update bank set MobileNo=%s where AccountNo=%s",(contact_info,account_info,))
        mydb.commit()
        mb.showinfo("Update","Contact Edited successful")
def contact():
    global Contact
    global con1
    con1=StringVar()
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        result=cur.fetchall()
        for x in result:
            contact=x[7]
        c1=Label(et,text="CURRENT CONTACT NO :",font=("Arial",15),bg="white",fg="black",height=2)
        c1.place(x=250,y=280)
        c2=Label(et,text=contact,font=("Arial",15),bg="white")
        c2.place(x=500,y=290)

        c3=Label(et,text="NEW CONTACT NO :",font=("Arial",15),bg="white",fg="black",height=2)
        c3.place(x=250,y=340)
        c4=Entry(et,textvariable=con1,font=("Arial",15))
        c4.place(x=500,y=350)
        c5=Button(et,text="CHANGE",font=("Arial",15),command=new_contact)
        c5.place(x=320,y=400)
        c6=Button(et,text="< GO BACK ",font=("Arial",15),command=lambda:[et_NOr(),Type(),c1.destroy(),c1.destroy(),c2.destroy(),c3.destroy(),c4.destroy(),c5.destroy(),c6.destroy()])
        c6.place(x=450,y=400)
def Type():
    global g1
    global g2
    global g3
    global g4
    g1=Button(et,text="CONTACT NO ",font=("Arial",15),bg="#B0E0E6",command=lambda:[et_dis(),contact()],width=15)
    g1.place(x=100,y=200)
    g2=Button(et,text="ACOOUNT TYPE",font=("Arial",15),bg="#B0E0E6",command=lambda:[et_dis(),type1()],width=15)
    g2.place(x=300,y=200)
    g3=Button(et,text="ADDRESS",font=("Arial",15),bg="#B0E0E6",command=lambda:[et_dis(),address()],width=15)
    g3.place(x=500,y=200)
    g4=Button(et,text="EXIT",font=("Arial",15),bg="#B0E0E6",command=lambda:[unable_me(),et.destroy()],width=15)
    g4.place(x=700,y=200)
           
def My():
    global Fullname
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("Update", "All fields are required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
        Label(et,text="FULL NAME :",font=("Arial",15),fg="black",bg="white",height=2).place(x=20,y=120)
        Label(et,text=Fullname,font=("Arial",15),bg="white").place(x=200,y=130)
def edit():
    global et
    et=LabelFrame(screen,text="EDIT PROFILE",font=("Arial",25),width=900,height=550,bg="white")
    et.place(x=350,y=220)
    Label(et,text="ACCOUNT NUMBER  :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Label(et,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(et,text="PROCED",width=10,height=1,font=("Arial",10),command=lambda:[My(),Type()]).place(x=120,y=80)  
#-------------------------------------------------------------

def mysql_pay():
        payment_info=pay
        loanac_my=loanac.get()
        if (payment_info=="" or loanac_my==""):
                mb.showinfo("insert status", "All fields are required")
        else:
                mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
                cur = mydb.cursor()
                cur.execute("update loan set Loanamt=Loanamt-%s where LoanAcc=%s",(payment_info,loanac_my,))
                mydb.commit()
                mb.showinfo("Insert status","Insert successful")
def pay_Pluse():
        global loanty_info
        global loanamt_info
        global time
        global pay
        pay=StringVar()
        loanac_my=loanac.get()
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from loan where LoanAcc=%s",(loanac_my,))
        result=cur.fetchall()
        for x in result:
            loanty_info=x[3]
            time=x[8]
            loanamt_info=x[9]
        if time=='3 Months':
                time=(3)
        elif time=='6 Months':
                time=(6)
        else:
                time=='9 Months'
                time=(9)
        if loanty_info=='Busisness Loan':
                loanty_info=(14)
        elif loanty_info=='Education Loan':
                loanty_info=(13)
        elif loanty_info=='Vehicle Loan':
                loanty_info=(12)
        elif loanty_info=='Farming Loan':
                loanty_info=(11)
        elif loanty_info=='Home Loan':
                loanty_info=(10)
        elif loanty_info=='Persional Loan':
                loanty_info=(9)
        elif loanty_info=='Mountly Loan':
                loanty_info=(8)
        else:
                loanty_info=='Morgage Loan'
                loanty_info=(7)
        a = loanamt_info*loanty_info/100*time/12
        b = loanamt_info
        c = a+b
        
        d = c/time
        pay= math.trunc(d)
        Label(pa,text="MONTHLY PAYMENT :",font=("Arial",19),fg="black",height=2,bg="white").place(x=400,y=100)
        Label(pa,text=pay,font=("Arial",19),bg="white").place(x=700,y=118)
        Button(pa,text="PAY",width=10,height=1,font=("Arial",10),command=mysql_pay).place(x=500,y=180)
        Button(pa,text="< GO BACK",width=10,height=1,font=("Arial",10),command=lambda:[pa.destroy(),loan_page()]).place(x=600,y=180)
def pay_Minuse():
        mb.showinfo("insert status", "please try again or contact to branch")
def show_pay():
    global FullName
    global moblieno
    global loanty
    global branch
    global Occ
    global time
    global loanamt

    loanac_info=loanac.get()
    if (loanac_info==""):
        mb.showinfo("insert status", "AccountNo is required")
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from loan where LoanAcc=%s",(loanac_info,))
        result=cur.fetchall()
        for x in result:
            FullName=x[0]
            mobileno=x[2]
            loanty=x[3]
            branch=x[5]
            Occ=x[6]
            time=x[8]
            loanamt=x[9]
        Label(pa,text="FULL NAME :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=130)
        Label(pa,text=FullName,font=("Arial",15),bg="white").place(x=200,y=140)
        
        Label(pa,text="CONTACT NO :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=170)
        Label(pa,text=mobileno,font=("Arial",15),bg="white").place(x=200,y=180)

        Label(pa,text="LOAN TYPE :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=210)
        Label(pa,text=loanty,font=("Arial",15),bg="white").place(x=200,y=220)

        Label(pa,text="BRANCH :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=250)
        Label(pa,text=branch,font=("Arial",15),bg="white").place(x=200,y=260)

        Label(pa,text="OCCUPATION :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=290)
        Label(pa,text=Occ,font=("Arial",15),bg="white").place(x=200,y=300)

        Label(pa,text="TIME PERIOD :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=330)
        Label(pa,text=time,font=("Arial",15),bg="white").place(x=200,y=340)

        Label(pa,text="LOAN AMOUNT :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=370)
        Label(pa,text=loanamt,font=("Arial",15),bg="white").place(x=200,y=380)

        Label(pa,text="This Details Accurate",font=("Arial",20),fg="#008080",height=2,bg="white").place(x=30,y=410)
        Button(pa,text="Yes",width=10,height=1,font=("Arial",10),command=pay_Pluse).place(x=60,y=465)
        Button(pa,text="No",width=10,height=1,font=("Arial",10),command=pay_Minuse).place(x=160,y=465)
        

    
def pay_loan():
    global pa
    global loanac
    loanac=StringVar()
    pa=LabelFrame(screen,text="PAYMENT",font=("Arial",25),width=900,height=550,bg="white")
    pa.place(x=350,y=220)
    
    Label(pa,text="LOAN ACCOUNT NO   :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Entry(pa,textvariable=loanac).place(x=300,y=38)
    Button(pa,text="DETAILS",width=10,height=1,font=("Arial",10),command=show_pay).place(x=120,y=80)
    
def calculater_info():
    loanac_info=loanac.get()
    time_info=time.get()
    loanty_info=loanty.get()
    if (loanac_info=="" or time_info=="" or loanty_info==""):
        mb.showinfo("insert status", "All fields are required",parent=screen1)
    else:
        a = loanac_info*loanty_info/100*time_info/12
        b = loanac_info
        c = a+b
        d = c/time_info
        e = math.trunc(d)
        Label(cal,text="MOUNTLY PAYMENT         :",font=("Bold",15),fg="black",bg="white",height=2).place(x=20,y=300)
        Label(cal,text=e,font=("Bold",15),bg="white").place(x=300,y=310)
        
        Label(cal,text="INTEREST PERSENTAGE   :",font=("Bold",15),fg="black",bg="white",height=2).place(x=20,y=340)
        Label(cal,text=loanty_info,font=("Bold",15),bg="white").place(x=300,y=350)
        
        Label(cal,text="TOTOAL INTEREST            :",font=("Bold",15),fg="black",bg="white",height=2).place(x=20,y=380)
        Label(cal,text=a,font=("Bold",15),bg="white").place(x=300,y=390)

        Label(cal,text="AMOUNT(+)                        :",font=("Bold",15),fg="black",bg="white",height=2).place(x=20,y=420)
        Label(cal,text=b,font=("Arial",15),bg="white").place(x=300,y=430)
        

        Label(cal,text="TOTAL                                :",font=("Bold",15),fg="black",bg="white",height=2).place(x=20,y=460)
        Label(cal,text=c,font=("Bold",15),bg="white").place(x=300,y=470)
        Button(cal,text="< Go Back",font=("Arial",15),command=lambda:[cal.destroy(),loan_page()]).place(x=200,y=510)
    
def calculater():
    global cal
    cal=LabelFrame(screen,text="INTEREST CALCULATE",font=("Arial",25),width=900,height=600,bg="white")
    cal.place(x=350,y=220)
    global loanac
    global time
    global loanty
    loanac=IntVar()
    time=IntVar()
    loanty=IntVar()
    Label(cal,text="LOAN AMOUNT :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=20)
    Entry(cal,textvariable=loanac).place(x=200,y=38)

    Label(cal,text="TIME PERIOD   :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=80)   
    radio_3Mounts=Radiobutton(cal,text="3 Mounts",value="3",variable=time,bg="white").place(x=200,y=98)
    radio_6Mounts=Radiobutton(cal,text="6 Mounts",value="6",variable=time,bg="white").place(x=300,y=98)
    radio_9Mounts=Radiobutton(cal,text="9 Mounts",value="9",variable=time,bg="white").place(x=200,y=125)
    time.set("K")

    Label(cal,text="LOAN TYPE      :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=140)
    radio_Busisness=Radiobutton(cal,text="Busisness Loan",value="14",variable=loanty,bg="white").place(x=200,y=158)
    radio_Education=Radiobutton(cal,text="Education Loan",value="13",variable=loanty,bg="white").place(x=200,y=178)
    radio_Vehicle=Radiobutton(cal,text="Vehicle Loan",value="12",variable=loanty,bg="white").place(x=200,y=198)
    radio_Farming=Radiobutton(cal,text="Farming Loan",value="11",variable=loanty,bg="white").place(x=200,y=218)
    radio_Home=Radiobutton(cal,text="Home Loan",value="5",variable=loanty,bg="white").place(x=350,y=158)
    radio_Persional=Radiobutton(cal,text="Persional Loan",value="10",variable=loanty,bg="white").place(x=350,y=178)
    radio_Mountly=Radiobutton(cal,text="Mountly Loan",value="9",variable=loanty,bg="white").place(x=350,y=198)
    radio_Morgage=Radiobutton(cal,text="Morgage Loan",value="8",variable=loanty,bg="white").place(x=350,y=218)
    loanty.set("L")

    Button(cal,text="CALCULAT",font=("Arial",15),command=calculater_info,width="10").place(x=125,y=250)
def Loan():
    fullname_info=fullname.get()
    gender_info=gender.get()
    moblieno_info=moblieno.get()
    loanty_info=loanty.get()
    loanac_info=loanac.get()
    
    branch_info=branch.get()
    Occ_info=Occ.get()
    inc_info=inc.get()
    time_info=time.get()
    loanamt_info=loanamt.get()
    
    if (fullname_info=="" or gender_info=="" or moblieno_info=="" or loanty_info=="" or loanac_info=="" or branch_info=="" or Occ_info=="" or inc_info=="" or time_info=="" or loanamt_info==""):
        mb.showinfo("insert status", "All fields are required",parent=screen)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql = "insert into Loan values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (fullname_info,gender_info,moblieno_info,loanty_info,loanac_info,branch_info,Occ_info,inc_info,time_info,loanamt_info)
        cur.execute(sql,val)
        mydb.commit()
        mb.showinfo("Insert status","Loan Account SuccessfulAdded",parent=screen)
def register1 ():
    global addme
    addme=LabelFrame(screen,text="ADD ACCOUNT",font=("Arial",25),width=900,height=550,bg="white")
    addme.place(x=350,y=220)
    global fullname
    global gender
    global moblieno
    global loanty
    global loanac
    global branch
    global Occ
    global inc
    global time
    global loanamt
    fullname=StringVar()
    gender=StringVar()
    moblieno=StringVar()
    loanty=StringVar()
    loanac=StringVar()
    branch=StringVar()
    Occ=StringVar()
    inc=StringVar()
    time=StringVar()
    loanamt=StringVar()
    
    Label(addme,text="FULL NAME :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=20)
    Entry(addme,textvariable=fullname).place(x=180,y=38)

    Label(addme,text="GENDER     :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=80)   
    radio_Male=Radiobutton(addme,text="Male",value="Saving",variable=gender,bg="white").place(x=180,y=100)
    radio_Female=Radiobutton(addme,text="Female",value="Current",variable=gender,bg="white").place(x=280,y=100)
    gender.set("M")

    Label(addme,text="CONTACT NO:",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=140)    
    Entry(addme,textvariable=moblieno).place(x=180,y=158)
    
    Label(addme,text="TYPE          :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=200)
    radio_Busisness=Radiobutton(addme,text="Busisness Loan",value="Busisness Loan",variable=loanty,bg="white").place(x=180,y=215)
    radio_Education=Radiobutton(addme,text="Education Loan",value="Education Loan",variable=loanty,bg="white").place(x=180,y=235)
    radio_Vehicle=Radiobutton(addme,text="Vehicle Loan",value="Vehicle Loan",variable=loanty,bg="white").place(x=180,y=255)
    radio_Farming=Radiobutton(addme,text="Farming Loan",value="Farming Loan",variable=loanty,bg="white").place(x=180,y=275)
    radio_Home=Radiobutton(addme,text="Home Loan",value="Home Loan",variable=loanty,bg="white").place(x=300,y=215)
    radio_Persional=Radiobutton(addme,text="Persional Loan",value="Persional Loan",variable=loanty,bg="white").place(x=300,y=235)
    radio_Mountly=Radiobutton(addme,text="Mountly Loan",value="Mountly Loan",variable=loanty,bg="white").place(x=300,y=255)
    radio_Morgage=Radiobutton(addme,text="Morgage Loan",value="Morgage Loan",variable=loanty,bg="white").place(x=300,y=275)
    loanty.set("L")

    Label(addme,text="ACCOUNT NO  :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=300)
    Entry(addme,textvariable=loanac).place(x=180,y=318)

    

    Label(addme,text="BRANCH      :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=360)   
    radio_Bhuj=Radiobutton(addme,text="Bhuj",value="Bhuj",variable=branch,bg="white").place(x=180,y=378)
    radio_Mundra=Radiobutton(addme,text="Mundra",value="Mundra",variable=branch,bg="white").place(x=280,y=378)
    radio_Mundra=Radiobutton(addme,text="Adipure",value="Adipure",variable=branch,bg="white").place(x=180,y=400)
    branch.set("B")

    Label(addme,text="OCCUPATION         :",font=("Arial",15),fg="black",height=2,bg="white").place(x=430,y=20)
    Entry(addme,textvariable=Occ).place(x=630,y=38)

    Label(addme,text="YEARLY INCOME   :",font=("Arial",15),fg="black",height=2,bg="white").place(x=430,y=80)
    Entry(addme,textvariable=inc).place(x=630,y=98)

    Label(addme,text="TIME PERIOD         :",font=("Arial",15),fg="black",height=2,bg="white").place(x=430,y=140)   
    radio_3=Radiobutton(addme,text="3 Month",value="3 Month",variable=time,bg="white").place(x=630,y=150)
    radio_6=Radiobutton(addme,text="6 Month",value="6 Month",variable=time,bg="white").place(x=730,y=150)
    radio_9=Radiobutton(addme,text="9 Month",value="9 Month",variable=time,bg="white").place(x=630,y=180)
    time.set("K")

    Label(addme,text="LOAN AMOUNT       :",font=("Arial",15),fg="black",height=2,bg="white").place(x=430,y=210)
    Entry(addme,textvariable=loanamt).place(x=630,y=228)
    
    Button(addme,text="ADD A\C",font=("Arial",15),command=Loan,width="10").place(x=460,y=300)   
    Button(addme,text="< BACK",font=("Arial",15),command=lambda:[addme.destroy(),loan_page()],width="10").place(x=600,y=300)
    
def loan_page ():
    global loa
    loa=LabelFrame(screen,text="LOAN",font=("Arial",25),width=900,height=600,bg="white")
    loa.place(x=350,y=220)

    
    Label(loa,text="1.BUSISNESS LOAN  -------  14%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=10)
    
        
    Label(loa,text="2.EDUCATION LOAN  -------  13%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=70)
    

    Label(loa,text="3.VEHICLE LOAN      -------  12%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=130)
    

    Label(loa,text="4.FARMING LOAN    -------   11%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=190)
    

    Label(loa,text="5.HOME LOAN       -------   10%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=250)
   

    Label(loa,text="6.PERSONAL LOAN  -------   9%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=310)
    

    Label(loa,text="7.MOUNTLY LOAN    -------   8%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=370)
    

    Label(loa,text="8.MORGAGE LOAN  -------   7%",font=("Arial",20),fg="black",bg="white",height=2).place(x=20,y=430)

    Button(loa,text="ADD ACCOUNT",font=("Arial",15),width="13",command=lambda:[loa.destroy(),register1()]).place(x=20,y=490)

    Button(loa,text="CALCULATER",font=("Arial",15),width="13",command=lambda:[loa.destroy(),calculater()]).place(x=180,y=490)

    Button(loa,text="PAYMENT",font=("Arial",15),width="13",command=lambda:[loa.destroy(),pay_loan()]).place(x=340,y=490)

    Button(loa,text="EXIT",font=("Arial",15),width="13",command=lambda:[loa.destroy(),unable_me()]).place(x=500,y=490)
#-------------------------------------------------------------
def withdraw_cheack():
    global rec1
    balance_info=Balance.get()
    my_info=accountnumber.get()
    tran3="Withdraw"
    mydb1 = ms.connect(host="localhost",user="root",passwd='',database='abc')
    cur1 = mydb1.cursor()
    cur1.execute("select Balance from bank where AccountNo=%s",(my_info,))
    rec=cur1.fetchall()
    for i in rec:
        rec1=i[0]
    if (balance_info==""):
        mb.showinfo("insert status", "All fields are required")
    elif(rec1>balance_info):
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql1="update bank set Balance=Balance-%s where AccountNo=%s"
        val=(balance_info,my_info,)
        cur.execute(sql1,val)
        cur.execute(" insert transation(Date,Time,AccountNo,Operation,AmountMinuse)values(curdate(),curtime(),%s,%s,%s)",(my_info,tran3,balance_info))
        mydb.commit()
        mb.showinfo("Insert status","Insert successful")
    else:
        mb.showerror("Error!!","Insufficient Balance")
def withdraw_final():
    Label(withd,text="PLEACE ENTER THE WITHDRAW AMOUNT PROPERLY",font=("Arial",15),fg="#008080",bg="white",height=2).place(x=360,y=100)
    global Balance
    Balance=IntVar()
    Label(withd,text="WITHDRAW AMOUNT:",font=("Arial",10),fg="black",bg="white").place(x=450,y=160)
    Entry(withd,textvariable=Balance).place(x=600,y=160)
    Button(withd,text="WITHDRAW",width=10,height=1,font=("Arial",10),command=withdraw_cheack).place(x=550,y=200)
    Button(withd,text="EXIT",width=5,height=1,font=("Arial",10),command=lambda:[unable_me(),withd.destroy()]).place(x=650,y=200)
    
def withdraw_info():
    global Fullname
    global accountno
    global type1
    global moblieno
    global Balance
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("insert status", "All fields are required",parent=withd)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        
        
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
            accountno=x[4]
            type1=x[5]
            moblieno=x[7]
            Balance=x[9]

        Label(withd,text="FULL NAME                :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=120)
        Label(withd,text=Fullname,font=("Arial",10),bg="white").place(x=220,y=130)
        
        Label(withd,text="ACCOUNT NO             :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=150)
        Label(withd,text=accountno,font=("Arial",10),bg="white").place(x=220,y=160)

        Label(withd,text="ACCOUNT TYPE         :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=180)
        Label(withd,text=type1,font=("Arial",10),bg="white").place(x=220,y=190)

        Label(withd,text="CONTACT NUMBER    :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=210)
        Label(withd,text=moblieno,font=("Arial",10),bg="white").place(x=220,y=220)

        Label(withd,text="CURRENT BALANCE   :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=240)
        Label(withd,text=Balance,font=("Arial",10),bg="white").place(x=220,y=250)
        
        Button(withd,text="OK",width=10,height=1,font=("Arial",10),command=withdraw_final).place(x=120,y=300)  

def withdraw():
    global withd
    withd=LabelFrame(screen,text="WITHDRAW",font=("Arial",25),width=900,height=550,bg="white")
    withd.place(x=350,y=220)
    
    Label(withd,text="ACCOUNT NUMBER  :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Label(withd,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(withd,text="DETAILS",width=10,height=1,font=("Arial",10),command=withdraw_info).place(x=120,y=80)
#show---------------------------------------------------------
def show():
    global Fullname
    global Idproof
    global gender
    global type1
    global caste
    global moblieno
    global address
    global Balance
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("insert status", "All fields are required",parent=mydata)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        
        
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
            Idproof=x[1]
            gender=x[3]
            type1=x[5]
            caste=x[6]
            moblieno=x[7]
            address=x[8]
            Balance=x[9]
            
        Label(mydata,text="FULL NAME:",font=("Arial",12),fg="black",height=2,bg="white").place(x=60,y=120)
        Label(mydata,text=Fullname,font=("Arial",12),bg="white").place(x=200,y=130)
        
        Label(mydata,text="GENDER:",font=("Arial",12),fg="black",height=2,bg="white").place(x=60,y=160)
        Label(mydata,text=gender,font=("Arial",12),bg="white").place(x=200,y=170)

        Label(mydata,text="ACCOUNT NO:",font=("Arial",12),fg="black",height=2,bg="white").place(x=60,y=200)
        Label(mydata,text=type1,font=("Arial",12),bg="white").place(x=200,y=210)

        Label(mydata,text="ID PROOF:",font=("Arial",12),fg="black",height=2,bg="white").place(x=60,y=240)
        Label(mydata,text=Idproof,font=("Arial",12),bg="white").place(x=200,y=250)


        Label(mydata,text="CASTE:",font=("Arial",12),fg="black",height=2,bg="white").place(x=400,y=120)
        Label(mydata,text=caste,font=("Arial",12),bg="white").place(x=530,y=130)

        Label(mydata,text="CONTACT NO:",font=("Arial",12),fg="black",height=2,bg="white").place(x=400,y=160)
        Label(mydata,text=moblieno,font=("Arial",12),bg="white").place(x=530,y=170)

        Label(mydata,text="ADDRESS:",font=("Arial",12),fg="black",height=2,bg="white").place(x=400,y=200)
        Label(mydata,text=address,font=("Arial",12),bg="white").place(x=530,y=210)

        Label(mydata,text="BALANCE:",font=("Arial",12),fg="black",height=2,bg="white").place(x=400,y=240)
        Label(mydata,text=Balance,font=("Arial",12),bg="white").place(x=530,y=250)

        Button(mydata,text="EXIT",width=8,height=1,font=("Arial",14),command=lambda:[unable_me(),mydata.destroy()]).place(x=300,y=300)       
def showme():
    global mydata
    mydata=LabelFrame(screen,text="VIEW PROFILE",font=("Arial",25),width=900,height=550,bg="white")
    mydata.place(x=350,y=220)
    Label(mydata,text="ACCOUNT NUMBER  :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Label(mydata,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(mydata,text="DETAILS",width=10,height=1,font=("Arial",10),command=show).place(x=120,y=80)

#online-------------------------------------------------------
def func2():
    give_info=ac.get()
    give1_info=accountnumber.get()
    bal1_info=bal.get()
    tran2="Transfer"
    if (give1_info=="" or bal1_info==""):
        mb.showinfo("insert status", "All fields are required",parent=onli)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql1="update bank set Balance=Balance-%s where AccountNo=%s"
        cur.execute(" insert transation(Date,Time,AccountNo,Operation,TransationAc,AmountMinuse)values(curdate(),curtime(),%s,%s,%s,%s)",(give1_info,tran2,give_info,bal1_info))
        val=(bal1_info,give1_info,)
        cur.execute(sql1,val)
        mydb.commit()
        
    
def func1():
    give_info=ac.get()
    bal_info=bal.get()
    give1_info=accountnumber.get()
    tran2="Transfer"
    if (give_info=="" or bal_info==""):
        mb.showinfo("insert status", "All fields are required",parent=onli)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql1="update bank set Balance=Balance+%s where AccountNo=%s"
        cur.execute(" insert transation(Date,Time,AccountNo,Operation,TransationAc,AmountPluse)values(curdate(),curtime(),%s,%s,%s,%s)",(give_info,tran2,give1_info,bal_info))
        val=(bal_info,give_info,)
        cur.execute(sql1,val)
        mydb.commit()
        mb.showinfo("Insert status","Insert successful",parent=onli)
def online1():
    am_info=ac.get()
    if (am_info==""):
        mb.showinfo("insert status", "All fields are required",parent=onli)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(am_info,))
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
    Label(onli,text="FULL NAME         :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=280)
    Label(onli,text=Fullname,font=("Arial",10),bg="white").place(x=190,y=290)

    Label(onli,text="TRANSFER AMT  :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=310)
    Entry(onli,textvariable=bal).place(x=190,y=320)

    Button(onli,text="TRANSFER",width=10,height=1,font=("Arial",10),command=lambda:[func1(),func2()]).place(x=100,y=360)
    Button(onli,text="EXIT",width=5,height=1,font=("Arial",10),command=lambda:[unable_me(),onli.destroy()]).place(x=200,y=360)
def online_final():
    global ac
    global bal
    ac=StringVar()
    bal=StringVar()

    Label(onli,text="TRANSFER A\C NO  :",font=("Arial",10),fg="black",bg="white").place(x=60,y=250)
    Entry(onli,textvariable=ac).place(x=230,y=255)

    Button(onli,text="DETAILS",width=10,height=1,font=("Arial",10),command=online1).place(x=400,y=250)

def online_info():
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("insert status", "All fields are required",parent=onli)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
            Balance=x[9]
        Label(onli,text="FULL NAME     :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=120)
        Label(onli,text=Fullname,font=("Arial",10),bg="white").place(x=180,y=130)
        
        Label(onli,text="BALANCE        :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=150)
        Label(onli,text=Balance,font=("Arial",10),bg="white").place(x=180,y=160)


        Button(onli,text="OK",width=10,height=1,font=("Arial",10),command=online_final).place(x=120,y=200)
def online():
    global onli
    onli=LabelFrame(screen,text="TRANSFER",font=("Arial",25),width=900,height=550,bg="white")
    onli.place(x=350,y=220)

    Label(onli,text="ACCOUNT NUMBER  :",font=("Arial",15),fg="black",bg="white",height=2).place(x=50,y=20)
    Label(onli,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(onli,text="BALANCE",width=10,height=1,font=("Arial",10),command=online_info).place(x=120,y=80)

#deposit-------------------------------------------------------
def deposite_cheack():
    tran1="Deposite"
    balance_info=Balance.get()
    my_info=accountnumber.get()
    
    if (balance_info==""):
        mb.showinfo("insert status", "All fields are required",parent=dep)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql1="update bank set Balance=Balance+%s where AccountNo=%s"
        val=(balance_info,my_info,)
        cur.execute(sql1,val)
        cur.execute(" insert transation(Date,Time,AccountNo,Operation,AmountPluse)values(curdate(),curtime(),%s,%s,%s)",(my_info,tran1,balance_info))
        mydb.commit()
        
        mb.showinfo("Insert status","Insert successful",parent=dep)
def deposite_final():
    
    Label(dep,text="PLEACE ENTER THE DEPOSITE AMOUNT",font=("Arial",15),fg="#008080",bg="white",height=2).place(x=400,y=100)
    global Balance
    Balance=StringVar()
    Label(dep,text="DEPOSIT AMOUNT:",font=("Arial",10),fg="black",bg="white").place(x=450,y=160)
    Entry(dep,textvariable=Balance).place(x=600,y=160)
    Button(dep,text="DEPOSIT",width=10,height=1,font=("Arial",10),command=deposite_cheack).place(x=550,y=200)
    Button(dep,text="EXIT",width=5,height=1,font=("Arial",10),command=lambda:[unable_me(),dep.destroy()]).place(x=650,y=200)
def deposite_info():
    global Fullname
    global accountno
    global type1
    global moblieno
    global Balance
    
    account_info=accountnumber.get()
    if (account_info==""):
        mb.showinfo("insert status", "All fields are required",parent=dep)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        cur.execute("select* from bank where AccountNo=%s",(account_info,))
        
        
        result=cur.fetchall()
        for x in result:
            Fullname=x[0]
            accountno=x[4]
            type1=x[5]
            moblieno=x[7]
            Balance=x[9]
            
        Label(dep,text="FULL NAME                :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=120)
        Label(dep,text=Fullname,font=("Arial",10),bg="white").place(x=220,y=130)
        
        Label(dep,text="ACCOUNT NO             :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=150)
        Label(dep,text=accountno,font=("Arial",10),bg="white").place(x=220,y=160)

        Label(dep,text="ACCOUNT TYPE         :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=180)
        Label(dep,text=type1,font=("Arial",10),bg="white").place(x=220,y=190)

        Label(dep,text="CONTACT NUMBER    :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=210)
        Label(dep,text=moblieno,font=("Arial",10),bg="white").place(x=220,y=220)

        Label(dep,text="CURRENT BALANCE   :",font=("Arial",10),fg="black",height=2,bg="white").place(x=60,y=240)
        Label(dep,text=Balance,font=("Arial",10),bg="white").place(x=220,y=250)
        
        Button(dep,text="OK",width=10,height=1,font=("Arial",10),command=deposite_final).place(x=120,y=300)
def deposite():
    global dep
    dep=LabelFrame(screen,text="DEPOSITE",font=("Arial",25),width=900,height=550,bg="white")
    dep.place(x=350,y=220)
    Label(dep,text="ACCOUNT NUMBER  :",font=("Arial",15),height=2,bg="white").place(x=50,y=20)
    Label(dep,textvariable=accountnumber,font=("Arial",15),bg="white").place(x=300,y=30)
    Button(dep,text="DETAILS",width=10,height=1,font=("Arial",10),command=deposite_info).place(x=120,y=80)
#----------------------------------------------------------------------------------
def main():
    global main
    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8
    main=Frame(screen,width=310,height=650,bg="white")
    main.place(x=10,y=170)

    m1=Button(main,text="DEPOSITE",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),deposite()])
    m1.place(x=4,y=10)

    m2=Button(main,text="TRANSEFER",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),online()])
    m2.place(x=4,y=90)

    m3=Button(main,text="DETAILS",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),showme()])
    m3.place(x=4,y=170)

    m4=Button(main,text="WITHDRAW",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),withdraw()])
    m4.place(x=4,y=250)

    #Button(main,text="DELETE ACCOUNT",bg="white",font=("Arial",15),command=delete).place(x=600,y=90)

    m5=Button(main,text="LOAN",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),loan_page()])
    m5.place(x=4,y=330)

    m6=Button(main,text="EDIT",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),edit()])
    m6.place(x=4,y=410)

    m7=Button(main,text="STATMENT",font=("Arial",25),width="15",bg="#E6E6FA",command=lambda:[Disable_me(),statement_show()])
    m7.place(x=4,y=490)

    m8=Button(main,text="LOG OUT",font=("Arial",25),command=lambda:[screen.destroy()],width="15",bg="#E6E6FA")
    m8.place(x=4,y=570)
#------------------------------------------------------------------------------------------------
def Disable():
        b1.configure(state=DISABLED, background='cadetblue')
        b2.configure(state=DISABLED, background='cadetblue')
        b3.configure(state=DISABLED, background='cadetblue')
        e1.configure(state=DISABLED, background='cadetblue')
        e2.configure(state=DISABLED, background='cadetblue')
#------------------------------------------------------------------------------------------------
def Add_user():
    fullname_info=add_name.get()
    Id_info=Id.get()
    nationality_info=nationality.get()
    gender_info=gender.get()
    accountno_info=add_accno.get()
    type1_info=type1.get()
    caste_info=caste.get()
    moblieno_info=add_cont.get()
    address_info=address.get()
    amt_info=amt.get()
    tran4="Account open"
    if (fullname_info=="" or Id_info=="" or nationality_info=="" or gender_info=="" or accountno_info=="" or type1_info=="" or caste_info=="" or moblieno_info=="" or address_info=="" or amt_info==""):
        mb.showinfo("insert status", "All fields are required",parent=screen)
    else:
        mydb = ms.connect(host="localhost",user="root",passwd='',database='abc')
        cur = mydb.cursor()
        sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (fullname_info,Id_info,nationality_info,gender_info,accountno_info,type1_info,caste_info,moblieno_info,address_info,amt_info)
        cur.execute(sql,val)
        cur.execute(" insert transation(Date,Time,AccountNo,Operation,AmountPluse)values(curdate(),curtime(),%s,%s,%s)",(accountno_info,tran4,amt_info))
        mydb.commit()
        mb.showinfo("Insert status","Insert successful",parent=screen)
        Button(New,text="Exit",font=("Arial",15),fg="white",bg="orange",command=lambda:[Lonin_normal(),New.destroy()]).place(x=500,y=450)
    

#------------------------------------------------------------------------------------------------
def register_user():
    first_in=add_name.get()
    sur_in=add_name.get()
    email_in=email.get()
    accountnumber_in=add_accno.get()
    password_in=password.get()
    contact_in=add_cont.get()
    if (first_in=="" or sur_in=="" or email_in=="" or accountnumber_in=="" or
        password_in=="" or contact_in==""):
        mb.showinfo("insert status", "All fields are required",parent=screen)
    else:
        mydb=ms.connect(host='localhost',user='root',passwd='',database='abc')
        cur=mydb.cursor()
        sql=("insert into register values(%s,%s,%s,%s,%s,%s)")
        val=(first_in,sur_in,email_in,accountnumber_in,password_in,contact_in)
        cur.execute(sql,val)
        mydb.commit()
        Add_user()
        
def getme():
    my_meet=myotp.get()
    if my_meet ==  a:
        mb.showinfo("Registation","OTP Is Correct",parent=screen)
        register_user()
        Add_user()
    else:
        mb.showerror("Error","OTP Is Incorrect",parent=screen)
          
def Cheack():
    global myotp
    myotp=StringVar()
    Label(New,text="ENTER OTP:",font=("Arial",15),bg="white").place(x=200,y=400)
    Entry(New,text=myotp,font=("Arial",10)).place(x=350,y=405)
    Button(New,text="Register",font=("Arial",15),fg="white",bg="orange",command=getme).place(x=375,y=450)
    
       
def my():
    global a
    a=StringVar()
    otp="0123456789"
    lent =len(otp)
    a=''
    for i in range(6):
        a+=otp[math.floor(random.random()*lent)]
    mb.showinfo("OTP","OTP Genrated successful",parent=screen)
    otp_contact=add_cont.get()
    if otp_contact=="":
        mb.showinfo("OTP Sent","OTP Sent TO Your Mobile No.",parent=screen)
    else:
        account_sid = '<id>'
        auth_token = '<token>'
        client = Client(account_sid, auth_token)
        ''' Change the value of 'from' with the numberreceived from Twilio and the value of 'to' with the number in which you want to send message.'''
        message = client.messages.create( 
                              from_='+15674851403', 
                              body = "Your BANK One Time Passwod(OTP)- " +str(a), 
                              to = otp_contact
                          )
        #print(message.sid)
    Cheack()
def register_otp():
    first_info=add_name.get()
    sur_info=add_name.get()
    email_info=email.get()
    accountnumber_info=add_accno.get()
    password_info=password.get()
    contact_info=add_cont.get()
    if (first_info=="" or sur_info=="" or email_info=="" or accountnumber_info=="" or
        password_info=="" or contact_info==""):
        mb.showinfo("insert status", "All fields are required",parent=screen)
    else:
        my()
def add():
    global New
    New=LabelFrame(screen,text="ADD ACCOUNT",font=("Arial",25),width=800,height=550,bg="white")
    New.place(x=350,y=220)
    global add_name
    global Id
    global nationality
    global gender
    global add_accno
    global type1
    global caste
    global add_cont
    global address
    global email
    global password
    global amt
    add_name=StringVar()
    Id=StringVar()
    nationality=StringVar()
    gender=StringVar()
    add_accno=IntVar()
    type1=StringVar()
    caste=StringVar()
    add_cont=StringVar()
    address=StringVar()
    email=StringVar()
    password=StringVar()
    amt=StringVar()
    Label(New,text="FULL NAME :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=20)
    Entry(New,textvariable=add_name).place(x=200,y=35)
    
    Label(New,text="ID PROOF :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=70)
    radio_male=Radiobutton(New,text="Adhaar Card",font=("Arial",10),value="Adhaar Card",variable=Id,bg="white").place(x=200,y=85)
    radio_female=Radiobutton(New,text="Pan card",font=("Arial",10),value="Pan card",variable=Id,bg="white").place(x=300,y=85)
    radio_female=Radiobutton(New,text="Any outher",font=("Arial",10),value="Any outher",variable=Id,bg="white").place(x=200,y=120)
    Id.set("g")

    Label(New,text="ACCOUNT NO :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=130)    
    Entry(New,textvariable=add_accno).place(x=200,y=148)

    Label(New,text="ACCOUNT TYPE :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=180)   
    radio_saving=Radiobutton(New,text="Saving",font=("Arial",10),value="Saving",variable=type1,bg="white").place(x=200,y=195)
    radio_Current=Radiobutton(New,text="Current",font=("Arial",10),value="Current",variable=type1,bg="white").place(x=300,y=195)
    type1.set("s")

    Label(New,text="ADDRESS :",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=230)    
    Entry(New,textvariable=address).place(x=200,y=245)

    Label(New,text="EMAIL:",font=("Arial",15),fg="black",height=2,bg="white").place(x=20,y=290)
    Entry(New,textvariable=email).place(x=200,y=300)
    
    Label(New,text="NATIONALITY:",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=20)
    Entry(New,textvariable=nationality).place(x=610,y=38)
    
    Label(New,text="GENDER :",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=70)   
    radio_saving=Radiobutton(New,text="Male",font=("Arial",10),value="Male",variable=gender,bg="white").place(x=550,y=85)
    radio_Current=Radiobutton(New,text="Female",font=("Arial",10),value="Female",variable=gender,bg="white").place(x=650,y=85)
    gender.set("s")
    
    Label(New,text="CASTE :",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=130)    
    Entry(New,textvariable=caste).place(x=610,y=148)

    Label(New,text="MOBILE NO :",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=180)    
    Entry(New,textvariable=add_cont).place(x=610,y=199)

    Label(New,text="PASSWORD:",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=230)
    Entry(New,text=password,show="*").place(x=610,y=245)

    Label(New,text="DEPOSITE AMT:",font=("Arial",15),fg="black",height=2,bg="white").place(x=450,y=280)    
    Entry(New,textvariable=amt).place(x=610,y=295)
    
    Button(New,text="OTP",bg="white",font=("Arial",15),command=register_otp).place(x=375,y=350)

def login_user():
    acc_info=accountnumber.get()
    pass_info=password.get()
    if acc_info=="":
        mb.showinfo("Error","Please Enter AccountNo")
    elif pass_info=="":
        mb.showinfo("Error","Please Enter Password")
    
    else:
        mydb=ms.connect(host='localhost',user='root',passwd='',database='abc')
        cur=mydb.cursor()
        cur.execute("select AccountNo,Password from register where AccountNo=%s and Password=%s",(acc_info,pass_info))
        myrecords=cur.fetchall()
        count=cur.rowcount
        if count==0:
            mb.showinfo("Error","No user found",parent=screen)
        else:
            for x in myrecords:
                AccountNo=x[0]
                Password=x[1]
            if AccountNo==acc_info and Password==pass_info:
                
                main()
            else:
                mb.showinfo("Error","Invalid credentials",parent=screen)
def pass_show():
    global e3
    pass_me=password.get()
    if (pass_me==""):
        mb.showinfo("Error status", "Password is required",parent=screen)
    else:
        e3=Entry(login,text=password,font=("Arial",10))
        e3.place(x=150,y=66)
        
def main_screen():
    global screen
    global login
    global b1
    global b2
    global b3
    global e1
    global e2
    screen=Tk()
    screen.title("BANK")
    screen.geometry("1550x850+1+1")
    screen.configure(background='White')
    screen.iconbitmap('D:\\Bank\\coin.ico')

    canvas=Canvas(screen,width=140,height=140,bg="white")
    image=ImageTk.PhotoImage(Image.open("D:\\Bank\\coin.ico"))
    canvas.create_image(70,70,image=image)
    canvas.place(x=80,y=20)
    
    login=LabelFrame(screen,text="Login",font=("Arial",25),width=400,height=200,bg="white")
    login.place(x=1000,y=10)
    global accountnumber
    global password
    accountnumber=IntVar()
    password=StringVar()

    Label(screen,text="Welcome To Bank!!",font=("Arial",35),bg="white").place(x=450,y=10)

    Label(login,text="Account No:",font=("Arial",15),bg="white").place(x=20,y=20)
    e1=Entry(login,text=accountnumber,font=("Arial",10))
    e1.place(x=150,y=26)
    
    Label(login,text="Password:",font=("Arial",15),bg="white").place(x=20,y=60)
    e2=Entry(login,text=password,show="*",font=("Arial",10))
    e2.place(x=150,y=66)

    b1=Button(login,text="Show",font=("Arial",15),command=pass_show)
    b1.place(x=300,y=60)
    b2=Button(login,text="Login",font=("Arial",15),command=lambda:[Disable(),login_user()])
    b2.place(x=100,y=100)
    b3=Button(login,text="Register",font=("Arial",15),command=lambda:[Disable(),add()])
    b3.place(x=180,y=100)
    screen.mainloop()   
main_screen()
