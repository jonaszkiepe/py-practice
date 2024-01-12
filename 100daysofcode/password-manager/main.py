from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def search():
    pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for n in range(randint(8, 10))]
    password_list += [choice(symbols) for n in range(randint(2, 4))]
    password_list += [choice(numbers) for n in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="error", message="You left some fields empty")
    else:
        entry = {
            website: {
                "email": email_username,
                "password": password,
            }
        }
        try:
            with open("passwords.json", mode="r") as passwords:
                data = json.load(passwords)
                data.update(entry)
        except json.decoder.JSONDecodeError:
            with open("passwords.json", mode="w") as passwords:
                json.dump(entry, passwords, indent=4)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as passwords:
                json.dump(entry, passwords, indent=4)
        else:
            with open("passwords.json", mode="w") as passwords:
                json.dump(data, passwords, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry's

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "stevejobless@googles.com")

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)
# Buttons
generate_password_button = Button(text="Generate Password", width=35, command=generate_password)
generate_password_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=5, column=1, columnspan=2)

# search_button = Button(text="Search", command=search, width=35)
# search_button.grid(column=1, row=6, columnspan=2)

window.mainloop()
