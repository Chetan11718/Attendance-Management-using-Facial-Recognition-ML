from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        title_lbl = Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="WHITE",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=50)
        
        img_top = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=50,width=1500,height=720)

        dep_label2=Label(f_lb1,text="Email:tanya@gmail.com",font=("times new roman",20,"bold"),bg="#CACFD2")
        dep_label2.place(x=500,y=300)
    

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()