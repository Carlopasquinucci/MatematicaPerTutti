import tkinter as tk
from random import randint
import pymsgbox
import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def risultato(c, response):
# Calcola se il risultato è corretto, scrive sul file del giorno se l'operazione è stata svolta correttamente 1, altrimenti 0  (TO DO difficoltà più elevata= risultato più elevato, tipo 2-3-4)
	continua=True
	date_object = datetime.date.today()
	nomefile="giorni/"+str(date_object)
	f= open(nomefile,"a")
	if str(c)==response:
			pymsgbox.alert('Corretto', 'Risultato')
			f.write(str(1)+" ")
			continua=False
	else:
			pymsgbox.alert('Sbagliato', 'Risultato')
			restart=pymsgbox.confirm('Vuoi provare un nuovo risultato?', 'Continua')
			f.write(str(0)+" ")
			if restart!='OK':
				continua=False
				pymsgbox.alert('Il risultato corretto è '+str(c), 'Risultato')
	f.close()
	return continua
def somma():
#esegue la somma
	naddendi=randint(2,5)
	lista=[]
	a=randint(0,10)
	lista.append(a)
	stringa='Quanto fa '+str(a)	
	for i in range(0,naddendi):
		a=randint(0,10)
		stringa=stringa+'+'+str(a)
		lista.append(a)
	stringa=stringa+' ?'
	c=sum(lista)

	continua=True
	while continua:
			response = pymsgbox.prompt(stringa)
			continua=risultato(c, response)

def sottrazione():
#esegue la sottrazione, con il secondo termine minore del primo termine (i risultato è sempre un numero positivo)
	a=randint(0,10)
	b=randint(a,10)
	continua=True
	c=b-a
	while continua:
		response = pymsgbox.prompt('Quanto fa '+str(b)+'-'+str(a)+'?')
		continua=risultato(c, response)
		
def sommmaesottrazione():
#Esegue una espressione contenente randomicamente somme e sottrazioni
	naddendi=randint(2,5)
	lista=[]
	a=randint(0,10)
	lista.append(a)
	stringa='Quanto fa '+str(a)	
	for i in range(0,naddendi):
		a=randint(-10,10)
		lista.append(a)
		if a<0:
			stringa=stringa+'-'+str(a)
		else:
			stringa=stringa+'+'+str(a)		
	print(lista)
	stringa=stringa+' ?'
	c=sum(lista)

	continua=True

	while continua:
			response = pymsgbox.prompt(stringa)
			continua=risultato(c, response)
		
def moltiplicazione():
	naddendi=randint(2,2)
	lista=[]
	c=randint(0,10)
	stringa='Quanto fa '+str(c)	
	for i in range(0,naddendi):
		a=randint(0,10)
		stringa=stringa+'x'+str(a)
		c=c*a
	stringa=stringa+' ?'

	continua=True
	while continua:
			response = pymsgbox.prompt(stringa)
			continua=risultato(c, response)
			
def divisioneconvirgola():
#esegue la divisione, il risultato è un numero decimale. Se intero, scrive il numero seguito da ".0"
	a=randint(0,10)
	b=randint(a,10)
	c=b/a
	continua=True
	while continua:
		response = pymsgbox.prompt('Quanto fa '+str(b)+'/'+str(a)+'?')
		continua=risultato(c, response)
		
def divisioneintero():
#esegue la divisione avendo come risultato sempre un numero intero.
#un termine della moltiplicazione può essere maggiore di 10.
	c=randint(0,10)
	b=randint(0,10)
	a=c*b
	continua=True
	while continua:
		response = pymsgbox.prompt('Quanto fa '+str(a)+'/'+str(b)+'?')
		continua=risultato(c, response)
		

