from tkinter import *
import pickle
"""Main employee view and error handling."""
class view_employee:
    def __init__(self, window):
        self.wn = window
        self.wn.config(bg='black')
        self.wn.resizable(0, 0)
        self.wn.geometry("880x500")
        self.wn.title("View")
        Label(self.wn, text="Name", font=("Bold", 13), bg='black', fg='yellow').place(x=30, y=0)
        Label(self.wn, text="Employee ID", font=("Bold", 13), bg='black', fg='yellow').place(x=140, y=0)
        Label(self.wn, text="AGE", font=("Bold", 13), bg='black', fg='yellow').place(x=300, y=0)
        Label(self.wn, text="Address", font=("Bold", 13), bg='black', fg='yellow').place(x=400, y=0)
        Label(self.wn, text="Contact", font=("Bold", 13), bg='black', fg='yellow').place(x=540, y=0)
        Label(self.wn, text="Department", font=("Bold", 13), bg='black', fg='yellow').place(x=680, y=0)
        try:
            with open('E.txt', 'rb') as file:
                self.lst = pickle.load(file)
            if not self.lst:
                Label(self.wn, text="No any Entries! Please Add some entries and come back again",
                      font=("Bold", 13), bg='black', fg='yellow').place(x=200, y=100)
            else:
                place = 30
                for i, j, k, l, m, n in self.lst:
                    Label(self.wn, text=j, font=("Bold", 13), bg='black', fg='yellow').place(x=30, y=place)
                    Label(self.wn, text=i, font=("Bold", 13), bg='black', fg='yellow').place(x=140, y=place)
                    Label(self.wn, text=k, font=("Bold", 13), bg='black', fg='yellow').place(x=300, y=place)
                    Label(self.wn, text=l, font=("Bold", 13), bg='black', fg='yellow').place(x=400, y=place)
                    Label(self.wn, text=m, font=("Bold", 13), bg='black', fg='yellow').place(x=540, y=place)
                    Label(self.wn, text=n, font=("Bold", 13), bg='black', fg='yellow').place(x=680, y=place)
                    place = place + 30
        except FileNotFoundError:
            Label(self.wn, text="Entries not found",font=("Bold", 13), bg='black', fg='yellow').place(x=300, y=100)
