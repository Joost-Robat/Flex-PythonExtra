import os

bestand = open("klasgenoten.txt")

tekst_regel = bestand.readline()
count = 1
while tekst_regel:
	print(tekst_regel)
	tekst_regel = bestand.readline()