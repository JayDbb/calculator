import tkinter
from tkinter import font



calculator = tkinter.Tk(screenName=None, baseName=None, className='Calculator', useTk=1)

calculator.geometry('150x250')
# def animation():
    
#     clown = tkinter.PhotoImage(file='clown.png')
#     image = canvas.create_image(0,0, image=clown, anchor= 'n')
# canvas = tkinter.Canvas(calculator, width=WIDTH, height=HEIGHT, background='#000')
# animation()
equation = tkinter.Entry(calculator, fg='white', bg='#38b789', cursor='arrow', font=('Monospace'))
equation.grid(columnspan =20, row=0,rowspan=1, sticky='nesw' )
calculator.rowconfigure(0,weight=1)
calculator.columnconfigure(0,weight=1)
calculator.rowconfigure(1,weight=1)
calculator.columnconfigure(1,weight=1)
calculator.rowconfigure(2,weight=1)
calculator.columnconfigure(2,weight=1)
calculator.rowconfigure(3,weight=1)
calculator.columnconfigure(3,weight=0)
calculator.rowconfigure(4,weight=1)
calculator.columnconfigure(4,weight=1)
def errorclear():
    if ('error' in (tkinter.Entry.get(equation))):
        equation.delete(0,'end')

def one():
    global one
    one = 1
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,1)
    
    
frame=tkinter.Frame(calculator)
# frame.pack()


button_one = tkinter.Button( text='1', width=10, command=one, relief='flat', bg='#2b2b2b', fg='white')
button_one.grid(column=0, row=1,sticky='nesw')
def two():
    global two
    two = 2
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,2)
    
button_two = tkinter.Button( text='2', width=10, command=two, relief='flat', bg='#2b2b2b', fg='white')
button_two.grid(column=1, row=1,sticky='nesw')

def three():
    global three
    three = 3
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,3)
    
button_three = tkinter.Button( text='3', width=10, command=three, relief='flat', bg='#2b2b2b', fg='white')
button_three.grid(column=2, row=1,sticky='news')

def four():
    global four
    four = 4
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,4)
    
button_four = tkinter.Button( text='4', width=10, command=four, relief='flat', bg='#2b2b2b', fg='white')
button_four.grid(column=0, row=2,sticky='news')

def five():
    global five
    five = 5
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,5)
    
button_five = tkinter.Button( text='5', width=10, command=five, relief='flat', bg='#2b2b2b', fg='white')
button_five.grid(column=1, row=2,sticky='news')

def six():
    global six
    six = 6
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,6)
    
button_six = tkinter.Button( text='6', width=10, command=six, relief='flat', bg='#2b2b2b', fg='white')
button_six.grid(column=2, row=2,sticky='news')

def seven():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,7)
  
button_seven = tkinter.Button( text='7', width=10, command=seven, relief='flat', bg='#2b2b2b', fg='white')
button_seven.grid(column=0, row=3,sticky='news')

def eight():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,8)

button_eight = tkinter.Button( text='8', width=10, command=eight, relief='flat', bg='#2b2b2b', fg='white')
button_eight.grid(column=1, row=3,sticky='news')

def nine():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,9)

button_nine = tkinter.Button( text='9', width=10, command=nine, relief='flat', bg='#2b2b2b', fg='white')
button_nine.grid(column=2, row=3,sticky='nesw')

def zero():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,0)

button_zero = tkinter.Button( text='0', width=10, command=zero, relief='flat', bg='#2b2b2b', fg='white')
button_zero.grid(column=1, row=4,sticky='news')

def plus():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,'+')

button_plus = tkinter.Button( text='+', width=10, command=plus, relief='flat', bg='#2b2b2b', fg='white')
button_plus.grid(column=4, row=1,sticky='nesw')

def minus():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,'-')

button_minus = tkinter.Button( text='-', width=10, command=minus, relief='flat', bg='#2b2b2b', fg='white')
button_minus.grid(column=4, row=2,sticky='nesw')

def divide():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,'/')

button_divide = tkinter.Button( text='/', width=10, command=divide, relief='flat', bg='#2b2b2b', fg='white')
button_divide.grid(column=4, row=4,sticky='news')

def multiply():
    errorclear()
    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,'*')

button_multiply = tkinter.Button( text='*', width=10, command=multiply, relief='flat', bg='#2b2b2b', fg='white')
button_multiply.grid(column=4, row=3,sticky='nesw')

def clear():

    equation.delete(0,'end')

button_clear = tkinter.Button( text='clear', width=10, command=clear, relief='flat', bg='#2b2b2b', fg='white')
button_clear.grid(column=0, row=4,sticky='nesw')

def backspace():

    characters = len(tkinter.Entry.get(equation))
    fwdcharacter = characters-1
    equation.delete(fwdcharacter, 'end')

button_back = tkinter.Button( text='del', width=10, command=backspace, relief='flat', bg='#2b2b2b', fg='white')
button_back.grid(column=2, row=4,sticky='nesw')
answer= ""

def enter():
    
    characters = len(tkinter.Entry.get(equation))
    try:
        answer = float(eval(tkinter.Entry.get(equation)))
    except:
        answer='error'
    answer=str(answer)
    try:
        num =answer.split('.')
    except:
        answer =answer
            
    if answer == 'error':
        equation.delete(0,'end')
        equation.insert(characters, 'error')
    elif num[1] == '0':
        fwdcharacter = characters-1
        equation.delete(0,'end')
        equation.insert(characters, num[0])
        equation.delete(fwdcharacter, 'end')
        
    else:
        equation.delete(0,'end')
        equation.insert(characters, answer)


    
    return enter

def brac():

    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,'(')

button_brac = tkinter.Button( text='(', width=10, command=brac, relief='flat', bg='#2b2b2b', fg='white')
button_brac.grid(column=4, rowspan=2,sticky='news')

def brac2():

    characters = len(tkinter.Entry.get(equation))
    equation.insert(characters,')')

button_brac2 = tkinter.Button( text=')', width=10, command=brac2, relief='flat', bg='#2b2b2b', fg='white')
button_brac2.grid(column=4, rowspan=2,sticky='news')

button_enter = tkinter.Button( text='''=''', width=20,height=2, command =enter, relief='flat', bg='#2b2b2b', fg='white')
button_enter.grid(columnspan=4, row=5,rowspan=200,sticky='news')


# frame.pack(calculator,expand=True)
def resize(e):
    width = e.width /15
    button_one.config(font=('Monospace', int(width)))
    button_two.config(font=('Monospace', int(width)))
    button_three.config(font=('Monospace', int(width)))
    button_five.config(font=('Monospace', int(width)))
    button_four.config(font=('Monospace', int(width)))
    button_six.config(font=('Monospace', int(width)))
    button_seven.config(font=('Monospace', int(width)))
    button_eight.config(font=('Monospace', int(width)))
    button_nine.config(font=('Monospace', int(width)))
    button_zero.config(font=('Monospace', int(width)))
    button_plus.config(font=('Monospace', int(width)))
    button_minus.config(font=('Monospace', int(width)))
    button_multiply.config(font=('Monospace', int(width)))
    button_divide.config(font=('Monospace', int(width)))
    button_brac.config(font=('Monospace', int(width)))
    button_brac2.config(font=('Monospace', int(width)))
    button_enter.config(font=('Monospace', int(width)))
    button_back.config(font=('Monospace', int(width)))
    button_clear.config(font=('Monospace', int(width/2)))
    equation.config(font=('Monospace', int(width)))




calculator.bind('<Configure>', resize)

equation.delete(0,'end')
calculator.mainloop()
