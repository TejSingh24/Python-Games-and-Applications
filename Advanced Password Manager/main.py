import tkinter as tk
from turtle import title
import random
import pyperclip
import json

default_email_id = 'name@gmail.com'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            'Email': email_id,
            'Password': password,
        }
    }

    if website_name == '' or password == '':
        tk.messagebox.showinfo(title='Ooops', message="Please don't leave any fields empty!")
    else: 
        is_ok = tk.messagebox.askokcancel(title=website_name, message=f'These are the details that you entered: \nEmail:{email_id}'
                                                                f'\nPassword: {password} \n Is it ok to save?')

        if is_ok:
            try:    
                with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='r') as file:
                    data = json.load(file)
                    data.update(new_data)
            except json.decoder.JSONDecodeError:
                with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            except FileNotFoundError:
                with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                # email_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


def search():
        try:    
            with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='w') as file:
                new_data = {}
                json.dump(new_data, file)
        except json.decoder.JSONDecodeError:
            with open('app_brewery-365 days code\\password-manager-start\\Password_Manager.json', mode='w') as file:
                new_data = {}
                json.dump(new_data, file)
        else:
            website_name = website_entry.get()
            try:
                email_id = data[website_name]['Email']
                password = data[website_name]['Password']
            except KeyError:
                tk.messagebox.showinfo(title='Error', message='No data for this website exists!')
            else:
                tk.messagebox.showinfo(title=website_name, message=f'Email: {email_id}\nPassword: {password}')
                pyperclip.copy(password)
            

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file='app_brewery-365 days code\\password-manager-start\\logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = tk.Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = tk.Label(text='Password:')
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky='W')
website_entry.focus()
email_entry = tk.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky='W')
email_entry.insert(tk.END, default_email_id)
password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3, sticky='W')
search_button = tk.Button(text='Search', command=search, width=14)
search_button.grid(column=2, row=1, sticky='W')
password_button = tk.Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3, sticky='W')
add_button = tk.Button(text='Add', width=44, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky='W')






window.mainloop()