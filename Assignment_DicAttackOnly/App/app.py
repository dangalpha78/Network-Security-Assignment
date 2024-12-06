import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Toplevel, messagebox
from user.user_auth import is_username_exist, save_user, verify_login

# GUI for creating a new account
def create_account_window():
    def create_account():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        confirm_password = confirm_password_entry.get().strip()
        if is_username_exist(username):
            messagebox.showerror("Error", "Username already exists! Please choose a different one.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match! Please try again.")
        else:
            save_user(username, password)
            messagebox.showinfo("Success", "Account created successfully!")
            account_window.destroy()

    account_window = tk.Toplevel(root)
    account_window.title("Create Account")
    account_window.geometry("400x400")

    Label(account_window, text="Username:", font=("Arial", 14)).pack(pady=10)
    username_entry = tk.Entry(account_window, font=("Arial", 14))
    username_entry.pack(pady=10, padx=20)
    
    Label(account_window, text="Password:", font=("Arial", 14)).pack(pady=10)
    password_entry = tk.Entry(account_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10, padx=20)
    
    Label(account_window, text="Confirm Password:", font=("Arial", 14)).pack(pady=10)
    confirm_password_entry = tk.Entry(account_window, show="*", font=("Arial", 14))
    confirm_password_entry.pack(pady=10, padx=20)

    Button(account_window, text="Create Account", font=("Arial", 14), command=create_account).pack(pady=20)

# GUI for logging in
def login_window():
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        if not is_username_exist(username):
            messagebox.showerror("Error", "Username does not exist! Please create an account.")
        elif verify_login(username, password):
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid password. Please try again.")

    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("400x300")

    Label(login_window, text="Username:", font=("Arial", 14)).pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Arial", 14))
    username_entry.pack(pady=10, padx=20)
    
    Label(login_window, text="Password:", font=("Arial", 14)).pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10, padx=20)

    Button(login_window, text="Login", font=("Arial", 14), command=login).pack(pady=20)

# Main GUI window
root = Tk()
root.title("Application")
Label(root, text="Welcome to User Application!!!", font=("Arial", 30)).pack(pady=20)
Button(root, text="Login", command=login_window, height=3, width=40).pack(pady=10)
Button(root, text="Create Account", command=create_account_window, height=3, width=40).pack(pady=10)
Button(root, text="Exit", command=root.quit, height=3, width=40).pack(pady=10)

root.mainloop()
