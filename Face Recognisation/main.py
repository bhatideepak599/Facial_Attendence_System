from tkinter import * #used to create GUI applications
from tkinter import ttk
import tkinter #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from student import Student
from time import strftime
from datetime import datetime
import os
from train import Train
from Recognise_face import Face_recognition
from attendence import Attendance
from develpoer import Developer
from help import Help

      
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")
        
        #image 1
        img1=Image.open(r"clg images\img1.jpg")
        img1=img1.resize((433,100),Image.ANTIALIAS)
        self.photoImg1=ImageTk.PhotoImage(img1)

        fstlbl=Label(self.root,image=self.photoImg1)
        fstlbl.place(x=0,y=0,width=433,height=100)
        
        #image 2
        img2=Image.open(r"clg images\img10.jpg")
        img2=img2.resize((433,100),Image.ANTIALIAS)
        self.photoImg2=ImageTk.PhotoImage(img2)

        fstlbl=Label(self.root,image=self.photoImg2)
        fstlbl.place(x=433,y=0,width=433,height=100)

        #image 3
        img3=Image.open(r"clg images\img3.jpg")
        img3=img3.resize((433,100),Image.ANTIALIAS)
        self.photoImg3=ImageTk.PhotoImage(img3)

        fstlbl=Label(self.root,image=self.photoImg3)
        fstlbl.place(x=866,y=0,width=433,height=100)

        #background image
        img4=Image.open(r"clg images\img 5.jpeg")
        img4=img4.resize((1500,600),Image.ANTIALIAS)
        self.photoImg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoImg4)
        bg_image.place(x=0,y=100,width=1500,height=600)

        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=45)


        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman ',14,'bold'),background="white",foreground="black")
        lbl.place(x=2,y=0,width=120,height=50)
        time()

        #student button 1
        img5=Image.open(r"clg images\img2.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoImg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoImg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=220)

        b1_1=Button(bg_image,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=220,height=40)

        # Face detect button 2
        img6=Image.open(r"clg images\DEV2.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoImg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_image,image=self.photoImg6,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=70,width=220,height=220)

        b2_1=Button(bg_image,text="Detect Face",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=400,y=270,width=220,height=40)
        
        # Attendence  button 3
        img7=Image.open(r"clg images\ATTENDENCE12.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoImg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_image,image=self.photoImg7,cursor="hand2",command=self.show_Attendance)
        b3.place(x=700,y=70,width=220,height=200)

        b3_1=Button(bg_image,text="Attendence ",cursor="hand2",command=self.show_Attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=700,y=270,width=220,height=40)

        #Help Desk 4
        img8=Image.open(r"clg images\stinfo.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoImg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_image,image=self.photoImg8,cursor="hand2",command=self.help_desk)
        b4.place(x=1000,y=70,width=220,height=220)

        b4_1=Button(bg_image,text="Help Desk ",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1000,y=270,width=220,height=40)

        #Train face Button 5
        img9=Image.open(r"clg images\traindata.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoImg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_image,image=self.photoImg9,cursor="hand2",command=self.train_data)
        b5.place(x=100,y=330,width=220,height=220)

        b5_1=Button(bg_image,text="Train Data ",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=100,y=530,width=220,height=40)

        #Photos button 6
        img10=Image.open(r"clg images\PHOTOS.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoImg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_image,image=self.photoImg10,cursor="hand2",command=self.open_img)
        b6.place(x=400,y=330,width=220,height=200)

        b6_1=Button(bg_image,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=400,y=530,width=220,height=40)

        # Developer 7
        img11=Image.open(r"clg images\DEV.jpg") 
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoImg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_image,image=self.photoImg11,cursor="hand2",command=self.developer_data)
        b7.place(x=700,y=330,width=220,height=220)

        b7_1=Button(bg_image,text="Developer ",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=700,y=530,width=220,height=40)

        # Exit Button 8
        img12=Image.open(r"clg images\EXE1.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoImg12=ImageTk.PhotoImage(img12)
 
        b6=Button(bg_image,image=self.photoImg12,cursor="hand2",command=self.iExit)
        b6.place(x=1000,y=330,width=220,height=220)

        b6_1=Button(bg_image,text="Exit  ",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=1000,y=530,width=220,height=40)

    
    def open_img(self):
        os.startfile("data")
    
    def  iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()


    # function Buttons
    def student_details(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def show_Attendance(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk(self):
            
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

