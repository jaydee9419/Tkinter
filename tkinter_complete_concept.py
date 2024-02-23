from tkinter import *
from tkinter import messagebox
from tkinter import ttk



def close_window():
    window.destroy()

window = Tk()

p1 = PhotoImage(file = '123.png') 
window.iconphoto(False, p1) 


window.title("Input Form")
window.geometry('400x250')
window.configure(bg="light blue")
window.resizable(0, 0)

yscrollbar = Scrollbar(window)
yscrollbar.pack(side=RIGHT, fill=Y)

label1 = Label(window, text='Please enter login credentials', font=('Times new roman', 13, "bold"))
label1.configure(bg="light blue")
label1.pack()

# Use StringVar to associate entry fields with variables
username_var = StringVar()

username_label = Label(window, text="Username:", font=('Times new roman', 10, "bold"))
username_label.configure(bg="light blue")
username_label.pack()

username_entry = Entry(window, textvariable=username_var)
username_entry.configure(bg="light yellow")
username_entry.pack()

password_var = StringVar()

password_label = Label(window, text="Password:", font=('Times new roman', 10, "bold"))
password_label.configure(bg="light blue")
password_label.pack()

password_entry = Entry(window, show="*", textvariable=password_var)
password_entry.configure(bg="light yellow")
password_entry.pack()

label2 = Label(window, text='Choose the required tools', font=('Times new roman', 13, "bold"))
label2.configure(bg="light blue")
label2.pack()

x = ['JAVA', 'Python', 'C++', 'PowerBI', 'Linux', 'Oracle', 'AI & ML']

list = Listbox(window, font=('Times new roman', 12, 'bold'), bg="light blue", height=1, width=1, selectmode='multiple', yscrollcommand=yscrollbar.set)
for item in range(len(x)):
    list.insert(END, x[item])
    list.itemconfigure(item, bg='bisque')

list.pack(fill=BOTH, expand=True)

def print_values():
    name = username_var.get()
    pwd = password_var.get()
    itm = [list.get(idx) for idx in list.curselection()]
    if not name:
        messagebox.showerror("Error", "username is required.")
    
    elif not pwd:
        messagebox.showerror("Error", "Password is required.")
    
    elif not itm:
        messagebox.showerror("Error", "Please select atleast one course.")
    else:
        print("User Name:", name)
        # print("User Password:", pwd)
        print("List of items: ", itm)
        window.destroy()

yscrollbar.configure(command=list.yview)

submit_button = Button(window, text='Submit', font=('Times new roman', 10, 'bold'), command=print_values, height=1, width=5)
submit_button.configure(bg="green")
submit_button.pack()

window.mainloop()
