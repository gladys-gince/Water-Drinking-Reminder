import time
from tkinter import *

n=12
m = Tk()
m.title('Water drinking reminder')
LabelTitle = Label(m,text='Water Drinking Reminder').grid(row=1,column=4)
LabelStitle = Label(m,text='Lets keep you hydrated!!').grid(row=2,column=4)
Labeldescription1 = Label(m,text='Can you help us with some information').grid(row=3,column=4)
Labeldescription2 = Label(m,text='to customize experience for you?').grid(row=4,column=4)

Label(m,text=' ').grid(row=5,column=3)
Label(m,text=' ').grid(row=6,column=3)
#Label(m,text=' ').grid(row=7,column=3)

Label(m,text='First Name').grid(row=8,column=3)
e1 = Entry(m)
e1.grid(row=8,column=4)

Label(m,text='Last Name').grid(row=9,column=3)
e2 = Entry(m)
e2.grid(row=9,column=4)

LabelH = Label(m,text='Height').grid(row=12,column=2)
e3 = Entry(m)
e3.grid(row=12,column=3)
#e3.insert(0,"Enter your height in centimetres")

LabelW = Label(m,text='Weight').grid(row=12,column=5)
e4 = Entry(m)
e4.grid(row=12,column=6)

LabelA = Label(m,text='Age').grid(row=14,column=2)
e5 = Entry(m)
e5.grid(row=14,column=3)

Label(m,text=' ').grid(row=20,column=3)
Label(m,text=' ').grid(row=21,column=3)
Label(m,text=' ').grid(row=22,column=3)
Label(m,text=' ').grid(row=23,column=3)
Label(m,text=' ').grid(row=24,column=3)
Label(m,text=' ').grid(row=25,column=3)
Label(m,text=' ').grid(row=27,column=3)

clicked=StringVar()
LabelA = Label(m,text='Gender').grid(row=14,column=5)
drop = OptionMenu(m,clicked,"Male","Female","Other")
drop.grid(row=14,column=6)
gender=clicked.get()
l3=Label(m,text=gender).grid(row=15,column=4)

def Click():
    global n
    hello = "Hello "+e1.get()+" "+e2.get()
    l1=Label(m,text=hello).grid(row=11,column=4)

    bmi = float(e4.get())/((float(e3.get())/100)**2)
    bmiL = "Your BMI is "+str(bmi)
    l2=Label(m,text=bmiL).grid(row=13,column=4)

    if(bmi<16):
        body="severely thin"
    elif(bmi>=16) and (bmi<17):
        body="moderately thin"
    elif(bmi>=17) and (bmi<18.5):
        body="mildly thin"
    elif(bmi>=18.5) and (bmi<25):
        body="healthy"
    elif(bmi>=25) and (bmi<30):
        body="overweight"
    elif(bmi>=30) and (bmi<35):
        body="stage I obese"
    elif(bmi>=35) and (bmi<40):
        body="stage II obese"
    elif(bmi>40):
        body="stage III obese"

    if(float(e4.get())<=36):
        n=5
    elif(float(e4.get())>36) and (float(e4.get())<=45):
        n=6
    elif(float(e4.get())>45) and (float(e4.get())<=54):
        n=7
    elif(float(e4.get())>54) and (float(e4.get())<=64):
        n=9
    elif(float(e4.get())>64) and (float(e4.get())<=73):
        n=10
    elif(float(e4.get())>73) and (float(e4.get())<=82):
        n=11
    elif(float(e4.get())>82) and (float(e4.get())<=91):
        n=13
    elif(float(e4.get())>91) and (float(e4.get())<=100):
        n=14
    elif(float(e4.get())>100) and (float(e4.get())<=109):
        n=15
    elif(float(e4.get())>109) and (float(e4.get())<=118):
        n=16
    elif(float(e4.get())>118) and (float(e4.get())<=127):
        n=18
    elif(float(e4.get())>127) and (float(e4.get())<=136):
        n=19
    elif(float(e4.get())>136) and (float(e4.get())<=145):
        n=20

    if(clicked.get()=="Male"):
        n=n+2
    
    des = e1.get()+" is a "+body+" "+clicked.get()+" of age "+e5.get()
    l3=Label(m,text=des).grid(row=15,column=4)

from plyer import notification
def main():
    c=1
    while c<=n:
        notification.notify(
            title = "Please Drink Water",
            message = "This is your glass "+str(c)+" of water, "+str(n-c)+" remaining",
            timeout = 10)
        c+=1
        time.sleep(40*60)
B1 = Button(m, text="Enter",command=Click).grid(row=16,column=4)
B2 = Button(m, text="Start Notifications",command=main).grid(row=26,column=4)

m.mainloop()
