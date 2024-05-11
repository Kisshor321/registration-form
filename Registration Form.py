from tkinter import*
from tkinter import ttk
root=Tk()

def add():
    text=en.get()
    listbox.insert(END,text)
    en.delete(0,END)
root.title("Registrtion From")
root.geometry("400x600+400+100")
root.resizable(False,False)

l1=Label(root,bg="green",width=30,text="Registration From",font=("arial",25,"bold")).pack()

l2=Label(root,text="Enter Name:",font=("arial",10,"bold"))
l2.place(x=60,y=60)
e2=Entry(root,width=28)
e2.place(x=170,y=60)

l2=Label(root,text="Enter Email:",font=("arial",10,"bold"))
l2.place(x=60,y=90)
e2=Entry(root,width=28)
e2.place(x=170,y=90)

l2=Label(root,text="Enter Password:",font=("arial",10,"bold"))
l2.place(x=60,y=120)
e2=Entry(root,width=28)
e2.place(x=170,y=120)

l2=Label(root,text="Enter Mobile:",font=("arial",10,"bold"))
l2.place(x=60,y=150)
e2=Entry(root,width=28)
e2.place(x=170,y=150)

l2=Label(root,text="Enter Gender:",font=("arial",10,"bold"))
l2.place(x=60,y=180)
e2=ttk.Combobox(root,values=(["Male","Female","Others"]),width=25)
e2.place(x=170,y=180)

l2=Label(root,text="Enter Age:",font=("arial",10,"bold"))
l2.place(x=60,y=210)
e2=Spinbox(root,from_=18,to=150,width=26)
e2.place(x=170,y=210)

l2=Label(root,text="Enter Language:",font=("arial",10,"bold"))
l2.place(x=60,y=240)
e2=ttk.Combobox(root,values=(["Telugu","English","Hindi","Tamil","Kanada"]),width=25)
e2.place(x=170,y=240)


en=Entry(root,width=35,bd=5,relief=SUNKEN,bg="pink")
en.place(x=50,y=280)

b1=Button(root,text="add",command=add,bg="blue",width=8)
b1.place(x=290,y=280)

frame=LabelFrame(root,text="Note Here",width=600,height=100)
frame.pack(pady=(280,0))

listbox=Listbox(frame)
listbox.pack(side=LEFT,fill=BOTH)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

b2=Button(root,text="Submit").place(x=130,y=550)

b3=Button(root,text="Clear").place(x=250,y=550)

root.mainloop()