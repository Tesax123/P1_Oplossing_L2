# Schrijf een functie die de oppervlakte van de rechthoek berekent, op basis van de lengte en de breedte.
#
# In het programma, vraag aan de gebruiker een lengte en een breedte. Dit kunnen kommagetallen zijn!
#
# Roep de functie op met die lengte en die breedte, en toon tot slot het resultaat aan de gebruiker.

def bereken_oppervlakte(lengte, breedte):
    return lengte * breedte


lengte = float(input("Wat is de lengte van de rechthoek? "))
breedte = float(input("Wat is de breedte van de rechthoek? "))
oppervlakte = bereken_oppervlakte()
print("De oppervlakte van de rechthoek is:", oppervlakte)