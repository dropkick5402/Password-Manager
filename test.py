from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas1 = Canvas(height=200, width=200)
logo_img = PhotoImage(file="../Password Project for Interviews/logo.png")
canvas1.create_image(100, 100, image=logo_img)
canvas1.grid(row=0, column=1)

window_width = window.winfo_width()
window_height = window.winfo_height()
window_x = window.winfo_x()
window_y = window.winfo_y()

overlay = Toplevel(window)
overlay.attributes('-alpha', 0.5)
overlay.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
overlay.grab_set()
overlay.



website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, sticky=W)
generate_password_button = Button(text="Generate Password", width=15)
generate_password_button.grid(row=4, column=1, sticky=W)



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
generate_password_button = Button(text="Generate Password", width=15)
generate_password_button.grid(row=4, column=1, sticky=W)
generate_passphrase_button = Button(text="Generate Passphrase", width=15)
generate_passphrase_button.grid(row=4, column=2, sticky=W)
add_button = Button(text="Add", width=38)
add_button.grid(row=5, column=1, columnspan=2, sticky=W)
search_button = Button(text="Search", width=15)
search_button.grid(row=1, column=2, sticky=W)

window.mainloop()