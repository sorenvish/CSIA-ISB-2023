from tkinter import *             
#from turtle import heading  
import sqlite3          

#DATABASE---------------------------------------------------------
conn = sqlite3.connect('hotelmanager.db') #creating database
c = conn.cursor()
#make new database if not exists

jobs = """CREATE TABLE IF NOT EXISTS jobs(
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name STRING,
    room_num INTEGER,
    clean_type STRING,
    time INTEGER)"""
c.execute(jobs) #Creation of table which stores all jobs

c.execute("SELECT * FROM jobs")

conn.commit()
#------------------------------------------------------------------

root=Tk()
root.title('Login') #defining root
root.geometry('925x500+300+200') 
root.configure(bg="#fff")
root.resizable(False,False) #makes it so you cannot resize the screen

def stopwatch():
    pass

def admin_screen(): #admin screen code, everything that is the admin screen
    screen=Toplevel(root)
    screen.title("adminPage")
    screen.geometry('1200x800+300+200')
    screen.config(bg="white")
    screen.resizable(False,False) #makes it so you cannot resize the screen
    
    Label(screen,
            text='Admin Page',
            bg='#fff',
            font=('Calibri(Body)',50,'bold')
    ).pack(expand=True, anchor = N, pady = 20)
   
    dropdownframe = Frame(screen)
    dropdownframe.pack(pady = 200, side = TOP)

    roombuttonframe = Frame(screen) #creates frame for room perfrormance page select buttons
    roombuttonframe.pack(pady = 20, side = BOTTOM)

    def openuser1perf(): #button action to open user 1 performance screen
        user1perf()

    def openuser2perf(): #button action to open user 2 performance screen
        user2perf()

    def submitjob():  #INDEX -1 in order to input the last value of the string
        c.execute("INSERT INTO jobs (employee_name, room_num, clean_type) values (?, ?, ?)", #creating new job
        (uservar.get(), roomvar.get(),cleanvar.get()))
        conn.commit()

    useroptions = ['user1', 'user2'] #user select dropdown
    uservar = StringVar()
    uservar.set(useroptions[0])
    userdrop = OptionMenu(dropdownframe, uservar, *useroptions)
    
    userdrop.config(width=20)
    userdrop.pack(pady=20,padx = 10, side = LEFT)
    
    userlabel= Label(screen,            #page labels
                        text='User',
                        font=('Microsoft YaHei UI Light',12)
    ).place(x=230,y=500)

    roomlabel= Label(screen,
                        text='Room Number',
                        font=('Microsoft YaHei UI Light',12)
    ).place(x=460,y=500)

    cleanlabel= Label(screen,
                        text='Clean Type',
                        font=('Microsoft YaHei UI Light',12)
    ).place(x=710,y=500)
   
    roomoptions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #room creation option
    roomvar = IntVar()
    roomvar.set(roomoptions[0])
    roomdrop = OptionMenu(dropdownframe, roomvar, *roomoptions)
    roomdrop.config(width=20)
    roomdrop.pack(pady=20, padx = 10, side = LEFT)
    
    cleanoptions = ['Turndown', 'Turnover'] #type creation option
    cleanvar = StringVar()
    cleanvar.set(cleanoptions[0])
    cleandrop = OptionMenu(dropdownframe, cleanvar, *cleanoptions)
    cleandrop.config(width=20)
    cleandrop.pack(pady=20, padx = 10, side = LEFT)

    submitbutton = Button(dropdownframe,
                        text = "Submit Job",
                        font = ("Comic Sans", 30),
                        fg = "black",
                        bg = "#00acdf",
                        activeforeground = "black",
                        activebackground = "#00acdf",
                        command = submitjob
                        )
    submitbutton.pack(side = LEFT)

    button = Button(roombuttonframe,      #button to open user 1 performance screen
                text="User 1 Performance",
                command=openuser1perf,
                font = ("Comic Sans", 30),
                fg = "black",
                bg = "#00acdf",
                activeforeground = "black",
                activebackground = "#00acdf",
                state=ACTIVE,

                compound = "bottom")
    button.place(x=10, y=20)
    button.pack(padx = 10,pady = 10, side = LEFT)

    button2 = Button(roombuttonframe,      #button to open user 2 performance screen
                text="User 2 Performance",
                command=openuser2perf,
                font = ("Comic Sans", 30),
                fg = "black",
                bg = "#00acdf",
                activeforeground = "black",
                activebackground = "#00acdf",
                state=ACTIVE,
                compound = "bottom")
    button2.pack(padx = 10,pady = 10, side = LEFT)

    screen.mainloop()

