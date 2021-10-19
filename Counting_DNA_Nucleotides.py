from typing import Counter
DNA = "GTGCTTGATCACTAGGGGAACAAAGAACGAGTATGATGGTTTACCTTCTGTTGCTTGCCTTACCGCCTTCACGTAGTTTCGGAGACCAATACATGTATTCGGATCCTCGGCGCTGATTATTACCGTGAGTTTCATCTGAAGTGGCCGGGTTATAGTGGACCTGTTTAACGGGATAGGGTTAAGCAACACGAAGACAGTATTGCGTACCCGGGGAACCTAGGACTACAAGTGCTTTCGTTATTTCAATCACTAATACGAGCAACGACTGATAAACTAAGTTTGTGCCTGGTCTTGTCGGTTCCGATTTTTAAGCCCAACTCATGATGATCTAGTAGAAGACTACTTCAAAATCCGAAATTCCTTCCGAAACTCGGGAATGCACACTTCTGAAAAGCGCCGTTAATGTTCGTATCGGGTTGTACTTATACTGATCTGGGCGGCAGTGGTGCAAAAAGTAGGCGGATTTACGGGAACAATGCCTGACCCGATCCTATATCGTGTTGCTAGATCCGCATATATTTGCTCTAAGATGACTCCGATAGCCAACAGCCTATAGCGCACGTCTGGCCAGCTCATGGCTCCGCGTAGTGTTTCACAACAGTCGGGTGACGCTCTTGTGCGTTAGGCGCGAGACGTGCCCAGAGTTAGCGTGCCTCTATGTGACGACTCATTACCAGGCCAGGTGCCGCCATATTATTCTGAGCTCCGGTCGATATAGCCAACCAGCATTTCTGCGCCAAGAGCCTTTAAAGCCATCTGTAACCGAGTAAGCGGCCATGAAAGCACTTCCTTATGCTAGATAAAGCACCCGAGGACCATAGAGAAAGCCCGAACTTGAATATGTATTTCTTTCGATCCAGTAATTACCGTCCGATTGTAGAACTTTAACGGGCACGAAACGGTC"
#The function STRING.count('letter') tells you how many times a character is repeated in a string.
adenine = DNA.count('A')
cytosine = DNA.count('C')
guanine = DNA.count('G')
Thymine = DNA.count('T')

print(adenine, cytosine, guanine, Thymine)

