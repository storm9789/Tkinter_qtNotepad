import tkinter


def the_box():
    main()


def main():

    root = tkinter.Tk()
    root.geometry("250x150+300+300")
    app = tkinter.Frame(root)
    app.pack()
    t = tkinter.Text(app)
    t.pack(fill = "both", expand = 1)
    B = tkinter.Button(text = "New Tab", command = the_box)
    B.pack(side = "top")
    root.mainloop()

# Opens tkinter with a textbox that resizes?
# button does not show above the textbox
# the_box needs to be reworked in such a way to make new
# tabs have the same contents as the main

if __name__ == '__main__':
    main()
