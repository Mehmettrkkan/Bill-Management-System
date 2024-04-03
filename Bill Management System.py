from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)
def Reset():
  entry_ciğer.delete(0,END)
  entry_adana.delete(0,END)
  entry_urfa.delete(0,END)
  entry_tavukşiş.delete(0,END)
  entry_aayran.delete(0,END)
  entry_kola.delete(0,END)
  entry_su.delete(0,END)
def Total():
  try:a1=int(Ciğer.get())
  except:a1=0

  try:a2=int(Adana.get())
  except:a2=0

  try:a3=int(Urfa.get())
  except:a3=0

  try:a4=int(TavukŞiş.get())
  except:a4=0

  try:a5=int(AçikAyran.get())
  except:a5=0

  try:a6=int(Kola.get())
  except:a6=0

  try:a7=int(Su.get())
  except:a7=0

  c1=150*a1
  c2=130*a2
  c3=120*a3
  c4=100*a4
  c5=20*a5
  c6=15*a6
  c7=5*a7

  lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
  lbl_total.place(x=0,y=50)

  entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_Bill,bd=6,width=15,bg="lightgreen")
  entry_total.place(x=20,y=100)

  totalcost=c1+c2+c3+c4+c5+c6+c7
  string_bill="TL",str('%.2f' %totalcost)
  Total_Bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

 #MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Ciğer...150 TL/tabak",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Adana...130 TL/tabak",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Urfa....120 TL/tabak",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="TavukŞiş..100 TL/tabak",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="AçikAyran..20 TL/Tane",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Kola........15 TL/Tane",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Su..........5 TL/Tane",fg="black",bg="lightgreen").place(x=10,y=260)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)

#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Ciğer=StringVar()
Adana=StringVar()
Urfa=StringVar()
TavukŞiş=StringVar()
AçikAyran=StringVar()
Kola=StringVar()
Su=StringVar()
Total_Bill=StringVar()

#Label 
lbl_Ciğer=Label(f1,font=("aria",20,'bold'),text="Ciğer",width=12,fg="blue4")
lbl_adana=Label(f1,font=("aria",20,'bold'),text="Adana",width=12,fg="blue4")
lbl_urfa=Label(f1,font=("aria",20,'bold'),text="Urfa",width=12,fg="blue4")
lbl_tavukşiş=Label(f1,font=("aria",20,'bold'),text="TavukŞiş",width=12,fg="blue4")
lbl_aayran=Label(f1,font=("aria",20,'bold'),text="AçikAyran",width=12,fg="blue4")
lbl_kola=Label(f1,font=("aria",20,'bold'),text="Kola",width=12,fg="blue4")
lbl_su=Label(f1,font=("aria",20,'bold'),text="Su",width=12,fg="blue4")

lbl_Ciğer.grid(row=1,column=0)
lbl_adana.grid(row=2,column=0)
lbl_urfa.grid(row=3,column=0)
lbl_tavukşiş.grid(row=4,column=0)
lbl_aayran.grid(row=5,column=0)
lbl_kola.grid(row=6,column=0)
lbl_su.grid(row=7,column=0)

#Entry
entry_ciğer=Entry(f1,font=("aria",20,'bold'),textvariable=Ciğer,bd=6,width=8,bg="lightpink")
entry_adana=Entry(f1,font=("aria",20,'bold'),textvariable=Adana,bd=6,width=8,bg="lightpink")
entry_urfa=Entry(f1,font=("aria",20,'bold'),textvariable=Urfa,bd=6,width=8,bg="lightpink")
entry_tavukşiş=Entry(f1,font=("aria",20,'bold'),textvariable=TavukŞiş,bd=6,width=8,bg="lightpink")
entry_aayran=Entry(f1,font=("aria",20,'bold'),textvariable=AçikAyran,bd=6,width=8,bg="lightpink")
entry_kola=Entry(f1,font=("aria",20,'bold'),textvariable=Kola,bd=6,width=8,bg="lightpink")
entry_su=Entry(f1,font=("aria",20,'bold'),textvariable=Su,bd=6,width=8,bg="lightpink")

entry_ciğer.grid(row=1,column=1)
entry_adana.grid(row=2,column=1)
entry_urfa.grid(row=3,column=1)
entry_tavukşiş.grid(row=4,column=1)
entry_aayran.grid(row=5,column=1)
entry_kola.grid(row=6,column=1)
entry_su.grid(row=7,column=1)

#buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
