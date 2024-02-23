from fileinput import filename
from importlib.resources import contents
from tkinter import *
from tkinter import filedialog



class Menudemo:
    
    def __init__(self, root):
        self.menubar = Menu(root)

        root.config(menu=self.menubar)
        
        self.filemenu = Menu(root, tearoff=0)
        
        self.filemenu.add_command(label='New', command=self.donothing)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        
        self.filemenu.add_separator()
        
        self.filemenu.add_command(label='Exit', command=root.destroy)
        
        self.menubar.add_cascade(label='file', menu=self.filemenu)
        
        self.editmenu= Menu(root, tearoff=0)
        
        self.editmenu.add_command(label='Cut', command=self.donothing)
        self.editmenu.add_command(label='Copy', command=self.donothing)
        self.editmenu.add_command(label='Paste', command=self.donothing)
        
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)
        
    def donothing():
        pass
    
    def open_file(self):
        self.filename = filedialog.askopenfilename(parent=root, title='select a file', filetypes=(("python files,", "*.py"),("All files","*.*")))
        if filename !=None:
            f = open(self.filename, 'r')
            contents = f.read()
    def save_file():
        pass
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
root = Tk()
root.title('Menu Section')
obj = Menudemo(root)
root.mainloop()


