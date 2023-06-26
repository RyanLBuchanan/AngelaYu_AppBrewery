import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# Constants
FONT = ("Calibri", 12, "normal")
BGCOLOR_DARKTHEME1 = "#1F3B4D"
BGCOLOR_DARKTHEME2 = "#92A8A0"
CYAN_DARKTHEME1 = "#33CCCC"
CYAN_DARKTHEME2 = "#009999"
DEFAULT_EMAIL = "buchanan.ryan22@gmail.com"

# ---------------------------- SEARCH WEBSITES ------------------------------- #
def search_websites():
    website_to_find = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            password_to_search = data.get(website_to_find, {}).get("password")

        if password_to_search:
            messagebox.showinfo(title=website_to_find, message=f"Email: {DEFAULT_EMAIL}\nPassword: {password_to_search}")
        else:
            messagebox.showwarning(title="Website Not Found",
                                   message=f"Website not found for your entry \"{website_to_find}\""
                                           f"\n\nMake sure to enter the website exactly as you saved it.")

    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="Data file not found.")

    except json.JSONDecodeError:
        messagebox.showwarning(title="Invalid JSON", message="Invalid JSON format in data file.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Define character sets
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate password using list comprehension
    password_list = [
        choice(letters) for _ in range(randint(8, 10))
    ] + [
        choice(numbers) for _ in range(randint(2, 4))
    ] + [
        choice(symbols) for _ in range(randint(2, 4))
    ]

    # Shuffle the password characters
    shuffle(password_list)

    # Combine the characters into a string
    password = "".join(password_list)

    # Clear and insert the generated password into the entry field
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

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

    # Check if any fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please fill in all fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            # Create a new 'data.json' file with initial data
            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(new_data, data_file, indent=4)

        # except json.decoder.JSONDecodeError:
        #     # Handle invalid JSON data in 'data.json' file
        #     print("Invalid JSON data in 'data.json' file.")
        #     # Create a new 'data.json' file with initial data
        #     with open("data.json", "w") as data_file:
        #         # Save updated data
        #         json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)

        finally:
            # Clear website and password fields for next entry
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg=BGCOLOR_DARKTHEME1, padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=BGCOLOR_DARKTHEME1, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)  # Display the canvas in column 1, spanning 4 rows

# Labels
website_label = Label(text="Website:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
website_label.grid(column=0, row=1)  # Display the website label in column 0, row 2

email_label = Label(text="Email/Username:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
email_label.grid(column=0, row=2)  # Display the email label in column 0, row 3

password_label = Label(text="Password:", fg=BGCOLOR_DARKTHEME2, bg=BGCOLOR_DARKTHEME1, font=FONT, highlightthickness=0)
password_label.grid(column=0, row=3)  # Display the password label in column 0, row 4

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=1)  # Display the website entry field in column 1, row 2
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)  # Display the email entry field in column 1, row 3
email_entry.insert(0, DEFAULT_EMAIL)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)  # Display the password entry field in the frame, with right padding

# Buttons
password_button = Button(text="Generate Password", fg="white", bg=BGCOLOR_DARKTHEME2, font=("Calibri", 9, "normal"), highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)  # Display the password button in the frame, with left alignment


add_button = Button(width=50, text="Add", fg="white", bg=BGCOLOR_DARKTHEME2, font=("Calibri", 9, "normal"), highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

search_button = Button(width=17, text="Search", fg="white", bg=CYAN_DARKTHEME2, font=("Calibri", 9, "normal"), highlightthickness=0, command=search_websites)
search_button.grid(column=2, row=1)  # Display the password button in the frame, with left alignment

# ---------------------------- Development Tools ------------------------------- #
# Function for closing on space bar
def exit_program(event):
    window.destroy()  # Destroy the Tk window


# Bind the space bar key to the exit_program function
window.bind("<space>", exit_program)

# Start the main event loop to display the window and handle user interactions
window.mainloop()
