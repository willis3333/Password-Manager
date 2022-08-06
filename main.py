# TODO: Add custom password generation constraints
# TODO; pip install pyperclip and use it to copy pw to clipboard then display popup
# TODO: encrypt text file
# TODO: Create Postgres DB and save info to DB Table
# TODO: Add popup (messagebox) validation for saving and popup warning for empty fields
# TODO: delete fields after save

import tkinter
import random
# import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
with open('pw_generator_char.txt', 'r') as pw_gen_txt:
    pw_txt = pw_gen_txt.read()
pw_char_list = [char for char in pw_txt]


def generate_pw():
    password = ''
    for _ in range(0, 10):
        password += random.choice(pw_char_list)
        password_stringvar = tkinter.StringVar(value=password)
    pw_entry.configure(textvariable=password_stringvar)


# ---------------------------- SAVE PASSWORD ------------------------------- #
add_confirmation_label = tkinter.Label(text='')
add_confirmation_label.grid(column=2, row=6)


def save_text(text):
    global add_confirmation_label
    add_confirmation_label.config(text=text)


def print_pw_entries():
    global entry_list
    with open('password_safe.txt', 'a') as f:
        for entry in entry_list:
            f.write(f'{entry.get()} | ')
        f.write('\n ----------\n')
        window.after(1000, save_text, 'Saved!')
        window.after(5000, save_text, '')
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Generating Safe')
window.config(padx=100, pady=100)
canvas = tkinter.Canvas(height=200, width=200)

logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)

# Create/ Grid Labels in column 0
site_label = tkinter.Label(text='Website/ Account Name')
url_label = tkinter.Label(text='Website URL')
username_label = tkinter.Label(text='Username/ Email')
pw_label = tkinter.Label(text='Password:')
label_list = [site_label, url_label, username_label, pw_label]
label_row = 2
for label in label_list:
    label.grid(column=0, row=label_row)
    label_row += 1

# Create/ Grid Entries in column 1
site_entry = tkinter.Entry(width=35)
url_entry = tkinter.Entry(width=35)
username_entry = tkinter.Entry(width=35)
pw_entry = tkinter.Entry(width=20)
entry_list = [site_entry, url_entry, username_entry, pw_entry]
entry_row = 2
for entry in entry_list:
    if entry == pw_entry:
        entry.grid(column=1, row=entry_row)
        print('pw')
    else:
        entry.grid(column=1, row=entry_row, columnspan=2)
        print('not pw')
    entry_row += 1

# Create/ Grid Buttons
generate_pw_button = tkinter.Button(text='Generate Password', command=generate_pw)
generate_pw_button.grid(row=5, column=2)
add_button = tkinter.Button(text='Add to Safe', command=print_pw_entries)
add_button.grid(row=6, column=1)

tkinter.mainloop()

