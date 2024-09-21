from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,width=1000,height=1000)

        img1=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1550,height=800)


        frame=Frame(self.root,bg="light blue")
        frame.place(x=450,y=150,width=340,height=400)


        img2=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\login.jpg")
        img2=img2.resize((80,80),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=580,y=160,width=80,height=80)

        login_str=Label(frame,text="LOGIN",font=("times new roman",20,"bold"),fg="black",bg="light blue")
        login_str.place(x=120,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",18,"bold"),fg="black",bg="light blue")
        username.place(x=25,y=130)
        self.txtuser=ttk.Entry(frame,font=("times new roman",10,"bold"))
        self.txtuser.place(x=25,y=170,width=250)


        password=lbl=Label(frame,text="Password",font=("times new roman",18,"bold"),fg="black",bg="light blue")
        password.place(x=25,y=205)
        self.txtpass=ttk.Entry(frame,font=("times new roman",10,"bold"))
        self.txtpass.place(x=25,y=245,width=250)

        #login button
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="Green",fg="white",activeforeground="white",activebackground="green")
        login_btn.place(x=115,y=280,width=100,height=35)

        #registration button

        register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bd=3,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        register_btn.place(x=25,y=325,width=130)


        #forget password button

        forget_btn=Button(frame,text="Forget Password ",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bd=3,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        forget_btn.place(x=190,y=325,width=130)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="chetan" and self.txtpass.get()=="chetu":
            messagebox.showinfo("Success","Login Successful")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="dimpu123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()

                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return 
            conn.commit()
            conn.close()

        #==============================reset password===========================
    def reset_pass(self):
        if self.combo_sec_ques.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txtsec_ans.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="dimpu123",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_sec_ques.get(),self.txtsec_ans.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.show("Error","Please enter the correct anwser",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password has been Reset ,Enter New Password",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="dimpu123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            

            if row==None:
                messagebox.showerror("My Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("390x450+410+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",18,"bold"),fg="dark blue",bg="white")
                l.place(x=0,y=10,relwidth=1)

                sec_ques = Label(self.root2,text="Security Ques",font=("times new roman",15,"bold"),bg = "white")
                sec_ques.place(x=50,y=90)
                self.combo_sec_ques = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state = "readonly")
                self.combo_sec_ques["values"] = ("Select","Your Birth Place","Your NickName")
                self.combo_sec_ques.place(x=50,y=130,width=250)
                self.combo_sec_ques.current(0)
                
                sec_ans = Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec_ans.place(x=50,y=170)
                self.txtsec_ans = ttk.Entry(self.root2,font=("times new roman",15))
                self.txtsec_ans.place(x=50,y=210,width=250)

                new_password= Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=250)
                self.txt_newpassword= ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpassword.place(x=50,y=290,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="white",fg="Green")
                btn.place(x=150,y=350)

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #========variables======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        
        img1=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1550,height=800)
        
        #===========main frame========
        frame = Frame(self.root,bg="white")
        frame.place(x=250,y=100,width=800,height=500)
        register_lb1 = Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="dark blue",bg="white")
        register_lb1.place(x=270,y=20)  
        
        #=======label and entry=====
        
        #row1....
        fname = Label(frame,text="First Name",font=("times new roman",15,"bold"),bg = "white")
        fname.place(x=100,y=100)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=100,y=130,width=250)
        
        l_name = Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=400,y=100)
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=400,y=130,width=250)
        
        # #row2....
        contact = Label(frame,text="Contact",font=("times new roman",15,"bold"),bg = "white")
        contact.place(x=100,y=180)
        contact_entry = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=100,y=210,width=250)
        
        email = Label(frame,text="Email ID",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=400,y=180)
        self.txtemail = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txtemail.place(x=400,y=210,width=250)
        
        #row3..........
        sec_ques = Label(frame,text="Security Ques",font=("times new roman",15,"bold"),bg = "white")
        sec_ques.place(x=100,y=265)
        self.combo_sec_ques = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state = "readonly")
        self.combo_sec_ques["values"] = ("Select","Your Birth Place","Your NickName")
        self.combo_sec_ques.place(x=100,y=295,width=250)
        self.combo_sec_ques.current(0)
        
        sec_ans = Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec_ans.place(x=400,y=265)
        self.txtsec_ans = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txtsec_ans.place(x=400,y=295,width=250)
        
        # #row4...
        pwd = Label(frame,text="Password",font=("times new roman",15,"bold"),bg = "white")
        pwd.place(x=100,y=350)
        pwd_entry = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        pwd_entry.place(x=100,y=380,width=250)
        
        conf_pwd = Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        conf_pwd.place(x=400,y=350)
        self.txtconf_pwd = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txtconf_pwd.place(x=400,y=380,width=250)
        
        #========check button=====
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree to the terms and conditions",font = ("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=100,y=445)
        
        #Register NOW button
        
        img = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\register.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=450,y=430,width=200)
        
        # img = Image.open(r"D:\Face_recog\login_button.png")
        # img = img.resize((200,50),Image.Resampling.LANCZOS)
        # self.photoimage = ImageTk.PhotoImage(img)
        # b1 = Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        # b1.place(x=400,y=440,width=300)
        #==========function declaration=======

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree out terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="dimpu123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try email")
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
        messagebox.showinfo("Success","Register Successful")

    # def return_login(self):
    #     self.root.destroy()


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        
        img=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\apisero.jpg")
        img=img.resize((1280,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1280,height=130)
        #second image
        
        #bg image
        img3=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\light.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl = Label(bg_img,text="Attendance Tracker using Face Recognition",font=("times new roman",30,"bold"),bg="light blue",fg="Dark Blue")
        # title_lbl.place(x=0,y=0,width=1530,height=45)
        title_lbl.place(x=-85,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\student.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=100,y=200,width=180,height=40)
        

        #Detect Face
        img5=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\face_detect.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognition,cursor="hand2")
        b1.place(x=400,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=400,y=200,width=180,height=40)

        #Attendence Face Button
        img6=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\attendance.jpg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=700,y=200,width=180,height=40)


        #Help Button
        img7=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\help.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=1000,y=200,width=180,height=40)
        

        #Train 
        
        img8=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\train.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command = self.train_data)
        b1.place(x=100,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command = self.train_data,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=100,y=420,width=180,height=40)


         #photo
        img9=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\photo.jpg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=400,y=420,width=180,height=40)


        #Developer
        img10=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\developer.jpg")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Developer Details",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=700,y=420,width=180,height=40)


        #Exit
        img11=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\exit.jpg")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="Dark Blue")
        b1_1.place(x=1000,y=420,width=180,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        confirm_exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this page?", parent=self.root)
        if confirm_exit:
            self.root.destroy()

    ##function buttons##
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        

if __name__=="__main__":
    main()


