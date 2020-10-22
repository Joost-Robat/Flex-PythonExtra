import os

bestand = open("klasgenoten.txt")

tekst_regel = bestand.readline()
tekst_regel = tekst_regel.strip()
count = 1
while tekst_regel:
	print(tekst_regel)
	tekst_regel = bestand.readline()
