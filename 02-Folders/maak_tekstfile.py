import os

vraag = input("Welk bestand wil je openen/maken?\n")
vraag2 = input("Wat wil je er in schrijven?\n")
bestand = open(vraag, "w")

bestand.write(vraag2)

print("Procces voltooid!")

bestand = open("nieuw.txt", "r")


inhoud = bestand.read()
print("De inhoud van het bestand is:")
print(inhoud)