from tkinter import*
import easygui
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

vari=Tk()
# vari.geometry("1920x1080")
vari.minsize(800,700)

photo1 = PhotoImage(file="sc.png")
photolab = Label(image=photo1, width=740, height=450)
photolab.place(x=50, y=-180)
vari.title("Smarrt Cookie Pvt Ltd.")

def home():
    a1=Label(text="SMART COOKIE", bg="White", font=('Times New Roman',30,'bold'),borderwidth=15,fg='#000000',pady=7,padx=50)
    a1.pack()
    def file():
        global pdf1
        pdf1 = easygui.fileopenbox(default='*.csv')
        #print(pdf1)
    def send():
        data  = pd.read_csv(pdf1)
        data_dict = data.to_dict('list')
        leads = data_dict['MobileNumber']
        messages = data_dict['Message']
        combo = zip(leads,messages)
        first = True
        for lead,message in combo:
            time.sleep(4)
            web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
            if first:
                time.sleep(6)
                first=False
            width,height = pg.size()
            pg.click(width/2,height/2)
            time.sleep(8)
            pg.press("enter")
            time.sleep(8)
            pg.hotkey('ctrl','w')

    f1=Frame(vari,bg='grey', borderwidth=6)
    f1.pack(side=TOP, fill="x", padx=500, pady=70)

    l1=Label(f1,text="ADMINISTRATOR PAGE", font=('Arial', 22,'bold'),fg='green')
    l1.pack(pady=20,padx=10)

    f2=Frame(vari,bg='#A3E4D7')
    f2.place(x=360,y=320,width=700,height=300)


    b1= Button(f2, text="Select File", bg="#5D6D7E", fg="#FEF9E7", font=("Helvetica", 18, "bold"), command=file)
    b1.place(x=80, y=150, width=220, height=50)

    b2= Button(f2, text="Send", bg="#5D6D7E", fg="#FEF9E7", font=("Helvetica", 18, "bold"),command=send)
    b2.place(x=350, y=150, width=220, height=50)

    

home()
vari.mainloop()
