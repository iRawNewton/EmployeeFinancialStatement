from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import Canvas
from tkinter import simpledialog
from tkinter.font import Font
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="efs")
mycursor = mydb.cursor()
root = Tk()
root.title("Employee Data")
root.configure(bg='teal')
root.resizable(False, False)  # prevent resizing

# Window size starts
window_height = 680
window_width = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, 5))
root.configure(bg="#232f34")
root.focus_force()
# Window size ends

# fonts and colours
hFont = Font(family="Georgia", size=20, weight="bold")
bLabelFont = Font(family="Times New Roman", size=14, weight="bold")
bEntryFont = Font(family="Consolas", size=14)
fFont = Font(family="Times New Roman", size=10, weight="bold")
buttonFont = Font(family="Times New Roman", size=10, weight="bold")
bg1 = "#232f34"
bg2 = "SystemButtonFace"
FontColor1 = "White"


# photos
ALogin = PhotoImage(file="./res/Admin-Login.png")
AshokChakra = PhotoImage(file="./res/new1.png")
LoginButton = PhotoImage(file="./res/login.png")
ERegistration = PhotoImage(file="./res/Employee-Registration.png")
Certificate = PhotoImage(file="./res/Certificate-Form.png")

Home = PhotoImage(file="./res/Home-Page.png")
RegistrationButton = PhotoImage(file="./res/Registration.png")
PICFormButton = PhotoImage(file="./res/PICForm.png")
PrintPICButton = PhotoImage(file="./res/PrintPIC.png")
AddUserButton = PhotoImage(file="./res/AddUser.png")
image = Image.open('./res/flag.png')
image = image.resize((300, 300), Image.ANTIALIAS)
flagLabel = ImageTk.PhotoImage(image)
CerFormLogo = PhotoImage(file="./res/Certificate-Form.png")
AddUserHeader = PhotoImage(file="./res/AddUserHeader.png")
backButton = PhotoImage(file="./res/back.png")
CertificateFormHeader = PhotoImage(file="./res/PICCertificate.png")
logoutButtonimage = PhotoImage(file="./res/logout.png")
# photos

# Frame *-*-*-*-*-*-*-*-*-*-
frame1 = Frame(root, bd=0, bg="black", relief=RAISED)  # For Header
frame1.pack(side=TOP, fill=X)

frame3 = Frame(root, bg="Black", relief=FLAT)  # For Footer
frame3.pack(side=BOTTOM, fill=X)

frameLogin = Frame(root, width=1200, height=800, bd=1, bg=bg1, relief=FLAT)
frameLogin.pack(side=TOP, fill=BOTH)  # For Login Frame

""" Inside Home frame starts """
frameHome = Frame(root, bd=0, bg=bg1, relief=RAISED)  # Homepage Frame

frameLEFT = Frame(frameHome, bd=0, bg=bg1, relief=RAISED)
frameLEFT.pack(side=LEFT, fill=Y,pady=5)
frameRIGHT = Frame(frameHome, bd=0, bg=bg1, relief=RAISED)
frameRIGHT.pack(side=RIGHT, fill=X)
""" Inside Home frame ends """

""" Registration form frame starts """
frame2 = Frame(root, width=1200, height=800, bd=1, bg=bg1, relief=FLAT)  # Registration upper frame
frame4 = Frame(root, width=600, height=800, bd=10, bg="#1E262A", relief=FLAT, highlightthickness=1, highlightbackground="Black")  # Registration lower frame

frameCer = Frame(root, width=1200, height=800, bd=1, bg=bg1, relief=FLAT)
frameCer1 = Frame(root, width=600, height=800, bd=10, bg="#1E262A", relief=FLAT, highlightthickness=1, highlightbackground="Black")
""" Registration form frame ends """

"""***********Add User frame starts****************"""
frameAddUser1 = Frame(root, bd=0, bg=bg1, relief=RAISED)

frameAddUser2 = Frame(root, bd=1, bg=bg1, relief=RIDGE)

frameAddUser3 = Frame(frameAddUser2, bd=0, bg=bg1, relief=RAISED)
frameAddUser3.pack(side=TOP, fill=X, pady=10)

frameAddUser4 = Frame(frameAddUser2, bd=1, bg=bg1, relief=RAISED)
frameAddUser4.pack(side=BOTTOM, fill=X, pady=30)
"""************Add User frame ends***************"""

"""************Print certificate starts*************"""
frameCertform1 = Frame(root, bd=0, bg=bg1, relief=RAISED)

frameCertform2 = Frame(root, bd=1, bg=bg1, relief=RIDGE)


frameCertform3 = Frame(frameCertform2, bd=0, bg=bg1, relief=RAISED)
frameCertform3.pack(side=TOP, fill=X, pady=10)

frameCertform4 = Frame(frameCertform2, bd=1, bg=bg1, relief=FLAT)
frameCertform4.pack(side=BOTTOM, fill=X, pady=10, padx=100)
"""************Print certificate ends*************"""

""" ************Header section*************** """
loginLbl = StringVar
PassLbl = StringVar
# login Page
labelLoginHeader = Label(frame1, image=ALogin, textvariable=loginLbl, bg="black", fg="White", font=hFont, anchor=CENTER)
labelLoginHeader.pack()
# Registration Page
label1RegistrationHeader = Label(frame1, image=ERegistration, textvariable=PassLbl, bg="black", fg="White", font=hFont, anchor=CENTER)
# Home Page
labelHomeHeader = Label(frame1, image=Home, bg="black", fg="White", font=hFont, anchor=CENTER)
# Certificate Page
labelPicCerHeader = Label(frame1, image=CerFormLogo, bg="black", fg="White", font=hFont, anchor=CENTER)
# Add user page
labelUserHeader = Label(frame1, image=AddUserHeader, bg="black", fg="White", font=hFont, anchor=CENTER)
# Print certificate page
labelCertificateHeader = Label(frame1, image=CertificateFormHeader, bg="black", fg="White", font=hFont, anchor=CENTER)

# frame login contents starts here

labelIMG = Label(frameLogin,image=AshokChakra, bg=bg1)
labelIMG.place(x=25,y=60)

labelUser = Label(frameLogin,text="Username",fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w")
labelUser.place(x=285,y=125)
labelPass = Label(frameLogin,text="Password",fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w")
labelPass.place(x=285,y=200)

UserId = StringVar
UserPass = StringVar

entryUser = Entry(frameLogin, textvariable=UserId,  font=bEntryFont, width=20, borderwidth=2)
entryUser.place(x=285,y=160)
entryPass = Entry(frameLogin, textvariable=UserPass, font=bEntryFont, width=20, borderwidth=2)
entryPass.config(show="*")
entryPass.place(x=285,y=235)
entryUser.focus_force()


def login():
    a=entryUser.get()
    b=entryPass.get()
    find = "select pwd from admin where binary id = '%s'"%(a)
    mycursor.execute(find)
    result = mycursor.fetchall()
    id1 = StringVar()
    for i in result:
        id1 = i[0]
    if id1 == b:
        messagebox.showinfo("Information", "Login Successful!")
        labelLoginHeader.pack_forget()
        labelHomeHeader.pack()
        frameLogin.pack_forget()
        frameHome.pack(side=TOP, fill=X, pady=30)
    else:
        messagebox.showerror("Login Message", "Incorrect username of password.")
        #print("2")


buttonLogin = Button(frameLogin, fg="sky blue", bg="#232f34", bd=0, image=LoginButton,activebackground="#232f34",command=login)
buttonLogin.place(x=290,y=300)


# Home page start here
def registration():
    labelHomeHeader.pack_forget()
    label1RegistrationHeader.pack()
    frameHome.pack_forget()
    frame2.pack(side=TOP, fill=BOTH)
    frame4.pack(side=TOP, fill=BOTH)


def PICform():
    labelHomeHeader.pack_forget()
    frameHome.pack_forget()
    window_height = 680
    window_width = 900
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, 5))
    labelPicCerHeader.pack()
    frameCer.pack(side=TOP, fill=BOTH)
    frameCer1.pack(side=TOP, fill=BOTH)


