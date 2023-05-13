from tkinter import *

root = Tk()
#Creating objects
box = Entry(root,width=60,borderwidth=5)
root.configure(bg="grey45")
box.grid(row = 0, column = 0, columnspan=3,padx=10,pady=10)

def add_no():
    global temp
    global operator
    operator = "+"
    temp = int(box.get())
    clear_board()
    
def multi_no():
    global temp
    global operator
    operator = "x"
    temp = int(box.get())
    clear_board()

def divide_no():
    global temp
    global operator
    operator = "/"
    temp = int(box.get())
    clear_board()

def sub_no():
    global temp
    global operator
    operator = "-"
    temp = int(box.get())
    clear_board()
    
def clear_board():
    box.delete(0,END)
    
def get_number(num):
    num1=str(num)
    newnum = str(box.get())+num1
    box.delete(0,END)
    box.insert(0,newnum)

def equals_to():
    new = int(box.get())
    box.delete(0,END)
    if (operator == '+'):
        sum = temp+new
        box.insert(0,sum)
    elif(operator == '-'):
        minus = temp-new
        box.insert(0,minus)
    elif(operator == 'x'):
        multi = temp*new
        box.insert(0,multi)
    else:
        div = temp/new
        box.insert(0,div)
    

button1 = Button(root,text="9",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(9))
button2 = Button(root,text="8",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(8))
button3 = Button(root,text="7",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(7))

button4 = Button(root,text="6",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(6))
button5 = Button(root,text="5",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(5))
button6 = Button(root,text="4",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(4))

button7 = Button(root,text="3",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(3))
button8 = Button(root,text="2",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(2))
button9 = Button(root,text="1",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(1))

button0 = Button(root,text="0",bg="azure4",fg="black",padx=40,pady=20,command = lambda: get_number(0))

#operators
add = Button(root, text="+",bg="azure4",fg="black",padx=39,pady=20,command=add_no)
minus = Button(root, text="-",bg="azure4",fg="black",padx=41,pady=20,command=sub_no)
multi = Button(root, text="x",bg="azure4",fg="black",padx=40,pady=20,command=multi_no)
div = Button(root, text="/",bg="azure4",fg="black",padx=40,pady=20,command=divide_no)
equal = Button(root, text="=",bg="red",padx=40,pady=50,command = equals_to)
clear = Button(root, text="Clear",bg="red",padx=30,pady=50,command=clear_board)


#putting objects on screen
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)

add.grid(row=5,column=0)
minus.grid(row=4,column=1)
multi.grid(row=4,column=2)
div.grid(row=6,column=0)
equal.grid(row=5,column=2,rowspan=2)
clear.grid(row=5,column=1,rowspan=2)

root.resizable(False,False)
root.mainloop()
