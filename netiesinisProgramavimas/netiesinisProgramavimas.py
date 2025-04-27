from functions import *

x0 = [0.0, 0.0, 0.0]
x1 = [1.0, 1.0, 1.0]
x2 = [0.9, 0.8, 0.0]


# print("Tikslo funkcijos reiksme taske ", x0)
# print(tikslo_funkcija(x0))

# print("Tikslo funkcijos reiksme taske ", x1)
# print(tikslo_funkcija(x1))

# print("Tikslo funkcijos reiksme taske ", x2)
# print(tikslo_funkcija(x2))

#testavimas
# pasirinkimas = 't'
# while pasirinkimas != 'n':
#     pasirinkimas = test()
#     while pasirinkimas != 'n' and pasirinkimas !='t':
#         print("Neteisingas pasirinkimas")
#         pasirinkimas = input("Jei nebenorite testi, iveskite 'n', jei norite testi, iveskite 't'\n").lower()


optimumas(x0, x1, x2)