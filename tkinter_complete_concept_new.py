from tkinter import *
from tkinter import messagebox

def close_window():
    window.destroy()

window = Tk()

p1 = PhotoImage(file='123.png')
window.iconphoto(False, p1)

window.title("Input Form")
window.geometry('350x280')
window.configure(bg="light blue")
window.resizable(0, 0)

yscrollbar = Scrollbar(window)
yscrollbar.pack(side=RIGHT, fill=Y)

# Create a frame for elements managed by grid
grid_frame = Frame(window, bg="light blue")
grid_frame.pack(pady=10)

# Use grid for elements in the grid_frame
label1 = Label(grid_frame, text='Please enter login credentials', font=('Times new roman', 13, "bold"), bg="light blue")
label1.grid(row=0, column=0, columnspan=5, pady=10)

# Create a frame for elements managed by pack
pack_frame = Frame(window, bg="light blue")
pack_frame.pack(pady=10)

# Use pack for elements in the pack_frame
label2 = Label(pack_frame, text='Choose the required tools', font=('Times new roman', 13, "bold"), bg="light blue")
label2.pack()

username_var = StringVar()
password_var = StringVar()

username_label = Label(grid_frame, text="Username:", font=('Times new roman', 10, "bold"), bg="light blue")
username_label.grid(row=1, column=0, sticky="E")

username_entry = Entry(grid_frame, textvariable=username_var, bg="light yellow")
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

password_label = Label(grid_frame, text="Password:", font=('Times new roman', 10, "bold"), bg="light blue")
password_label.grid(row=2, column=0, sticky="E")

password_entry = Entry(grid_frame, show="*", textvariable=password_var, bg="light yellow")
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="W")


x = ['JAVA', 'Python', 'C++', 'PowerBI', 'Linux', 'Oracle', 'AI & ML']

list = Listbox(window, font=('Times new roman', 12, 'bold'), bg="light blue", height=1, width=1, selectmode='multiple', yscrollcommand=yscrollbar.set)
for item in range(len(x)):
    list.insert(END, x[item])
    list.itemconfigure(item, bg='bisque')

list.pack(fill=BOTH, expand=True)

def print_values():
    name = username_var.get()
    pwd = password_var.get()
    selected_items = [list.get(idx) for idx in list.curselection()]

    if not name:
        messagebox.showerror("Error", "Username is required.")
    elif not pwd:
        messagebox.showerror("Error", "Password is required.")
    elif not selected_items:
        messagebox.showerror("Error", "Please select at least one course.")
    else:
        print("User Name:", name)
        print("List of items: ", selected_items)
        window.destroy()

yscrollbar.configure(command=list.yview)


submit_button = Button(window, text='Submit', font=('Times new roman', 10, 'bold'), command=print_values, height=1, width=5)
submit_button.configure(bg="green")
submit_button.pack()
window.mainloop()
