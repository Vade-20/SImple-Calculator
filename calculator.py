from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, fg='red', width=45, bg='black', font=('Times','30'), borderwidth=25, justify=RIGHT, )
e.grid(row=0, column=0, columnspan=4)
root.config(bg = 'black')
root.iconbitmap('Simple-Calculator\\system_application_calculator_13032.ico')

def check(keys): #check where the entered value in the entery box is a valid input if not it prevent the invalid input to be entered
    if str(keys.char).isdigit():
        number(keys.char)
    elif keys.char in ['+','-','/','*','(',')','[',']','.'] :
        number(keys.char)
    elif str(keys.char).isalpha():
        number(keys.char)
        back()
        from tkinter import messagebox
        messagebox.showerror('Error', 'Non-numerical value added in calculator')
    else:
        pass


def number(n): #enter the value inside the entery box
    a = e.get()
    a1 = len(a) - 1
    a = a + str(n)
    clear()
    e.insert(a1, a)


def clear(n=None): #empty the entry box
    e.delete(0, END)


def back(n=None): #delete the last character from entery box 
    a = e.get()
    a1 = len(a)-1
    e.delete(a1, END)

def equal(n=None): #Give us the output
    try:
        a = e.get()
        a = eval(a)
        a = round(a, 2)
        clear()
        e.insert(0, a)
    except SyntaxError:
        from tkinter import messagebox
        messagebox.showerror('Error', 'Syntax Error')
    except NameError:
        from tkinter import messagebox
        messagebox.showerror('Error', 'Non-numerical value added in calculator')


def change(): #changes the integer into positive or negative
    a = e.get()
    a = list(a)
    b = ['-']
    if a[0] != '-':
        for i in a:
            b.append(i)
        b = ''.join(b)
        e.delete(0, END)
        e.insert(0, b)
    else:
        a.pop(0)
        a = ''.join(a)
        e.delete(0, END)
        e.insert(0, a)


root.bind('<Key>',check)
root.bind('<Return>',equal)
root.bind('<BackSpace>',back)
root.bind('<Shift>')
root.bind('<Escape>',clear)

Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=clear,
       text='Clear').grid(row=1, column=0,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=equal,
       text='=').grid(row=5, column=1,columnspan=2,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=back,
       text='<--').grid(row=1, column=3,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(1),
       text='1').grid(row=4, column=0,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(2),
       text='2').grid(row=4, column=1,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(3),
        text='3').grid(row=4, column=2,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(4),
       text='4').grid(row=3, column=0,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(5),
       text='5').grid(row=3, column=1,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(6),
       text='6').grid(row=3, column=2,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(7),
       text='7').grid(row=2, column=0,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(8),
       text='8').grid(row=2, column=1,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number(9),
       text='9').grid(row=2, column=2,sticky=W+E)

Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number('+'),
       text='+').grid(row=2, column=3,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number('-'),
       text='-').grid(row=3, column=3,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number('*'),
       text='*').grid(row=4, column=3,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda: number('/'),
       text='/').grid(row=5, column=3,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda:number('0'),
       text='0').grid(row=5, column=0,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=lambda:number('.'),
       text='.').grid(row=1, column=2,sticky=W+E)
Button(root, fg='red', bg='black', font=('Times', '20'), width=10, borderwidth=20, justify=RIGHT, command=change,
       text='+/-').grid(row=1, column=1,sticky=W+E)
root.mainloop()
