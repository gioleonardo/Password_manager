import json
from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M,' 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    user_letters = random.randint(8, 10)
    user_symbols = random.randint(2, 4)
    user_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(user_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(user_symbols)]
    password_numbers = [random.choice(numbers) for num in range(user_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"your new password is: {password}")
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    password = password_entry.get()
    email = email_entry.get()
    website = web_name.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_name.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH FOR DATA ------------------------------- #


def find_password():
    website = web_name.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            print(data)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n"                                                          
                                                                f"password: {password}")
            elif website not in data:
                messagebox.showinfo(title="Error", message="No details for the website found")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=100)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website")
web_label.grid(column=0, row=1)
web_name = Entry(width=35)
web_name.focus()
web_name.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=55)
email_entry.insert(END, "leonardo@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", highlightthickness=0, command=create_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=48, highlightthickness=0, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()

