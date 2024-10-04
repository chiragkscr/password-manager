from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for i in range(0, nr_letters)]

    password_numbers = [random.choice(numbers) for n in range(0, nr_numbers)]

    password_symbols = [random.choice(symbols) for s in range(0, nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()

    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password}

    }
    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # reads the file

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)  # updates old data with new data
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)


        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------- FIND PASSWORD --------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Here's Your Password",
                                message=f"Here's your username/email and password for the website {website}\n Username/Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no passwords for {website}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=300)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image, )
canvas.grid(row=0, column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label()
email_label.config(text="Username/Email:")
email_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1,)

email_entry = Entry(width=42)
email_entry.insert(0, "@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2 )

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1,)


search_button = Button(text="Search",width=14, command=find_password)
search_button.grid(row=1, column=2)
generate_button = Button()
generate_button.config(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button()
add_button.config(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
