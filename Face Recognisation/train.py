from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")


        title_lbl=Label(self.root,text="Train Data Set ",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top=Image.open(r"clg images\TRAIND.jpg")
        img_top=img_top.resize((1500,300),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fstlbl=Label(self.root,image=self.photoimg_top)
        fstlbl.place(x=0,y=55,width=1280,height=300)

        #button for train data
        b1_1=Button(self.root,text="TRAIN DATA ",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="green",fg="white")
        b1_1.place(x=0,y=345,width=1280,height=60)


        img_bottom=Image.open(r"clg images\traindata.jpg")
        img_bottom=img_bottom.resize((1500,300),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        fstlbl=Label(self.root,image=self.photoimg_bottom)
        fstlbl.place(x=0,y=400,width=1280,height=300)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # conversion in grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()