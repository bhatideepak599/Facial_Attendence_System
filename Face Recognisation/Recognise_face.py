from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pymysql
import cv2
import os
import numpy as np


 


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")

        title_lbl=Label(self.root,text="Face Recognition ",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=300,y=0,width=650,height=45)
        #1st Image
        img_top=Image.open(r"clg images\FD1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        fstlbl=Label(self.root,image=self.photoimg_top)
        fstlbl.place(x=0,y=55,width=650,height=645)
        #2nd image
        img_bottom=Image.open(r"clg images\traindata.jpg")
        img_bottom=img_bottom.resize((650,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        fstlbl=Label(self.root,image=self.photoimg_bottom)
        fstlbl.place(x=650,y=55,width=650,height=700)
        
        #Adding Button
        b1_1=Button(fstlbl,text="Face Recognition ",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=350,y=580,width=200,height=40)

    def mark_attendance(self,i,r,n,d):
        with open("Attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
               
            if((i  not in name_list) and (r not in name_list)and (n not in name_list) and (d not in name_list)):
                
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                    

    # Face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int ((100*(1-predict/300)))

                def CreateConn():
                    return pymysql.connect(host="localhost",database="face_recognizer",user="root",password="Deepak@123",port=3306)
                
                conn=CreateConn()
                cursor=conn.cursor()
                args=(str(id))
                query="select Name from student where Student_id=(%s)"
                cursor.execute(query,args)
                n=cursor.fetchone()
                n="+".join(n)
               
                
                

                query="select Roll from student where Student_id=(%s)"
                cursor.execute(query,args)
                r=cursor.fetchone()
                r="+".join(r)
                
                
                query="select Dep from student where Student_id=(%s)"
                cursor.execute(query,args)
                d=cursor.fetchone()
                d="+".join(d)
               
    

                query="select Student_id from student where Student_id=(%s)"
                cursor.execute(query,args)
                i=cursor.fetchone()
                i="+".join(i)
                


                if confidence>=85:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h) ,(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
       
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


    


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()