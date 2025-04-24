from functions import *


#testavimas
pasirinkimas = 't'
while pasirinkimas != 'n':
    pasirinkimas = test()
    while pasirinkimas != 'n' and pasirinkimas !='t':
        print("Neteisingas pasirinkimas")
        pasirinkimas = input("Jei nebenorite testi, iveskite 'n', jei norite testi, iveskite 't'\n").lower()

greiciausiasNusileidimas(1.0, 1.0, 1.0)