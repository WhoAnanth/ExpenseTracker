import csv
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import *



ctk.set_appearance_mode('dark')
window=ctk.CTk()
img=PhotoImage(file='BackgroundImage.png') 
tk.Label(window,image=img).pack()

def MainFunc():
    global window
    window.grid()
    window.geometry("500x500")
    
    ctk.CTkLabel(window, text="Welcome",text_color='black',bg_color="#A3BBB3",font=("BOOKMAN OLD STYLE",40)).place(x=170,y=90)
    
    create_user_button = ctk.CTkButton(window, text='Create user', command=Create_user,
                                       fg_color='#5bff68',bg_color='#AFB7A4', text_color='#121212', hover_color='#3baf45',corner_radius=32,font=("BOOKMAN OLD STYLE",15))
    create_user_button.place(x=185,y=150)

    login_button = ctk.CTkButton(window, text='Login', command=auth,
                                 fg_color='#5bff68',bg_color='#A3BBB3', text_color='#121212', hover_color='#3baf45',corner_radius=32,font=("BOOKMAN OLD STYLE",15))
    login_button.place(x=185,y=200)  

    close_button = ctk.CTkButton(window, text='Close', command=window.destroy,
                                  fg_color='#5bff68',bg_color='#BEB7A2',  text_color='#121212', hover_color='#3baf45',corner_radius=32,font=("BOOKMAN OLD STYLE",15))
    close_button.place(x=185,y=250)  

    window.mainloop()




uname = ''
entry_date=''
entry_category=''
entry_description=''
entry_expense=''

def Create_user():
    def inside_func():
        with open('user.csv','a',newline='') as userFile:
                writer = csv.writer(userFile)
                username=var.get()
                userpassword=var2.get()
                userconfpass=var3.get()
                if var.get()=='':
                    CTkMessagebox(title='Notification',message='Please Enter A Valid Username',font=('BOOKMAN OLD STYLE',18),icon='warning')
                    window2.destroy()
                    return Create_user()
                if var2.get()=='':
                    CTkMessagebox(title='Notification',message='Please Enter A Valid password',font=('BOOKMAN OLD STYLE',18),icon='warning')
                    window2.destroy()
                    return Create_user()

                
                while True: 
                    
                    if userpassword == userconfpass:
                        writer.writerow([username,userconfpass])                      
                        CTkMessagebox(title='Notification',message="USER CREATED!",font=('BOOKMAN OLD STYLE',15),icon='check')
                        Entry4.delete(0,tk.END)
                        Entry2.delete(0,tk.END)
                        Entry3.delete(0,tk.END) 
                        window2.destroy()
                        return auth()
                        
                    else:
                        CTkMessagebox(title='Notification',message='Password error or incomplete entry',font=('BOOKMAN OLD STYLE',18),icon="warning")
                        break
                
    global window
    
    window.withdraw()
    window2=ctk.CTkToplevel(window)
    window2.title('USER DETAILS')
    window2.geometry('500x500')
    window2.grid()   
    var=tk.StringVar()
    var2=tk.StringVar() 
    var3=tk.StringVar()    
    ctk.CTkLabel(window2,text='Enter username:',font=("BOOKMAN OLD STYLE",20)).place(x=50,y=100)
    Entry2 = ctk.CTkEntry(window2,textvariable=var)
    Entry2.place(x=240,y=105)
    ctk.CTkLabel(window2,text='Enter password:',font=("BOOKMAN OLD STYLE",20)).place(x=50,y=130)
    Entry3 = ctk.CTkEntry(window2,textvariable=var2)
    Entry3.place(x=240,y=135)  
    ctk.CTkLabel(window2,text='Confirm password:',font=("BOOKMAN OLD STYLE",20)).place(x=50,y=160)
    Entry4 = ctk.CTkEntry(window2,textvariable=var3)
    Entry4.place(x=240,y=165)   
    ctk.CTkButton(window2,text='SUBMIT',
                  fg_color='#e68d07',
                  text_color='black',
                  hover_color='#c57600',
                  font=('bookman old style',18),
                  corner_radius=32,
                  command=inside_func).place(x=250,y=210)
    def on_closing():
        window2.destroy()
        window.deiconify()
        
    window2.protocol("WM_DELETE_WINDOW", on_closing)
    
    
