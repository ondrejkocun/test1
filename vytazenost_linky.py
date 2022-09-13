import tkinter  #importovanie kninice
canvas = tkinter.Canvas()   nastavenie platna
canvas.pack()

subor=open('vytazenost_autobusovej_linky.txt','r',encoding='utf-8') #otvorenie textoveho subboru na citanie

kapacita=0 #deklaracia premennej na kapacitu autobusu
plus=[]     #deklaracia zoznamu na pripocitavanie cisel
minus=[]    #deklaracia zoznamu na odcitaanie cisel
zastavky=[] #deklaracia zoznamu na zastavky
poc=1       #deklaracia premmenej na pocitadlo
hocico=0    #deklaracia premmenej na vypocet cestujucich
farba=' '   #deklaracia stringu na farbu
for riadok in subor:    #cyklus na citanie riadkov v subore
    riadok=riadok.split()   #prikaz na rozdelenie riadka na medzere 
    if len(riadok)==1:      #podmienka na precitanie kapacity z textoveho suboru
        kapacita=int(riadok[0]) #nastavenie hodnoty kapacity
    else:
        plus.append(int(riadok[0])) #pridanie cisla na pripocitanie do zoznamu
        minus.append(int(riadok[1])) #pridanie cisla na odpocitanie do zoznamu
    zastavky.append(riadok[2:]) #pridanie nazvu zastavky do zoznamu   
def volaco(event):  #funkcia viazana na tlacidlo na myske 
    global poc,hocico,farba #globalne premmene
    if poc<len(zastavky):   #podmienka na kreslenie textu s grafom naplnenosti
        canvas.create_text(50,poc*25+10,text=zastavky[poc],anchor='w')  #kreslenie nazvu zastavvok
        canvas.create_rectangle(130,poc*25,230,poc*25+20,)              #kreslenie grafu bez farby
        hocico=hocico+(int(plus[poc-1])-int(minus[poc-1]))              #vypocet naplnenosti autobusu
        print(hocico)                                                   #zbytocny print sluziaci na to aby som vedel ci viem pocitat
        if hocico>50:           #podmienka urcujuca farbu na zaklade naplnenosti
            farba='red'
        else:
            farba='green'       #podmienka urcujuca farbu na zaklade naplnenosti
        canvas.create_rectangle(130,poc*25,130+hocico*2,poc*25+20,fill=farba)   #kreslenie grafu naplnenosti 
        poc+=1  #pocitadlo sa zvacsi o jedna
canvas.bind('<Button>',volaco)  #bindovanie tlacidka na myske aby spustilo fukciu 
    
