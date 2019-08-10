from tkinter import *
from tkinter.ttk import *
import mysql.connector
from tkinter import messagebox
conn=mysql.connector.connect(host="localhost",user="Rahul",passwd="pithen",auth_plugin="mysql_native_password",database="NewDatabase")
var=conn.cursor()
root = Tk()
root.geometry("800x600")
root.title("Project")
bgimg=PhotoImage(file=r"images/kid.png")
mainmenu = Menu(root)

#for file menu
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=quit)
m1.add_command(label="Open",command=quit)
m1.add_separator()
m1.add_command(label="Save",command=quit)
m1.add_command(label="Save As",command=quit)
m1.add_command(label="Print",command=quit)
m1.add_command(label="Exit",command=root.destroy)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

#for edit menu
m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=quit)
m2.add_command(label="Copy",command=quit)
m2.add_separator()
m2.add_command(label="Paste",command=quit)
m2.add_command(label="Find",command=quit)
m2.add_command(label="Print",command=quit)
m2.add_command(label="Exit",command=root.destroy)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

#frame
frame=Frame(root,borderwidth=0,relief=SUNKEN)
frame.pack(side=RIGHT)
frame1=Frame(root,borderwidth=0,relief=SUNKEN)
frame1.pack(side=BOTTOM,anchor="sw")
#images
st=PhotoImage(file=r"images/student.png").subsample(5,5)
tea=PhotoImage(file=r"images/classroom.png").subsample(5,5)
staf=PhotoImage(file=r"images/service.png").subsample(5,5)
boo=PhotoImage(file=r"images/books.png").subsample(5,5)
fee=PhotoImage(file=r"images/fee.png").subsample(5,5)
sms=PhotoImage(file=r"images/sms.png").subsample(5,5)
res=PhotoImage(file=r"images/analysis.png").subsample(5,5)
atten=PhotoImage(file=r"images/attend.png").subsample(5,5)
sal=PhotoImage(file=r"images/salary.png").subsample(5,5)
exi=PhotoImage(file=r"images/exit.png").subsample(5,5)

#defition of functions
def AddStudent():
    studentWindow=Tk()
    studentWindow.geometry("500x500")
    studentWindow.title("Add Record")

    #Stringvar
    s1=StringVar(studentWindow)
    s2=StringVar(studentWindow)
    s3=StringVar(studentWindow)
    s4=StringVar(studentWindow)
    s5=StringVar(studentWindow)
    s6=StringVar(studentWindow)

    #frames
    f1=Frame(studentWindow)
    f1.pack(side=LEFT,anchor="nw",padx="10",pady="10")

    #label
    l1=Label(f1,text="Name:").grid(row=0,column=0,padx=10,pady=10)
    l2=Label(f1,text="Class:").grid(row=1,column=0,padx=10,pady=10)
    l3=Label(f1,text="Section").grid(row=2,column=0,padx=10,pady=10)
    l4=Label(f1,text="Gender").grid(row=3,column=0,padx=10,pady=10)
    l5=Label(f1,text="Birth Date").grid(row=4,column=0,padx=10,pady=10)
    l5=Label(f1,text="Admission Date").grid(row=5,column=0,padx=10,pady=10)

    #Combobox
    choices=['1','2','3','4','5','6','7','8','9','11','12']
    choices2=['Male','Female']
    op1=Combobox(f1,values=choices,width="18",textvariable=s2)
    op1.grid(row=1,column=1,padx=10,pady=10)
    op2=Combobox(f1,values=choices2,width="18",textvariable=s4).grid(row=3,column=1,padx=10,pady=10)


    #entry
    e1=Entry(f1,width=20,textvariable=s1).grid(row=0,column=1)
    e2=Entry(f1,width=20,textvariable=s3).grid(row=2,column=1)
    e3=Entry(f1,width=20,textvariable=s5).grid(row=4,column=1)
    e4=Entry(f1,width=20,textvariable=s6).grid(row=5,column=1)


    #userinstruction
    s6.set("yyyy-mm-dd")
    s5.set("yyyy-mm-dd")

    def clr():
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        s6.set("")
    #sql connectivity
    def save():
        global var
        global conn
        quer="Insert into Student(Name, Class, Section, Gender,DOB,Admis_Date) values(%s,%s,%s,%s,%s,%s)"
        var.execute(quer,(s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get()))
        conn.commit()
        messagebox.showinfo("Info","Record submitted successfully")
        clr()
    b1=Button(f1,text="Submit",command=save).grid(row=6,column=0,padx=10,pady=10)
    b2=Button(f1,text="Clear",command=clr).grid(row=6,column=7,padx=10,pady=10)
    Label(f1,text="Note : Date format is yyyy-mm-dd").grid(row=8,column=0,pady=10,padx=10)
