# TODO: Add custom password generation constraints
# TODO: encrypt/ zip json file and add code to decrypt/ unzip with zipper
# TODO: Create Postgres DB and save info to DB Table

import json
import tkinter
import random
import pyperclip

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title('Password Generating Safe')
window.config(padx=100, pady=100)
canvas = tkinter.Canvas(height=200, width=200)

logo_img = tkinter.PhotoImage(file='Password-Manager/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
with open('Password-Manager/pw_generator_char.txt', 'r') as pw_gen_txt:
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
add_confirmation_label.grid(column=1, row=7)


def save_text(text):
    global add_confirmation_label
    add_confirmation_label.config(text=text)


def save_pw_entries():
    global entry_dict
    for key in entry_dict:
        print(key.get())
        print(len(f'{key.get()}'))
        if len(f'{key.get()}') == 0:
            window.after(1000, save_text, 'Please verify all fields')
            window.after(5000, save_text, '')
        else:
            if key == site_entry:
                json_pw_data = {f'{key.get()}': {}}
            else:
                json_pw_data[f'{site_entry.get()}'][entry_dict[key]] = f'{key.get()}'
                if key == pw_entry:
                    pyperclip.copy(f'{key.get()}')
    try:
        with open('Password-Manager/password_safe.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        window.after(3000, save_text, 'No JSON file exists. Creating password safe...')
        with open('Password-Manager/password_safe.json', 'w') as f:
            json.dump(json_pw_data, f, indent=4)
        window.after(5000, save_text, 'Saved! Password copied to Clipboard')
        window.after(10000, save_text, '')
    else:
        try:
            pw_data = data[f'{site_entry.get()}']
        except KeyError:
            window.after(1000, save_text, 'No Record found. Saving record..')
            with open('Password-Manager/password_safe.json', 'r+') as f:
                    # First we load existing data into a dict.
                    file_data = json.load(f)
                    # Join new_data with file_data inside emp_details
                    file_data.update(json_pw_data)
                    # Sets file's current position at offset.
                    f.seek(0)
                    # convert back to json.
                    json.dump(file_data, f, indent=4)
                # data = json.load(f)
                # data.update(json_pw_data)
                # json.dump(data, f, indent=4)
            window.after(1000, save_text, 'Saved! Password copied to Clipboard')
            window.after(5000, save_text, '')
        else:
            window.after(1000, save_text, f'record exists:\n{pw_data} \n If you wish to update,\n'
                                          f' edit in password safe')
    finally:
        for key in entry_dict:
            key.delete(0, len(f'{key.get()}'))

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
entry_dict = {site_entry: '', url_entry: 'URL: ', username_entry: 'username: ', pw_entry: 'password: '}
entry_row = 2
for key in entry_dict:
    if key == pw_entry:
        key.grid(column=1, row=entry_row)
        print('pw')
    else:
        key.grid(column=1, row=entry_row, columnspan=2)
        print('not pw')
    entry_row += 1

# Create/ Grid Buttons
generate_pw_button = tkinter.Button(text='Generate Password', command=generate_pw)
generate_pw_button.grid(row=5, column=2)
add_button = tkinter.Button(text='Add to Safe', command=save_pw_entries)
add_button.grid(row=6, column=1)

tkinter.mainloop()