def trovaoperazioni():
#Quale operazione è stata fatta?
	operazione=randint(0,2) #0 somma, 1 sottrazione , 2 moltiplicazione 
	a=randint(1,10)
	b=randint(1,a)
	if operazione==0:
		d=a+b
		c='+'
	elif operazione==1:
		d=a-b
		c='-'
	elif operazione==2:	
		d=a*b
		c='x'
	stringa= str(a)+'    ......    '+str(b)+'='+str(d) +' Quale operazione è stata eseguita? "+", "-" o "x"?'
	
	continua=True
	while continua:
			response = pymsgbox.prompt(stringa)
			continua=risultato(c, response)
	
def confronto():
	a=randint(0,40)
	b=randint(0,40)
	test=randint(0,1) #0 cerca il maggiore, 1 cerca il minore
	c="Vero"
	if test==0:
		stringa=' > '
		if a<=b:
			c='Falso'
	else:
		stringa=' < '
		if a>=b:
			c='Falso'
		
	continua=True
	while continua:
		response = pymsgbox.prompt(str(a)+stringa+str(b)+'. Vero o Falso?')
		continua=risultato(c, response)
		
def numsuccessivo():
	a=randint(0,40)
	c="Vero"
	if a<=b:
		c="Falso"
	
	continua=True
	while continua:
		response = pymsgbox.prompt(str(a)+' > '+str(b)+'?')
		continua=risultato(c, response)
		
def numprecosuccess():  #numero precedente o successivo?
	a=randint(0,40)
	test=randint(0,1) #0 sucessivo, 1 precedente
	c=a+1
	stringa=" dopo di "
	if test==1:
			c=a-1
	stringa=" prima di "
	continua=True
	while continua:
		response = pymsgbox.prompt('Quale numero viene'+stringa+str(a)+' ?')
		continua=risultato(c, response)
	
def completalaserie():  #inserisci il numero successivo
	"""
	numerodipassi=randint(1,3)
	listpasso2=list()
	listaa=list()
	a=randint(0,5)
	print(a)
	listaa.append(a)
	stringa='Completa la serie: '
	for i in range(0,numerodipassi):
		stringa=stringa+str(a)+"; "
		passo2=randint(-5,5)
		a=a+passo2
		listpasso2.append(passo2)
		listaa.append(a)


	print(stringa)
	print(listpasso2)
	print(listaa)
	c=listaa[numerodipassi]
	print(c)
	"""
	
	passo=randint(0,5)
	a=randint(-5,5)
	b=a+passo
	d=b+passo
	c=d+passo
	continua=True
	while continua:
		response = pymsgbox.prompt('Completa la serie: '+str(a)+'; '+str(b)+'; '+str(d)+'; ...')
		continua=risultato(c, response)
	
"""		
def equazioni2grado():

	d=-1
	while d< 0:
		a=randint(-10,10)
		b=randint(-10,10)
		c=randint(-10,10)
		d = (b ** 2) - (4 * a * c)
	aux=sqrt(d)
	num1 = -b +aux
	num2 = -b -aux
	denum = 2*a
	x1=num1/denum
	x2=num2/denum
	continua=True
	res=str(x1)+"_"+str(x2)
	while continua:
		response = pymsgbox.prompt('Risolvi '+str(a)+'x2+'+str(b)+'x'+str(c)+'=0 /n .Sciriv il risultato come x1_x2 con x1>x2.')
		continua=risultato(res, response)
"""

		
def statistiche():

     
	fgiorni=(os.listdir('giorni'))
	ngiorni=len(fgiorni)
	
	f= open('statistica/all.csv',"w")
#	f.close
	listasomme=[]
	listapercent=[]
	listatentativi=[]
	#cicla su i vari file dei giorni
	for i in fgiorni:

		with open('giorni/'+i, 'r') as file:
			content = file.read()
			splitted=content.split(' ')
			j=len(splitted) #numero totale di tentativi per quel giorno
			summe=0
			#somma tutti gli i risultati positivi
			for k in range(0,j-1):
				summe=summe+int(splitted[k])
