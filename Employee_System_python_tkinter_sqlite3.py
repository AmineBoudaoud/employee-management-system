from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import  databaes


data = databaes("employee.db")

#window code
root = Tk()

root.title('Employee Managent System')
root.geometry('1210x615+0+0')
root.resizable(FALSE,FALSE)
root.configure(bg='#2c3e50')


name = StringVar()
job = StringVar()
age = StringVar()
email = StringVar()
mobile = StringVar()
gender = StringVar()



logo = PhotoImage(file='logo.png')
logo=logo.subsample(3,3)
lbl_logo = Label(root,image=logo,bg='#2c3e50')
lbl_logo.place(x=80,y=520)



#-------- Enter Frame --------

enter_frame = Frame(bg='#2c3e50')
enter_frame.place(x=1,y=1,width=360,height=510)
title = Label(enter_frame,text = 'Employee Company',font=('Calibri',18,),bg='#2c3e50',fg='white')
title.place(x=10,y=1)

lblname = Label(enter_frame,text ='Name',font=('Calibri',16),bg='#2c3e50',fg='white')
lblname.place(x=10,y=50)
txtname = Entry(enter_frame,textvariable=name,width=20,font=('Calibri',16))
txtname.place(x=120,y=50)


lbljob = Label(enter_frame,text ='Job',font=('Calibri',16),bg='#2c3e50',fg='white')
lbljob.place(x=10,y=90)
txtjob = Entry(enter_frame,textvariable=job,width=20,font=('Calibri',16))
txtjob.place(x=120,y=90)



lblage = Label(enter_frame,text ='Age',font=('Calibri',16),bg='#2c3e50',fg='white')
lblage.place(x=10,y=130)
txtage = Entry(enter_frame,textvariable=age,width=20,font=('Calibri',16))
txtage.place(x=120,y=130)

lblemail = Label(enter_frame,text ='Email',font=('Calibri',16),bg='#2c3e50',fg='white')
lblemail.place(x=10,y=170)
txtemail = Entry(enter_frame,textvariable=email,width=20,font=('Calibri',16))
txtemail.place(x=120,y=170)

lblcontact = Label(enter_frame,text ='Mobile',font=('Calibri',16),bg='#2c3e50',fg='white')
lblcontact.place(x=10,y=210)
txtcontact = Entry(enter_frame,textvariable=mobile,width=20,font=('Calibri',16))
txtcontact.place(x=120,y=210)

lblgender = Label(enter_frame,text ='Gender',font=('Calibri',16),bg='#2c3e50',fg='white')
lblgender.place(x=10,y=250)
combogender = ttk.Combobox(enter_frame,textvariable=gender,state='readonly',width=18,font=('Calibri',16))
combogender['values'] = ("Male","Female")
combogender.place(x=120,y=250)



lbladdress = Label(enter_frame,text ='Address :',font=('Calibri',16),bg='#2c3e50',fg='white')
lbladdress.place(x=10,y=290)
txtaddress = Text(enter_frame,width=30,height=2,font=('Calibri',16))
txtaddress.place(x=10,y=330)


#-------- Define --------

def getdata(event):
    selected_row = tv.focus()
    db = tv.item(selected_row)
    global row
    row = db["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    mobile.set(row[5])
    gender.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in data.fetch():
        tv.insert("",END,values=row)


def delete():
    data.remove(row[0])
    Clear()
    displayAll()



def Clear():
    name.set("")
    job.set("")
    age.set("")
    email.set("")
    mobile.set("")
    gender.set("")
    txtaddress.delete(1.0,END)



def add_employee():
    if txtname.get()=="" or txtjob.get() == "" or txtage.get() == "" or txtemail.get()== "" or txtcontact.get()=="" or combogender.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please Fill all the Entry")
        return

    data.insert(

        txtname.get(),
        txtjob.get(),
        txtage.get(),
        txtemail.get(),
        txtcontact.get(),
        combogender.get(),
        txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Added new employee")
    Clear()
    displayAll()


def update():
    if txtname.get()=="" or txtjob.get() == "" or txtage.get() == "" or txtemail.get()== "" or txtcontact.get()=="" or combogender.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please Fill all the Entry")
        return
    data.update(row[0],
         txtname.get(),
         txtjob.get(),
         txtage.get(),
         txtemail.get(),
         txtcontact.get(),
         combogender.get(),
         txtaddress.get(1.0, END))

    messagebox.showinfo("Success","The employee data is update")
    Clear()
    displayAll()


def hide():
    root.geometry("360x515")
def show():
    root.geometry('1210x615+0+0')

btnhide = Button(enter_frame,text='HIDE',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)

btnshow = Button(enter_frame,text='SHOW',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)


#-------- Button --------

btn_frame = Frame(enter_frame,bg='#2c3e50',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)


btnadd = Button(btn_frame,
               text='Add Detailes',
               width=14,
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#16a085',
               bd=0,
               command = add_employee
                ).place(x=4,y=5)

btnedit = Button(btn_frame,
               text='Update Detailes',
               width=14,
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#2980b9',
               bd=0
                ).place(x=4,y=50)


btnedit = Button(btn_frame,
               text='Update Detailes',
               width=14,
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#045F5F',
               bd=0,
               command=update
                ).place(x=4,y=50)



btndelete= Button(btn_frame,
               text='Delete Detailes',
               width=14,
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#008B8B',
               bd=0,
               command=delete

                ).place(x=170,y=5)

btnclear= Button(btn_frame,
               text='Clear Detailes',
               width=14,
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#008080',
               bd=0,
               command=Clear
                ).place(x=170,y=50)



#--------Table Frame--------

tree_frame = Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=610)
style= ttk.Style()
style.configure('mystyle.Treeview',font=('Calibri,12'),rowhegiht=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri,12'),rowhegiht=50)


tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")

tv.heading("1",text="ID")
tv.column("1",width="35")

tv.heading("2",text="Name")
tv.column("2",width="135")


tv.heading("3",text="Age")
tv.column("3",width="50")

tv.heading("4",text="Job")
tv.column("4",width="120")

tv.heading("5",text="Email")
tv.column("5",width="150")

tv.heading("6",text="Mobile")
tv.column("6",width="150")

tv.heading("7",text="Gender")
tv.column("7",width="90")

tv.heading("8",text="Address")
tv.column("8",width="100")

tv['show']= 'headings'


tv.bind("<ButtonRelease-1>",getdata)

tv.place(x=1,y=1,height=610)

displayAll()

root.mainloop()
