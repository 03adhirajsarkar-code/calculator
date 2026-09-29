import tkinter as tk
window=tk.Tk()
label=tk.Label(window, text="Calculator")
window.title("Calculator")
window.geometry("500x400")
window.config(bg="black")


entry = tk.Entry(window)
entry.pack()
def seven():
    entry.insert(tk.END, "7")

button7=tk.Button(window, text="7", command=seven,font=("arial",16))
button7.place(x=110, y=130, width=60, height=50)

def eight():
    entry.insert(tk.END, "8")

button8=tk.Button(window, text="8", command=eight,font=("arial",16))
button8.place(x=180, y=130, width=60, height=50)
def nine():
    entry.insert(tk.END, "9")

button9=tk.Button(window, text="9", command=nine,font=("arial",16))
button9.place(x=250, y=130, width=60, height=50)
def multiply():
    entry.insert(tk.END, "*")

buttonx=tk.Button(window, text="x", command=multiply,font=("arial",16))
buttonx.place(x=320, y=130, width=60, height=50)
def divide():
    entry.insert(tk.END, "/")

buttondivide=tk.Button(window, text="/", command=divide,font=("arial",16))
buttondivide.place(x=320, y=70, width=60, height=50)
def four():
    entry.insert(tk.END, "4")

button4=tk.Button(window, text="4", command=four,font=("arial",16))
button4.place(x=110, y=190, width=60, height=50)
def five():
    entry.insert(tk.END, "5")

button5=tk.Button(window, text="5", command=five,font=("arial",16))
button5.place(x=180, y=190, width=60, height=50)
def six():
    entry.insert(tk.END, "6")

button6=tk.Button(window, text="6", command=six,font=("arial",16))
button6.place(x=250, y=190, width=60, height=50)
def minus():
    entry.insert(tk.END, "-")

buttonminus=tk.Button(window, text="-", command=minus,font=("arial",16))
buttonminus.place(x=320, y=190, width=60, height=50)
def one():
    entry.insert(tk.END, "1")

button1=tk.Button(window, text="1", command=one,font=("arial",16))
button1.place(x=110, y=250, width=60, height=50)
def two():
    entry.insert(tk.END, "2")

button2=tk.Button(window, text="2", command=two,font=("arial",16))
button2.place(x=180, y=250, width=60, height=50)
def three():
    entry.insert(tk.END, "3")

button3=tk.Button(window, text="3", command=three,font=("arial",16))
button3.place(x=250, y=250, width=60, height=50)
def add():
    entry.insert(tk.END, "+")

buttonadd=tk.Button(window, text="+", command=add,font=("arial",16))
buttonadd.place(x=320, y=250, width=60, height=50)
def zerozero():
    entry.insert(tk.END, "00")

buttonzerozero=tk.Button(window, text="00", command=zerozero,font=("arial",16))
buttonzerozero.place(x=110, y=310, width=60, height=50)
def zero():
    entry.insert(tk.END, "0")

buttonzero=tk.Button(window, text="0", command=zero,font=("arial",16))
buttonzero.place(x=180, y=310, width=60, height=50)
def dot():
    entry.insert(tk.END, ".")

buttondot=tk.Button(window, text=".", command=dot,font=("arial",16))
buttondot.place(x=250, y=310, width=60, height=50)
def equals():
    data=entry.get()
    result=eval(data)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)

buttonequals=tk.Button(window, text="=", command=equals,font=("arial",16))
buttonequals.place(x=320, y=310, width=60, height=50)
def delete1():
    entry.delete(len(entry.get()) - 1, tk.END)

buttond=tk.Button(window, text="⌫", command=delete1,font=("arial",16))
buttond.place(x=110, y=70, width=60, height=50)
def deleteall():
    entry.delete(0, tk.END)

buttond2=tk.Button(window, text="AC", command=deleteall,font=("arial",16))
buttond2.place(x=180, y=70, width=60, height=50)
def percentage():
    entry.insert(tk.END,"*(0.01)")

buttonp=tk.Button(window, text="%", command=percentage,font=("arial",16))
buttonp.place(x=250, y=70, width=60, height=50)
button=[button3,button1,button6,button5,button4,button7,button8,button9,buttonzerozero,buttonzero,button2,buttondot]
for items in button:
    items.config(bg="darkgrey",fg="white")
buttonop=[buttondivide,buttonminus,buttonx,buttonadd,buttonequals]
for items in buttonop:
    items.config(bg="#FFBD66",fg="white") 
buttont=[buttond,buttond2,buttonp]   
for items in buttont:
    items.config(bg="#222222",fg="white")    
    






window.mainloop()
  