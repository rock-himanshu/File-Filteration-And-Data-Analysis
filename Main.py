from tkinter import *
from tkinter import filedialog
import os
import tkinter.messagebox as messagebox
import pandas as pd
# import config
from info import *

#Global variable
flag=0
filename=''

#function library
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.grid()

def about_us():
    messagebox.showinfo('About ONGC:File handling','This is File filter software, Developed for ONGC.');

def contact_us():
    messagebox.showinfo('Contact us','This software is developed at ONGC-Dehradun using python .\n Contribution: @Himanshu Agarwal, @Aman Agarwal, @Archit Singh, @Abhishek Bartwal, @shivam Kimothi, @Jazz\n Mentor:Himanshu Gupta');

def exit_button():
   exit();

def next_btn():
    global filename
    if flag==1:
        next_window(filename)
    else:
        messagebox.showerror('Upload File','Please select/Upload a File.')


def choose_file():
    global flag
    global filename
    filename=filedialog.askopenfilename()
    f_name=os.path.basename(filename) #file name only
    File_Name.set(f_name)

    if filename.endswith('.docx'):
       messagebox.showinfo('Upload File','DOCX File is selected.\n Click Next to Continue.');
       flag=1

    elif filename.endswith('.doc'):
       messagebox.showinfo('Upload File','DOC File is selected.\n Click Next to Continue.');
       flag=1
    elif filename.endswith('.txt'):
       messagebox.showinfo('Upload File','TXT File is selected.\n Click Next to Continue.');
       flag=1
    elif filename.endswith('.xls'):
       messagebox.showinfo('Upload File','XLS File is selected.\n Click Next to Continue.');
       flag=1

    elif filename.endswith('.xlsx'):
       messagebox.showinfo('Upload File','XLSL File is selected.\n Click Next to Continue.');
       flag=1

    elif filename.endswith('.ods'):
       messagebox.showinfo('Upload File','ODS File is selected.\n Click Next to Continue.');
       flag=1
    elif filename.endswith('.csv'):
       messagebox.showinfo('Upload File','CSV File is selected.\n Click Next to Continue.');
       flag=1
    elif filename.endswith('.csv'):
       messagebox.showinfo('Upload File','CSV File is selected.\n Click Next to Continue.');
       flag=1
    else:
       messagebox.showerror('Upload File','Please Try again.\nInvalid File is selected.');
       flag=0
    return
    #print(filename)
    #address.set((string)filename)


#general Settings
title="ONGC:File Handling"
text="#f0f0f0"
font=""
size="500x400"
background=""
length=700
width=700

#root window
window=Tk()

#images
icon=PhotoImage(file='images//background.png')
upload=PhotoImage(file='images//upload.png')

#window page-1
window.iconbitmap(r'images//icon.ico')
window.title(title)
#window.color=bg="#ffffff"
window.geometry(size)
window.resizable(width=False, height=False)
#window division
window_body = Frame(window)#,bg="#d5e5e2")
window_bottom = Frame(window, height=8)#,bg="#a0a5a4")
window_body.pack(fill='both',expand=True,)
window_bottom.pack(fill='both')

r=0
c=0

# window menubar
menubar = Menu(window)

# sub-menu:File
fileMenu = Menu(menubar, tearoff=0)
# File toggle button
fileMenu.add_command(label="New project", command=donothing)
fileMenu.add_command(label="Save",command=donothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exit_button)
menubar.add_cascade(label="File",menu=fileMenu)
# Help toggle button
helpMenu=Menu(menubar, tearoff=0)
helpMenu.add_command(label="Verson",command=donothing)
helpMenu.add_command(label="About Us",command=about_us)
helpMenu.add_command(label="Contact Us",command=contact_us)
menubar.add_cascade(label="About",menu=helpMenu)
window.config(menu=menubar)

#window Body

P_1= Label(window_body, image=icon)
P_1.grid(sticky=E+W+S+N)

H_1=Label(window_body,text="Welcome To ONGC")
H_1.grid(column=c+1,row=r)

L_1=Label(window_body,text="Upload File")
L_1.grid(column=c,row=r+3)

File_Name=StringVar()
File_Name.set("Please select a file")
flag=0
E_1=Entry(window_body,textvariable=File_Name,state='disabled',fg='#000000')
E_1.grid(column=c+1, row=r+3,sticky=W)

upload=PhotoImage(file='images//upload.png')
B_1=Button(window_body,image=upload,command=choose_file)#text="choose file",bg="#ffffff")
B_1.grid(column=c+4, row=r+3)

B_2=Button(window_body,text=">> Next >>",command=next_btn)
B_2.grid(column=c+1,row=r+4,columnspan = 2,padx=2,pady=2, sticky=E+W)

#canvas=Canvas.create_line(15, 25, 200, 25)
#canvas.pack()

foot_1=Label(window_bottom,text="Copyright© 2019 by Hianshu Agarwal. All rights reserved under ONGC.")
foot_1.grid(columnspan=3,sticky=E)

window.mainloop()



# create entry field
#----------------------------------
# text_field=Text(master=window, height=10 ,wdth=30)
# text_field.grid()

# Create slider
#----------------------------------
#S_1=Scale(window,from=0,to=100,orient=HORIZONTAL)

# add text to text box
#----------------------------------
#g_d=tk.Text(master=window, height= 10, width=10)
#g_d.grid()
#g_d.inster(tk.END,greeting)

#insert image
#----------------------------------
#ph=PhotoImage(file='background.png')
#labelphoto= Label(window, image=ph)
#labelphoto.pack()


#image link
#-----------------------------------
#https://www.flaticon.com/free-icon/data_1767086
#https://www.youtube.com/watch?v=UxSeMIBCKP0&list=PLhTjy8cBISEp6lNKUO3iwbB1DKAkRwutl&index=11

#Grid option attributes
#------------------------------------
#http://effbot.org/tkinterbook/grid.htm
