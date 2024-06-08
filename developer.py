from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lb1=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"college_images\developer.webp")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=720)


        #Frame
        main_frame=Frame(f_lb1,bd=2)
        main_frame.place(x=1000,y=55,width=500,height=600)


        img_top1=Image.open(r"college_images\developer.webp")
        img_top1=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top)

        f_lb1=Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Hello my name is Priya",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=5)



        img2=Image.open(r"C:\Users\priya\Desktop\face_recognition_system\college_images\image.jpg")
        img2=img2.resize((500,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(main_frame,image=self.photoimg2)
        f_lb1.place(x=0,y=210,width=500,height=300)


        


        

        
        










if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()