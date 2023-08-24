from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")



        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top=Image.open(r"clg images\dev22.jpg")
        img_top=img_top.resize((1500,690),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fstlbl=Label(self.root,image=self.photoimg_top)
        fstlbl.place(x=0,y=55,width=1280,height=690)



        #Creating Frame
        main_frame=Frame(fstlbl,bd=2,bg="black")
        main_frame.place(x=800,y=0,width=430,height=500)

        img_top1=Image.open(r"clg images\my.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        fstlbl=Label(main_frame,image=self.photoimg_top1)
        fstlbl.place(x=230,y=0,width=200,height=200)

        # Developer
        dev_label=Label(main_frame,text="Hello , My Name Is Deepak.  ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I Am A Software Developer, ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=30)

        dev_label=Label(main_frame,text="4th year Computer Science ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=55)

        dev_label=Label(main_frame,text="student pursuing a B.Tech ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=80)

        dev_label=Label(main_frame,text="degree  I am eager to apply",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=105)

        dev_label=Label(main_frame,text="my theoretical knowledge ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=130)

        dev_label=Label(main_frame,text="and practical skills. ",font=("times new roman",13,"bold"),fg="white",background="black")
        dev_label.place(x=0,y=155)

        img_top2=Image.open(r"clg images\webDev.jpg")
        img_top2=img_top2.resize((430,300),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        fstlbl=Label(main_frame,image=self.photoimg_top2)
        fstlbl.place(x=-2,y=200,width=430,height=300)







if __name__ == "__main__":
    root=Tk()
    obj=Developer (root)
    root.mainloop()