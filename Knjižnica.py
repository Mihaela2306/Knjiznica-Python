#seminarski rad, Mihaela Čalogović, 3.5

from tkinter import*
from operator import itemgetter

izbornik=Tk()
izbornik.title("Knjižnica")
izbornik.geometry("444x250+100+100")

C1=Canvas(izbornik,height=250,width=444)
filename1=PhotoImage(file="simple1.gif")
C1.create_image(222,125,image=filename1)
C1.create_text(222,50,text="Dobro došli u knjižnicu!",font=("Times",25))
C1.create_text(100,237,text="Napravila: Mihaela Čalogović, 3.5",font=("Times",10))

popis=[["August","Šenoa","Zlatarevo zlato","aaa","123","Posuđeno"],["Matthew","Skelton","Endymion Spring","bbb","456","Posuđeno"],["J. K.","Rowling","Harry Potter i zatočenik Azkabana","ccc","789","Posuđeno"],["Marin","Držić","Skup","ddd","101112","Posuđeno"],["Antun Gustav","Matoš","Camao","eee","131415","Posuđeno"],["William","Shakespeare","Hamlet","fff","161718","Posuđeno"],["Ivan","Mažuranić","Smrt Smail-Age Čengića","ggg","192021","Posuđeno"],["Honore de","Balzac","Čiča Goriot","hhh","222324","Posuđeno"],["Gustave","Flaubert","Gospođa Bovary","iii","252627","Posuđeno"],["Nikolaj Vasiljevič","Gogolj","Kabanica","jjj","282930","Posuđeno"],["Lav Nikolajevič","Tolstoj","Zločin i kazna","kkk","313233","Dostupno"],["August","Šenoa","Prijan Lovro","lll","343536","Dostupno"],["Ante","Kovačić","U registraturi","mmm","373839","Dostupno"],["Eugen","Kumičić","Urota zrinsko-frankopanska","nnn","404142","Dostupno"],["Josip","Kozarac","Tena","ooo","434445","Dostupno"],["Ksaver Šandor","Gjalski","Pod starim krovovima","ppp","464748","Dostupno"],["Vjenceslav","Novak","Posljednji Stipančići","rrr","495051","Dostupno"],["Silvije S.","Kranjčević","Gospodskomu Kastoru","sss","525354","Dostupno"],["Janko","Leskovar","Misao na vječnost","ttt","555657","Dostupno"],["Ivo","Vojnović","Dubrovačka trilogija","uuu","585960","Dostupno"]]

def Upis():
   global Ime
   global Prezime
   global Naslov
   global Šifra
   global Pozicija
   global popis
   global UpisKnjige
   global EntryImeAutora
   global EntryPrezimeAutora
   global EntryNaslovKnjige
   global EntryŠifraKnjige
   global EntryPozicijaKnjige
   global ImeStr
   global PrezimeStr
   global NaslovStr
   global ŠifraStr
   global PozicijaStr
   global status
   
   UpisKnjige.withdraw()

   Ime=EntryImeAutora.get()
   Prezime=EntryPrezimeAutora.get()
   Naslov=EntryNaslovKnjige.get()
   Šifra=EntryŠifraKnjige.get()
   Pozicija=EntryPozicijaKnjige.get()
   
   ImeStr=str(Ime)
   PrezimeStr=str(Prezime)
   NaslovStr=str(Naslov)
   ŠifraStr=str(Šifra)
   PozicijaStr=str(Pozicija)

   status="Dostupno"

   popis=popis+[[ImeStr,PrezimeStr,NaslovStr,ŠifraStr,PozicijaStr,status]]

def Potvrdi1():
   global popis
   global Knjiga
   global OtpisKnjige1

   OtpisKnjige1.withdraw()
   
   del popis[Knjiga]

def Odustani1():
   global popis
   global OtpisKnjige1
   
   OtpisKnjige1.withdraw()

