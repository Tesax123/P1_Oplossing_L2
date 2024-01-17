# Schrijf een programma dat een interactief verhaal creëert. Het programma vraagt de gebruiker om
# - een naam
# - een plaats
# - een dier
#
# Daarna genereert het programma een grappig verhaal waarin deze elementen worden gebruikt.
# 
# Maak de volgende functies:
# - vraag_input(onderwerp)
#     Vraagt aan de gebruiker voor een bepaald onderwerp “Geef me een onderwerp: ”.
#     Vergeet het antwoord niet te returnen!
# - print_verhaal(naam, plaats, dier)
#     Gaat het midden van het verhaal printen, met de naam, de plaats en het dier in verwerkt.
# - verhaal_generator()
#     Brengt alles samen:\
#         - Print een eerste lijntje, bv. "Welkom bij de Verhaalgenerator!"
#         - Vraag naam, plaats en dier
#         - Print het verhaal
#         - Print een laatste lijntje, bv. "Het einde van het verhaal."

def vraag_input(onderwerp):
    return input("Geef me een " + onderwerp + ": ")


def print_verhaal(naam, plaats, dier):
    print("\nEr was eens een kindje genaamd " + naam + ". Op een dag besloot " + naam + " om een spannend avontuur te beleven in " + plaats + ".")
    print("\nSamen met " + naam + "'s trouwe metgezel, een " + dier + " genaamd Fluffy, beleefden ze geweldige avonturen en creëerden ze onvergetelijke herinneringen.")

def verhaal_generator():
    print("Welkom bij de Verhaalgenerator!")

    naam = vraag_input("naam")
    plaats = vraag_input("plaats")
    dier = vraag_input("dier")

    print_verhaal(naam, plaats, dier)
    print("\nHet einde van het verhaal. Bedankt voor het spelen met de Verhaalgenerator!")

# Start het programma
verhaal_generator()