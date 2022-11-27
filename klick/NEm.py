from tkinter import *


wd = Tk()



def clicked():
    global click
    global a
    if click == 100000:
        lbl1.configure(text = '!!!!!!ПОБЕДА!!!!!!')
        click += a

    else:
        click += a
        lbl.configure(text  = click)
        lbl1.configure(text = '')
click = 0
a = 1
    

def clickas():
    global click
    global a
    if click >= 100:
        a = 10
        lbl1.configure(text = "Update (+10)")
    elif click < 100:
        lbl1.configure(text = "тебе нужно набрать 100 кликов")
def clicka():
    global click
    global a
    if click >= 100:
        a = 1
        lbl1.configure(text = "Update (-10)")
    elif click < 100:
        lbl1.configure(text = "тебе нужно набрать 100 кликов")

def clickbs():
    global click
    global a
    if click >= 1000:
        a = 100
        lbl1.configure(text = "Update (+100)")
    elif click < 1000:
        lbl1.configure(text = "тебе нужно набрать 1000 кликов")
def clickb():
    global click
    global a
    if click >= 1000:
        a = 10
        lbl1.configure(text = "Update (-100)")
    elif click < 1000:
        lbl1.configure(text = "тебе нужно набрать 1000 кликов")



def clickcs():
    global click
    global a
    if click >= 10000:
        a = 1000
        lbl1.configure(text = "Update (+1000)")
    elif click < 10000:
        lbl1.configure(text = "тебе нужно набрать 10000 кликов")
def clickc():
    global click
    global a
    if click >= 10000:
        a = 100
        lbl1.configure(text = "Update (-100)")
    elif click < 10000:
        lbl1.configure(text = "тебе нужно набрать 10000 кликов")




wd.title("Кликер")
wd.geometry('500x500')


lbl = Label(wd, text= '')
lbl.grid(column= 3, row = 3)

lbl1 = Label(wd, text= '')
lbl1.grid(column= 4, row = 4)


btn = Button(wd, text = "Нажимай", command=clicked , bg = 'red')
btn.grid(column= 0, row = 0)



btn1 = Button(wd, text= '+10', command=clickas, bg = 'blue', )
btn1.grid(column= 0, row= 6)
btn2 = Button(wd, text= '-10', command=clicka, bg = 'blue', )
btn2.grid(column= 0, row= 5)




btn3 = Button(wd, text= '+100', command=clickbs, bg = 'blue', )
btn3.grid(column= 1, row= 6)
btn4 = Button(wd, text= '-100', command=clickb, bg = 'blue', )
btn4.grid(column= 1, row= 5)

btn4 = Button(wd, text= '+1000', command=clickcs, bg = 'blue', )
btn4.grid(column= 2, row= 6)
btn5 = Button(wd, text= '-1000', command=clickc, bg = 'blue', )
btn5.grid(column= 2, row= 5)
wd.mainloop()