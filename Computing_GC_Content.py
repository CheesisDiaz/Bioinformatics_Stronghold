from os import read, sep
import itertools
import re
import operator

FATSA = open('rosalind_gc.txt', 'r')

#Reading file and removing endline
lista = []
with FATSA as f:
    for line in f:
        line = line.split()
        lista.append(line)
        merged = list(itertools.chain(*lista))
        merged_string = ''.join(merged)

#Separate the strings by the character ">". Without counting the first value
separation = merged_string.split('>')
separation_1 = separation.pop(0)

GC_value = []
Code = []
for item in separation:
    GC_count = item.count('G') + item.count('C')
    GC_ave = (GC_count / (len(item) - 13)) * 100
    GC_value.append(GC_ave)
    # Crear una lista con el codigo de adn
    code = item[:13]
    Code.append(code)

dic = dict(zip(Code, GC_value))

Maxkey = max(dic.items(), key = operator.itemgetter(1))[0]
print(Maxkey)
print(dic[Maxkey])