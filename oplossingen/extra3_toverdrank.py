# Welkom bij de Magische Toverdrank Brouwerij! Vandaag ga je je eigen magische toverdrank maken. Volg de onderstaande stappen om je eigen toverdrank te brouwen:
#
# - Schrijf een functie genaamd mix_toverdrank die drie bestanddelen als parameters accepteert en een zin retourneert
#   die aangeeft dat je een toverdrank hebt gemaakt met deze bestanddelen.
#
# - Schrijf een functie genaamd brouw_toverdrank die de gebruiker begroet en vervolgens naar drie bestanddelen vraagt.
#   Zeg nu aan de gebruiker dat je aan de slag gaat.
#   Roep daarna de mix_toverdrank-functie aan om het resultaat te krijgen. Toon dit aan de gebruiker.
#
# - Voer de brouw_toverdrank functie uit om je eigen magische toverdrank te maken!


def mix_toverdrank(bestanddeel1, bestanddeel2, bestanddeel3):
    return "Je hebt een magische toverdrank gemaakt met " + bestanddeel1 + ", " + bestanddeel2 + " en ook een beetje " + bestanddeel3 + "!"

def brouw_toverdrank():
    print("Welkom bij de Magische Toverdrank Brouwerij!")
    print("Voeg drie bestanddelen toe om je eigen toverdrank te maken.")

    # Vraag de gebruiker om elk bestanddeel
    bestanddeel1 = input("Eerste bestanddeel: ")
    bestanddeel2 = input("Tweede bestanddeel: ")
    bestanddeel3 = input("Derde bestanddeel: ")
    print("Ik ga daarmee aan de slag!")
    # Roep de mix_toverdrank functie aan om de toverdrank te maken
    resultaat = mix_toverdrank(bestanddeel1, bestanddeel2, bestanddeel3)
    print(resultaat)

brouw_toverdrank()