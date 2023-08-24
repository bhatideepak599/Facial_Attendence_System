from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")



        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top=Image.open(r"clg images\help1.jpg")
        img_top=img_top.resize((1280,690),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fstlbl=Label(self.root,image=self.photoimg_top)
        fstlbl.place(x=0,y=55,width=1280,height=690)

        help_label=Label(fstlbl,text="Email:bhatideepak599@gmail.com ",font=("times new roman",30,"bold"),fg="blue",background="white")
        help_label.place(x=400,y=80)


















if __name__ == "__main__":
    root=Tk()
    obj=Help (root)
    root.mainloop()