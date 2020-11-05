#!/usr/bin/env python3
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
	return round(freq_acl/tamanho,4) *100
	
#criando a lista
arquivo= open("numbers/numbers.txt","r")
a = arquivo.read()
arquivo.close()
lista = list(map(int, a.split(" - ")))
sorted(lista)

#definições iniciais
tamanho = len(lista)
frequence_acl = 0
lista_frequencias=[]
minimo = int(input("Qual o valor mínimo?"))
h = int(input("Qual a amplitude?"))

for l in lista:
	amp= minimo + (h-1)
	if (amp < lista[-1]):
		lista_amp = getFreque(lista, amp)
		frequence = len(lista_amp)
		minimo = lista[0]

		frequence_relative = getFrequeReL(frequence, tamanho)

		frequence_acl +=frequence

		frequence_rel_acl = getFrequeAclRel(frequence_acl, tamanho)

		frequence_object = Numbers(lista_amp, frequence, frequence_relative, frequence_acl, frequence_rel_acl)
		lista_frequencias.append(frequence_object)

#ultimos numeros
last_numbers_frequency = len(lista)
last_numbers_frequency_relative = round(last_numbers_frequency/tamanho,3)*100
last_numbers_frequency_acl = frequence_acl+ last_numbers_frequency
last_numbers_frequency_acl_relative = round(last_numbers_frequency_acl/tamanho,4)*100
last_frequence_object = Numbers(lista, last_numbers_frequency, last_numbers_frequency_relative, last_numbers_frequency_acl, last_numbers_frequency_acl_relative)

lista_frequencias.append(last_frequence_object)
print(" "," ","Classe", " "," ", "FA", " ", "FI%", " ", "FAci", " ", "FAci%")
for x in lista_frequencias:

	print(min(x.number),"| - ",max(x.number)," ",x.frequencia," ", x.frequencia_rel," ", x.frequencia_acl," ", x.frequencia_acl_rel)