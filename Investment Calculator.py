from tkinter import *

root=Tk()
root.title("Investment calculator")
root.geometry("800x500")

def Calculate():
    prin=int(principalentry.get())
    rat=int(rateentry.get())
    tim=int(timeentry.get())
    amount=prin*(1+(rat/100)*tim)
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)


principal=Label(root,text="Principal:",font="arial 20")
rate=Label(root,text="Interest rate:",font="arial 20")
time=Label(root,text="Time:",font="arial 20")


principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)

Amount=Label(root,text="Amount:",font="arial 20")
Amount.place(x=50,y=230)


principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()


principalentry=Entry(root,textvariable=principalvalue,font="arial 20",width=20)
rateentry=Entry(root,textvariable=ratevalue,font="arial 20",width=20)
timeentry=Entry(root,textvariable=timevalue,font="arial 20",width=20)

principalentry.place(x=300,y=20)
rateentry.place(x=300,y=90)
timeentry.place(x=300,y=160)

Button(text="Calculate",font="arial 15",command=Calculate).place(x=650,y=20)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=650,y=90)



root.mainloop()