def Otpis():
   global popis
   global Knjiga
   global OtpisKnjige
   global EntryŠifraKnjige1
   global OtpisKnjige1
   global C4
   global filename4

   OtpisKnjige.withdraw()

   OtpisKnjige1=Toplevel(izbornik)

   C4=Canvas(OtpisKnjige1,height=370,width=370)
   filename4=PhotoImage(file="simple3.gif")
   C4.create_image(185,185,image=filename4)

   Šifra1=EntryŠifraKnjige1.get()
   ŠifraStr1=str(Šifra1)

   Knjiga=""

   for i in popis:
      for j in i:
         if j==ŠifraStr1:
            Knjiga=popis.index(i)
         else:
            continue

   C4.create_text(185,30,text="Ime Autora:",font=("Times",15))
   C4.create_text(185,50,text=popis[Knjiga][0],font=("Times",15))

   C4.create_text(185,80,text="Prezime Autora:",font=("Times",15))
   C4.create_text(185,100,text=popis[Knjiga][1],font=("Times",15))

   C4.create_text(185,130,text="Naslov Knjige:",font=("Times",15))
   C4.create_text(185,150,text=popis[Knjiga][2],font=("Times",15))

   C4.create_text(185,180,text="Šifra Knjige:",font=("Times",15))
   C4.create_text(185,200,text=popis[Knjiga][3],font=("Times",15))

   C4.create_text(185,230,text="Pozicija Knjige:",font=("Times",15))
   C4.create_text(185,250,text=popis[Knjiga][4],font=("Times",15))

   gumb4=Button(C4,text="Potvrdi Otpis",width=12,height=1,command=Potvrdi1)
   gumb4.bind("<Button>")
   gumb4_window=C4.create_window(77,300,anchor=NW,window=gumb4)

   gumb5=Button(C4,text="Odustani",width=12,height=1,command=Odustani1)
   gumb5.bind("<Button>")
   gumb5_window=C4.create_window(197,300,anchor=NW,window=gumb5)

   C4.pack()

def gumbAkcija1(event):
   global UpisKnjige
   global EntryImeAutora
   global EntryPrezimeAutora
   global EntryNaslovKnjige
   global EntryŠifraKnjige
   global EntryPozicijaKnjige
   global C2
   global filename2

   UpisKnjige=Toplevel(izbornik)

   C2=Canvas(UpisKnjige,height=310,width=310)
   filename2=PhotoImage(file="simple4.gif")
   C2.create_image(155,155,image=filename2)
   
   C2.create_text(155,20,text="\nIme Autora:",font=("Times",18))
   EntryImeAutora=Entry(UpisKnjige)
   EntryImeAutora.pack()
   C2.create_window(155,60,window=EntryImeAutora)

   C2.create_text(155,70,text="\nPrezime Autora:",font=("Times",18))
   EntryPrezimeAutora=Entry(UpisKnjige)
   EntryPrezimeAutora.pack()
   C2.create_window(155,110,window=EntryPrezimeAutora)

   C2.create_text(155,120,text="\nNaslov Knjige:",font=("Times",18))
   EntryNaslovKnjige=Entry(UpisKnjige)
   EntryNaslovKnjige.pack()
   C2.create_window(155,160,window=EntryNaslovKnjige)

   C2.create_text(155,170,text="\nŠifra Knjige:",font=("Times",18))
   EntryŠifraKnjige=Entry(UpisKnjige)
   EntryŠifraKnjige.pack()
   C2.create_window(155,210,window=EntryŠifraKnjige)

   C2.create_text(155,220,text="\nPozicija Knjige:",font=("Times",18))
   EntryPozicijaKnjige=Entry(UpisKnjige)
   EntryPozicijaKnjige.pack()
   C2.create_window(155,260,window=EntryPozicijaKnjige)

   gumb7=Button(C2,text="Submit",command=Upis)
   gumb7.bind("<Button>")
   gumb7_window=C2.create_window(130,275,anchor=NW,window=gumb7)
   
   C2.pack()

def gumbAkcija2(event):
   global EntryŠifraKnjige1
   global OtpisKnjige
   global C3
   global filename3

   OtpisKnjige=Toplevel(izbornik)

   C3=Canvas(OtpisKnjige,height=150,width=350)
   filename3=PhotoImage(file="simple2.gif")
   C3.create_image(152,100,image=filename3)

   C3.create_text(182,20,text="\nŠifra Knjige:",font=("Times",18))
   EntryŠifraKnjige1=Entry(OtpisKnjige)
   EntryŠifraKnjige1.pack()
   C3.create_window(182,70,window=EntryŠifraKnjige1)

   gumb3=Button(C3,text="Potvrdi",command=Otpis)
   gumb3.bind("<Button>")
   gumb3_window=C3.create_window(157,100,anchor=NW,window=gumb3)

   C3.pack()

