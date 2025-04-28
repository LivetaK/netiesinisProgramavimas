import math
import numpy as np


def tikslo_funkcija(taskas):
    a = taskas[0]
    b = taskas[1]
    c = taskas[2]
    f = a*b*c 
    return -f

def gi(taskas):
    a = taskas[0]
    b = taskas[1]
    c = taskas[2]
    return 2*(a*b+b*c+a*c) - 1

def hi(taskas):
    return [-taskas[0], -taskas[1], -taskas[2]]
    
def bauda(taskas, r):
    g = gi(taskas)
    h = hi(taskas)
    b = sum((max(0, x))**2 for x in h)
    b += g**2
    return tikslo_funkcija(taskas) + 1.0 / r * b

def antigradientas(taskas):
    x1 = taskas[0]
    x2 = taskas[1]
    x3 = taskas[2]
    fGrad = [-x2 * x3, -x1 * x3, -x1 * x2]
    return fGrad;


def baudsosGradientas(taskas, r):
    a = taskas[0]
    b = taskas[1]
    c = taskas[2]

    grad = antigradientas(taskas)

    g = gi(taskas)
    giGrad_a = 4 * g * (b+c)
    giGrad_b = 4 * g * (a+c)
    giGrad_c = 4 * g * (a+b)

    h = hi(taskas)
    gradH_a, gradH_b, gradH_c = 0, 0, 0

    if h[0] > 0:
        gradH_a = 2 * h[0];
    if h[1] > 0:
        gradH_b = 2 * h[1];
    if h[2] > 0:
        gradH_c = 2 * h[2];
            
    gradientasA = grad[0] + (1.0 / r) * (giGrad_a + gradH_a)
    gradientasB = grad[1] + (1.0 / r) * (giGrad_b + gradH_b)
    gradientasC = grad[2] + (1.0 / r) * (giGrad_c + gradH_c)

    return [gradientasA, gradientasB, gradientasC]


def test():
    print("Iveskite pradinio tasko koordinates\n")
    x1 = float(input("a = "))
    x2 = float(input("b = "))
    x3 = float(input("c = "))
    r = float(input("Iveskite r reiksme\n"))
    taskas = [x1, x2, x3]
    print("Tikslo funkcijos reiksme = ", tikslo_funkcija(taskas))
    print("Bauda su pasirinktu r = ", bauda(taskas, r))
    return input("Jei nebenorite testi, iveskite 'n', jei norite testi, iveskite 't'\n").lower()




def auksoPjuvis(taskas, r):
    t = 0
    auksoPjuv = (math.sqrt(5) - 1) / 2
    a = 0.0
    b = 10.0
    epsilon = 1e-6
    
    x1 = b - auksoPjuv * (b - a)
    x2 = a + auksoPjuv * (b - a)
    grad = baudsosGradientas(taskas, r)
    
    taskasX1 = [
        taskas[0] - x1 * grad[0],
        taskas[1] - x1 * grad[1],
        taskas[2] - x1 * grad[2]
    ]
    taskasX2 = [
		taskas[0] - x2 * grad[0],
		taskas[1] - x2 * grad[1],
		taskas[2] - x2 * grad[2]
	]

    fx1 = bauda(taskasX1, r)
    fx2 = bauda(taskasX2, r)
    t += 2
    
    while abs(b - a) > epsilon:
        if fx1 < fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = b - auksoPjuv * (b - a)
            
            taskasX1 = [
                taskas[0] - x1 * grad[0],
                taskas[1] - x1 * grad[1],
                taskas[2] - x1 * grad[2]
            ]
            fx1 = bauda(taskasX1, r)
            t +=1
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + auksoPjuv * (b - a)
            
            taskasX2 = [
                taskas[0] - x2 * grad[0],
                taskas[1] - x2 * grad[1],
                taskas[2] - x2 * grad[2]
            ]
            fx2 = bauda(taskasX2, r)
            t += 1
    
    return (a + b) / 2, t

def norma(v):
    return np.linalg.norm(v)


def tenkina_apribojimus(taskas):
    return gi(taskas) <= 0 and all(x >= 0 for x in taskas)

