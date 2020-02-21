from tkinter import *
from tkinter.ttk import Combobox
import os
import pickle

from tkinter import messagebox
"""Add employee."""
class add_employee:
    def __init__(self, window):
        self.wn = window
        self.wn.resizable(0, 0)
        self.wn.title('Employee Management System')
        self.wn.config(bg='black')
        self.wn.geometry("400x370")
        self.course = ["Java", "Python", "C & C++"]
        self.Employee_ID = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.address = StringVar()
        self.contact = StringVar()

        self.lb1 = Label(self.wn, text='Employee form', fg='yellow', bg='black', font=("bold", 20)).pack(fill=X)
        self.lb2 = Label(self.wn, text="Employee ID:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=60)
        self.lb3 = Label(self.wn, text="Name:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=100)
        self.lb4 = Label(self.wn, text="AGE:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=140)
        self.lb5 = Label(self.wn, text="Address:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=180)
        self.lb6 = Label(self.wn, text="Contact:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=220)
        self.lb7 = Label(self.wn, text="Department:", font=('bold', 15), fg='yellow', bg='black').place(x=70, y=260)
        self.e1 = Entry(self.wn, textvariable=self.Employee_ID)
        self.e1.place(x=210, y=63)
        self.e2 = Entry(self.wn, textvariable=self.name)
        self.e2.place(x=210, y=103)
        self.e3 = Entry(self.wn, textvariable=self.age)
        self.e3.place(x=210, y=143)
        self.e4 = Entry(self.wn, textvariable=self.address)
        self.e4.place(x=210, y=183)
        self.e5 = Entry(self.wn, textvariable=self.contact)
        self.e5.place(x=210, y=223)
        self.k = []
        try:
            with open('d.txt', 'rb') as file:
                self.lst = pickle.load(file)

            for i, j in self.lst:
                self.k.append(i)

            self.combo = Combobox(self.wn, values=self.k, width=18)
            self.combo.place(x=210, y=265)
"""Error handling."""
        except FileNotFoundError:
            self.combo = Combobox(self.wn, values=self.k, width=18)
            self.combo.place(x=210, y=265)

        self.bt1 = Button(self.wn, text='Back', width=7, height=1, command=self.quit, fg='yellow', bg='black').place(
            x=70, y=310)
        self.bt2 = Button(self.wn, text='Delete', width=7, height=1, command=self.ret, fg='yellow', bg='black').place(
            x=170, y=309)
        self.bt3 = Button(self.wn, text='Add More', width=7, height=1, command=self.addddd, fg='yellow', bg='black').place(
            x=270, y=307)
"""Delete data."""
    def ret(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)

"""Quit."""
    def quit(self):
        self.wn.withdraw()
"""Add."""
    def addddd(self):
        Cb = self.combo.get()
        Em = self.Employee_ID.get()
        Na = self.name.get()
        Ag = self.age.get()
        Ad = self.address.get()
        Ct = self.contact.get()

        if not Em or not Na or not Ag or not Ad or not Ct or not Cb:
            messagebox.showerror('Failed', 'All Field Required')

        else:
            self.Add_Emp = []
            if os.path.exists('E.txt'):
                with open('E.txt', 'rb') as D:
                    self.Add_Emp = pickle.load(D)
            self.Add_Emp.append([Em, Na, Ag, Ad, Ct, Cb])

            with open('E.txt', 'wb') as file1:

                pickle.dump(self.Add_Emp, file1)
            messagebox.showinfo('Success', 'Successfully Added')

        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