def Potvrdi2():
   global PosuđivanjeKnjige1
   global popis
   global Knjiga1

   PosuđivanjeKnjige1.withdraw()

   for i in popis[Knjiga1]:
      if i=="Dostupno":
         del popis[Knjiga1][5]
         popis[Knjiga1]+=["Posuđeno"]
      else:
         continue

def Odustani2():
   global popis
   global PosuđivanjeKnjige1
   
   PosuđivanjeKnjige1.withdraw()

def Posuđivanje():
   global EntryŠifraKnjige2
   global PosuđivanjeKnjige
   global PosuđivanjeKnjige1
   global Knjiga1
   global C6
   global filename6

   PosuđivanjeKnjige.withdraw()

   PosuđivanjeKnjige1=Toplevel(izbornik)

   C6=Canvas(PosuđivanjeKnjige1,height=370,width=370)
   filename6=PhotoImage(file="simple3.gif")
   C6.create_image(185,185,image=filename6)

   Šifra2=EntryŠifraKnjige2.get()
   ŠifraStr2=str(Šifra2)

   Knjiga1=""

   for i in popis:
      for j in i:
         if j==ŠifraStr2:
            Knjiga1=popis.index(i)
         else:
            continue

   C6.create_text(185,30,text="Ime Autora:",font=("Times",15))
   C6.create_text(185,50,text=popis[Knjiga1][0],font=("Times",15))

   C6.create_text(185,80,text="Prezime Autora:",font=("Times",15))
   C6.create_text(185,100,text=popis[Knjiga1][1],font=("Times",15))

   C6.create_text(185,130,text="Naslov Knjige:",font=("Times",15))
   C6.create_text(185,150,text=popis[Knjiga1][2],font=("Times",15))

   C6.create_text(185,180,text="Šifra Knjige:",font=("Times",15))
   C6.create_text(185,200,text=popis[Knjiga1][3],font=("Times",15))

   C6.create_text(185,230,text="Pozicija Knjige:",font=("Times",15))
   C6.create_text(185,250,text=popis[Knjiga1][4],font=("Times",15))

   gumb9=Button(C6,text="Potvrdi posudbu",width=12,height=1,command=Potvrdi2)
   gumb9.bind("<Button>")
   gumb9_window=C6.create_window(77,300,anchor=NW,window=gumb9)

   gumb10=Button(C6,text="Odustani",width=12,height=1,command=Odustani2)
   gumb10.bind("<Button>")
   gumb10_window=C6.create_window(197,300,anchor=NW,window=gumb10)

   C6.pack()

def gumbAkcija3():
   global EntryŠifraKnjige2
   global PosuđivanjeKnjige
   global C5
   global filename5
   
   PosuđivanjeKnjige=Toplevel(izbornik)

   C5=Canvas(PosuđivanjeKnjige,height=150,width=350)
   filename5=PhotoImage(file="simple2.gif")
   C5.create_image(152,100,image=filename5)

   C5.create_text(182,20,text="\nŠifra Knjige:",font=("Times",18))
   EntryŠifraKnjige2=Entry(PosuđivanjeKnjige)
   EntryŠifraKnjige2.pack()
   C5.create_window(182,70,window=EntryŠifraKnjige2)

   gumb8=Button(C5,text="Potvrdi",command=Posuđivanje)
   gumb8.bind("<Button>")
   gumb8_window=C5.create_window(157,100,anchor=NW,window=gumb8)

   C5.pack()

def Potvrdi3():
   global VraćanjeKnjige1
   global popis
   global Knjiga2

   VraćanjeKnjige1.withdraw()

   for i in popis[Knjiga2]:
      if i=="Posuđeno":
         del popis[Knjiga2][5]
         popis[Knjiga2]+=["Dostupno"]
      else:
         continue

def Odustani3():
   global popis
   global VraćanjeKnjige1
   
   VraćanjeKnjige1.withdraw()

