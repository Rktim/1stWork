import tkinter as tk

def on_button_click():
    print("Hi,myself Raktim kalita")
    
root = tk.Tk()
root.geometry("350x100")
button = tk.Button(root, text="Click it.", command=on_button_click,bg="blue",fg='yellow',font="Georiga")

button.pack()



root.mainloop()
