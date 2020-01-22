from tkinter import *
import system

def initLabels(window):
    lbl = Label(window, text="PO System", font=("Arial Bold", 12)) 
    lbl.grid(column=0, row=0)

def initButtons(window):
    generatePOButton = Button(window, text="Generate PO", font=("Arial Bold", 12), command=buttonCallback)
    generatePOButton.grid(column=1, row=0)

def buttonCallback():
    system.generatePO()
    
def main():
    window = Tk()
    window.title("PO System")
    window.geometry('1000x500')

    initLabels(window)
    initButtons(window)

    window.mainloop()
    
if  __name__ == "__main__":
    main()
