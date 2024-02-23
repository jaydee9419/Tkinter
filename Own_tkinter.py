from cProfile import label
from ensurepip import bootstrap
from tkinter import *
from turtle import down, position

window = Tk()

window.title("Input form")
window.geometry('300x300')

label = Label(window, text="Please select the below options")
label.pack()



scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill="y")
scrollbar.config(command=YView)  



list = Listbox(window, selectmode='multiple', yscrollcommand = scrollbar.set)
list.pack(pady=10, padx=10, expand = YES, fill= "y")

x = ["C", "C++", "C#", "Java", "Python", 
    "R", "Go", "Ruby", "JavaScript", "Swift", 
	"SQL", "Perl", "XML"]

for each_item in range (len(x)):
    list.insert(END, x[each_item])
     
    list.itemconfig(each_item, bg = "lime")
    
button = Button(window, text = "Click", command=window.destroy)
button.pack()

window.mainloop()