def Vraćanje():
   global EntryŠifraKnjige3
   global VraćanjeKnjige
   global VraćanjeKnjige1
   global Knjiga2
   global C8
   global filename8

   VraćanjeKnjige.withdraw()

   VraćanjeKnjige1=Toplevel(izbornik)

   C8=Canvas(VraćanjeKnjige1,height=370,width=370)
   filename8=PhotoImage(file="simple3.gif")
   C8.create_image(185,185,image=filename8)

   Šifra3=EntryŠifraKnjige3.get()
   ŠifraStr3=str(Šifra3)

   Knjiga2=""

   for i in popis:
      for j in i:
         if j==ŠifraStr3:
            Knjiga2=popis.index(i)
         else:
            continue

   C8.create_text(185,30,text="Ime Autora:",font=("Times",15))
   C8.create_text(185,50,text=popis[Knjiga2][0],font=("Times",15))

   C8.create_text(185,80,text="Prezime Autora:",font=("Times",15))
   C8.create_text(185,100,text=popis[Knjiga2][1],font=("Times",15))

   C8.create_text(185,130,text="Naslov Knjige:",font=("Times",15))
   C8.create_text(185,150,text=popis[Knjiga2][2],font=("Times",15))

   C8.create_text(185,180,text="Šifra Knjige:",font=("Times",15))
   C8.create_text(185,200,text=popis[Knjiga2][3],font=("Times",15))

   C8.create_text(185,230,text="Pozicija Knjige:",font=("Times",15))
   C8.create_text(185,250,text=popis[Knjiga2][4],font=("Times",15))

   gumb13=Button(C8,text="Potvrdi povrat",width=12,height=1,command=Potvrdi3)
   gumb13.bind("<Button>")
   gumb13_window=C8.create_window(77,300,anchor=NW,window=gumb13)

   gumb14=Button(C8,text="Odustani",width=12,height=1,command=Odustani3)
   gumb14.bind("<Button>")
   gumb14_window=C8.create_window(197,300,anchor=NW,window=gumb14)

   C8.pack()

def gumbAkcija4():
   global EntryŠifraKnjige3
   global VraćanjeKnjige
   global C7
   global filename7
   
   VraćanjeKnjige=Toplevel(izbornik)

   C7=Canvas(VraćanjeKnjige,height=150,width=350)
   filename7=PhotoImage(file="simple2.gif")
   C7.create_image(152,100,image=filename7)

   C7.create_text(182,20,text="\nŠifra Knjige:",font=("Times",18))
   EntryŠifraKnjige3=Entry(VraćanjeKnjige)
   EntryŠifraKnjige3.pack()
   C7.create_window(182,70,window=EntryŠifraKnjige3)

   gumb12=Button(C7,text="Potvrdi",command=Vraćanje)
   gumb12.bind("<Button>")
   gumb12_window=C7.create_window(157,100,anchor=NW,window=gumb12)

   C7.pack()

def gumbAkcija5():
   global popis
   global IspisTablice
   global C11
   global filename11
   global visina_scrollbar

   IspisTablice=Toplevel(izbornik)

   okvir=LabelFrame(IspisTablice)
   okvir.pack()
   C11=Canvas(okvir,height=425,width=852,scrollregion=(0,0,425,70+len(popis)*20))
   filename11=PhotoImage(file="simple6.gif")
   C11.create_image(425,241,image=filename11)
   C11.pack(side="left")
   visina_scrollbar=Scrollbar(okvir,orient=VERTICAL)
   visina_scrollbar.pack(side="left",fill=Y)
   visina_scrollbar.config(command=C11.yview)

   C11.create_text(60,20,text="Ime Autora",font=("Times",12,"bold"))
   C11.create_text(180,20,text="Prezime Autora",font=("Times",12,"bold"))
   C11.create_text(360,20,text="Naslov Knjige",font=("Times",12,"bold"))
   C11.create_text(545,20,text="Šifra Knjige",font=("Times",12,"bold"))
   C11.create_text(665,20,text="Pozicija Knjige",font=("Times",12,"bold"))
   C11.create_text(780,20,text="Status Knjige",font=("Times",12,"bold"))

   PopisPosuđeno=[]
   PopisDostupno=[]

   for i in popis:
      for j in i:
         if j=="Posuđeno":
            PopisPosuđeno=PopisPosuđeno+[i]
         elif j=="Dostupno":
            PopisDostupno=PopisDostupno+[i]

   PopisDostupno=sorted(PopisDostupno,key=itemgetter(1))

   a=50
   
   for i in PopisDostupno:
      for j in i:
         if (i.index(j))==0:
            C11.create_text(60,a,text=j,font=("Times",12))
         elif (i.index(j))==1:
            C11.create_text(180,a,text=j,font=("Times",12))
         elif (i.index(j))==2:
            C11.create_text(360,a,text=j,font=("Times",12))
         elif (i.index(j))==3:
            C11.create_text(545,a,text=j,font=("Times",12))
         elif (i.index(j))==4:
            C11.create_text(665,a,text=j,font=("Times",12))
         elif (i.index(j))==5:
            C11.create_text(780,a,text=j,font=("Times",12))
      a=a+20

   PopisPosuđeno=sorted(PopisPosuđeno,key=itemgetter(1))

   a=a+20

   for i in PopisPosuđeno:
      for j in i:
         if (i.index(j))==0:
            C11.create_text(60,a,text=j,font=("Times",12))
         elif (i.index(j))==1:
            C11.create_text(180,a,text=j,font=("Times",12))
         elif (i.index(j))==2:
            C11.create_text(360,a,text=j,font=("Times",12))
         elif (i.index(j))==3:
            C11.create_text(545,a,text=j,font=("Times",12))
         elif (i.index(j))==4:
            C11.create_text(665,a,text=j,font=("Times",12))
         elif (i.index(j))==5:
            C11.create_text(780,a,text=j,font=("Times",12))
      a=a+20

