from tkinter import *
A=Tk()
B=Canvas(A)
B.place(x=0,y=0,height=256,width=256)
for a in range(256):
    for b in range(256):
        B.create_line(a,b,a+1,b+1,fill=pyList[a][b])#where pyList is a matrix of hexadecimal strings
A.geometry("256x256")
mainloop()
