from tkinter import * #used to create GUI applications
from tkinter import ttk #Stylish Toolkit
from PIL import Image,ImageTk # to crop the images
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    obj=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Login ")

        bg_image=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\b2.jpg")
        bg_image=bg_image.resize((1300,690),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)

        fstlbl=Label(self.root,image=self.bg)
        fstlbl.place(x=0,y=0,relheight=1,relwidth=1)

        #Creating Frame
        main_frame=Frame(self.root,bd=2,bg="black")
        main_frame.place(x=480,y=80,width=350,height=500)

        image1=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\login.webp")
        image1=image1.resize((350,100),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(image1)

        fstlbl=Label(image=self.img1,bg="black",borderwidth=0)
        fstlbl.place(x=480,y=80,height=100,width=350)

        title_lbl=Label(main_frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        title_lbl.place(x=95,y=100)


        #labels
        username=lbl=Label(main_frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username.place(x=70,y=135)

        self.txtuser=ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=160,width=270)

        
        password=lbl=Label(main_frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=70,y=205)

        self.txtpass=ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=230,width=270)


        # UserName icon image

        image2=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\profileedit.jpg")
        image2=image2.resize((  30,25),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(image2)

        fstlbl1=Label(main_frame,image=self.img2,bg="black",borderwidth=0)
        fstlbl1.place(x=40,y=135,height=25,width=30)

        image3=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\p1.jpg")
        image3=image3.resize((  30,20),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(image3)

        fstlbl2=Label(main_frame,image=self.img3,bg="black",borderwidth=0)
        fstlbl2.place(x=40,y=208,height=20,width=30)

        # creating login button
        loginbtn=Button(main_frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # creating Register button
        registerbtn=Button(main_frame,command=self.register_window,text="New User Register",font=("times new roman",13,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=380,width=160)

        # creating Forget Password button
        forgetbtn=Button(main_frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",13,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=20,y=410,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error"," All Fields Required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Deepak@123",database="user_data",port="3306")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()       
                                                                                        ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Yes or No", "Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()
            #self.root.destroy()

    #==============reset function===========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select The security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Deepak@123",database="user_data",port="3306")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None :
                messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
            else:
                q1=("update register set password=%s where email=%s")
                v1=(self.txt_new_pass.get(),self.txtuser.get())
                my_cursor.execute(q1,v1)

                conn.commit()
                conn.close()
                messagebox.showinfo("Password Reset","Password has been reset , Please login with new Password",parent=self.root2)   
                self.root2.destroy()


    # =========forget password Window===========
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter Email to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Deepak@123",database="user_data",port="3306")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Email does not Exist","Enter valid Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("350x500+480+80")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                # Security Question
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select"," Your Birth Place","Favourite Sport","Your pet Name",)
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150,width=250)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_pass.place(x=50,y=220,width=250)

                self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset ",font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)
                



# class for register
class Register:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1300x690+0+0")#here 0,0 is the coordinates
        self.root.title("Register ")

        # Variables Declaration
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()




        # backgroung image
        bg_image=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\registerbg.webp")
        bg_image=bg_image.resize((1300,690),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_image)
    
        fstlbl=Label(self.root,image=self.bg)
        fstlbl.place(x=0,y=0,relheight=1,relwidth=1)

        # left Image
        bg_image1=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\r1.webp")
        bg_image1=bg_image1.resize((470,550),Image.ANTIALIAS)
        self.bg1=ImageTk.PhotoImage(bg_image1)
    
        fstlbl=Label(self.root,image=self.bg1)
        fstlbl.place(x=50,y=100,width=470,height=550)


        # Creating Frames
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=700,height=550)

        #Creating Labels
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=220,y=20)

        # Creating labels and Entry Field
        # first Name
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        # last name
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        # contact
        contact=Label(frame,text="Contact No ",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        # Email
        email=Label(frame,text="Email ID ",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=370,y=200,width=250)

        # Security Question
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select"," Your Birth Place","Favourite Sport","Your pet Name",)
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240,width=250)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        # password
        pswd=Label(frame,text="Password ",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250) 


        # Confirm Password
        confirm_pswd=Label(frame,text="Confirm Password ",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        # creating CheckBox
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # creating buttons

        img1=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\registerBtn.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.im1,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")   # Register btn
        b1.place(x=210,y=420,width=200)
        
        img2=Image.open(r"C:\Users\bhati\Desktop\Face Recognisation\login images\log2.jpeg")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(img2)
        b2=Button(frame,command=self.return_login,image=self.im2,borderwidth=0,cursor="hand2",bg="white") #login Button
        b2.place(x=530,y=480,width=200)


    # Function for Register
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error"," Password & Confirm Must be Same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Terms and Conditions",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Deepak@123",database="user_data",port="3306")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist, Try with another Email",parent=self.root)
                
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

            conn.commit()
            conn.close()

    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
    main()