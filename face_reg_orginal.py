from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import cv2
# Use the 'face' submodule from the 'contrib' package
from cv2 import face


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')
        
        title_lbl = Label(self.root,text="Recognization",font=("times new roman",35,"bold"),bg="light blue",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=60)
        
        #1st img
        img_top = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\cyan.jpg")  
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=650,height=700)
        
    
    #     #2nd img
        img_bottom = Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
 
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=650,y=55,width=950,height=700)
        
    #     #button
        
        b1 = Button(f_lb1,text = "Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="light blue",fg="dark blue")
        b1.place(x=350,y=50,width=200,height=40)
        
 
    # # ==========face recog==========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="dimpu123",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(str(n))

                my_cursor.execute("select Roll from student where Student_id =" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(str(r))
                
                my_cursor.execute("select Dep from student where Student_id ="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(str(d))
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord = [x,y,w,y]
            return coord
    
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf) 
            return img
    
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
        video_cap = cv2.VideoCapture(0)
    
        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
