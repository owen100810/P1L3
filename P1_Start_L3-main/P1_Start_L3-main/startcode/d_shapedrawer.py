# Maak een programma dat de gebruiker in staat stelt een vorm te kiezen (vierkant, driehoek of cirkel)
# en de gekozen vorm op het scherm te tekenen.
#
# Als de gebruiker een ongeldige vorm invoert, moet het programma een foutmelding weergeven.
import turtle


input_figuur = input("kies een figuur, vierkant, driehoek, pentagon, ster, trapezium, of cirkel? ")

def driehoek():
    turtle.right(60)
    turtle.forward(200)
    turtle.right(60)
    turtle.forward(200)
    turtle.right(150)
    turtle.forward(350)

def vierkant():
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)

def cirkel():
    turtle.circle(100, 400, 400,)


def pentagon():
    for i in range(5):
        turtle.forward(150)
        turtle.left(72)

def ster():
    for i in range(5):
        turtle.forward(200)
        turtle.left(-144)

def trapezium():
    turtle.forward(400)
    turtle.right(-55.9)
    turtle.forward(200)
    turtle.right(144)
    turtle.forward(-60)

if input_figuur == "driehoek":
    driehoek()
elif input_figuur == "vierkant":
    vierkant()
elif input_figuur == "cirkel":
    cirkel()
elif input_figuur == "pentagon":
    pentagon()
elif input_figuur == "ster":
    ster()
elif input_figuur == "trapezium":
    trapezium()
else:
    print("Die figuur kan ik niet tekenen!")



turtle.done()
