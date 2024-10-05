# Maak een selectie om na te gaan of iemand oud genoeg is voor een rijbewijs.
def check_rijbewijsleeftijd(leeftijd):
    rijbewijsleeftijd = 18

    if(leeftijd >rijbewijsleeftijd):
        print("je mag je rijbewijs halen")
    else:
        print("je bent te jong")



# Vraag de leeftijd aan de gebruiker
input_leeftijd = int(input("Hoe oud ben je? "))

# Roep de functie aan om de leeftijd te controleren
check_rijbewijsleeftijd(input_leeftijd)