#!/usr/bin/env python3
import matplotlib.pyplot as plt
from Numbers import Numbers

def getFreque(num_list, amp):
	l=[]
	while True:
		if (num_list[0]<=amp and num_list[-1] >= amp):
			l.append(num_list[0])
			num_list.remove(num_list[0])
			pass
		else:
			break
	if (l!=[]): 
		return l
	else:
		return False

def getFrequeReL(freq, tamanho):
	return round(freq/tamanho,3) * 100

def getFrequeAclRel(freq_acl,tamanho):
	return round(freq_acl/tamanho,3) *100
	
arquivo= open("numbers/numbers.txt","r")
a = arquivo.read()
arquivo.close()

lista = list(map(int, a.split(" - ")))
sorted(lista)


tamanho = len(lista)
frequence_acl = 0
lista_frequencias=[]


minimo = int(input("Qual o valor minimo?"))
h = int(input("Qual a amplitude?"))
amp= minimo+(h-1)
for l in lista:
	if (amp < lista[-1]):
		lista_amp = getFreque(lista, amp)
		frequence = len(lista_amp)

		frequence_relative = getFrequeReL(frequence, tamanho)

		frequence_acl +=frequence

		frequence_rel_acl = getFrequeAclRel(frequence_acl, tamanho)

		frequence_object = Numbers(lista_amp, frequence, frequence_relative, frequence_acl, frequence_rel_acl)
		lista_frequencias.append(frequence_object)
		amp+= (h)

last_numbers_frequency = len(lista)
last_numbers_frequency_relative = round(last_numbers_frequency/tamanho,3)*100
last_numbers_frequency_acl = frequence_acl+ last_numbers_frequency
last_numbers_frequency_acl_relative = round(last_numbers_frequency_acl/tamanho,4)*100
last_frequence_object = Numbers(lista, last_numbers_frequency, last_numbers_frequency_relative, last_numbers_frequency_acl, last_numbers_frequency_acl_relative)

lista_frequencias.append(last_frequence_object)
lista_hist = []
lista_hist.append(minimo)
print(" "," ","Classe", " "," ", "FA", " ", "FI%", " ", "FAci", " ", "FAci%")
for x in lista_frequencias:
	for i in x.number:
		lista_hist.append(i)
		pass
	print(min(x.number),"| - ",max(x.number)," ",x.frequencia," ", x.frequencia_rel," ", x.frequencia_acl," ", x.frequencia_acl_rel)
lista_hist.append(amp)

plt.hist(lista_hist, len(lista_frequencias), rwidth=0.8,color='red', alpha=0.7, edgecolor='brown')
plt.show()