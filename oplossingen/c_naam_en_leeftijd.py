# Schrijf een Python-functie “vraag_naam_en_leeftijd() ” die de gebruiker vraagt naar hun naam en leeftijd.
# Vervolgens moet het programma de volgende zin afdrukken.
#
# "Je naam is [naam] en je leeftijd is [leeftijd] jaar."

def naam_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Hoe oud ben je? ")

    print("Je naam is " + naam + " en je leeftijd is " + leeftijd + " jaar.")

naam_leeftijd()