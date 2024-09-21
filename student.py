from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')


                #===========VARIABLES====
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        img=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\apisero.jpg")
        img=img.resize((1280,60),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1280,height=60)
        #second image
        
        # img1=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        # img1=img1.resize((500,90),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=90)

        # #third image
        # img2=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        # img2=img2.resize((500,90),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=500,height=90)
        
        #bg image
        img3=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\grey.jpg")
        img3=img3.resize((1330,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=60,width=1330,height=900)
        
        title_lbl = Label(bg_img,text="Student Management",font=("times new roman",30,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=48,width=1480,height=600)

        #left
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold") )
        left_frame.place(x=10,y=5,width=635,height=520)

        #current course
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold") )
        current_frame.place(x=5,y=15,width=615,height=160)

#dept
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","EEE","Mechanical","Civil","Biotech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #YEAR
        year_label=Label(current_frame,textvariable=self.var_year,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025","2025-2026")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Semester
        sem_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10)

        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10)


        #Class Student Info
        class_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Details",font=("times new roman",12,"bold") )
        class_frame.place(x=5,y=190,width=625,height=300)

        #Student ID

        student_label=Label(class_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        student_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry=ttk.Entry(class_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        studentname_label=Label(class_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class section
        section_label=Label(class_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        
        section_combo=ttk.Combobox(class_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        section_combo["values"]=("A","B","C")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #rollno
        roll_label=Label(class_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        roll_entry=ttk.Entry(class_frame,textvariable=self.var_roll,width=18,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #Gender
        
        gender_label=Label(class_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        
        gender_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        
        dob_label=Label(class_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phno
        phno_label=Label(class_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phno_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label=Label(class_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # bbframe
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=620,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=620,height=35)

        take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        take_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update Photo",width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

        #right
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold") )
        right_frame.place(x=650,y=10,width=610,height=520)

        #Search System
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold") )
        search_frame.place(x=5,y=10,width=600,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll_NO","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        show_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        show_btn.grid(row=0,column=4,padx=2)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=600,height=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","id","name","sec","rollno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Deparment")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("rollno",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #=======Function Declartion========

    def add_data(self):
        if self.var_dep.get()=="Select Deparment" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="dimpu123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                                
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
            #=================fetch data==============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="dimpu123",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
     # =========== get cursor===========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_div.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

    
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update these Student Details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dimpu123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep = %s, Year = %s,Semester = %s,Division = %s,Name= %s,Roll = %s,Gender = %s,Dob = %s,Email = %s,Phone = %s,Address = %s,Teacher = %s,PhotoSample = %s where Student_id = %s",
                                                                                                                                                                                                                                (
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_std_id.get()       
                                                                                                                                                                                            ))


                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                        
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #=================delete fxn=============
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dimpu123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfuly deleted student details!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
      #============RESET===========
    
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    


    #======Generate data set take Photo Sample========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="dimpu123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep = %s, Year = %s,Semester = %s,Division = %s,Roll = %s,Gender = %s,Dob = %s,Email = %s,Phone = %s,Address = %s,Teacher = %s,PhotoSample = %s where Student_id = %s",
                                                                                                                                                                                                                                (
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                # self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_std_id.get()==id+1       
                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #======Load Predefined data on face frontal from opencv=======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] 
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()