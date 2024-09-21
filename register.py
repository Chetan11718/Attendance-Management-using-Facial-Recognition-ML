from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        register_lb1 = Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="dark green",bg="white")
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
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
        
       
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()