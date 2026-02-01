import tkinter as tk

window=tk.Tk()
window.title("Tkinter App")

lable=tk.Label(text="WLCOME TO ATM",font=("Arial",24,"bold"),fg="blue"    )
lable.pack()  
     
pin=int(input("enter the pin"))

window.minsize(width=400,height=300)
window.mainloop()