def auth():
    global window
    window.withdraw()
    
    def inside_authfunc():
        
        global uname
        
        
        with open('user.csv', 'r') as userFile:
            reader = csv.reader(userFile)
            
            logname = var4.get()
            logpass = var5.get()
            
            for i in list(reader):
                if i[0] == logname:
                    if i[1] == logpass:
                        CTkMessagebox(title='Info',message='WELCOME',font=('BOOKMAN OLD STYLE',15),icon="check")
                        uname = logname
                        Entry6.delete(0, tk.END)
                        Entry5.delete(0, tk.END)
                        window3.destroy()
                        return options()
                        
                    else:
                        CTkMessagebox(title='Notification',message='Password is Incorrect',font=('BOOKMAN OLD STYLE',15),icon="warning")
                        window3.destroy()
                        return auth()
                 

            else:
                CTkMessagebox(title='Notification',message='User Not Found',font=('BOOKMAN OLD STYLE',15),icon="cancel")
                window3.destroy()
                return window.deiconify()
    
            
                    
                    


       
    global uname
    
    var4 = tk.StringVar()
    var5 = tk.StringVar()
    window3 = ctk.CTkToplevel(window)
    window3.grid()
    window3.title('LOGIN')
    window3.attributes('-topmost', 'true')
    window3.geometry('500x500')
    ctk.CTkLabel(window3,text='Enter username:',font=("BOOKMAN OLD STYLE",20)).place(x=55,y=150)
    Entry5 = ctk.CTkEntry(window3, textvariable=var4)
    Entry5.place(x=220,y=150)
    ctk.CTkLabel(window3,text='Enter password:',font=("BOOKMAN OLD STYLE",20)).place(x=55,y=200)
    Entry6 = ctk.CTkEntry(window3,textvariable=var5)
    Entry6.place(x=220,y=200)
    ctk.CTkButton(window3,
                   text='SUBMIT',
                   font=("BOOKMAN OLD STYLE",18),
                   fg_color='#e68d07',text_color='#121212', 
                   hover_color='#c57600',
                   corner_radius=32,
                   command=inside_authfunc).place(x=180,y=270)
    

    def on_closing():
        window3.destroy()
        window.deiconify()
        
    window3.protocol("WM_DELETE_WINDOW", on_closing)





def addExpense():
    global window,uname
    window4 = ctk.CTkToplevel(window)
    window4.title('ADD EXPENSE MENU')
    window4.geometry("500x500")
    window4.grid()
    window4.attributes('-topmost', 'true')
    date = tk.StringVar()
    expense_cat = tk.StringVar()
    description = tk.StringVar()
    expense = tk.StringVar()



    def submit_expenses():
        with open('expenses.csv','a', newline='') as expfile:
            csv.writer(expfile).writerow([uname,date.get(),expense_cat.get(),description.get(),expense.get()])
            CTkMessagebox(title='Notification',message="Expense added successfully.",font=('BOOKMAN OLD STYLE',15),icon='check')
            
            window4.destroy()
            


    date_label = ctk.CTkLabel(window4, text='Date:',font=("BOOKMAN OLD STYLE",20))
    date_label.place(x=50, y=100)
    date_entry = ctk.CTkEntry(window4, textvariable=date)
    date_entry.place(x=250, y=100)

    expcat_label = ctk.CTkLabel(window4, text='Expense Category:',font=("BOOKMAN OLD STYLE",20))
    expcat_label.place(x=20, y=130)
    expcat_entry = ctk.CTkEntry(window4, textvariable=expense_cat)
    expcat_entry.place(x=250, y=130)

    desc_label = ctk.CTkLabel(window4, text='Description:',font=("BOOKMAN OLD STYLE",20))
    desc_label.place(x=50, y=160)
    desc_entry = ctk.CTkEntry(window4, textvariable=description)
    desc_entry.place(x=250, y=160)

    exp_label = ctk.CTkLabel(window4, text='Expense:',font=("BOOKMAN OLD STYLE",20))
    exp_label.place(x=50, y=190)
    exp_entry = ctk.CTkEntry(window4, textvariable=expense)
    exp_entry.place(x=250, y=190)

    submit_button = ctk.CTkButton(window4,fg_color='#e68d07',font=("BOOKMAN OLD STYLE",18),text_color='#121212', hover_color='#c57600', command=submit_expenses, text='Submit',)
    submit_button.place(x=280, y=260)


    
    



