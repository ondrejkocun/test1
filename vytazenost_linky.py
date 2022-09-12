import tkinter
canvas = tkinter.Canvas()
canvas.pack()

subor=open('vytazenost_autobusovej_linky.txt','r',encoding='utf-8')

kapacita=0
plus=[]
minus=[]
zastavky=[]
poc=1
hocico=0
farba=' '
for riadok in subor:
    riadok=riadok.split()
    if len(riadok)==1:
        kapacita=int(riadok[0])
    else:
        plus.append(int(riadok[0]))
        minus.append(int(riadok[1]))
    zastavky.append(riadok[2:])
def volaco(event):
    global poc,hocico,farba
    if poc<len(zastavky):
        canvas.create_text(50,poc*25+10,text=zastavky[poc],anchor='w')
        canvas.create_rectangle(130,poc*25,230,poc*25+20,)
        hocico=hocico+(int(plus[poc-1])-int(minus[poc-1]))
        print(hocico)
        if hocico>50:
            farba='red'
        else:
            farba='green'
        canvas.create_rectangle(130,poc*25,130+hocico*2,poc*25+20,fill=farba)
        poc+=1
canvas.bind('<Button>',volaco)
    
