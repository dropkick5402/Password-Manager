from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import requests
import bcrypt


# ---------------------------- ENCRYPTION and DECRYPTION ------------------------------- #
def encrypt(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return str(hash)

# password = "abc123"
#
# bytes = password.encode('utf-8')
# salt = bcrypt.gensalt()
# hash = bcrypt.hashpw(bytes, salt)
# print(hash)
#
# userPass = input("what is your password")
# userBytes = userPass.encode('utf-8')
# result = bcrypt.checkpw(userBytes, hash)
#
# print(result)




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- PASSPHRASE GENERATOR ------------------------------- #


def generate_passphrase():
    url = f"https://random-word-api.vercel.app/api?words=5"
    words = requests.get(url)
    data = words.json()

    passphrase = "-".join(data)
    password_entry.delete(0,END)
    password_entry.insert(0, passphrase)
    pyperclip.copy(passphrase)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=website,
                                message=f"email: {data[website]['email']} \nPassword: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="sorry", message="No details for the website exists")


# only use exception handling when you don't have an easy alternative. If and else statements catches things that
# happen frequently, so if you can use it, use the if/else statements. the instructor's code:

# def find_password():
#     website = website_entry.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
#         else:
#             messagebox.showinfo(title="sorry", message=f"No details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="../Password Project for Interviews/logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "rodney@gmail.com")
password_entry = Entry(width=52)
password_entry.grid(row=3, column=1, columnspan=2, sticky=W)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=4, column=1, sticky=W)
generate_passphrase_button = Button(text="Generate Passphrase", width=15, command=generate_passphrase)
generate_passphrase_button.grid(row=4, column=2, sticky=W)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky=W)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky=W)

window.mainloop()
