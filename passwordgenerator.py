from tkinter import *
from tkinter import messagebox
from random import randint, choice

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x400")

# Variables to store checkbox states
use_all_chars = BooleanVar()
use_alpha = BooleanVar()
use_alphanum = BooleanVar()

def validate_checkboxes():
    selected_options = sum([use_all_chars.get(), use_alpha.get(), use_alphanum.get()])
    if selected_options > 1:
        messagebox.showwarning("Warning", "Please select only one password type")
        return False
    if selected_options == 0:
        messagebox.showwarning("Warning", "Please select at least one password type")
        return False
    return True

def new_rand():
    if not validate_checkboxes():
        return

    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''
    
    if use_all_chars.get():
        # Generate a completely random password with all characters
        for i in range(pw_length):
            my_password += chr(randint(33, 126))
    elif use_alpha.get():
        # Generate a password with only alphabets
        for i in range(pw_length):
            my_password += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif use_alphanum.get():
        # Generate a password with alphabets and numbers
        for i in range(pw_length):
            my_password += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    
    pw_entry.insert(0, my_password)

def clipper():
    # to clear clipboard
    root.clipboard_clear()
    # to copy
    root.clipboard_append(pw_entry.get())
    # Show success popup
    messagebox.showinfo("Success", "Password successfully copied to clipboard")

def checkboxes_handler():
    if use_all_chars.get() or use_alpha.get() or use_alphanum.get():
        validate_checkboxes()

# Label Frame
lf = LabelFrame(root, text="Enter number of Characters:")
lf.pack(pady=20)

# Box for entering number of characters
my_entry = Entry(lf, font=("Times", 24))
my_entry.pack(pady=20, padx=20)

# Checkbuttons
cb_frame = Frame(root)
cb_frame.pack(pady=10)

cb_all = Checkbutton(cb_frame, text="Use All Characters", variable=use_all_chars, command=checkboxes_handler)
cb_all.grid(row=0, column=0, padx=10, pady=5)

cb_alpha = Checkbutton(cb_frame, text="Only Alphabets", variable=use_alpha, command=checkboxes_handler)
cb_alpha.grid(row=0, column=1, padx=10, pady=5)

cb_alphanum = Checkbutton(cb_frame, text="Alphabets and Numbers", variable=use_alphanum, command=checkboxes_handler)
cb_alphanum.grid(row=0, column=2, padx=10, pady=5)

# Box for our returned password
pw_entry = Entry(root, text='', font=("Times", 16))
pw_entry.pack(pady=20)

# Frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