def Završi():
   global Pretraživanje1

   Pretraživanje1.withdraw()

def NovaPretraga():
   global C13
   global filename13
   global Pretraživanje
   global Pretraživanje1
   global EntryImeAutora1
   global EntryPrezimeAutora1
   global EntryNaslovKnjige1

   Pretraživanje1.withdraw()

   Pretraživanje=Toplevel(izbornik)

   C13=Canvas(Pretraživanje,height=225,width=400)
   filename13=PhotoImage(file="simple5.gif")
   C13.create_image(200,125,image=filename13)

   C13.create_text(200,20,text="\nIme Autora:",font=("Times",18))
   EntryImeAutora1=Entry(Pretraživanje)
   EntryImeAutora1.pack()
   C13.create_window(200,60,window=EntryImeAutora1)

   C13.create_text(200,75,text="\nPrezime Autora:",font=("Times",18))
   EntryPrezimeAutora1=Entry(Pretraživanje)
   EntryPrezimeAutora1.pack()
   C13.create_window(200,115,window=EntryPrezimeAutora1)

   C13.create_text(200,130,text="\nNaslov Knjige:",font=("Times",18))
   EntryNaslovKnjige1=Entry(Pretraživanje)
   EntryNaslovKnjige1.pack()
   C13.create_window(200,170,window=EntryNaslovKnjige1)

   gumb20=Button(C13,text="Pretraži",command=Traži)
   gumb20.bind("<Button>")
   gumb20_window=C13.create_window(175,195,anchor=NW,window=gumb20)

   C13.pack()

def Traži():
   global Pretraživanje
   global Pretraživanje1
   global EntryImeAutora1
   global EntryPrezimeAutora1
   global EntryNaslovKnjige1
   global Ime1
   global Prezime1
   global Naslov1
   global ImeStr1
   global PrezimeStr1
   global NaslovStr1
   global popis1
   global C12
   global filename12

   Pretraživanje.withdraw()
   Pretraživanje1=Toplevel(izbornik)

   Ime1=EntryImeAutora1.get()
   Prezime1=EntryPrezimeAutora1.get()
   Naslov1=EntryNaslovKnjige1.get()
   
   ImeStr1=str(Ime1)
   PrezimeStr1=str(Prezime1)
   NaslovStr1=str(Naslov1)

   popis1=[]

   for i in popis:
      for j in i:
         if j==ImeStr1 or j==PrezimeStr1 or j==NaslovStr1:
            popis1=popis1+[i]

   popis2=[]
   [popis2.append(x) for x in popis1 if x not in popis2]

   okvir1=LabelFrame(Pretraživanje1)
   okvir1.pack()
   C12=Canvas(okvir1,height=425,width=852,scrollregion=(0,0,425,70+len(popis1)*20))
   filename12=PhotoImage(file="simple6.gif")
   C12.create_image(425,241,image=filename12)
   C12.pack(side="left")
   visina_scrollbar1=Scrollbar(okvir1,orient=VERTICAL)
   visina_scrollbar1.pack(side="left",fill=Y)
   visina_scrollbar1.config(command=C12.yview)

   C12.create_text(60,20,text="Ime Autora",font=("Times",12,"bold"))
   C12.create_text(180,20,text="Prezime Autora",font=("Times",12,"bold"))
   C12.create_text(360,20,text="Naslov Knjige",font=("Times",12,"bold"))
   C12.create_text(545,20,text="Šifra Knjige",font=("Times",12,"bold"))
   C12.create_text(665,20,text="Pozicija Knjige",font=("Times",12,"bold"))
   C12.create_text(780,20,text="Status Knjige",font=("Times",12,"bold"))

   popis2=sorted(popis2,key=itemgetter(1))

   a=50

   for i in popis2:
      for j in i:
         if (i.index(j))==0:
            C12.create_text(60,a,text=j,font=("Times",12))
         elif (i.index(j))==1:
            C12.create_text(180,a,text=j,font=("Times",12))
         elif (i.index(j))==2:
            C12.create_text(360,a,text=j,font=("Times",12))
         elif (i.index(j))==3:
            C12.create_text(545,a,text=j,font=("Times",12))
         elif (i.index(j))==4:
            C12.create_text(665,a,text=j,font=("Times",12))
         elif (i.index(j))==5:
            C12.create_text(780,a,text=j,font=("Times",12))
      a=a+20

   gumb18=Button(C12,text="Nova pretraga",width=12,height=1,command=NovaPretraga)
   gumb18.bind("<Button>")
   gumb18_window=C12.create_window(276,390,anchor=NW,window=gumb18)

   gumb19=Button(C12,text="Završi",width=12,height=1,command=Završi)
   gumb19.bind("<Button>")
   gumb19_window=C12.create_window(576,390,anchor=NW,window=gumb19)