def greiciausiasNusileidimas(taskas, r):
    t = 0
    i = 0
    grad = baudsosGradientas(taskas, r)
    epsilon = 1e-6

    while norma(grad) > epsilon:

        i+=1

        gamma, tikslas = auksoPjuvis(taskas, r)
        t += tikslas

        naujasTaskas = [
            taskas[0] - gamma * grad[0],
            taskas[1] - gamma * grad[1],
            taskas[2] - gamma * grad[2]
        ]

        sena_bauda = bauda(taskas, r)
        nauja_bauda = bauda(naujasTaskas, r)
        t +=2

        if nauja_bauda > sena_bauda:
            while not tenkina_apribojimus(naujasTaskas):
                gamma *= 0.9
                if gamma < epsilon:
                    break
                naujasTaskas = [
                    taskas[0] - gamma * grad[0],
                    taskas[1] - gamma * grad[1],
                    taskas[2] - gamma * grad[2]
                ]

        if abs(taskas[0] - naujasTaskas[0]) + abs(taskas[1] - naujasTaskas[1]) + abs(taskas[2] - naujasTaskas[2]) < epsilon:
            break
        if gamma < epsilon:
            break

        grad = baudsosGradientas(naujasTaskas, r)
        taskas = naujasTaskas

    return taskas, i, t

def optimumas(taskas1, taskas2, taskas3):
    epsilon = 1e-6
    rArray = [10, 5, 3, 2, 1, 0.5, 0.1, 0.001]
    i1, i2, i3 = 0, 0, 0
    t1, t2, t3 = 0, 0, 0
    for r in rArray:
        print (f"\n=== Iteracija su r = {r} ===")
        n_taskas1, iteracija1, tikslas1 = greiciausiasNusileidimas(taskas1, r)
        n_taskas2, iteracija2, tikslas2 = greiciausiasNusileidimas(taskas2, r)
        n_taskas3, iteracija3, tikslas3 = greiciausiasNusileidimas(taskas3, r)
        i1 += iteracija1
        i2 += iteracija2
        i3 += iteracija3
        t1 += tikslas1
        t2 += tikslas2
        t3 += tikslas3
        print("****************************************************************")
        print("Nauji taskai")
        print(f"Taskas 1: {n_taskas1}")
        print(f"Taskas 2: {n_taskas2}")
        print(f"Taskas 3: {n_taskas3}")
        taskas1 = n_taskas1
        taskas2 = n_taskas2
        taskas3 = n_taskas3

    print("\n=== Galutiniai rezultatai ===")

    f1 = tikslo_funkcija(taskas1)
    f2 = tikslo_funkcija(taskas2)
    f3 = tikslo_funkcija(taskas3)
    t1 += 1
    t2 += 1
    t3 += 1

    print(f"Taskas 1: {taskas1}, Tikslo funkcija: {f1}")
    print(f"Iteraciju kiekis is tasko 1: {i1}")
    print(f"Tikslo funkcija is tasko 1 kviesta: {t1}")

    print("\n----------------------------------------------------")

    print(f"Taskas 2: {taskas2}, Tikslo funkcija: {f2}")
    print(f"Iteraciju kiekis is tasko 2: {i2}")
    print(f"Tikslo funkcija is tasko 2 kviesta: {t2}")

    print("\n----------------------------------------------------")

    print(f"Taskas 3: {taskas3}, Tikslo funkcija: {f3}")
    print(f"Iteraciju kiekis is tasko 3: {i3}")
    print(f"Tikslo funkcija is tasko 3 kviesta: {t3}")

    funkcijos = [f1, f2, f3]
    taskai = [taskas1, taskas2, taskas3]

    indeksas_geriausio = funkcijos.index(min(funkcijos))

    geriausias_taskas = taskai[indeksas_geriausio]

    print("\n=== Pasirinktas optimalus taskas ===")
    print(f"Optimalus taskas: {geriausias_taskas}")
    print(f"Optimalios funkcijos reiksme: {funkcijos[indeksas_geriausio]}")


