import math

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
    return [max(0, -x) for x in taskas]
    
def bauda(taskas, r):
    g = gi(taskas)
    b = sum((max(0, -x))**2 for x in taskas)
    b += g**2
    return tikslo_funkcija(taskas) + r * b



def test():
    print("Iveskite pradinio tasko koordinates\n")
    x1 = float(input("x1 = "))
    x2 = float(input("x2 = "))
    x3 = float(input("x3 = "))
    r = float(input("Iveskite r reiksme\n"))
    taskas = [x1, x2, x3]
    print("Tikslo funkcijos reiksme = ", tikslo_funkcija(taskas))
    print("Bauda su pasirinktu r = ", bauda(taskas, r))
    return input("Jei nebenorite testi, iveskite 'n', jei norite testi, iveskite 't'\n").lower()


def antigradientas(taskas, r, h=1e-5):
    base = bauda(taskas, r)
    grad = []
    for i in range(len(taskas)):
        t = taskas[:]
        t[i] += h
        delta = (bauda(t, r) - base) / h
        grad.append(-delta)
    return grad



def auksoPjuvis(taskas, r):
    auksoPjuv = (math.sqrt(5) - 1) / 2
    a = 0.0
    b = 10.0
    epsilon = 1e-6
    
    x1 = b - auksoPjuv * (b - a)
    x2 = a + auksoPjuv * (b - a)
    grad = antigradientas(taskas, r)
    
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

    
    return (a + b) / 2

def greiciausiasNusileidimas(taskas):
    r = 10.0
    grad = antigradientas(taskas, r)
    epsilon = 1e-6
    for i in range(1000):
        norma = math.sqrt(sum(g**2 for g in grad))
        if norma < epsilon:
            break

        print("****************************************************************")
        print(f"\nITERACIJA {i+1}")
        print(f"Taskas: {taskas}")
        print(f"Baudos funkcijos reiksme: {bauda(taskas, r)}")
        print(f"Gradiento norma: {norma}")
        print(f"Tiklso funkcijos reiksme: {tikslo_funkcija(taskas)}")
        r *= 1.2
        gamma = auksoPjuvis(taskas, r)
        naujasTaskas = [
            taskas[0] - gamma * grad[0],
            taskas[1] - gamma * grad[1],
            taskas[2] - gamma * grad[2]
        ]
        grad = antigradientas(naujasTaskas, r)
        taskas = naujasTaskas
        print(taskas)

    print(f"Minimumo taskas: {taskas[0]} {taskas[1]} {taskas[2]}")
    print(f"Minimumo reiksme: {tikslo_funkcija(taskas)}")
