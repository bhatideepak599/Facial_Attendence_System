from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Login_Window:
    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("1300x690+0+0")

        self.load_and_set_background()

    def load_and_set_background(self):
        img_path = r"C:\Users\bhati\Desktop\Face Recognisation\login images\b2.jpg"
        self.img1 = Image.open(img_path)

        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        self.img1 = self.img1.resize((window_width, window_height), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        fstlbl = Label(self.root, image=self.img1)
        fstlbl.pack(fill=BOTH, expand=YES)

if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