#			f.writelines(i+","+str(summe)+"\n")
			percent=int(summe/j*100) #percetnuale dirisultati corretti e tentativi effettuati
			listasomme.append(summe)
			listapercent.append(percent)
			listatentativi.append(j)
			
	x_pos = np.arange(ngiorni)
	fig, axes = plt.subplots(nrows=1, ncols=3)
	ax0, ax1 ,ax2 = axes.flatten()
	
	ax0.bar(fgiorni, listatentativi, width=0.5)
	ax0.set_title('Tentativi al giorno')
	
	ax1.bar(fgiorni, listasomme, width=0.5)
	ax1.set_title('Risultati corretti al giorno')
	

	ax2.bar(fgiorni, listapercent, width=0.5)
	ax2.set_title('Percentuale risultati corretti [%]')
	

	plt.savefig("statistica/Result.png", dpi=150, transparent=False)
	plt.show()

	
def help():
    pymsgbox.alert("Clicca sul pulsante dell'operazione che vuoi imparare.\n Per ogni risultato corretto ricevi un punto.\n Sulle statistiche vedrei i tuoi miglioramenti giorno per giorno")
"""
def quitcommand():
	quit()
"""
#main
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
count=0
date_object = datetime.date.today()

nomefile="giorni/"+str(date_object)

if os.path.exists('giorni')==False:
	 os.mkdir('giorni')



if os.path.isfile(nomefile):
	f= open(nomefile,"a")
else :
	f= open(nomefile,"w")
#	f.write(str(date_object)+",")

commandhelp = tk.Button(frame,
                   text="Istruzioni",
				   fg="blue",
                   command=help)
commandhelp.pack(side=tk.LEFT)


statistiche = tk.Button(frame,
                   text="Statistiche utilizzo",
				   fg="red",
                   command=statistiche)
statistiche.pack(side=tk.RIGHT)






"""
button = tk.Button(frame, 
                   text="ESCI", 
                   fg="red",
                   command=quitcommand)
button.pack(side=tk.RIGHT)
"""
commandsomma = tk.Button(frame,
                   text="Somma",
                   command=somma)
commandsomma.pack(side=tk.LEFT)

commandsottrazione = tk.Button(frame,
                   text="Sottrazione",
                   command=sottrazione)
commandsottrazione.pack(side=tk.LEFT)

commandmoltiplicazione = tk.Button(frame,
                   text="Moltiplicazione",
                   command=moltiplicazione)
commandmoltiplicazione.pack(side=tk.LEFT)

commanddivisione = tk.Button(frame,
                   text="Divisione",
                   command=divisioneconvirgola)
commanddivisione.pack(side=tk.RIGHT)

commanddivisione2 = tk.Button(frame,
                   text="Divisione con risultato intero",
                   command=divisioneintero)
commanddivisione2.pack(side=tk.RIGHT)


confronto = tk.Button(frame,
                   text="Confronto fra numeri",
                   command=confronto)
confronto.pack(side=tk.RIGHT)


sommmaesottrazione = tk.Button(frame,
                   text="Espressioni con somme e sottrazioni",
                   command=sommmaesottrazione)
sommmaesottrazione.pack(side=tk.LEFT)


numprecosuccess=tk.Button(frame,
                   text="Precedente o successivo",
                   command=numprecosuccess)
numprecosuccess.pack(side=tk.LEFT)


completalaserie=tk.Button(frame,
                   text="Completa la serie",
                   command=completalaserie)
completalaserie.pack(side=tk.LEFT)

trovaoperazionic=tk.Button(frame,
                   text="Trova l'operazione effettuata",
                   command=trovaoperazioni)
trovaoperazionic.pack(side=tk.LEFT)

"""
commandeq2grd = tk.Button(frame,
                   text="Divisione con risultato intero",
                   command=equazioni2grado)
commandeq2grd.pack(side=tk.RIGHT)
"""

f.close()


root.mainloop()
