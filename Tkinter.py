
from tkinter import *

window = Tk()
window.title("Select Below Options")

yscrollbar = Scrollbar(window)
yscrollbar.pack(side= RIGHT, fill= Y)


label = Label(window, 
              text="Select the below language",
              font=('Times new roman', 10),
              padx=10, pady=10)
label.pack()


list = Listbox(window, selectmode='multiple',
               yscrollcommand = yscrollbar.set)

list.pack(pady=10, padx=10, expand = YES, fill="both")

x =["C", "C++", "C#", "Java", "Python", 
	"R", "Go", "Ruby", "JavaScript", "Swift", 
	"SQL", "Perl", "XML"] 

for each_item in range(len(x)): 
	
	list.insert(END, x[each_item]) 
	list.itemconfig(each_item, bg = "lime")
 
yscrollbar.config(command = list.yview) 
window.mainloop()



