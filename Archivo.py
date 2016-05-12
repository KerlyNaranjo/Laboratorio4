#crear un archivo de texto 

def leertxt():
	archi=open('texto.txt','r')
	linea=archi.readline()
	while linea!="":
		print linea
		linea=archi.readline()
archi.close()