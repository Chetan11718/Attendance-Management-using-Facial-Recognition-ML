from tkinter import *
from tkinter import ttk   #ttk has stylish tooklikt
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from tkinter import filedialog

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('FACE RECOG SYS')

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\apisero.jpg")
        img=img.resize((1600,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1600,height=70)
        #second image
        
        # img1=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\orange.jpg")
        # img1=img1.resize((800,200),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=800,y=0,width=800,height=200)

        img3=Image.open(r"C:\Users\CHETAN\OneDrive\Pictures\Saved Pictures\grey.jpg")
        img3=img3.resize((1330,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=80,width=1330,height=600)

        title_lbl = Label(bg_img,text="Attendence Management",font=("times new roman",30,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=8,y=50,width=1251,height=529)

        #left
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold") )
        left_frame.place(x=6,y=3,width=614,height=520)

        left_inside_main_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_main_frame.place(x=4,y=10,width=599,height=380)

        #Student ID

        attendanceID_label=Label(left_inside_main_frame,text="AttendenceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_main_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        name_label=Label(left_inside_main_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=4,pady=8)

        atten_name=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #dept
        depLabel=Label(left_inside_main_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        timeLabel=Label(left_inside_main_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #date
        dateLabel=Label(left_inside_main_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)

        atten_dep=ttk.Entry(left_inside_main_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        atten_dep.grid(row=2,column=3,pady=8)

        #attendence
        atten_label=Label(left_inside_main_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        atten_label.grid(row=3,column=0)

        status_combo=ttk.Combobox(left_inside_main_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=17,state="readonly")
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=1,pady=8)


        # bbframe
        btn_frame=Frame(left_inside_main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=310,width=620,height=40)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #right
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold") )
        right_frame.place(x=629,y=3,width=610,height=520)


        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=8,y=5,width=587,height=400)


        #======scroll bar table========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #====fetch data=====
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")      
        except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def get_cursor(self):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content["values"]
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
    root = Tk()
    obj = Attendance(root)
    root.mainloop()