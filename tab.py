from tkinter import *


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")

        self.parent = parent

        self.initUI()


    def initUI(self):

        self.parent.title("Simple")
        self.pack(fill = BOTH, expand = 1)

def the_box():
    tkMessageBox.showinfo("ERROR!!!!!!", "Wazzzaaa!")

def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    B = tkinter.Button(top, text ="hello", command = the_box)
    B.pack()
    root.mainloop()
    

if __name__ == '__main__':
    main()
