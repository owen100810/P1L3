import turtle


# selectie
if getal > 0:
    print("Het ingevoerde getal is positief.")
elif getal < 0:
    print("Het ingevoerde getal is negatief.")
else:
    print("Het ingevoerde getal is nul.")


# conditionele lus
beurt_nummer = 0
while beurt_nummer <= 5:
    print(beurt_nummer)
    beurt_nummer += 1


# oneindige lus
while True:
	doe_iets()


# for-loop
for aantalBeurten in range(0, 5):
    print(aantalBeurten)


# turtle commando's
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.done()
