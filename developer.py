from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="WHITE",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=50)
        
        img_top = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=50,width=1500,height=720)
        
        #FRAME
        
        main_frame=Frame(f_lb1,bd=2,bg="#CACFD2")
        main_frame.place(x=150,y=0,width=1000,height=600)
        
        img_top1 = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\passport_photo.jpg")
        img_top1=img_top1.resize((210,187),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        f_lb1 = Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=400,y=7,width=200,height=185)
        
        #developer info
        dep_label=Label(main_frame,text=" Hello, my name is Chetan.",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=5)
        
        dep_label=Label(main_frame,text=" I'm studying in PES University.",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=40)
        dep_label=Label(main_frame,text=" I'm an intern at Apisero Inc.",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=75)
        
        
        img2=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\apisero.jpg")
        img2=img2.resize((1000,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=1000,height=150) 
        
        
        #===== #2 ========
        img_top2 = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\tanya.jpg")
        img_top2=img_top2.resize((210,127),Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        
        f_lb1 = Label(main_frame,image=self.photoimg_top2)
        f_lb1.place(x=400,y=380,width=200,height=185)
        
        #developer info#2
        dep_label=Label(main_frame,text=" Hello, my name is Tanya,",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=380)
        
        dep_label=Label(main_frame,text=" I'm studying in PES University.",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=415)
        dep_label=Label(main_frame,text=" I'm an intern at Apisero Inc.",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label.place(x=0,y=450)
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()