from models import Database
from views import LoginView, ProductView
import tkinter as tk

class AppController:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.show_login()

    def show_login(self):
        self.login_view = LoginView(self.root)
        self.login_view.login_button.config(command=self.login)

    def login(self):
        username, password = self.login_view.get_credentials()
        user = self.db.check_login(username, password)
        if user:
            self.login_view.show_message(f"Welcome {username}!")
            self.login_view.frame.destroy()
            self.show_products()
        else:
            self.login_view.show_message("Invalid username or password")

    def show_products(self):
        products = self.db.get_products()
        self.product_view = ProductView(self.root, products)
