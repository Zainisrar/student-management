import tkinter as tk
from tkinter import messagebox


def open_text_box():
    login_window.destroy()

    text_box_window = tk.Tk()
    text_box_window.title("Text Box")
    text_box_window.geometry("400x300")

    text_box = tk.Text(text_box_window)
    text_box.pack(fill=tk.BOTH, expand=True)

    text_box_window.mainloop()


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Perform the login validation
    if username == "admin" and password == "password":
        open_text_box()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Login Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x150")

# Username Label and Entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

# Password Label and Entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Login Button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

login_window.mainloop()
