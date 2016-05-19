#Traductor de un texto ingles a español
import goslate
with open('text.txt', 'r') as f:
	novel_text = f.read()
gs = goslate.Goslate()
print(gs.translate(novel_text,'es'))