#defition of Teacher
def Teacher():
    TeacherWin=Tk()
    TeacherWin.geometry("800x600")
    TeacherWin.title("Add Record")

    #frames
    ft=Frame(TeacherWin)
    ft.pack(side=LEFT,anchor="nw",padx=10,pady=10)

    #StringVar
    s1=StringVar(TeacherWin)
    s2=StringVar(TeacherWin)
    s3=StringVar(TeacherWin)
    s4=StringVar(TeacherWin)
    s5=StringVar(TeacherWin)
    s6=StringVar(TeacherWin)
    s7=StringVar(TeacherWin)
    s8=StringVar(TeacherWin)

    #Combobox
    choices=["Male","Female"]
    cho=Combobox(ft,values=choices,textvariable=s6,width="18").grid(row=5,column=1,padx=10,pady=10)

    #Label
    lt1=Label(ft,text="Name:").grid(row=0,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Birth Date:").grid(row=1,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Joining Date:").grid(row=2,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Contact:").grid(row=3,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Another Contact:").grid(row=4,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Gender:").grid(row=5,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Designation:").grid(row=6,column=0,padx=10,pady=10)
    lt1=Label(ft,text="Salary:  Rs").grid(row=7,column=0,padx=10,pady=10)

    #entry
    e1=Entry(ft,width=20,textvariable=s1).grid(row=0,column=1)
    e2=Entry(ft,width=20,textvariable=s2).grid(row=1,column=1)
    e3=Entry(ft,width=20,textvariable=s3).grid(row=2,column=1)
    e4=Entry(ft,width=20,textvariable=s4).grid(row=3,column=1)
    e5=Entry(ft,width=20,textvariable=s5).grid(row=4,column=1)
    e6=Entry(ft,width=20,textvariable=s7).grid(row=6,column=1)
    e1=Entry(ft,width=20,textvariable=s8).grid(row=7,column=1)

    def clr():
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        s6.set("")
        s7.set("")
        s8.set("")

    #sql connectivity
    def save():
        global var
        global conn
        quer="Insert into Staff(Name, DOB, DOJ, Contact, Another_Contact, Gender, Designation, Salary) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        var.execute(quer,(s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get()))
        conn.commit()
        messagebox.showinfo("Info","Record submitted successfully")
        clr()
    Button(ft,text="Submit",command=save).grid(row=8,column=0,padx=10,pady=10)
    Button(ft,text="Clear",command=clr).grid(row=8,column=7,padx=10,pady=10)
    Label(ft,text="Note : Date format is yyyy-mm-dd").grid(row=10,column=0,padx=10,pady=10)

#label for image
l1=Label(frame1,image=bgimg).pack(side=BOTTOM,anchor="sw")
#buttons
stu=Button(frame,text="Add Student",image=st,compound=TOP,command=AddStudent).grid(row=0,column=0,padx=5,pady=5,sticky="ew")
teach=Button(frame,text="Add Teacher",image=tea,compound=TOP,command=Teacher).grid(row=0,column=1,padx=5,pady=5,sticky="ew")
staff=Button(frame,text="Add Staff",image=staf,compound=TOP,command=quit).grid(row=0,column=2,padx=5,pady=5,sticky="ew")
book=Button(frame,text="Add books",image=boo,compound=TOP,command=quit).grid(row=0,column=3,padx=5,pady=5,sticky="ew")
fees=Button(frame,text="Fees",image=fee,compound=TOP,command=quit).grid(row=0,column=4,padx=5,pady=5,sticky="ew")
smss=Button(frame,text="SMS To All",image=sms,compound=TOP,command=quit).grid(row=1,column=0,padx=5,pady=5,sticky="ew")
resul=Button(frame,text="Result",image=res,compound=TOP,command=quit).grid(row=1,column=1,padx=5,pady=5,sticky="ew")
attend=Button(frame,text="Attendence",image=atten,compound=TOP,command=quit).grid(row=1,column=2,padx=5,pady=5,sticky="ew")
salary=Button(frame,text="Salary",image=sal,compound=TOP,command=quit).grid(row=1,column=3,padx=5,pady=5,sticky="ew")
exitt=Button(frame,text="Exit",image=exi,compound=TOP,command=root.destroy).grid(row=1,column=4,padx=5,pady=5,sticky="ew")

root.mainloop()