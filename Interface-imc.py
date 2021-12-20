import tkinter as tk
import tkinter.font as tkFont
from imccalc import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Calculadora IMC")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_344=tk.Entry(root)
        GLineEdit_344["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_344["font"] = ft
        GLineEdit_344["fg"] = "#333333"
        GLineEdit_344["justify"] = "center"
        GLineEdit_344["text"] = "Insira sua altura Ex. 1.72"
        GLineEdit_344.place(x=220,y=100,width=173,height=30)

        GLineEdit_708=tk.Entry(root)
        GLineEdit_708["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_708["font"] = ft
        GLineEdit_708["fg"] = "#333333"
        GLineEdit_708["justify"] = "center"
        GLineEdit_708["text"] = "Insira seu peso ex. 68"
        GLineEdit_708.place(x=220,y=190,width=173,height=30)

        GButton_228=tk.Button(root)
        GButton_228["activebackground"] = "#91c8f1"
        GButton_228["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_228["font"] = ft
        GButton_228["fg"] = "#000000"
        GButton_228["justify"] = "center"
        GButton_228["text"] = "Calcular"
        GButton_228.place(x=200,y=280,width=207,height=38)
        GButton_228["command"] = self.GButton_228_command

        GMessage_194=tk.Message(root)
        GMessage_194["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=12)
        GMessage_194["font"] = ft
        GMessage_194["fg"] = "#333333"
        GMessage_194["justify"] = "center"
        GMessage_194["text"] = "IMC"
        GMessage_194.place(x=200,y=20,width=210,height=30)

        GMessage_751=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_751["font"] = ft
        GMessage_751["fg"] = "#333333"
        GMessage_751["justify"] = "center"
        GMessage_751["text"] = "Resultado"
        GMessage_751.place(x=30,y=350,width=542,height=130)


    def GButton_228_command(self):
        print()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