def gumbAkcija6():
   global C9
   global filename9
   global Pretraživanje
   global EntryImeAutora1
   global EntryPrezimeAutora1
   global EntryNaslovKnjige1

   Pretraživanje=Toplevel(izbornik)

   C9=Canvas(Pretraživanje,height=225,width=400)
   filename9=PhotoImage(file="simple5.gif")
   C9.create_image(200,125,image=filename9)

   C9.create_text(200,20,text="\nIme Autora:",font=("Times",18))
   EntryImeAutora1=Entry(Pretraživanje)
   EntryImeAutora1.pack()
   C9.create_window(200,60,window=EntryImeAutora1)

   C9.create_text(200,75,text="\nPrezime Autora:",font=("Times",18))
   EntryPrezimeAutora1=Entry(Pretraživanje)
   EntryPrezimeAutora1.pack()
   C9.create_window(200,115,window=EntryPrezimeAutora1)

   C9.create_text(200,130,text="\nNaslov Knjige:",font=("Times",18))
   EntryNaslovKnjige1=Entry(Pretraživanje)
   EntryNaslovKnjige1.pack()
   C9.create_window(200,170,window=EntryNaslovKnjige1)

   gumb17=Button(C9,text="Pretraži",command=Traži)
   gumb17.bind("<Button>")
   gumb17_window=C9.create_window(175,195,anchor=NW,window=gumb17)

   C9.pack()
   
gumb1=Button(C1,text="Upis nove knjige",width=14,height=1)
gumb1.bind("<Button>",gumbAkcija1)
gumb1_window=C1.create_window(40,100,anchor=NW,window=gumb1)

gumb2=Button(C1,text="Otpis knjige",width=14,height=1)
gumb2.bind("<Button>",gumbAkcija2)
gumb2_window=C1.create_window(40,155,anchor=NW,window=gumb2)

gumb6=Button(C1,text="Posuđivanje knjige",width=14,height=1,command=gumbAkcija3)
gumb6.bind("<Button>")
gumb6_window=C1.create_window(173,100,anchor=NW,window=gumb6)

gumb11=Button(C1,text="Vraćanje knjige",width=14,height=1,command=gumbAkcija4)
gumb11.bind("<Button>")
gumb11_window=C1.create_window(173,155,anchor=NW,window=gumb11)

gumb16=Button(C1,text="Ispis Knjiga",width=14,height=1,command=gumbAkcija5)
gumb16.bind("<Button>")
gumb16_window=C1.create_window(304,100,anchor=NW,window=gumb16)

gumb15=Button(C1,text="Pretraživanje",width=14,height=1,command=gumbAkcija6)
gumb15.bind("<Button>")
gumb15_window=C1.create_window(304,155,anchor=NW,window=gumb15)

C1.pack()

izbornik.mainloop()
