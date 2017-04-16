from Tkinter import *
from tkMessageBox import *
import tkFileDialog

class Files(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Text Editor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        aboutMenu = Menu(menubar)
        fileMenu.add_command(label="Save", command = self.save_command)
        fileMenu.add_command(label="Open", command = self.onOpen)
        fileMenu.add_command(label="Exit", command=self.exit)
        aboutMenu.add_command(label="About the Software", command=self.popUp)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label = "About", menu=aboutMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def popUp(self):
        showinfo("About the software", "This software was developed by Vishal...")

    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

    def save_command(self):
        file = tkFileDialog.asksaveasfile(mode='w')
        if file != None:
                data = self.txt.get('1.0', END+'-1c')
                file.write(data)
                file.close()
    def exit(self):
        root.quit()

root = Tk()

top = Frame(root)
top.pack(fill=BOTH, expand=1)

def build():
    l = Label(top, text="test phrase")
    l.pack(side="left")
    ent = Entry(top)
    ent.pack(side="left")

bottom = Frame(root)
bottom.pack()

ex = Files(root)
ex.pack(side="bottom")

root.geometry("300x250+300+300")
root.mainloop()