def pdfPage():
    labelHomeHeader.pack_forget()
    frameHome.pack_forget()
    labelCertificateHeader.pack()
    frameCertform1.pack(side=TOP, fill=X, pady=10)


def AddingUserForm():
    labelHomeHeader.pack_forget()
    frameHome.pack_forget()
    frameAddUser1.pack(side=TOP, fill=X, pady=10)
    labelUserHeader.pack()


def logout():
    labelHomeHeader.pack_forget()
    frameHome.pack_forget()
    labelLoginHeader.pack()
    frameLogin.pack(side=TOP, fill=BOTH)
    entryUser.delete(0, END)
    entryPass.delete(0, END)


labelFlag = Label(frameLEFT, image=flagLabel, bg=bg1, fg="White", font=hFont, anchor=CENTER,width=300,height=500,)
labelFlag.pack(side=LEFT,anchor=CENTER,padx=30)

buttonRegister = Button(frameRIGHT, fg="sky blue", bg=bg1, bd=0, image=RegistrationButton,activebackground="#232f34",command=registration)
buttonRegister.pack(side=TOP,padx=10,pady=2,fill=X)

buttonPIC = Button(frameRIGHT, fg="sky blue",text="Clear", bg=bg1, bd=0, image=PICFormButton,activebackground="#232f34",command=PICform,)
buttonPIC.pack(side=TOP,padx=10,pady=5,fill=X)

buttonPrintPIC = Button(frameRIGHT, fg="sky blue", bg=bg1, bd=0, image=PrintPICButton,activebackground="#232f34",command=pdfPage)
buttonPrintPIC.pack(side=TOP,padx=10,pady=5,fill=X)

buttonAddUser = Button(frameRIGHT, fg="sky blue", bg="#232f34", bd=0, image=AddUserButton,activebackground="#232f34",command=AddingUserForm)
buttonAddUser.pack(side=TOP,padx=10,pady=5,fill=X)

buttonLogout = Button(frameRIGHT, fg="sky blue", bg="#232f34", bd=0, image=logoutButtonimage,activebackground="#232f34",command=logout)
buttonLogout.pack(side=TOP,padx=10,pady=8,fill=X)

# Frame registration starts here

######################### body part starts here ###############################################
labelb00 = Label(frame2, text="", bg="#232f34", font=bLabelFont, width=10, height=1).grid(row=0, column=0)
labelb01 = Label(frame2, text="", bg="#232f34", font=bLabelFont, width=10, height=1).grid(row=0, column=5)
labelb02 = Label(frame2, text="", bg="#232f34", font=bLabelFont, width=0, height=2).grid(row=8, column=0)
# ttk.Separator(frame2, orient=HORIZONTAL).grid(column=3, row=8, rowspan=100, sticky=E,ipady=1)

