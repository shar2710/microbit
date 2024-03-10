from tkinter import Label, Tk 
import time
def current_time(): 
    string = time.strftime('%H:%M:%S %p')
    lbl.config(text = string) 
    lbl.after(1000, current_time)
root = Tk() 
root.title('Digital Clock') 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'purple', 
            foreground = 'white') 
lbl.pack(anchor = 'center') 
current_time() 
root.mainloop()
