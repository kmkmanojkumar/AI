
from tkinter import * #pip install tkinter
import tkinter as tk
 
 
root = Tk()
 
# specify size of window.
root.geometry("600x600")



def tk1(Fact):
    # Create text widget and specify size.
    T = Text(root, height = 12, width = 52,font =("Time to new roman", 20))
    
    # Create label
    l = Label(root, text = "Translator")
    l.config(font =("Time to new roman", 40))
    
  

    
    # Create an Exit button.
    
    b2 = Button(root, text = "Exit",
                command = root.destroy)
    
    l.pack()
    T.pack()
    b2.pack()
    
    # Insert The Fact.
    T.insert(tk.END, Fact)
    tk.mainloop()
