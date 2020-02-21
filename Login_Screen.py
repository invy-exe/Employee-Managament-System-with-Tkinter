from tkinter import *
import os
import Employee_Sys
"""Delete screen"""
def delete2():
    screen3.withdraw()
    ase= Toplevel(screen3)
    Employee_Sys.Employee_sys(ase)


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()

"""Login Success."""
def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess", font=('calibri', 11)).pack()
    Button(screen3, text="OK", command=delete2).pack()

"""Password not recognized error."""
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error", font=('calibri', 11)).pack()
    Button(screen4, text="OK", command=delete3).pack()

"""User not found error."""
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success", font=('calibri', 11))
    screen5.geometry("250x150")
    Label(screen5, text="User Not Found", font=('calibri', 11)).pack()
    Button(screen5, text="OK", bg="black", fg="yellow", command=delete4).pack()

"""User Registration."""
def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="yellow", font=("calibri", 11)).pack()

"""Verify Login."""
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()

"""Register."""
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("350x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below", fg="yellow", bg="black", font=('calibri', 11)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", fg="yellow", bg="black", width=10, height=1, command=register_user).pack()

"""Login."""
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login", fg="yellow", bg="black").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username", font=('calibri', 11)).pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password", font=('calibri', 11)).pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", fg="yellow", bg="black", font=('calibri', 11), width=10, height=1, command=login_verify).pack()

"""This is the main screen."""
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Employee Management System")
    Label(text="Employee Login and Registration", bg="black", fg="yellow", font=('calibri', 11), width="300", height="2").pack()
    Label(text="").pack()
    Button(text="Login", bg="black", fg="yellow", height="2", width="30", font=('calibri', 11), command=login).pack()
    Label(text="").pack()
    Button(text="Register", bg="black", fg="yellow", height="2", width="30", font=('calibri', 11), command=register).pack()

    screen.mainloop()


main_screen()
