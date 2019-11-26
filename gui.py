from tkinter import *
from tkinter import filedialog
from assembler import open_file
import tkinter as tk
from tkinter import ttk


def sel_file():

    file = filedialog.askopenfile(initialdir="/", title="select file",
                                    filetypes=(("text files", ".txt"), ("all files", "*.*")))
    open_file(file)
    with open("data_mem.txt", "r") as file:
        data={}
        data = file.read()
        T = tk.Text(root, height=10, width=25)
   # T.pack()
        T.grid(row=5, column=3, pady=10)
        T.insert( 1.0, data)
        print("1")

        with open("reg_file.txt", "r") as file:
    
            data1={}
            data1 = file.read()
            T = tk.Text(root, height=10, width=25)
            T.grid(row=10, column=7, pady=10)
            T.insert( 1.0, data1)
            
            with open("inst_mem.txt", "r") as file:
                data2={}
                data2 = file.read()
                T = tk.Text(root, height=10, width=25)
                T.grid(row=25, column=11, pady=10)
                T.insert( 1.0, data2)
                print("1")



root = Tk()

Button(root, text="open file", command=sel_file).grid(row=0,column=3,sticky=W)
#button.pack()
root.geometry("1000x500")





root.mainloop()