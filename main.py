from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
        ##function buttons##

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        
        img=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #second image
        
        img1=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\cyan.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl = Label(bg_img,text="Attendance Tracker using Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=100,y=200,width=180,height=40)
        

        #Detect Face
        img5=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognition,cursor="hand2")
        b1.place(x=400,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=400,y=200,width=180,height=40)

        #Attendence Face Button
        img6=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=700,y=200,width=180,height=40)


        #Help Button
        img7=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=50,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1000,y=200,width=180,height=40)
        

        #Train 
        
        img8=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command = self.train_data)
        b1.place(x=100,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command = self.train_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=100,y=420,width=180,height=40)


         #photo
        img9=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=400,y=420,width=180,height=40)


        #Developer
        img10=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Developer Details",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=700,y=420,width=180,height=40)


        #Exit
        img11=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\purple.jpg")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1000,y=270,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1000,y=420,width=180,height=40)

    def open_img(self):
        os.startfile("data")

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


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()