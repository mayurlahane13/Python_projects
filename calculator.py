from tkinter import *
from tkmacosx import Button

root = Tk()
e = Entry(root, width =70, borderwidth = 7)
e.grid(row =0, column =0, columnspan = 4, padx= 10, pady = 10)

#operation = False
def button_click(number):
    #if not operation:
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    # else:
    #     current = e.get()
    #     e.delete(0, END)
    #     e.insert(0, str(number) + str(current))
    return

def button_clear():
    e.delete(0, END)
    return
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)
    return


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0,f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))
    return

button1 = Button(root, text = '1', padx = 30, pady = 20, command = lambda: button_click(1))
button2 = Button(root, text = '2', padx = 30, pady = 20, command = lambda: button_click(2))
button3 = Button(root, text = '3', padx = 30, pady = 20, command = lambda: button_click(3))
button4 = Button(root, text = '4', padx = 30, pady = 20, command = lambda: button_click(4))
button5 = Button(root, text = '5', padx = 30, pady = 20, command = lambda: button_click(5))
button6 = Button(root, text = '6', padx = 30, pady = 20, command = lambda: button_click(6))
button7 = Button(root, text = '7', padx = 30, pady = 20, command = lambda: button_click(7))
button8 = Button(root, text = '8', padx = 30, pady = 20, command = lambda: button_click(8))
button9 = Button(root, text = '9', padx = 30, pady = 20, command = lambda: button_click(9))
button0 = Button(root, text = '0', padx = 30, pady = 20, command = lambda: button_click(0))
button_dot = Button(root, text = '.', padx = 30, pady = 20, command = lambda: button_click())
button_equals = Button(root, text = '=', padx = 30, pady = 20, command = lambda: button_equal())
button_add = Button(root, text = '+', padx = 25, pady = 17, command = button_add)
button_sub = Button(root, text = '-', padx = 25, pady = 17, command = lambda: button_subtract())
button_mul = Button(root, text = '*', padx = 25, pady = 17, command = lambda: button_multiply())
button_div = Button(root, text = '/', padx = 25, pady = 17, command = lambda: button_divide())
button_clr = Button(root, text = 'AC', padx = 25, pady = 17, command = button_clear)


button1.grid(row= 1, column = 0)
button2.grid(row= 1, column = 1)
button3.grid(row= 1, column = 2)

button4.grid(row= 2, column = 0)
button5.grid(row= 2, column = 1)
button6.grid(row= 2, column = 2)

button7.grid(row= 3, column = 0)
button8.grid(row= 3, column = 1)
button9.grid(row= 3, column = 2)

button0.grid(row= 4, column = 1)
button_dot.grid(row= 4, column = 0)
button_equals.grid(row= 4, column = 2)

button_add.grid(row= 1, column = 3)
button_sub.grid(row= 2, column = 3)
button_mul.grid(row= 3, column = 3)
button_div.grid(row= 4, column = 3)
button_clr.grid(row= 5, column = 3)




root.mainloop()

