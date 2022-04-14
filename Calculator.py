import tkinter as tk
from tkinter import messagebox

win= tk.Tk()
win.title('CALCULATOR')   
win.geometry(f"265x275+100+200")    
win.resizable(False, False) 
win.config(bg='#717B7F')    
win.bind('<Key>, press_Key')

count = tk.Entry(win, justify=tk.RIGHT, font=('Agency FB',15),width=15)
count.insert(0,'0')
count.grid(row=0, column=0, columnspan=4, padx=5, stick='we')

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Agency FB', 13), fg='#4C4C54', command=lambda: add_operation(operation))

def make_culc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Agency FB', 18), fg='#4C4C54', command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Agency FB', 18), fg='#4C4C54', command=clear)

def press_Key(event):
    print(event.char)
    if event.char.isdiget():
        add_digit(event.char)  
    elif event.char in '+-*/':
        add_operation(event.char)     

def calculate():
    value = count.get()
    if value[-1] in '+-/*':
        value = value+value[:-1]
    count.delete(0, tk.END)
    try:
        count.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'ЦИФРЫ_ВВОДИ!!!')
        count.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'НА_НОЛЬ_ДЕЛИТЬ_НЕЛЬЗЯ!!!')
        count.insert(0, 0)

def add_digit(digit):
    value = count.get()
    if value[0]=='0'and len(value) == 1:
        value = value[1:]
    count.delete(0, tk.END)
    count.insert(0, value + str(digit))

def add_operation(operation):
    value = count.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = count.get()
    count.delete(0, tk.END)
    count.insert(0, value + operation)

def clear():
    count.delete(0, tk.END)
    count.insert(0, 0)

tk.Button(text = '1', bd=5, font=('Agency FB', 13), command=lambda: add_digit(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
tk.Button(text = '2', bd=5, font=('Agency FB', 13), command=lambda: add_digit(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
tk.Button(text = '3', bd=5, font=('Agency FB', 13), command=lambda: add_digit(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
tk.Button(text = '4', bd=5, font=('Agency FB', 13), command=lambda: add_digit(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
tk.Button(text = '5', bd=5, font=('Agency FB', 13), command=lambda: add_digit(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
tk.Button(text = '6', bd=5, font=('Agency FB', 13), command=lambda: add_digit(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
tk.Button(text = '7', bd=5, font=('Agency FB', 13), command=lambda: add_digit(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(text = '8', bd=5, font=('Agency FB', 13), command=lambda: add_digit(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(text = '9', bd=5, font=('Agency FB', 13), command=lambda: add_digit(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(text = '0', bd=5, font=('Agency FB', 13), command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_culc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('CE').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()