#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import filedialog 
import tkinter.messagebox
import pandas as pd
import docx2txt
from shutil import copyfile

#This is the starting of the main window of the GUI
root= Tk()


#This is the function to browse any type of the file
def Browse_a_File():
    root.filename = filedialog.askopenfilename(title = "select a file", filetypes = (("word file","*.docx"),("word file","*.doc"),("Excel file","*.xls"),("Excel file","*.xlsx"),("Excel file","*.ods"),("CSV files","*.csv"),("CSV files","*.txt")))
    select_file = root.filename
    #To select the word file
    if select_file.endswith('.docx'):
        df = docx2txt.process(select_file)
        print(df)
    if select_file.endswith('.doc'):
        df = open(select_file,'r')
        df.read()
    #To select the excel file
    if select_file.endswith('.xls'):
        df = pd.read_excel(z)
        print(df)
    if select_file.endswith('.xlsx'):
        df = pd.read_excel(select_file)
        print(df)
    if select_file.endswith('.ods'):
        df = pd.read_excel(select_file)
        print(df)
   

    #To select the CSV file
    if select_file.endswith('.csv'):
        df = pd.read_csv(select_file)
        rows,columns = df.shape
        list_of_columns = list(df.columns)
        #null_rows = str(df[df.isnull().any(axis = 1)].sum())
        null_columns =str(df.isnull().sum())
        display = "Total no. of rows are : " + str(rows) + "\n\nTotal no. of columns are : " + str(columns) + "\n\nColumns having null values are : \n\n" + null_columns #+ "\n\nRows having null values are : " + null_rows
        tkinter.messagebox.showinfo('Information of the selected file',display)
        list_of_check =list(range(16384))
        for i in list_of_check:
            list_of_check[i] = "a" + str(list_of_check[i])
            
        #this function is to get the values of the checkboxes
        def get_values_of_checkedboxes():
            for i in range(len(list_of_columns)):
                print(list_of_check[i].get())
        
        
        #This function is used for further operation after selecting the columns
        def further_operation():
            confirm = tkinter.messagebox.askquestion("Are You Sure???", icon='warning')
            if confirm:
                file = filedialog.asksaveasfile(title = "Create a file", filetypes = (("word file","*.docx"),("word file","*.doc"),("Excel file","*.xls"),("Excel file","*.xlsx"),("Excel file","*.ods"),("CSV files","*.csv"),("CSV files","*.txt")))
                new_file = file.name
                #print(new_file)
                #This function is used to create a copy of the file
                copyfile(select_file ,new_file)
                df1 = pd.read_csv(new_file)
                for i in range(len(list_of_columns)):
                    if list_of_check[i].get() == 1:
                        df1.drop(list_of_columns[i],axis = 1,inplace = True)
                        df1.to_csv(new_file, index = False)
                
        #this function is to select the columns
        def select_columns():
            check_window = Toplevel()
            check_window.geometry("600x350+300+300")
            for i in range(len(list_of_columns)):
                list_of_check[i] = IntVar()
                Checkbutton(check_window, text = list_of_columns[i], variable = list_of_check[i],padx = 10, pady=10).grid(row = i, sticky=W)
            Button(check_window,text = "ok",command = further_operation,padx = 10, pady=10).grid(row = i+1, sticky =W)
            check_window.mainloop()
            
            
        select_button = Toplevel()
        select_button.geometry("600x350+300+300")
        select_column_button = Button(select_button,text = 'Select columns',command = select_columns,padx = 10, pady=10)
        select_column_button.pack()
        select_button.mainloop()
        
        
root.geometry("600x350+300+300")
button1=Button(root,text="choose a File",command=Browse_a_File,padx = 10, pady=10)
button1.pack()
root.mainloop()


# In[ ]:




