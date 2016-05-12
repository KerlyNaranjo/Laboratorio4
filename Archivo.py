#crear un archivo de texto 

def creartxt():
	archi=open('texto.txt', 'w')
	archi.close()

#def contador():
	#return  (len(frase.split(" "))

def escribirtxt():
	archi=open('texto.txt','w')
	frase=archi.write (str(input("ingresar una frase:")))
	#archi.write('HOLA MUNDO COMO ESTAS!!!\n')
	archi.write(len(frase.split(" ")))
	archi.close()

def grabartxt():
	archi=open('texto.txt','a')
	archi.close()

creartxt()
escribirtxt()
grabartxt()