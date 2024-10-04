def bereken_oppervlakte(lengte, breedte):
    return lengte * breedte


rechthoek_lengte = float(input("Wat is de lengte van de rechthoek? "))
rechthoek_breedte = float(input("Wat is de breedte van de rechthoek? "))
oppervlakte = bereken_oppervlakte(rechthoek_lengte, rechthoek_breedte)
print("De oppervlakte van de rechthoek is:", oppervlakte)