def viewExpenses():
    global uname
    global window
    global window4
    window4.withdraw()
    lastx = tk.StringVar()
    window5 = ctk.CTkToplevel(window)
    window5.geometry("500x500")
    window5.grid()

    def fetch_expenses():
        try:
            count = int(lastx.get())
        except ValueError:
            CTkMessagebox(title="Error",message= "Please enter a valid number.",icon='warning')
            window5.destroy()
            return viewExpenses()

        with open('expenses.csv') as f:
            reader = csv.reader(f)
            reader = list(reader)[::-1]
            window8 = ctk.CTkToplevel(window5)
            window8.geometry("600x500")
            window8.attributes('-topmost', 'true')
            window8.title('Expenses')
            sb=ctk.CTkScrollbar(window8)
            output_text=ctk.CTkLabel(window8,text='Your expense(s) are systematically showcased in their designated order for your review',font=('bookman old style',13),wraplength=450)
            output_text.place(x=15,y=50)
            output_text2=ctk.CTkLabel(window8,text='USERNAME    DATE    EXPENSE_CATEGORY    DESCRIPTION    EXPENSE',font=('bookman old style',11))
            output_text2.place(x=15,y=100)
            tbox = ctk.CTkTextbox(window8,height=300,yscrollcommand=sb.set,width=600)
            tbox.grid(row=0,column=0,sticky='nsew')
            tbox.place(x=0,y=170)
            for i in reader:
                if count == 0:
                    break
                if i[0] == uname:
                    n =''
                    for j in i:
                        n+=j+'  '*6
                    tbox.insert('0.0','%s\n\n'%(n,))
                    count-=1

            tbox.configure(state=DISABLED)

    noexp_button = ctk.CTkLabel(window5, text="How many Expenses?:", font=("BOOKMAN OLD STYLE", 20))
    noexp_button.place(x=47, y=100)
    lastx_entry = ctk.CTkEntry(window5, textvariable=lastx)
    lastx_entry.place(x=270, y=100)
    fetch_button = ctk.CTkButton(window5, fg_color='#e68d07',font=("BOOKMAN OLD STYLE",18),text_color='#121212', hover_color='#c57600',text="Submit", command=fetch_expenses)
    fetch_button.place(x=280, y=260)

    def on_closing():
        window5.destroy()
        window4.deiconify()
    

    window5.protocol("WM_DELETE_WINDOW", on_closing)
            

def options():
    global window4
    
    window4 = ctk.CTkToplevel(window)
    window4.geometry('500x500')
    window4.title('Main Menu')
    

    label_main_menu = ctk.CTkLabel(window4,font=("BOOKMAN OLD STYLE",20),text='Main menu:')
    label_main_menu.place(x=190, y=70)

    btn_add_expense = ctk.CTkButton(window4, fg_color='#e68d07',font=("BOOKMAN OLD STYLE",18),text_color='#121212', hover_color='#c57600',text='Add Expense', command=addExpense)
    btn_add_expense.place(x=190, y=110)
    
    

    btn_logout = ctk.CTkButton(window4, fg_color='#e68d07',font=("BOOKMAN OLD STYLE",18),text_color='#121212', hover_color='#c57600', text='Logout', command=logout)
    btn_logout.place(x=190, y=190)
    btn_view_expenses = ctk.CTkButton(window4, fg_color='#e68d07',font=("BOOKMAN OLD STYLE",18),text_color='#121212', hover_color='#c57600',text='View Expenses', command=viewExpenses)
    btn_view_expenses.place(x=190, y=150) 

    def on_closing():
        window.destroy()
    window4.protocol("WM_DELETE_WINDOW", on_closing)

def logout():
    global uname
    global window4
    window4.destroy()
    uname = ''
    return window.deiconify()
