from tkinter import *

def initLabels(window):
    lbl = Label(window, text="Hello", font=("Arial Bold", 20)) 
    lbl.grid(column=0, row=0)

def initButtons(window):
    btn = Button(window, text="Click Me", font=("Arial Bold", 20))
    btn.grid(column=1, row=0)

def main():
    window = Tk()
    window.title("PO System")
    window.geometry('1000x500')

    initLabels(window)
    initButtons(window)

    window.mainloop()
    
if  __name__ == "__main__":
    main()