# labels
labelb1 = Label(frame2, text="Employee ID:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=1, column=1)
labelb2 = Label(frame2, text="Name:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=2, column=1)
labelb3 = Label(frame2, text="Level:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=3, column=1)
labelb4 = Label(frame2, text="Salary:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=4, column=1)
labelb5 = Label(frame2, text="Pay Band:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=5, column=1)
labelb6 = Label(frame2, text="Grade Pay:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=6, column=1)
labelb7 = Label(frame2, text="Last date of Increment:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor = "w").grid(row=7, column=1)

# Variable declaration
VarId = StringVar
VarName = StringVar
VarLevel = StringVar
VarSalary = StringVar
VarPayBand = StringVar
VarGradePay = StringVar
VarLDI = StringVar

# textbox
e1 = Entry(frame2, textvariable=VarId, font=bEntryFont, width=20, borderwidth=2)
e1.grid(row=1, column=2)
e2 = Entry(frame2, textvariable=VarName, font=bEntryFont, width=20, borderwidth=2)
e2.grid(row=2, column=2)


def SetSalary(event):
    a = e3.get()
    Sal = "select sal from matrix_val where level = '%s'" % (a)
    mycursor.execute(Sal)
    result2 = mycursor.fetchall()
    e4['values'] = result2
    e4.set('Select your option:')
    lev = "select distinct(grade_pay) from matrix_val where level = '%s'" % (a)
    mycursor.execute(lev)
    result4 = mycursor.fetchall()
    e6.configure(state='normal')
    e6.delete('0', END)
    e6.insert('0', result4)
    e6.configure(state='disable')


SalLevel = "select distinct(level) from matrix_val"
mycursor.execute(SalLevel)
result1 = mycursor.fetchall()
e3 = ttk.Combobox(frame2, textvariable=VarLevel, font=bEntryFont, width=18, state="readonly", value=result1)
e3.set('Select your option:')
e3.bind("<<ComboboxSelected>>", SetSalary)
e3.grid(row=3, column=2)


def SetPayBand(event):
    a = e3.get()
    b = e4.get()
    Sal = "select pay_band from matrix_val where level = '%s' and sal = '%s'" % (a, b)
    mycursor.execute(Sal)
    result3 = mycursor.fetchall()
    e5.configure(state='normal')
    e5.delete('0', END)
    e5.insert('0', result3)
    e5.configure(state='disable')


e4 = ttk.Combobox(frame2, textvariable=VarSalary, font=bEntryFont, width=18, state="readonly")
e4.bind("<<ComboboxSelected>>", SetPayBand)
e4.grid(row=4, column=2)
e5 = Entry(frame2, textvariable=VarPayBand, font=bEntryFont, width=20, borderwidth=2, state='disable')
e5.grid(row=5, column=2)
e6 = Entry(frame2, textvariable=VarGradePay, font=bEntryFont, width=20, borderwidth=2, state='disable')
e6.grid(row=6, column=2)
e7 = DateEntry(frame2, textvariable=VarLDI, font=bEntryFont, width=18, borderwidth=2, state='readonly', date_pattern='dd/mm/yyyy')
e7.grid(row=7, column=2)

# ----------------------------button coding start here -----------------------------------
labelframe4 = Label(frame4, text="", bg="#1E262A", width=5)
labelframe4.pack(side=LEFT)


def register():
    if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e6.get() == "":
        messagebox.showwarning("Warning", "Field/Fields Empty")
    else:
        a = e1.get()
        entryID = int(a)
        Select = "select id from employee where id='%s'" % (entryID)
        mycursor.execute(Select)
        result = mycursor.fetchall()
        id1 = StringVar()
        for i in result:
            id1 = i[0]
        if entryID == id1:
            messagebox.showerror("Error", "Record already exists")
        else:
            Insert = "Insert into employee values(%s,%s,%s,%s,%s,%s,%s)"
            name = e2.get()
            level = e3.get()
            salary = e4.get()
            pay_band = e5.get()
            grade = e6.get()
            dat = e7.get()
            #ldi = dat.strftime("%Y/%m/%d")
            ldi = datetime.strptime(dat, '%d/%m/%Y')
            Value = (a, name, level, salary, pay_band, grade, ldi)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.showinfo("Information", "Record inserted")
            buttonEdit.grid_forget()
            clear()


def clear():
    e1.configure(state='normal')
    e2.configure(state='normal')
    e3.configure(state='normal')
    e4.configure(state='normal')
    e7.configure(state='normal')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.set('Select your option:')
    e4.set('')
    e5.configure(state='normal')
    e5.delete(0, END)
    e5.configure(state='disable')
    e6.configure(state='normal')
    e6.delete(0, END)
    e6.configure(state='disable')
    e7.delete(0, END)
    buttonEdit.grid_forget()
    e1.focus_force()


def delete():
    empID = simpledialog.askinteger(title="Searching Information", prompt="Enter the Employee ID:")
    Delete = "delete from employee where id='%s'" % (empID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record deleted successfully!")
    clear()


def search():
    e1.configure(state='normal')
    e2.configure(state='normal')
    e3.configure(state='normal')
    e3.set("")
    e4.configure(state='normal')
    e5.configure(state='normal')
    e6.configure(state='normal')
    e7.configure(state='normal')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    searchID = simpledialog.askinteger(title="Searching Information", prompt="Enter the Employee ID:")
    sId = ""
    sName = ""
    sLevel = ""
    sSalary = ""
    sPayBand = ""
    sGradePay = ""
    sLDI = ""
    Select = "select * from employee where id='%s'" % (searchID)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    id1 = StringVar()
    for i in result:
        id1 = i[0]
    if searchID == id1:
        for i in result:
            sId = i[0]
            sName = i[1]
            sLevel = i[2]
            sSalary = i[3]
            sPayBand = i[4]
            sGradePay = i[5]
            sLDI = i[6]
        e1.insert(0, sId)
        e2.insert(0, sName)
        e3.insert(0, sLevel)
        e4.insert(0, sSalary)
        e5.insert(0, sPayBand)
        e6.insert(0, sGradePay)
        e7.insert(0, sLDI)
        e7.configure(date_pattern='dd/mm/yyyy')
        e1.configure(state='disable')
        e2.configure(state='disable')
        e3.configure(state='disable')
        e4.configure(state='disable')
        e5.configure(state='disable')
        e6.configure(state='disable')
        e7.configure(state='disable')
        buttonEdit.grid(row=1, column=3, padx=30)
    else:
        messagebox.showerror("Error", "Record doesn't exists")


def editText():
    e1.configure(state='readonly')
    e2.configure(state='normal')
    e3.configure(state='normal')
    e4.configure(state='normal')
    e7.configure(state='normal')


def update():
    if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e6.get() == "":
        messagebox.showwarning("Warning", "Field/Fields Empty")
    else:
        id = e1.get()
        name = e2.get()
        level = e3.get()
        salary = e4.get()
        pay_band = e5.get()
        grade = e6.get()
        ldi = e7.get()
        Update = "Update employee set name='%s', level='%s', salary='%s', pay_band='%s', grade='%s', ldi=%s where id='%s'" %(id, name, level, salary, pay_band, grade, ldi)
        mycursor.execute(Update)
        messagebox.showinfo("Info", "Record Updated!")
        buttonEdit.grid_forget()


def back():
    clear()
    frameHome.pack()
    frame2.pack_forget()
    frame4.pack_forget()
    labelHomeHeader.pack()
    label1RegistrationHeader.pack_forget()


button1 = Button(frame4, text="Register", width=10, height=1, command=register, bd=3, font=buttonFont, fg="white", bg="#232f34")
button1.pack(side=LEFT, padx=10, pady=10)

button2 = Button(frame4, text="Clear", width=10, height=1, padx=10, command=clear, bd=3, font=buttonFont, fg="white", bg="#232f34")
button2.pack(side=LEFT, padx=10, pady=10)

button3 = Button(frame4, text="Delete", width=10, height=1, padx=10, command=delete, bd=3, font=buttonFont, fg="white", bg="#232f34")
button3.pack(side=LEFT, padx=10, pady=10)

photo = PhotoImage(file="./res/edt.png")
edt = Font(family="Times New Roman", size=15, weight="bold")
buttonEdit = Button(frame2, text=" Edit", font=edt, fg="sky blue", bg="#232f34", bd=0, command=editText, image=photo, compound=LEFT)

button4 = Button(frame4, text="Search", width=10, height=1, padx=10, command=search, bd=3, font=buttonFont, fg="white", bg="#232f34")
button4.pack(side=LEFT, padx=10, pady=10)

button5 = Button(frame4, text="Update", width=10, height=1, padx=10, command=update, bd=3, font=buttonFont, fg="white", bg="#232f34")
button5.pack(side=LEFT, padx=10, pady=10)

button6 = Button(frame4, text="Back", width=10, height=1, padx=10, command=back, bd=3, font=buttonFont, fg="white", bg="#232f34")
button6.pack(side=LEFT, padx=10, pady=10)


# ------------------------------ body part ends here --------------------------------------

# Frame PIC Form starts here***************************************************************

# for space
labelbSpace = Label(frameCer, text="", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=0, column=1, padx=20)
labelbSpace1 = Label(frameCer, text="", fg=FontColor1, bg=bg1, font=bLabelFont, width=2, height=2, anchor="w").grid(row=0, column=3)

labelbc1 = Label(frameCer, text="Employee ID:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=1, column=1)
labelbc2 = Label(frameCer, text="Name:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=2, column=1)
labelbc3 = Label(frameCer, text="Pay Band:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=3, column=1)
labelbc4 = Label(frameCer, text="Grade Pay:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=4, column=1)
labelbc5 = Label(frameCer, text="Level:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=5, column=1)
labelbc6 = Label(frameCer, text="Current Salary:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=6, column=1)
labelbc7 = Label(frameCer, text="Last Increment:", fg=FontColor1, bg=bg1, font=bLabelFont, width=20, height=2, anchor="w").grid(row=7, column=1)
labelbc8 = Label(frameCer, text="Increment Type:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="w").grid(row=1, column=4)
labelbc9 = Label(frameCer, text="Next Grade Pay:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="w").grid(row=2, column=4)
labelbc10 = Label(frameCer, text="Next Level:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="w").grid(row=3, column=4)
labelbc11 = Label(frameCer, text="Next Salary:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="w").grid(row=4, column=4)
labelbc12 = Label(frameCer, text="Increment Date:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="w").grid(row=5, column=4)
labelbc13 = Label(frameCer, text="Reason:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=1, anchor="w").grid(row=7, column=4)

#variable declaration
cVarID=StringVar
cVarName=StringVar
cVarPayband=StringVar
cVarGradepay=StringVar
cVarLevel=StringVar
cVarCrntSalary=StringVar
cVarLDI=StringVar
cVarIncTyp=StringVar
cVarnGradepay=StringVar
cVarnLevel=StringVar
cVarnSalary=StringVar
cVarReason=StringVar
cVarChange=StringVar


def FillIdDetails(event):
    a=ec1.get()
    ec2.configure(state="normal")
    ec3.configure(state="normal")
    ec4.configure(state="normal")
    ec5.configure(state="normal")
    ec6.configure(state="normal")
    ec7.configure(state="normal")
    ec2.delete(0, END)
    ec3.delete(0, END)
    ec4.delete(0, END)
    ec5.delete(0, END)
    ec6.delete(0, END)
    ec7.delete(0, END)
    name = ""
    level = ""
    salary = ""
    pay_band = ""
    grade = ""
    ldi = ""
    Details = "select name, level, salary, pay_band, grade, ldi from employee where id = '%s'" %a
    mycursor.execute(Details)
    result = mycursor.fetchall()
    for i in result:
        name = i[0]
        level = i[1]
        salary = i[2]
        pay_band = i[3]
        grade = i[4]
        ldi = i[5]
        date_str = datetime.strftime(ldi, '%d/%m/%Y')
    ec2.insert(0, name)
    ec3.insert(0, pay_band)
    ec4.insert(0, grade)
    ec5.insert(0, level)
    ec6.insert(0, salary)
    ec7.insert(0, date_str)
    ec2.configure(state="readonly")
    ec3.configure(state="readonly")
    ec4.configure(state="readonly")
    ec5.configure(state="readonly")
    ec6.configure(state="readonly")
    ec7.configure(state="readonly")


ec1 = Entry(frameCer, textvariable=cVarID, font=bEntryFont, width=18, borderwidth=2)
ec1.bind("<Return>", FillIdDetails)
ec1.grid(row=1, column=2)
ec2 = Entry(frameCer, textvariable=cVarName, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec2.grid(row=2, column=2)
ec3 = Entry(frameCer, textvariable=cVarPayband, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec3.grid(row=3, column=2)
ec4 = Entry(frameCer, textvariable=cVarGradepay, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec4.grid(row=4, column=2)
ec5 = Entry(frameCer, textvariable=cVarLevel, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec5.grid(row=5, column=2)
ec6 = Entry(frameCer, textvariable=cVarCrntSalary, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec6.grid(row=6, column=2)
ec7 = Entry(frameCer, textvariable=cVarLDI, font=bEntryFont, width=18, borderwidth=2, state="readonly")
ec7.grid(row=7, column=2)


def IncType(event):
    a = ec8.get()  # Retrieving increment type
    c = ec6.get()  # Retrieving salary info
    b = ec5.get()  # Retrieving level info
    d = ec4.get()  # Retrieving grade info
    NextSalary = ""
    NextGrade = ""
    ec9.configure(state="normal")
    ec10.configure(state="normal")
    ec11.configure(state="normal")
    ec9.delete(0, END)
    ec10.delete(0, END)
    ec11.delete(0, END)

    if a == "Annual Increment":
       Select = "select sal from matrix_val where level = %s and sal > %s limit 1" %(b,c)
       mycursor.execute(Select)
       result = mycursor.fetchall()
       for i in result:
           NextSalary = i[0]
       ec11.insert(0, NextSalary)
       ec10.insert(0, b)
       ec9.insert(0, d)
       ec9.configure(state="readonly")
       ec10.configure(state="readonly")
       ec11.configure(state="readonly")
    else:
        if b == "13":
            b = "13A"
        elif b == "13A":
            b = "14"
        else:
            b = int(b)  # typecast
            b = b + 1
        Select = "select sal from matrix_val where level = %s and sal > %s limit 2" % (b, c)
        mycursor.execute(Select)
        result = mycursor.fetchall()
        for i in result:
            NextSalary = i[0]
        ec11.insert(0, NextSalary)
        ec10.insert(0, b)
        Select1 = "select grade_pay from matrix_val where level = %s " % (b)  # For Grade pay
        mycursor.execute(Select1)
        result1 = mycursor.fetchall()
        for i in result1:
            NextGrade = i[0]
        ec9.insert(0, NextGrade)
        ec9.configure(state="readonly")
        ec10.configure(state="readonly")
        ec11.configure(state="readonly")


options = ['Annual Increment','Promotional Increment']

ec8 = ttk.Combobox(frameCer, textvariable=cVarIncTyp, font=bEntryFont, width=18, state="readonly",value=options)
ec8.set('Select your option:')
ec8.bind("<<ComboboxSelected>>", IncType)
ec8.grid(row=1, column=5)

ec9 = Entry(frameCer, textvariable=cVarnGradepay, font=bEntryFont, width=20, borderwidth=2, state="readonly")
ec9.grid(row=2, column=5)
ec10 = Entry(frameCer, textvariable=cVarnLevel, font=bEntryFont, width=20, borderwidth=2, state="readonly")
ec10.grid(row=3, column=5)
ec11 = Entry(frameCer, textvariable=cVarnSalary, font=bEntryFont, width=20, borderwidth=2, state="readonly")
ec11.grid(row=4, column=5)
ec12 = DateEntry(frameCer, textvariable=cVarChange, font=bEntryFont, width=18, borderwidth=2, state='readonly', date_pattern='dd/mm/yyyy')
ec12.grid(row=5, column=5)

frameLab = LabelFrame(frameCer, text="During Increment",bg=bg1, bd=1, fg=FontColor1,font=bLabelFont)  # Frame for radio button
frameLab.grid(row=6, column=4)


def selectedradiobutton():
    a=var.get()
    if a == 1:
        ereason.delete("1.0","end")
        ereason.configure(state=DISABLED)
        ec13.configure(state='normal')
        ec14.configure(state='normal')
        ec13.delete(0, END)
        ec14.delete(0, END)
        ec13.configure(state='disabled')
        ec14.configure(state='disabled')
    else:
        ereason.configure(state='normal')
        ec13.configure(state='normal')
        ec14.configure(state='normal')


rbFONT = Font(family="Consolas", size=10, weight="bold")
var=IntVar()
rb1 = Radiobutton(frameLab, text="Present", variable=var, value=1,command=selectedradiobutton, bg=bg1, fg="white", selectcolor="black", font=rbFONT)
rb1.grid(row=1,column=1)
rb2 = Radiobutton(frameLab, text="Absent", variable=var, value=2,command=selectedradiobutton, bg=bg1, fg="White", selectcolor="black",font=rbFONT )
rb2.grid(row=1,column=2)

frameLabDate = LabelFrame(frameCer, text="From / to",bg=bg1, bd=1, fg=FontColor1,font=bLabelFont)  # Frame for from and to date
frameLabDate.grid(row=6, column=5)

dateFont = Font(family="Times New Roman", size=8, weight="bold")
ec13 = DateEntry(frameLabDate, textvariable=cVarChange, font=dateFont, width=10, borderwidth=2, date_pattern='dd/mm/yyyy', state='disabled')
ec13.grid(row=0, column=1, padx=10)
ec14 = DateEntry(frameLabDate, textvariable=cVarChange, font=dateFont, width=10, borderwidth=2, state='disabled', date_pattern='dd/mm/yyyy')
ec14.grid(row=0, column=2, padx=8)

ereason = Text(frameCer, width=22,height=5)
ereason.grid(row=7,column=5)

# Frame Certificate buttons


def save():
    if ec1.get() == "" or ec12.get() == "":
        messagebox.showwarning("Warning", "Field/Fields Empty")
    else:
        test = ec11.get()
        if test == "":
            messagebox.showerror("Error", "Cannot increment further.")
        else:
            a = ec1.get()
            b = ec12.get()
            x = ec7.get()
            test = datetime.strptime(b, '%d/%m/%Y')
            test1 = datetime.strptime(x, '%d/%m/%Y')
            if test.year > test1.year:
                date_str = datetime.strptime(b, '%d/%m/%Y')  # From string to date format
                c = datetime.strftime(date_str, '%Y/%m/%d')  # Date format arranged
                Select = "select count(*) from PIC where emp_id = %s and year(currentDate) = '%s'" % (a,c)
                mycursor.execute(Select)
                result = mycursor.fetchall()
                RecordsInaYear = StringVar()
                for i in result:
                    RecordsInaYear = i[0]
                if RecordsInaYear > 0:
                    messagebox.showerror("Error", "Record present for the current year.")
                    messagebox.showinfo("Information", "Change increment date and then try again.")
                else:
                    Insert = "Insert into PIC values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    empID = ec1.get()
                    payBand = ec3.get()
                    presentPay = ec6.get()
                    presentGrade = ec4.get()
                    prevDate = ec7.get()
                    currDate = ec12.get()
                    nxtPay = ec11.get()
                    nxtGrade = ec9.get()
                    absntFrom = ec13.get()
                    absntTo = ec14.get()
                    reason = ereason.get("1.0",'end-1c')
                    iType = ec8.get()

                    if prevDate == "":
                        prevDatec = "Null"
                    else:
                        date_prev = datetime.strptime(prevDate, '%d/%m/%Y')  # From string to date format
                        prevDatec = datetime.strftime(date_prev, '%Y/%m/%d')  # Date format arranged

                    if currDate == "":
                        currDatec = "Null"
                    else:
                        date_curr = datetime.strptime(currDate, '%d/%m/%Y')
                        currDatec = datetime.strftime(date_curr, '%Y/%m/%d')

                    if absntFrom == "":
                        absntFromc = None
                    else:
                        date_absFr = datetime.strptime(absntFrom, '%d/%m/%Y')
                        absntFromc = datetime.strftime(date_absFr, '%Y/%m/%d')

                    if absntTo == "":
                        absntToc = None
                    else:
                        date_absTo = datetime.strptime(absntTo, '%d/%m/%Y')
                        absntToc = datetime.strftime(date_absTo, '%Y/%m/%d')

                    Value = (empID, payBand, presentPay, presentGrade, prevDatec, currDatec, nxtPay, nxtGrade, absntFromc, absntToc, reason, iType)
                    mycursor.execute(Insert, Value)
                    mydb.commit()

                    # update in employee table
                    nxtLevel = ec10.get()
                    Find = "select pay_band from matrix_val where level ='%s' limit 1" %(nxtLevel)
                    mycursor.execute(Find)
                    result3 = mycursor.fetchall()
                    payBandRetrieved = StringVar()
                    for i in result3:
                        payBandRetrieved = i[0]
                    Update = "Update employee set level='%s', salary='%s', pay_band='%s', grade='%s', ldi='%s' where id='%s'" % (nxtLevel, nxtPay, payBandRetrieved, nxtGrade, currDatec, a)
                    mycursor.execute(Update)
                    messagebox.showinfo("Information", "Record inserted")
                    clearPIC()
            else:
                messagebox.showwarning("Warning", "Present increment date equals/less than previous increment date.")


def clearPIC():
    ec1.delete(0, END)
    ec2.configure(state='normal')
    ec3.configure(state='normal')
    ec4.configure(state='normal')
    ec5.configure(state='normal')
    ec6.configure(state='normal')
    ec7.configure(state='normal')
    ec8.set('Select your option:')
    ec9.configure(state='normal')
    ec10.configure(state='normal')
    ec11.configure(state='normal')
    ec12.configure(state='normal')
    ec13.configure(state='normal')
    ec14.configure(state='normal')
    ereason.configure(state='normal')

    ec2.delete(0, END)
    ec3.delete(0, END)
    ec4.delete(0, END)
    ec5.delete(0, END)
    ec6.delete(0, END)
    ec7.delete(0, END)
    ec9.delete(0, END)
    ec10.delete(0, END)
    ec11.delete(0, END)
    ec12.delete(0, END)
    ec13.delete(0, END)
    ec14.delete(0, END)
    ereason.delete(1.0, END)

    ec2.configure(state='disabled')
    ec3.configure(state='disabled')
    ec4.configure(state='disabled')
    ec5.configure(state='disabled')
    ec6.configure(state='disabled')
    ec7.configure(state='disabled')
    ec9.configure(state='disabled')
    ec10.configure(state='disabled')
    ec11.configure(state='disabled')
    ec13.configure(state='disabled')
    ec14.configure(state='disabled')
    ereason.configure(state='disabled')


def deletePIC():
    empID = simpledialog.askinteger(title="Searching Information", prompt="Enter the Employee ID:")
    empYear = simpledialog.askinteger(title="Searching Information", prompt="Enter the Year:")
    Delete = "delete from PIC where emp_ID='%s' and year(current_date)='%s'" % (empID, empYear)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record deleted successfully!")
    clearPIC()


def backPIC():
    clearPIC()
    frameHome.pack()
    frameCer.pack_forget()
    frameCer1.pack_forget()
    labelHomeHeader.pack()
    labelPicCerHeader.pack_forget()


labelCerSpace = Label(frameCer1, text="", bg="#1E262A", font=bLabelFont, width=10, height=2, anchor="w").pack(side=LEFT, pady=10, anchor=CENTER)

buttonc1 = Button(frameCer1, text="Save", width=15, height=1, bd=3, font=buttonFont, fg="white", bg="#232f34", command=save)
buttonc1.pack(side=LEFT, padx=20, pady=10, anchor=CENTER)

buttonc2 = Button(frameCer1, text="Clear", width=15, height=1, padx=10, bd=3, font=buttonFont, fg="white", bg="#232f34", command=clearPIC)
buttonc2.pack(side=LEFT, padx=20, pady=10, anchor=CENTER)

buttonc3 = Button(frameCer1, text="Delete", width=15, height=1, padx=10, bd=3, font=buttonFont, fg="white", bg="#232f34", command=deletePIC)
buttonc3.pack(side=LEFT, padx=20, pady=10, anchor=CENTER)

buttonc4 = Button(frameCer1, text="Back", width=15, height=1, padx=10, bd=3, font=buttonFont, fg="white", bg="#232f34", command=backPIC)
buttonc4.pack(side=LEFT, padx=20, pady=10, anchor=CENTER)

# Frame PIC Form ends here

# Frame Add User starts here


def backadd():
    labelUserHeader.pack_forget()
    frameAddUser1.pack_forget()
    entryAddUser.delete(0, END)
    entryAddPass.delete(0, END)
    entryUser1.delete(0, END)
    entryPass2.delete(0, END)
    entryPass3.delete(0, END)
    frameAddUser2.pack_forget()
    frameHome.pack()
    labelHomeHeader.pack()


buttonBackAddUser = Button(frameAddUser1, fg="sky blue", bg="#232f34", bd=0, image=backButton,activebackground="#232f34", command=backadd)
buttonBackAddUser.grid(row=0, column=0)
labelAddSpace = Label(frameAddUser1, text="", bg="#232f34", font=bLabelFont, width=10, height=1).grid(row=1, column=0, pady=2, padx=10)

labelAdd1 = Label(frameAddUser1, text="Current User ID", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor = "e").grid(row=2, column=1)
labelAdd2 = Label(frameAddUser1, text="Password", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor = "e").grid(row=3, column=1)

UserAddId = StringVar
UserAddPass = StringVar

entryAddUser = Entry(frameAddUser1, textvariable=UserAddId,  font=bEntryFont, width=20, borderwidth=2)
entryAddUser.grid(row=2, column=3)
entryAddPass = Entry(frameAddUser1, textvariable=UserAddPass, font=bEntryFont, width=20, borderwidth=2)
entryAddPass.config(show="*")
entryAddPass.grid(row=3, column=3)
entryAddUser.focus_force()


def confirm():
    a = entryAddUser.get()
    b = entryAddPass.get()
    find = "select binary pwd from admin where binary id = '%s'" % (a)
    mycursor.execute(find)
    result = mycursor.fetchall()
    id1 = StringVar()
    for i in result:
        id1 = i[0]
    if id1 == b:
        frameAddUser2.pack(side=TOP, fill=X, pady=30)
    else:
        messagebox.showerror("Error", "User not found or wrong password entered")
        frameAddUser2.pack_forget()


buttonAdduserConfirm = Button(frameAddUser1, text="Confirm", font=buttonFont, fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=10, anchor="center", command=confirm)
buttonAdduserConfirm.grid(row=4,column=2,padx=5, pady=15)

# Add Space
labelAddSpace2 = Label(frameAddUser3, text="", bg="#232f34", font=bLabelFont, width=10, height=1).grid(row=0, column=0)

labelAdd3 = Label(frameAddUser3, text="New User ID:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="e").grid(row=4, column=1)
labelAdd4 = Label(frameAddUser3, text="New Password:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="e").grid(row=5, column=1)
labelAdd5 = Label(frameAddUser3, text="Confirm Password:", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor="e").grid(row=6, column=1)

UserAddId1 = StringVar
UserAddPass1 = StringVar
UserAddPass2 = StringVar

entryUser1 = Entry(frameAddUser3, textvariable=UserAddId1,  font=bEntryFont, width=20, borderwidth=2)
entryUser1.grid(row=4, column=3, padx=90)
entryPass2 = Entry(frameAddUser3, textvariable=UserAddPass1, font=bEntryFont, width=20, borderwidth=2)
entryPass2.grid(row=5, column=3)
entryPass3 = Entry(frameAddUser3, textvariable=UserAddPass2,  font=bEntryFont, width=20, borderwidth=2)
entryPass3.grid(row=6, column=3)


def addUser():
    a = entryPass2.get()
    b = entryPass3.get()
    c = entryUser1.get()
    if a == "" or b == "" or c == "":
        messagebox.showinfo("Information", "Fields left empty")
    else:
        Select = "select count(*) from admin where id = '%s' " %c
        mycursor.execute(Select)
        result = mycursor.fetchall()
        idUser = IntVar()
        for i in result:
            idUser = i[0]
        if idUser > 0:
            messagebox.showwarning("Error", "User with this username is already present")
        else:
            if a == b:
                Insert = "Insert into admin values(%s,%s)"
                Value = (c, a)
                mycursor.execute(Insert, Value)
                mydb.commit()
                messagebox.showinfo("Information", "Record inserted")
                entryUser1.delete(0, END)
                entryPass2.delete(0, END)
                entryPass3.delete(0, END)
                frameAddUser2.pack_forget()
            else:
                messagebox.showerror("Error", "Password do not match!")


def addDelete():
    Select = "select count(*) from admin"
    mycursor.execute(Select)
    result = mycursor.fetchall()
    id1 = StringVar()
    for i in result:
        id1 = i[0]
    print (id1)
    if id1 == 1:
        messagebox.showwarning("Warning", "Minimum 1 user required to login")
    else:
        UserID = simpledialog.askstring(title="Searching Information", prompt="Enter the Admin user ID:")
        Delete = "delete from admin where id='%s'" % (UserID)
        mycursor.execute(Delete)
        mydb.commit()
        entryUser1.delete(0, END)
        entryPass2.delete(0, END)
        entryPass3.delete(0, END)
        frameAddUser2.pack_forget()
        messagebox.showinfo("Information", "Record deleted successfully!")


def addCancel():
    entryUser1.delete(0, END)
    entryPass2.delete(0, END)
    entryPass3.delete(0, END)
    frameAddUser2.pack_forget()


# Add Space
labelAddSpace3 = Label(frameAddUser4, text="", bg="#232f34", font=bLabelFont, width=10, height=1).pack(side="left", padx=6, pady=10)

buttonAdduserAdd = Button(frameAddUser4, text="Add", fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=15, anchor="center", command=addUser)
buttonAdduserAdd.pack(side="left", padx=20)
buttonAdduserDelete = Button(frameAddUser4, text="Delete", fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=15, anchor="center", command=addDelete)
buttonAdduserDelete.pack(side="left", padx=25)
buttonAdduserCancel = Button(frameAddUser4, text="Cancel", fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=15, anchor="center", command=addCancel)
buttonAdduserCancel.pack(side="left", padx=20)

# Print certificate .pdf frame starts here

def backCert():
    frameCertform1.pack_forget()
    frameCertform2.pack_forget()
    labelCertificateHeader.pack_forget()
    certclear()
    frameHome.pack()
    labelHomeHeader.pack()


buttonBackCert = Button(frameCertform1, fg="sky blue", bg="#232f34", bd=0, image=backButton,activebackground="#232f34", command=backCert)
buttonBackCert.grid(row=0, column=0)
labelAddSpace1 = Label(frameCertform1, text="", bg="#232f34", font=bLabelFont, width=10, height=1).grid(row=1, column=0, pady=2, padx=10)

labelCert1 = Label(frameCertform1, text="User ID", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor = "e").grid(row=2, column=1)
labelCert2 = Label(frameCertform1, text="Year", fg=FontColor1, bg=bg1, font=bLabelFont, width=15, height=2, anchor = "e").grid(row=3, column=1)

CertId = StringVar
CertYear = StringVar

entryCertUser = Entry(frameCertform1, textvariable=CertId,  font=bEntryFont, width=20, borderwidth=2)
entryCertUser.grid(row=2, column=3)
entryCertYear = Entry(frameCertform1, textvariable=CertYear, font=bEntryFont, width=20, borderwidth=2)
entryCertYear.grid(row=3, column=3)
entryCertUser.focus_force()


def CertNext():
    frameCertform2.pack(side=TOP,fill=X)


buttonCertNext = Button(frameCertform1, text="Next", font=buttonFont, fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=10, anchor="center", command=CertNext)
buttonCertNext.grid(row=4,column=2,padx=5, pady=15)


a = "Certified that the Government servants named below have earned the prescribed periodical"
b = "increment from the date cited in Col.6 having been the incumbents of the posts specified for not less"
c = "than (A)______________ year(s) from the date shown in col.5, after deducting periods of absence from"
d = "duty not counting for increment, absence on leave without pay etc. Further certified that the"
e = "period/periods of leave taken from (B)____________ to (C)____________ and from (D)____________ to (E)____________"

label1 = Label(frameCertform3,text=a,bg=bg1, fg="White").pack(side=TOP, anchor="w", padx=140)
label2 = Label(frameCertform3,text=b,bg=bg1, fg="White").pack(side=TOP, anchor="w", padx=120)
label3 = Label(frameCertform3,text=c,bg=bg1, fg="White").pack(side=TOP, anchor="w", padx=120)
label4 = Label(frameCertform3,text=d,bg=bg1, fg="White").pack(side=TOP, anchor="w", padx=120)
label5 = Label(frameCertform3,text=e,bg=bg1, fg="White").pack(side=TOP, anchor="w", padx=120)

Varcert1 = StringVar
Varcert2 = StringVar
Varcert3 = StringVar
Varcert4 = StringVar
Varcert5 = StringVar

# For space
labelAddSpace21 = Label(frameCertform3, text="", bg="#232f34", font=bLabelFont, width=5, height=1).pack(side=LEFT, padx=5, pady=10)

Certentry1 = Entry(frameCertform3, textvariable=Varcert1,  font=bEntryFont, width=10, borderwidth=2)
Certentry1.pack(side=LEFT, padx=10, pady=5)
Certentry2 = Entry(frameCertform3, textvariable=Varcert2,  font=bEntryFont, width=10, borderwidth=2)
Certentry2.pack(side=LEFT, padx=10, pady=5)
Certentry3 = Entry(frameCertform3, textvariable=Varcert3,  font=bEntryFont, width=10, borderwidth=2)
Certentry3.pack(side=LEFT, padx=10, pady=5)
Certentry4 = Entry(frameCertform3, textvariable=Varcert4,  font=bEntryFont, width=10, borderwidth=2)
Certentry4.pack(side=LEFT, padx=10, pady=5)
Certentry5 = Entry(frameCertform3, textvariable=Varcert5,  font=bEntryFont, width=10, borderwidth=2)
Certentry5.pack(side=LEFT, padx=10, pady=5)


def certsave():
    chk1 = entryCertUser.get()
    chk2 = entryCertYear.get()
    check = "select count(*) from pic where emp_id=%s and year(currentDate)=%s" % (chk1, chk2)
    mycursor.execute(check)
    check1 = mycursor.fetchall()
    for i in check1:
        rslt = i[0]
    if rslt == 0:
        messagebox.showwarning("Warning", "No records present for current data")
    else:
        aBlank1 = Certentry1.get()
        aBlank2 = Certentry2.get()
        aBlank3 = Certentry3.get()
        aBlank4 = Certentry4.get()
        aBlank5 = Certentry5.get()
        a = entryCertUser.get()
        b = entryCertYear.get()
        c1 = ""
        c3 = ""
        c4a = ""
        c4b = ""
        c5 = ""
        c6 = ""
        c7a = ""
        c7b = ""
        c8 = ""
        c9 = ""
        c10 = ""
        c11 = ""
        Select = "select employee.name,employee.level,pic.presentPay,pic.presentGrade,pic.prevDate,pic.currentDate,pic.nextPay,pic.nextGrade,pic.absntFrom,pic.absntTo,pic.reason,pic.nextPay from employee,pic where employee.id=pic.emp_id and pic.emp_id= %s and year(pic.currentdate)=%s" % (a, b)
        mycursor.execute(Select)
        result = mycursor.fetchall()
        for i in result:
            values = i[0]
        for i in result:
            c1 = i[0]
            c3 = i[1]
            c4a = i[2]
            c4b = i[3]
            c5 = i[4]
            c6 = i[5]
            c7a = i[6]
            c7b = i[7]
            c8 = i[8]
            c9 = i[9]
            c11 = i[10]
        # Report lab starts here

        from reportlab.platypus.flowables import Flowable

        class verticalText(Flowable):

            def __init__(self, text):
                Flowable.__init__(self)
                self.text = text

            def draw(self):
                canvas = self.canv
                canvas.rotate(90)
                fs = canvas._fontsize
                canvas.translate(1, -fs / 1.2)  # canvas._leading?
                canvas.drawString(0, 0, self.text)

            def wrap(self, aW, aH):
                canv = self.canv
                fn, fs = canv._fontname, canv._fontsize
                return canv._leading, 1 + canv.stringWidth(self.text, fn, fs)

        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import Table, TableStyle, Paragraph
        from reportlab.lib import colors
        from reportlab.lib.styles import ParagraphStyle
        #from rotatedtext import verticalText
        from reportlab.lib.units import cm
        import os

        addname = c6.year
        addname1 = str(addname)
        filename = c1 + '_' + addname1 + '.pdf'
        documentTitle = 'PIC Certificate'

        # filename and title
        pdf = canvas.Canvas(filename, pagesize=A4)
        pdf.setTitle(documentTitle)

        """**************Heading*******************"""

        heading = 'PERIODICAL INCREMENT CERTIFICATE'
        pdf.setFont("Times-Bold", 14)
        pdf.drawCentredString(296, 720, heading)
        pdf.underlineWidth = 'baseUnderlineWidth'
        pdf.line(155, 718, 437, 718)

        heading_side = ['  21/G.A.R.21',
                        '24/Form T.R.24',
                        '(See Rule 272)'
                        ]

        text = pdf.beginText(450, 760)
        text.setFont("Times-Roman", 10)
        for line in heading_side:
            text.textLine(line)
        pdf.drawText(text)
        """****************************************"""

        # --------------------------------paragraphs--------------------------------------------
        style = ParagraphStyle(
            name='Normal',
            fontName='Times-Roman',
            fontSize=12,
            leftIndent=1,
            rightIndent=10,
            justifyLastLine=0,
            splitLongWords=1,
            leading=16
        )
        """ *************Variables****************** """
        if aBlank1 == "":
            p1 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            p1 = aBlank1

        if aBlank2 == "":
            p2 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            p2 = aBlank2

        if aBlank3 == "":
            p3 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            p3 = aBlank3

        if aBlank4 == "":
            p4 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            p4 = aBlank4

        if aBlank5 == "":
            p5 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            p5 = aBlank5
        """******************************************"""

        para1 = Paragraph(
            f"""1. &nbsp; &nbsp; &nbsp; &nbsp; Certified that the Government servants named below have earned the prescribed periodical<br />
        increment from the date cited in Col.6 having been the incumbents of the posts specified for not less<br />
        than <u> {p1} </u> year(s) from the date shown in col.5, after deducting periods of absence from<br />
        duty not counting for increment, absence on leave without pay etc. Further certified that the<br />
        period/periods of leave taken from <u> {p2} </u> to <u> {p3} </u> and from <u> {p4} </u> to <u> {p5} </u><br />
        has/have been counted for increment in the case of officiating Government servant/servants named<br />
         he/they would have officiated in the post/posts but for his/their proceeding on leave.""", style=style)
        w, h = para1.wrap(500, 500)
        para1.drawOn(pdf, 50, 570)

        para2 = Paragraph("""2. &nbsp; &nbsp; &nbsp; &nbsp; Certified that the Government servant/servants named below has/have earned/will earn<br />
        periodical increments from the date cited for reason stated in the explanatory memo attached hereto. """,
                          style=style)
        w, h = para2.wrap(500, 500)
        para2.drawOn(pdf, 50, 520)

        footer1 = Paragraph(
            f"""Note :- 1. &nbsp &nbsp &nbsp &nbsp When the increment claimed is the first to carry a Government servant over an<br />
         &nbsp &nbsp &nbsp &nbsp &nbsp efficiency bar, column 5,6 and 7 should be filled up in red ink. """, style=style)

        footer2 = Paragraph(
            f"""2. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp The figure (1) and (2) should be placed against each name according as the certificate<br />
        (1) or (2) applies. The explanatory memorandum should be submitted in any case in which<br />certificate (2) applies.""",
            style=style)

        footer1.wrap(500, 500)
        footer1.drawOn(pdf, 50, 200)

        footer2.wrap(500, 400)
        footer2.drawOn(pdf, 81, 145)

        # ---------------------- Table part ---------------------------------
        import datetime
        one = c1

        two = 'Officiating'

        three = 'Level' + ' ' + c3 #level

        t1 = str(c4a)
        four = 'Rs ' + t1

        t2 = str(c4b)
        five = "0"

        t3 = str(c5)
        t31 = datetime.datetime.strptime(t3, '%Y-%m-%d')
        t32 = t31.strftime("%d/%m/%Y ")
        six = t32

        t4 = str(c6)
        t41 = datetime.datetime.strptime(t4, '%Y-%m-%d')
        t42 = t41.strftime("%d/%m/%Y ")
        seven = t42

        t5 = str(c7a)
        eight = t5
        t6 = str(c7b)
        nine = t6

        t7 = str(c8)

        if t7 == 'None':
            ten = 'Nil'
        else:
            t71 = datetime.datetime.strptime(t7, '%Y-%m-%d')
            t72 = t71.strftime("%d/%m/%Y ")
            ten = t72

        t8 = str(c9)
        if t8 == 'None':
            eleven = 'Nil'
        else:
            t81 = datetime.datetime.strptime(t8, '%Y-%m-%d')
            t82 = t81.strftime("%d/%m/%Y ")
            eleven = t82

        twelve = 'NIL'
        t9 = c11

        t9 = t9.strip('.')
        thirteen = t9

        table_data = [
            ['Name of\nincumbent', 'Whether\nsubstantive\nor officiating', 'Scale\nof pay\npost',
             'Present\npay &\nGrade Pay', '', 'Date from\nwhich\npresent\npay is\ndrawn', 'Date of\npresent\nincrement',
             'Future\npay with\nGrade\npay', '', 'Absence from\nduty not counting\nfor increment', '',
             'Leave without pay and in the\ncase of those holding the posts\nis the officiating capacity, all\nother kinds of leave during\nwhich he/they would not have\ncontinued to the officiate in the\nposts',''],
            ['', '', '', '', '', '', '', '', '', 'From', 'To', 'From', 'To'],
            ['1', '2', '3', '4', '', '5', '6', '7', '', '8', '9', '10', '11'],
            [verticalText(one), verticalText(two), verticalText(three), verticalText(four), verticalText(five), verticalText(six), verticalText(seven), verticalText(eight), verticalText(nine), verticalText(ten), verticalText(eleven), verticalText(twelve), verticalText(thirteen)]
        ]

        cw = [2 * cm] + [1.8 * cm] + [0.9 * cm] + [0.8 * cm] + [0.8 * cm] + [1.4 * cm] + [1.4 * cm] + [0.8 * cm] + [0.8 * cm] + [1.2 * cm] + [1.2 * cm] + [1.8 * cm] + [2.4 * cm] * 4
        rh = [3 * cm] + [0.5 * cm] + [0.5 * cm] + [4.1 * cm]
        table = Table(table_data, colWidths=cw, rowHeights=rh)

        style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (3, 0), colors.white), ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'), ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('SPAN', (3, 0), (4, 0)), ('SPAN', (7, 0), (8, 0)), ('SPAN', (9, 0), (10, 0)), ('SPAN', (11, 0), (12, 0)),
            ('SPAN', (0, 0), (0, 1)), ('SPAN', (1, 0), (1, 1)), ('SPAN', (2, 0), (2, 1)), ('SPAN', (3, 0), (4, 1)),
            ('SPAN', (5, 0), (5, 1)), ('SPAN', (6, 0), (6, 1)), ('SPAN', (7, 0), (8, 1)),
            ('SPAN', (3, 2), (4, 2)), ('SPAN', (7, 2), (8, 2)), ('SPAN', (7, 3), (8, 3)),
            ('VALIGN', (0, 3), (-1, -1), 'MIDDLE'),

        ])

        table.setStyle(style)
        width, height = A4
        table.wrapOn(pdf, 500, 500)
        table.drawOn(pdf, 50, 265)

        # ---------------------------table part ends here -------------------------------

        signature = 'Signature & designation of Drawing Officer.'
        pdf.setFont("Times-BoldItalic", 10)
        pdf.drawString(300, 100, signature)

        pdf.save()
        pdf.showPage()
        messagebox.showinfo("Information", "File is ready to print.")
        os.system('"%s"' %filename)


def certclear():
    entryCertUser.delete(0, END)
    entryCertYear.delete(0, END)
    Certentry1.delete(0, END)
    Certentry2.delete(0, END)
    Certentry3.delete(0, END)
    Certentry4.delete(0, END)
    Certentry5.delete(0, END)


def certcancel():
    certclear()
    frameCertform2.pack_forget()


buttonCertSave = Button(frameCertform4, text="Save", font=buttonFont, fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=10, anchor="center", command=certsave)
buttonCertSave.pack(side=LEFT, padx=(90,30))

buttonCertClear = Button(frameCertform4, text="Clear", font=buttonFont, fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=10, anchor="center", command=certclear)
buttonCertClear.pack(side=LEFT, padx=50)

buttonCertCancel = Button(frameCertform4, text="Cancel", font=buttonFont, fg="sky blue", bg="#232f34", bd=1,activebackground="#232f34",width=10, anchor="center", command=certcancel)
buttonCertCancel.pack(side=LEFT, padx=50)

# Print certificate .pdf frame starts here
# Frame Add User ends here

status = Label(frame3, text='All Rights Reserved.', fg="white", font=fFont, bg="Black", bd=3, relief=FLAT, anchor=CENTER)
status.pack(side=BOTTOM, fill=BOTH)

root.mainloop()