def user1_screen():         #User1 screen that came from the sign in if statement

    screen1=Toplevel(root) #puts scree1 at the top
    screen1.geometry('1200x800+300+200')
    screen1.config(bg="white")

#---------------------------
    c.execute('SELECT * FROM jobs WHERE employee_name = "user1" LIMIT 0,10') 
    # Creates datatable for user info
    
    i=0
    for job in c:
        for j in range(len(job)):
            table = Label(screen1,
                    width=20,
                    height=2,
                    fg='blue',
                    text = job[j],
                    
            )
            table.grid(row=i,column=j)
        i=i+1

#---------------------------
    def time_submit():
        minutesgot = int(minutes_entry.get()) #Minutes
        secondsgot = int(seconds_entry.get()) #Seconds
        totalSeconds = (minutesgot * 60) + secondsgot #Time inputed
        id = int(id_entry.get())

        c.execute("UPDATE jobs SET time=? WHERE rowid=?", (totalSeconds, id))
        conn.commit()   #Recursive screen refresh
        screen1.destroy()
        user1_screen()

    minutes_label=Label(screen1,          #Entry box labels
                        text='Enter Minutes:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+2,column=0, pady=40)

    seconds_label=Label(screen1,
                        text='Enter Seconds:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+3,column=0, pady=40)

    id_label=Label(screen1,
                   text='Enter Job ID:',
                   font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+4,column=0, pady=40)

    minutes_entry = Entry(screen1, 
                          font=('Microsoft YaHei UI Light',12))
    minutes_entry.grid(row=i+2,column=1)
    
    seconds_entry = Entry(screen1,
                          font=('Microsoft YaHei UI Light',12)
    )
    seconds_entry.grid(row=i+3,column=1)
    
    id_entry = Entry(screen1,
                     font=('Microsoft YaHei UI Light',12))
    id_entry.grid(row=i+4,column=1)

    user = Entry(screen1,         #text entry bar (first line)
                border=0,
                bg="white",
                font=('Microsoft YaHei UI Light',20)
    )
 

    time_button=Button(screen1,            #Time submit button
                       text="Submit",
                       font=('Microsoft YaHei UI Light',12),
                       command=time_submit
    ).grid(row=i+2,column=2)

    pagename = Label(screen1,
        text='User 1 Page',
        font=('Microsoft YaHei UI Light',30),
        bg='#fff',
    ).grid(row=1,column=j+2,sticky='n',padx=55)

    jobidlabel= Label(screen1,
                        text='Job ID',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=0, pady=10)

    usernamelabel= Label(screen1,
                        text='User Name',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=1, pady=10)

    roomnumberlabel= Label(screen1,
                        text='Room Number',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=2, pady=10)

    cleantypelabel= Label(screen1,
                        text='Clean Type',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=3, pady=10)

    timelabel= Label(screen1,
                        text='Time',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=4, pady=10)

    screen1.mainloop()

def user2_screen(): #user 2 screen
    screen2=Toplevel(root)
    screen2.geometry('1200x800+300+200')
    screen2.config(bg="white")

    c.execute('SELECT * FROM jobs WHERE employee_name = "user2" LIMIT 0,10') #make it user1 only
    i=0
    for job in c:
        for j in range(len(job)):
            table = Label(screen2,
                    width=20,
                    height=2,
                    fg='blue',
                    text = job[j],
                    
            )
            table.grid(row=i,column=j)
        i=i+1

    def time_submit():
        x = int(minutes_entry.get()) # x refers to the minutes given
        y = int(seconds_entry.get()) # y refers to seconds given
        z = (x * 60) + y     # z is the total time in seconds
        id = int(id_entry.get())
        c.execute("UPDATE jobs SET time=? WHERE rowid=?", (z, id))
        conn.commit()   #figure out refreshing screen
        screen2.destroy() #refreshes page
        user2_screen()

    jobidlabel= Label(screen2,          #table labels
                        text='Job ID',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=0, pady=10)

    usernamelabel= Label(screen2,
                        text='User Name',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=1, pady=10)

    roomnumberlabel= Label(screen2,
                        text='Room Number',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=2, pady=10)

    cleantypelabel= Label(screen2,
                        text='Clean Type',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=3, pady=10)

    timelabel= Label(screen2,
                        text='Time',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=4, pady=10)

    minutes_label=Label(screen2,
                        text='Enter Minutes:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+2,column=0, pady=40)            #on screen labels for  entries

    seconds_label=Label(screen2,
                        text='Enter Seconds:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+3,column=0, pady=40)

    id_label=Label(screen2,
                   text='Enter Job ID:',
                   font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+4,column=0, pady=40)

    minutes_entry = Entry(screen2, font=('Microsoft YaHei UI Light',12)) #time entry boxes
    minutes_entry.grid(row=i+2,column=1)
    
    seconds_entry = Entry(screen2, font=('Microsoft YaHei UI Light',12))
    seconds_entry.grid(row=i+3,column=1)
    
    id_entry = Entry(screen2, font=('Microsoft YaHei UI Light',12))
    id_entry.grid(row=i+4,column=1)

    user = Entry(screen2,         #text entry bar (first line)
                border=0,
                bg="white",
                font=('Microsoft YaHei UI Light',20)
    )

    time_button=Button(screen2,
                text="Submit", 
                font=('Microsoft YaHei UI Light',12),
                command=time_submit
                ).grid(row=i+2,column=2) #button that submits time

    pagename = Label(screen2,
        text='User 2 Page',
        font=('Microsoft YaHei UI Light',30),
        bg='#fff',
    ).grid(row=1,column=j+2,sticky='n',padx=55)

    screen2.mainloop()

def user1perf():
    screen3=Toplevel(root)
    screen3.geometry('1200x800+300+200')
    screen3.config(bg="white")
    
    def delete_submit(): # command for submitting a delete query
        x = int(delete_entry.get()) # x refers to value to be deleted
        c.execute("DELETE FROM jobs WHERE rowid=?", (x,))
        screen3.destroy()
        user1perf()
#---------------------------
    c.execute('SELECT * FROM jobs WHERE employee_name = "user1" LIMIT 0,10') #make it user1 only
    i=0
    for job in c:
        for j in range(len(job)):
            table = Label(screen3,
                    width=20,
                    height=2,
                    fg='blue',
                    text = job[j],

            )
            table.grid(row=i,column=j)
        i=i+1
#---------------------------

    c.execute("SELECT AVG (time) FROM jobs WHERE employee_name = 'user1' AND clean_type = 'Turnover'")
    num1 = c.fetchone()
    average1 = num1[0] #takes raw number of seconds for turnover

    hour1=average1%(24*3600)//3600 #finds hours
    second1=average1%60 #finds seconds

    average1=average1%3600
    minutes1=average1//60 #finds minutes

    avgval1 = ("%d:%d:%d"%(hour1,minutes1,second1)) #all changes seconds into minutes and hours

    c.execute("SELECT AVG (time) FROM jobs WHERE employee_name = 'user1' AND clean_type = 'Turndown'")
    num2 = c.fetchone()
    average2 = num2[0] #raw number of seconds for turndown

    hour2=average2%(24*3600)//3600 #finding average hours for turndown
    second2=average2%60 #finds seconds

    average2=average2%3600 
    minutes2=average2//60 #finds minutes

    avgval2 = ("%d:%d:%d"%(hour2,minutes2,second2)) #displays in hours:minutes:seconds

    pagename = Label(screen3,
        text='User 1 Perf',
        font=('Microsoft YaHei UI Light',30),
        bg='#fff',
    ).grid(row=1,column=j+2,sticky='n',padx=55)

    jobidlabel= Label(screen3,          #screen labels
                        text='Job ID',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=0, pady=10)

    usernamelabel= Label(screen3,
                        text='User Name',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=1, pady=10)

    roomnumberlabel= Label(screen3,
                        text='Room Number',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=2, pady=10)

    cleantypelabel= Label(screen3,
                        text='Clean Type',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=3, pady=10)

    timelabel= Label(screen3,
                        text='Time',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=4, pady=10)

    delete_label= Label(screen3,
                        text='Job ID to Delete:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+2,column=0, pady=40)

    delete_entry = Entry(screen3, 
                        font=('Microsoft YaHei UI Light',12)
    )
    delete_entry.grid(row=i+2,column=1)

    averageturnover_label= Label(screen3,
                        text='Turnover Average: ' +avgval1,
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+3,column=0, pady=40)

    averageturndown_label= Label(screen3,
                        text='Turndown Average: ' +avgval2,
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+4,column=0, pady=40)

    time_button=Button(screen3,  #delete submit button
                        text="Submit", 
                        font=('Microsoft YaHei UI Light',12),
                        command=delete_submit
    ).grid(row=i+2,column=2)

    screen3.mainloop()

def user2perf():         #User 2 performance screen
    screen4=Toplevel(root)
    screen4.geometry('1200x800+300+200')
    screen4.config(bg="white")

    def delete_submit():
        x = int(delete_entry.get()) #x refers to the value getting deleted
        c.execute("DELETE FROM jobs WHERE rowid=?", (x,))
        screen4.destroy()
        user2perf()
#---------------------------
    c.execute('SELECT * FROM jobs WHERE employee_name = "user2" LIMIT 0,10') #make it user1 only
    i=0
    for job in c:
        for j in range(len(job)):
            table = Label(screen4,
                    width=20,
                    height=2,
                    fg='blue',
                    text = job[j],
            )
            table.grid(row=i,column=j)
        i=i+1
#---------------------------

    c.execute("SELECT AVG (time) FROM jobs WHERE employee_name = 'user2' AND clean_type = 'Turnover'")
    num1 = c.fetchone()    #takes one value from time
    average1 = num1[0]

    hour1=average1%(24*3600)//3600   #find hour values
    second1=average1%60

    average1=average1%3600
    minutes1=average1//60    #find minute values

    avgval1 = ("%d:%d:%d"%(hour1,minutes1,second1)) #all changes seconds into minutes and hours

    c.execute("SELECT AVG (time) FROM jobs WHERE employee_name = 'user2' AND clean_type = 'Turndown'")
    num2 = c.fetchone()    #takes one value from time
    average2 = num2[0]

    hour2=average2%(24*3600)//3600     #find hour values
    second2=average2%60

    average2=average2%3600
    minutes2=average2//60       #find minute values

    avgval2 = ("%d:%d:%d"%(hour2,minutes2,second2)) 

    pagename = Label(screen4, #screen page labels here and below
        text='User 1 Perf',
        font=('Microsoft YaHei UI Light',30),
        bg='#fff',
    ).grid(row=1,column=j+2,sticky='n',padx=55)

    jobidlabel= Label(screen4,
                        text='Job ID',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=0, pady=10)

    usernamelabel= Label(screen4,
                        text='User Name',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=1, pady=10)

    roomnumberlabel= Label(screen4,
                        text='Room Number',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=2, pady=10)

    cleantypelabel= Label(screen4,
                        text='Clean Type',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=3, pady=10)

    timelabel= Label(screen4,
                        text='Time',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+1,column=4, pady=10)

    delete_label= Label(screen4,
                        text='Job ID to Delete:',
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+2,column=0, pady=40)

    delete_entry = Entry(screen4, 
                        font=('Microsoft YaHei UI Light',12)
    )
    delete_entry.grid(row=i+2,column=1)

    averageturnover_label= Label(screen4,
                        text='Turnover Average: ' +avgval1,
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+3,column=0, pady=40)

    averageturndown_label= Label(screen4,
                        text='Turndown Average: ' +avgval2,
                        font=('Microsoft YaHei UI Light',12)
    ).grid(row=i+4,column=0, pady=40)

    time_button=Button(screen4, text="Submit", font=('Microsoft YaHei UI Light',12),command=delete_submit
    ).grid(row=i+2,column=2)

    screen4.mainloop()

def signin():   #sign in page (first page that is encountered)
    username=user.get()
    password=code.get()

    if username=='admin' and password == 'admin1': #This is the admin page that signing in opens up
        admin_screen()
    
    elif username =='user1' and password == 'cat': #User page that signing in opens up for user1 page
        user1_screen()

    elif username =='user2' and password == 'dog': # signing in to open user 2 page
        user2_screen()

img = PhotoImage(file='HotelManager.png') #image of 'Hotel Manager' on login page
Label(root,image=img,bg='white').place(x=-50,y=50) #positions image

frame=Frame(root, #creates frame for the login system
            width=350,
            height = 350,
            bg="white"
)
frame.place(x=480,y=70)

heading=Label(frame,             #heading that says 'Sign In'
                text = 'Sign in',
                fg='#57a1f8',
                bg = 'white',
                font = ('Microsoft YaHei UI Light',35)
)
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0, 'end') #def to make user disapear on click

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame,         #text entry bar (first line)
                width=20, 
                fg='black',
                border=0,
                bg="white",
                font=('Microsoft YaHei UI Light',20)
)
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)   #puts focus on entry box
user.bind('<FocusOut>', on_leave)  #removes focus from entry box

Frame(frame,
        width=295,
        height=2,
        bg='black'
).place(x=25,y=107)

def on_enter(e):
    code.delete(0, 'end') #def to make password disapear on click

def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,         #text entry bar (second line)
                width=20, 
                fg='black',
                border=0,
                bg="white",
                font=('Microsoft YaHei UI Light',20)
)
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)   #puts focus on entry box
code.bind('<FocusOut>', on_leave)  #removes focus from entry box

Frame(frame,
        width=295,
        height=2,
        bg='black'
).place(x=25,y=177)

Button(frame,       #sign in button
        width=25,
        pady=7,
        text='Sign in',
        bg='#57a1f8',
        fg='white',
        border=0,
        command=signin
).place(x=35,y=204)

root.mainloop()  #closes loop