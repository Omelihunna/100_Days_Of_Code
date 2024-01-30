import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
GREEN = "#9bdeac"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers =  [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(pady=50, padx=50)

canvas = Canvas(width=150, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(75, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", width=21)
website_label.grid(column=0, row=1, sticky="e")
email_label = Label(text="Email/Username:", width=21)
email_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3, sticky="e")


#Enries
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="w")
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "omelihunna@gmail.com")

#Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", width=15, command=password_generate)
password_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()
# is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: \n Email: {email} "
#                                                       f"\nPassword: {password}\nIs it okay to save?")
# if is_ok: