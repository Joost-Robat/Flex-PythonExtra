import os

werkmap = os.getcwd()

print("De huidige werkmap is: " + werkmap)

#os.mkdir("Test map xD")
loop = True
while loop:
	mapnaam = input("Welke naam wil je voor de map?")
	
	lengte_mapnaam = len(mapnaam)
	if lengte_mapnaam > 0:
		os.mkdir(mapnaam)
		print("De map " + mapnaam + " is gemaakt.")
		continue
	else:
		print("Je hebt niks ingevoerd...")
		continue