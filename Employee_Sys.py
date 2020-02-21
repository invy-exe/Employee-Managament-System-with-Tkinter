from tkinter import*
import View_Employee

import Add_Emp

"""Main window."""
class Employee_sys:
    def __init__(self, window):
        self.wn= window
        self.wn.title('Employee system')
        self.wn.geometry('500x500')
        self.wn.config(bg='white')
        self.lb_heading = Label(self.wn, text='Employee Management System', font=('calibri', 18, 'bold'), bg='#000014', fg='yellow')
        self.lb_heading.place(x=0, y=0, relwidth=1)

        #Entry and Label

        self.lb_employee_form = Button(self.wn, text='Employee Form', font=('calibri', 12, 'bold'), command=self.employee_Form,fg='#f5f5f5', bg='black', width='35')
        self.lb_employee_form.place(x=80, y=80)

        
        self.lb_view_Form = Button(self.wn, text='View Employee', font=('calibri', 12, 'bold'), command=self.view_Form,fg='#f5f5f5', bg='black', width='35')
        self.lb_view_Form.place(x=80, y=140)
"""Employee Form."""
    def employee_Form(self):
        emq = Toplevel(self.wn)
        Add_Emp.add_employee(emq)


    
"""View Form."""
    def view_Form(self):
        abc = Toplevel(self.wn)
        View_Employee.view_employee(abc)
