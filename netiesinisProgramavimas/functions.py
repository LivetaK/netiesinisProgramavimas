import math

def tikslo_funkcija(taskas):
    x1 = taskas[0]
    x2 = taskas[1]
    x3 = taskas[2]
    f = (1.0 / 8) * (x1 * x2 * x3)
    return -f

def gi(taskas):
    x1 = taskas[0]
    x2 = taskas[1]
    x3 = taskas[2]
    return x1+x2+x3 - 1

def hi(taskas):
    x1 = -taskas[0]
    x2 = -taskas[1]
    x3 = -taskas[2]
    naujas_taskas = [x1, x2, x3]
    return naujas_taskas
    
def bauda(taskas, r):
    h = hi(taskas)
    g = gi(taskas)
    b = 0
    for t in h:
        if t > 0:
            b += t*t
    b+= g * g
    return tikslo_funkcija(taskas) + 1.1/r * b


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




def antigradientas(taskas):
    x1 = taskas[0]
    x2 = taskas[1]
    x3 = taskas[2]
    fGrad = [
	-1.0 / 8 * x2 * x3,
    -1.0 / 8 * x1 * x3,
    -1.0 / 8 * x1 * x2]
    return fGrad;


def auksoPjuvis(taskas):
    auksoPjuv = (math.sqrt(5) - 1) / 2
    a = 0.0
    b = 1.0
    epsilon = 1e-6
    
    x1 = b - auksoPjuv * (b - a)
    x2 = a + auksoPjuv * (b - a)
    
    taskasX1 = [
        taskas[0] - x1 * antigradientas(taskas)[0],
        taskas[1] - x1 * antigradientas(taskas)[1],
        taskas[2] - x1 * antigradientas(taskas)[2]
    ]
    taskasX2 = [
		taskas[0] - x2 * antigradientas(taskas)[0],
		taskas[1] - x2 * antigradientas(taskas)[1],
		taskas[2] - x2 * antigradientas(taskas)[2]
	]

    fx1 = tikslo_funkcija(taskasX1); 
    fx2 = tikslo_funkcija(taskasX2)
    
    while abs(b - a) > epsilon:
        if fx1 < fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = b - auksoPjuv * (b - a)
            
            taskasX1 = [
                taskas[0] - x1 * antigradientas(taskas)[0],
                taskas[1] - x1 * antigradientas(taskas)[1],
                taskas[2] - x1 * antigradientas(taskas)[2]
            ]
            fx1 = tikslo_funkcija(taskasX1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + auksoPjuv * (b - a)
            
            taskasX2 = [
                taskas[0] - x2 * antigradientas(taskas)[0],
                taskas[1] - x2 * antigradientas(taskas)[1],
                taskas[2] - x2 * antigradientas(taskas)[2]
            ]
            fx2 = tikslo_funkcija(taskasX2)
    
    return (a + b) / 2

def greiciausiasNusileidimas(taskas):
    grad = antigradientas(taskas)
    epsilon = 1e-6
    while abs(grad[0]) > epsilon or abs(grad[1]) > epsilon:
        gamma = auksoPjuvis(taskas)
        naujasTaskas = [
        taskas[0] - gamma * grad[0],
        taskas[1] - gamma * grad[1],
        taskas[2] - gamma * grad[2]
        ]
        grad = antigradientas(naujasTaskas)

    print(f"Minimumo taskas: {taskas[0]} {taskas[1]} {taskas[2]}")
    print(f"Minimumo reiksme: {tikslo_funkcija(taskas)}")