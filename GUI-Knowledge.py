from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

def Mymoney():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Mymoney)
B2.pack(ipadx=20,ipady=20)


GUI,mainloop()
