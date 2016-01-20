import tkinter


def the_box():
    new_window = tkinter.Toplevel()
    new_window.geometry("800x600+300+300")
    app = tkinter.Frame(new_window)
    app.pack()
    t = tkinter.Text(app)
    t.pack(fill = "both", expand = 1)
    B = tkinter.Button(text = "New Tab", command = the_box)
    B.pack(side = "top")
    new_window.mainloop()


def main():

    root = tkinter.Tk()
    root.geometry("800x600+300+300")
    app = tkinter.Frame(root)
    app.pack()
    t = tkinter.Text(app)
    t.pack(fill = "both", expand = 1)
    B = tkinter.Button(text = "New Tab", command = the_box)
    B.pack(side = "top")
    root.mainloop()
# The main problem seems to be defining the parent
# tried opening the new window as top level was unsuccessful
# This was most likely because it does not put it atop the widget hierarchy
# -------------------------------------------
# Opens tkinter with a textbox that resizes?
# button does not show above the textbox
# the_box needs to be reworked in such a way to make new
# tabs have the same contents as the main

if __name__ == '__main__':
    main()
