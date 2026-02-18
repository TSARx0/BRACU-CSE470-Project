import tkinter as tk
from controllers import AppController

root = tk.Tk()
root.title("Firearm Inventory App")
root.geometry("500x400")

app = AppController(root)

root.mainloop()
