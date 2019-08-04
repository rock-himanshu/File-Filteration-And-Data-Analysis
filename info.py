#This function is used for further operation after selecting the columns

# from __main__ import *
import pandas as pd
from functools import partial
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import *
# list_of_columns= []
select_columns= []
list_of_check=[]
i=0

def further_operation():
     confirm =messagebox.askquestion("Are You Sure???", icon='warning')
     if confirm=='yes':
         file = filedialog.asksaveasfile(title = "Create a file", filetypes = (("word file","*.docx"),("word file","*.doc"),("Excel file","*.xls"),("Excel file","*.xlsx"),("Excel file","*.ods"),("CSV files","*.csv"),("CSV files","*.txt")))
         print(file)
         new_file = file.name

         #This function is used to create a copy of the file
         copyfile(select_file ,new_file)
         df1 = pd.read_csv(new_file)
         for i in range(len(list_of_columns)):
             if list_of_check[i].get() == 1:
                 df1.drop(list_of_columns[i],axis = 1,inplace = True)
                 df1.to_csv(new_file, index = False)

#this function is to get the values of the checkboxes
def get_values_of_checkedboxes():
    for i in range(len(list_of_columns)):
        print(list_of_check[i].get())

#this function is to select the columns
def select_columns(list_of_columns):
    # i=10
    for i in list_of_columns:
        print(i)
    check_window = Toplevel()
    check_window.geometry("600x350+300+300")
    for i in range(len(list_of_columns)):
        # list_of_check[i] = IntVar()
        Checkbutton(check_window, text = list_of_columns[i], variable = list_of_check[i],padx = 10, pady=10).grid(row = i, sticky=W)
    Button(check_window,text = "ok",command = further_operation,padx = 10, pady=10).grid(row = i+1, sticky =W)
    check_window.mainloop()

def next_window(filename):
    if filename.endswith('.docx'):
        df = docx2txt.process(filename)
        print(df)
    if filename.endswith('.doc'):
        df = open(filename,'r')
        df.read()
    if filename.endswith('.xls'):
        df = pd.read_excel(filename)
        print(df)
    if filename.endswith('.xlsx'):
        df = pd.read_excel(filename)
        print(df)
    if filename.endswith('.ods'):
        df = pd.read_excel(filename)
        print(df)
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
        rows,columns = df.shape
        list_of_columns = list(df.columns)
        #null_rows = str(df[df.isnull().any(axis = 1)].sum())
        null_columns =str(df.isnull().sum())
        display = "Total no. of rows are : " + str(rows) + "\n\nTotal no. of columns are : " + str(columns) + "\n\nColumns having null values are : \n\n" + null_columns #+ "\n\nRows having null values are : " + null_rows
        messagebox.showinfo('Information of the selected file',display)
        print("\n\n")
        print(filename)
        print("\n\n")
        list_of_check =list(range(16384))
        for i in list_of_check:
            list_of_check[i] = "a" + str(list_of_check[i])
            # print(list_of_check[i])


    select_button = Toplevel()
    select_button.geometry("600x350+300+300")
    L_1=Label(select_button,text="Remove options")
    L_1.pack()
    # list_of_columns  = []
    select_column_button = Button(select_button,text = 'Select columns',command =partial(select_columns,list_of_columns),padx = 10, pady=10)
    select_column_button.pack()
    select_button.mainloop()
