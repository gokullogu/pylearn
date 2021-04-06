import tkinter as tkr
import tkinter.messagebox as tkmsg
w=tkr.Tk()

w.title("welcome")


lb=tkr.Label(w,text="hello world !").pack()


def helloCallBack():
   tkmsg.showinfo("Hello Python", "Hello World")


B = tkr.Button(w, text="Hello", command=helloCallBack,bg='pink')

B.pack()

w.mainloop()
