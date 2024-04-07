from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "06283D"


mydatabase = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Manoragavi-2517') # Connecting to the database
mycur = mydatabase.cursor()
print("Connected to Database")

querry_create_db = "CREATE DATABASE IF NOT EXISTS student"
querry_use_db = "use student"
querry_create_table = "create table if not exists login (rollnumber int(10), username VARCHAR(255), password VARCHAR(255), admissionno int(10), class VARCHAR(10), phnumber VARCHAR(10), email VARCHAR(255), city VARCHAR(100), hobby VARCHAR(255), result int(10))"
mycur.execute(querry_create_db)
mycur.execute(querry_use_db)
mycur.execute(querry_create_table)

exit_mode = False

while not exit_mode:
    #Trial Count
    trialCount = 0
    def trial():
        global trialCount
        trialCount += 1
        print("TrialCount is ", trialCount)
        if trialCount == 3:
            messagebox.showerror("Warning", "You have tried more than limit!!!")
            root.destroy()

    passwordButtonMode = True

    # User register
    def register():
        root.destroy()
        regtkin = Tk()
        regtkin.title("Register System")
        regtkin.geometry("1280x720")
        regtkin.config(bg = background)
        regtkin.resizable(False,False)

        image_icon = PhotoImage(file = "images\\loginn.png")
        regtkin.iconphoto(False, image_icon)

        regframe = Frame(regtkin, bg="red")
        regframe.pack(fill=Y)

        backgroundimage = PhotoImage(file = "images\\Details.png")
        Label(regframe,image=backgroundimage).pack()

    # Details about user
        topic = f"Enter your Details"
        label = Label(regtkin,
                    text=topic,
                    fg = "#fff",
                    bg = "#5FC7FC",
                    font = ('Arial', 24, 'bold'))
        label.place(x=500, y=70)

    #UserID
        label = Label(regtkin, 
                    text="Username", 
                    fg = "#fff", 
                    bg = "#155CA2", 
                    borderwidth=5, 
                    relief="groove",
                    font = ('Arial', 20, 'bold'), width=16)
        label.place(x=250,y=150)

        def user_enter_username(e):
            if userName.get() == 'Enter Your User Name':
                userName.delete(0,'end')

        def user_leave_username(e):
            if userName.get() == '':
                userName.insert(0,'Enter Your User Name')

        userName = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        userName.insert(0,'Enter Your User Name')
        userName.bind("<FocusIn>", user_enter_username)
        userName.bind("<FocusOut>", user_leave_username)
        userName.place(x=550, y=150)

    # UserPassword
        label = Label(regtkin, 
                    text="Password", 
                    fg = "#fff", 
                    bg = "#155CA2", 
                    borderwidth=5, 
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=200)

        def user_enter_password(e):
            if userPassword.get() == 'Enter Your Password':
                userPassword.delete(0,'end')

        def user_leave_password(e):
            if userPassword.get() == '':
                userPassword.insert(0,'Enter Your Password')
        
        userPassword = Entry(width=30,
                            fg="#375174",
                            border=0,bg="#fff",
                            font=('Arial Bold', 24))
        userPassword.insert(0,'Enter Your Password')
        userPassword.bind("<FocusIn>", user_enter_password)
        userPassword.bind("<FocusOut>", user_leave_password)
        userPassword.place(x=550, y=200)

        def passwordhide():
            global passwordButtonMode
            if passwordButtonMode:
                passwordeyeButton.config(image=passwordcloseeye,activebackground="white")
                userPassword.config(show="*")
                passwordButtonMode = False
            else:
                passwordeyeButton.config(image=passwordopeneye,activebackground="white")
                userPassword.config(show="")
                passwordButtonMode = True
        passwordopeneye = PhotoImage(file="images\\show.png")
        passwordcloseeye = PhotoImage(file="images\\hide.png")
        passwordeyeButton = Button(regframe, 
                                image=passwordopeneye, 
                                fg="#fff", 
                                bd = 0, 
                                command=passwordhide)
        passwordeyeButton.place(x=1090, y=195)

    # RollNo
        label = Label(regtkin, 
                    text="Roll Number", 
                    fg = "#fff", 
                    bg = "#155CA2", 
                    borderwidth=5, 
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=250)

        def user_enter_rollno(e):
            if userRoll.get() == 'Enter Your Roll Number':
                userRoll.delete(0,'end')

        def user_leave_rollno(e):
            if userRoll.get() == '':
                userRoll.insert(0,'Enter Your Roll Number')

        userRoll = Entry(width=30,fg="#375174",border=0,bg="#fff",font=('Arial Bold', 24))
        userRoll.insert(0,'Enter Your Roll Number')
        userRoll.bind("<FocusIn>", user_enter_rollno)
        userRoll.bind("<FocusOut>", user_leave_rollno)
        userRoll.place(x=550, y=250)

    # Admission Number
        label = Label(regtkin, 
                    text="Admission Number", 
                    fg = "#fff", 
                    bg = "#155CA2", 
                    borderwidth=5, 
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=300)

        def user_enter_admno(e):
            if useradmno.get() == 'Enter Your Admission Number':
                useradmno.delete(0,'end')

        def user_leave_admno(e):
            if useradmno.get() == '':
                useradmno.insert(0,'Enter Your Admission Number')

        useradmno = Entry(width=30,fg="#375174",border=0,bg="#fff",font=('Arial Bold', 24))
        useradmno.insert(0,'Enter Your Admission Number')
        useradmno.bind("<FocusIn>", user_enter_admno)
        useradmno.bind("<FocusOut>", user_leave_admno)
        useradmno.place(x=550, y=300)

    # Class
        label = Label(regtkin, 
                    text="Class and Section", 
                    fg = "#fff", 
                    bg = "#155CA2", 
                    borderwidth=5, 
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=350)

        def user_enter_class(e):
            if userclass.get() == 'Enter Your Class and Section':
                userclass.delete(0,'end')

        def user_leave_class(e):
            if userclass.get() == '':
                userclass.insert(0,'Enter Your Class and Section')

        userclass = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        userclass.insert(0,'Enter Your Class and Section')
        userclass.bind("<FocusIn>", user_enter_class)
        userclass.bind("<FocusOut>", user_leave_class)
        userclass.place(x=550, y=350)

    # Phone Number
        label = Label(regtkin, 
                    text="Phone Number",
                    fg = "#fff",
                    bg = "#155CA2",
                    borderwidth=5,
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=400)

        def user_enter_phno(e):
            if userphno.get() == 'Enter Your Phone Number':
                userphno.delete(0,'end')

        def user_leave_phno(e):
            if userphno.get() == '':
                userphno.insert(0,'Enter Your Phone Number')

        userphno = Entry(width=30,
                        fg="#375174",
                        border=0,bg="#fff",
                        font=('Arial Bold', 24))
        userphno.insert(0,'Enter Your Phone Number')
        userphno.bind("<FocusIn>", user_enter_phno)
        userphno.bind("<FocusOut>", user_leave_phno)
        userphno.place(x=550, y=400)

    # Email
        label = Label(regtkin, 
                    text="Email",
                    fg = "#fff",
                    bg = "#155CA2",
                    borderwidth=5,
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=450)

        def user_enter_email(e):
            if useremail.get() == 'Enter Your Email':
                useremail.delete(0,'end')

        def user_leave_email(e):
            if useremail.get() == '':
                useremail.insert(0,'Enter Your Email')

        useremail = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        useremail.insert(0,'Enter Your Email')
        useremail.bind("<FocusIn>", user_enter_email)
        useremail.bind("<FocusOut>", user_leave_email)
        useremail.place(x=550, y=450)

    # City
        label = Label(regtkin, 
                    text="City",
                    fg = "#fff",
                    bg = "#155CA2",
                    borderwidth=5,
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=500)

        def user_enter_city(e):
            if usercity.get() == 'Enter Your City':
                usercity.delete(0,'end')

        def user_leave_city(e):
            if usercity.get() == '':
                usercity.insert(0,'Enter Your City')

        usercity = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        usercity.insert(0,'Enter Your City')
        usercity.bind("<FocusIn>", user_enter_city)
        usercity.bind("<FocusOut>", user_leave_city)
        usercity.place(x=550, y=500)

    # Hobby
        label = Label(regtkin, 
                    text="Hobby",
                    fg = "#fff",
                    bg = "#155CA2",
                    borderwidth=5,
                    relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=550)

        def user_enter_hobby(e):
            if userhobby.get() == 'Enter Your Hobby':
                userhobby.delete(0,'end')

        def user_leave_hobby(e):
            if userhobby.get() == '':
                userhobby.insert(0,'Enter Your Hobby')

        userhobby = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        userhobby.insert(0,'Enter Your Hobby')
        userhobby.bind("<FocusIn>", user_enter_hobby)
        userhobby.bind("<FocusOut>", user_leave_hobby)
        userhobby.place(x=550, y=550)

    # 10th Result
        label = Label(regtkin, 
                    text="10th Result",
                    fg = "#fff",bg = "#155CA2",
                    borderwidth=5,relief="groove",
                    font = ('Arial', 20, 'bold'), 
                    width=16)
        label.place(x=250,y=600)

        def user_enter_result(e):
            if userresult.get() == 'Enter Your 10th Result':
                userresult.delete(0,'end')

        def user_leave_result(e):
            if userresult.get() == '':
                userresult.insert(0,'Enter Your 10th Result')

        userresult = Entry(width=30,
                        fg="#375174",
                        border=0,
                        bg="#fff",
                        font=('Arial Bold', 24))
        userresult.insert(0,'Enter Your 10th Result')
        userresult.bind("<FocusIn>", user_enter_result)
        userresult.bind("<FocusOut>", user_leave_result)
        userresult.place(x=550, y=600)
        
    #Submit
        def submit():
            if userName.get().strip() == '' or userName.get() == 'Enter your User Name': # Checks if username field is empty
                messagebox.showerror("Entry Error", "Enter your Username")
            
            elif userPassword.get().strip() == '' or userPassword.get() == "Enter Your Password": # Checks if password field is empty
                messagebox.showerror("Entry Error", "Enter your Password")        
            
            elif userRoll.get().strip() == '' or userRoll.get() == "Enter Your Roll Number" or userRoll.get().isdigit() == False: # Checks if roll number field is empty and also it should be digits
                if userRoll.get().strip() == '' or userRoll.get() == "Enter Your Roll Number":
                    messagebox.showerror("Entry Error", "Enter your Roll Number")
                if useradmno.get().isdigit() == False:
                    messagebox.showerror("Entry Error", "Roll Number Should Be In Numbers")
            
            elif useradmno.get().strip() == '' or useradmno.get() == "Enter Your Admission Number" or useradmno.get().isdigit() == False: # Checks if admission number field is empty and also it should be digits
                if useradmno.get().strip() == '' or useradmno.get() == "Enter Your Admission Number":
                    messagebox.showerror("Entry Error", "Enter your Admission Number")
                if useradmno.get().isdigit() == False:
                    messagebox.showerror("Entry Error", "Admission Number Should Be In Numbers")
            
            elif userclass.get().strip() == '' or userclass.get() == "Enter Your Class and Section": # Checks if userclass field is empty
                messagebox.showerror("Entry Error", "Enter your Class and Section") 
            
            elif userphno.get().strip() == '' or userphno.get() == "Enter Your Phone Number" or userphno.get().isdigit() == False: # Checks if phone number field is empty and also it should be digits
                if userphno.get().strip() == '' or userphno.get() == "Enter Your Admission Number":
                    messagebox.showerror("Entry Error", "Enter your Phone Number")
                if userphno.get().isdigit() == False:
                    messagebox.showerror("Entry Error", "Phone Number Should Be In Numbers")
            
            elif useremail.get().strip() == '' or useremail.get() == "Enter Your Email" or useremail.get()[-10:] != '@gmail.com': # Checks if email field is empty and also checks if it is proper mail
                if useremail.get().strip() == '' or useremail.get() == "Enter Your Email":
                    messagebox.showerror("Entry Error", "Enter your Email")
                if useremail.get()[-10:] != '@gmail.com':
                    messagebox.showerror("Entry Error", "Enter Proper Email")
            
            elif usercity.get().strip() == '' or usercity.get() == "Enter Your City": # Checks if city field is empty
                messagebox.showerror("Entry Error", "Enter your City")
            
            elif userhobby.get().strip() == '' or userhobby.get() == "Enter Your Hobby": # Checks if hobby field is empty
                messagebox.showerror("Entry Error", "Enter your Hobby")
            
            elif userresult.get().strip() == '' or userresult.get() == "Enter Your 10th Result": # Checks if 10th result field is empty
                messagebox.showerror("Entry Error", "Enter your 10th Result")

            else:
                rollno = userRoll.get()
                username = userName.get()
                password = userPassword.get()
                admissionno = useradmno.get()
                classandsec = userclass.get()
                phno = userphno.get()
                email = useremail.get()
                city = usercity.get()
                hobby = userhobby.get()
                result = userresult.get()
                
                
                querry_insert_val = "INSERT INTO login VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (rollno, username, password, admissionno, classandsec, phno, email, city, hobby, result)
                mycur.execute(querry_insert_val, values)
                mydatabase.commit()
                messagebox.showinfo("Connection", "Registered Successfully")
                messagebox.showinfo("Connection", "You can now Login!!!")
                
                regtkin.destroy()
                #messagebox.showerror("Connection", "User Already Exists")
                #return

        registerbutton = Button(regtkin,text = "SUBMIT", bg = "#6237CF", fg = "#fff", width = 50, height = 2, command=submit)
        registerbutton.place(x=470, y=660)

        regtkin.mainloop()

    #User Login
    def loginuser():
        username = user.get()
        password = code.get()
        print(username)
        if (username == "UserID" or username == "" or username == " ") and (password == "Password" or password == "" or password == " "):
            messagebox.showerror("Entry Error", "Type Username and Password")
        else:
            try:
                mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Manoragavi-2517', database = "student")
                mycursor = mydb.cursor()
                print("Connected to Database")
            except:
                messagebox.showerror("Connection", "Database connection not establish")
                return

            command = "use student"
            mycursor.execute(command)
            
            command = "select * from login where username=%s and password=%s"
            mycursor.execute(command, (username, password))
            myresult = mycursor.fetchone()

            if myresult == None:
                messagebox.showinfo("Invalid", "Invalid UserID or Password")
                trial()

            else:
                messagebox.showinfo("Login", "Successfully Logined!!!")
                root.destroy()

                # Details Window
                tkin = Tk()
                tkin.title("Login System")
                tkin.geometry("1280x720")
                tkin.config(bg = background)
                tkin.resizable(False,False)
                image_icon = PhotoImage(file = "images\\loginn.png")
                tkin.iconphoto(False, image_icon)
                frame = Frame(tkin, bg="red")
                frame.pack(fill=Y)
                backgroundimage = PhotoImage(file = "images\\Details.png")
                Label(frame,image=backgroundimage).pack()

    # Details about user
                topic = f"Details About {myresult[1]}"
                label = Label(tkin, 
                            text=topic, 
                            fg = "#fff", 
                            bg = "#5FC7FC", 
                            font = ('Arial', 24, 'bold'))
                label.place(x=500, y=70)
    # UserName
                label = Label(tkin, 
                            text="Name", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=165)

                label = Label(tkin, 
                            text=myresult[1], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700,y=165)

    # UserRoll
                label = Label(tkin, 
                            text="Roll Number", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=220)

                label = Label(tkin, 
                            text=myresult[0], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=220)

    # Admisson Number
                label = Label(tkin, 
                            text="Admission Number", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=275)

                label = Label(tkin, 
                            text=myresult[3], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=275)

    # Class
                label = Label(tkin, 
                            text="Class", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=330)

                label = Label(tkin, text=myresult[4], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=330)

    # PhoneNumber
                label = Label(tkin, 
                            text="Phone Number", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=385)

                label = Label(tkin, 
                            text=myresult[5], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=385)

    # Email
                label = Label(tkin, 
                            text="Email", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=440)

                label = Label(tkin, 
                            text=myresult[6], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=440)

    # City
                label = Label(tkin, 
                            text="City", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=495)

                label = Label(tkin, 
                            text=myresult[7], 
                            fg = "#fff", 
                            bg = "#155CA2",
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'),
                            width=22)
                label.place(x=700, y=495)

    # Hobby
                label = Label(tkin, 
                            text="Hobby", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=550)

                label = Label(tkin, 
                            text=myresult[8], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=550)

    # 10th result
                label = Label(tkin, 
                            text="10th Result", 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=16)
                label.place(x=250,y=605)

                label = Label(tkin, 
                            text=myresult[9], 
                            fg = "#fff", 
                            bg = "#155CA2", 
                            borderwidth=5, 
                            relief="groove",
                            font = ('Arial', 20, 'bold'), 
                            width=22)
                label.place(x=700, y=605)

                tkin.mainloop()

    #Window
    root = Tk()
    root.title("Login System")
    root.geometry("1280x720")
    root.config(bg = background)
    root.resizable(False,False)

    #icon
    image_icon = PhotoImage(file = "images\\loginn.png")
    root.iconphoto(False, image_icon)

    #background image
    frame = Frame(root, bg="red")
    frame.pack(fill=Y)
    backgroundimage = PhotoImage(file = "images\\LOGINUI.png")
    Label(frame,image=backgroundimage).pack()

    #user entry
    def user_enter(e):
        if user.get() == 'UserID':
            user.delete(0,'end')

    def user_leave(e):
        if user.get() == '':
            user.insert(0,'UserID')

    user = Entry(frame,
                width=18,
                fg="#375174",
                border=0,
                bg="#fff",
                font=('Arial Bold', 24))
    user.insert(0,'UserID')
    user.bind("<FocusIn>", user_enter)
    user.bind("<FocusOut>", user_leave)
    user.place(x=520, y=255)

    #password entry
    def password_enter(e):
        if code.get() == 'Password':
            code.delete(0,'end')

    def password_leave(e):
        if code.get() == '':
            code.insert(0,'Password')

    code = Entry(frame,
                width=18,
                fg="#375174",
                border=0,
                bg="#fff",
                font=('Arial Bold', 24))
    code.insert(0,'Password')
    code.bind("<FocusIn>", password_enter)
    code.bind("<FocusOut>", password_leave)
    code.place(x=530, y=370)

    #hide and show button
    button_mode = True
    def hide():
        global button_mode

        if button_mode:
            eyeButton.config(image=closeeye,activebackground="white")
            code.config(show="*")
            button_mode = False
        else:
            eyeButton.config(image=openeye,activebackground="white")
            code.config(show="")
            button_mode = True

    # Eye button
    openeye = PhotoImage(file="images\\show.png")
    closeeye = PhotoImage(file="images\\hide.png")
    eyeButton = Button(frame, 
                    image=openeye, 
                    fg="#fff", 
                    bd = 0, 
                    command=hide)
    eyeButton.place(x=800, y=365)

    #login
    loginbutton = Button(root,
                        text = "LOGIN", 
                        bg = "#6237CF", 
                        fg = "#fff", 
                        width = 50, 
                        height = 2, 
                        command=loginuser)
    loginbutton.place(x=470, y=503)

    #register
    registerbutton = Button(root,
                            text = "REGISTER", 
                            bg = "#6237CF", 
                            fg = "#fff", 
                            width = 50, 
                            height = 2, 
                            command=register)
    registerbutton.place(x=470, y=572)

    #exit
    def exit():
        global exit_mode
        exit_mode = True
        root.destroy()
    

    registerbutton = Button(root,
                            text = "EXIT", 
                            bg = "#ff3300", 
                            fg = "black", 
                            width = 50, 
                            height = 2,
                            command=exit)
    registerbutton.place(x=470, y=670)

    if exit_mode:
        root.destroy()
    else:
        root.mainloop()