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
# this is the current Error msg.
# ===== RESTART: C:\Users\storm\Documents\GitHub\Tkinter_qtNotepad\tab.py =====
# Traceback (most recent call last):
#   File "C:\Users\storm\Documents\GitHub\Tkinter_qtNotepad\tab.py", line 33, in <module>
#     main()
#   File "C:\Users\storm\Documents\GitHub\Tkinter_qtNotepad\tab.py", line 27, in main
#     B = tkinter.Button(top, text ="hello", command = the_box)
# NameError: name 'tkinter' is not defined
# >>> 
def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    B = tkinter.Button(top, text ="hello", command = the_box)
    B.pack()
    root.mainloop()
    

if __name__ == '__main__':
    main()
