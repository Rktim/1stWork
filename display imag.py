from tkinter import*
from tkinter import PhotoImage
pho= Tk()
pho.geometry("500x700")
pho.title('rk')
im=PhotoImage(file=r"C:\Users\raktm\OneDrive\Pictures\Screenshot (17).png")
x=Label(pho,image=im)
x.place(relheight=1,relwidth=1)


txt_l= Label(pho,text="what's up",font=("Georgia",24))
txt_l.pack()

def bt():
    print('yoo')
pho.geometry('350x160')
button=Button(pho,text='click it',command=bt,bg='lightblue',font="Arial")
button.pack()
    






pho.mainloop()
