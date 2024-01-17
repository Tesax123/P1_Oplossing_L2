# Schrijf functie begroet_vriend, die een begroeting voor een vriend gaat printen!
# Er is één parameter, namelijk de naam van de vriend.

# Voorbeeldinput:
# begroet_vriend("Bob")
#
# Voorbeeldoutput:
# Dag Bob! Wat leuk om je te zien.

def begroet_vriend(naam):
    begroeting = "Dag " + naam + "! Wat leuk om je te zien."
    print(begroeting)

begroet_vriend("Bob")