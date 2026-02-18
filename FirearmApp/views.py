import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Username").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        tk.Label(self.frame, text="Password").pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.frame, text="Login")
        self.login_button.pack(pady=10)

    def get_credentials(self):
        return self.username_entry.get(), self.password_entry.get()

    def show_message(self, msg):
        messagebox.showinfo("Info", msg)


class ProductView:
    def __init__(self, root, products):
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Product List").pack()
        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack()

        for product in products:
            self.listbox.insert(tk.END, f"{product['name']} - {product['type']} - Stock: {product['stock']} - ${product['price']}")
