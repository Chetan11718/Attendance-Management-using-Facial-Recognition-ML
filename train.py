from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

# Use the 'face' submodule from the 'contrib' package



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        title_lbl = Label(self.root,text="Train Dataset",font=("times new roman",35,"bold"),bg="light blue",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=50)
        
        img_top = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=50,width=1500,height=300)
        
        #button
        
        b1 = Button(self.root,text = "TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="light blue",fg="dark blue")
        b1.place(x=-95,y=350,width=1530,height=60)
        
        img_bottom = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\blue.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=400,width=1530,height=325)
        
    def train_classifier(self):
        data_dir = ("data")  #storing the data collected
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  #gray scale img
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #======TRAIN THE CLASSIFIER==========
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()