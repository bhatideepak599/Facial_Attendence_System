from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Face Recogination System ")


        # ==================Variables===============

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()









        #image 1
        img1=Image.open(r"clg images\clg1.jpg")
        img1=img1.resize((645,150),Image.ANTIALIAS)
        self.photoImg1=ImageTk.PhotoImage(img1)

        fstlbl=Label(self.root,image=self.photoImg1)
        fstlbl.place(x=0,y=0,width=645,height=150)
        
        #image 2
        img2=Image.open(r"clg images\clg3.jpg")
        img2=img2.resize((645,150),Image.ANTIALIAS)
        self.photoImg2=ImageTk.PhotoImage(img2)

        fstlbl=Label(self.root,image=self.photoImg2)
        fstlbl.place(x=645,y=0,width=645,height=150)

        #BackGround 
        img4=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\clg images\clgbg1.jpg")
        img4=img4.resize((1290,600),Image.ANTIALIAS)
        self.photoImg4=ImageTk.PhotoImage(img4)

        bg_image=Label(self.root,image=self.photoImg4)
        bg_image.place(x=0,y=150,width=1290,height=600)

        title_lbl=Label(bg_image,text="ATTENDENCE MANAGEMENT SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        # creating frame below images
        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1250,height=530)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=595,height=480)

        lft_img=Image.open(r"clg images\new.jpeg")
        lft_img=lft_img.resize((580,150),Image.ANTIALIAS)
        self.lft_Img1=ImageTk.PhotoImage(lft_img)

        fstlbl=Label(Left_frame,image=self.lft_Img1)
        fstlbl.place(x=5,y=0,width=580,height=150)

        leftinside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        leftinside_frame.place(x=5,y=150,width=580,height=400)
        
        #ATTENDANCE ID
        attendanceId_label=Label(leftinside_frame,text="Attendance ID:",font=("times new roman",15,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        

        #Roll No label
        roll_label=Label(leftinside_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name label
        name_label=Label(leftinside_frame,text="NAME :",font=("times new roman",15,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Time label
        time_label=Label(leftinside_frame,text="Time:",font=("times new roman",15,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Department label
        department_label=Label(leftinside_frame,text="Department :",font=("times new roman",15,"bold"),bg="white")
        department_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Date label
        date_label=Label(leftinside_frame,text="Date :",font=("times new roman",15,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(leftinside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Attendence label
        attendence_label=Label(leftinside_frame,text="Attendance status:",font=("times new roman",15,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        
        

        self.atten_status=ttk.Combobox(leftinside_frame,width=13,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #buttons Frame
        btn_frame=Frame(leftinside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=575,height=38)
        
        #Button for Import CSV
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=14,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)
        
        #Button for Export CSV
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Button for Update
        reset_btn=Button(btn_frame,text="Update",width=13,font=("times new roman",13,"bold"),bg="orange",fg="white")
        reset_btn.grid(row=0,column=2)

        #Button for Reset
        delete_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=3)




        #RIGHT FRAME
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=610,y=10,width=580,height=510)

        # Table buttons Frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=0,width=565,height=450)



        # =============== Scrool Bar =====================
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)


        self.AttendenceReportTable.heading("id",text="Attendance ID")
        self.AttendenceReportTable.heading("roll",text="Roll No")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendance",text="Attendance ")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width="100")
        self.AttendenceReportTable.column("roll",width="100")
        self.AttendenceReportTable.column("name",width="100")
        self.AttendenceReportTable.column("department",width="100")
        self.AttendenceReportTable.column("time",width="100")
        self.AttendenceReportTable.column("date",width="100")
        self.AttendenceReportTable.column("attendance",width="100")
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)



    # =============Fetch data ====================

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    # Import CSV file
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=( ("CSV File","*.csv" ),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

        

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=( ("CSV File","*.csv" ),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data has been Exported to "+os.path.basename(fln)+" successfullly")

        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    


    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")    




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()