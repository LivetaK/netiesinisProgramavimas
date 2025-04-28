 
1.	UŽDUOTIS
Kokia turėtų būti stačiakampio gretasienio formos dėžė, kad vienetiniam paviršiaus plotui jos tūris būtų maksimalus?
1	Aprašykite tikslo funkciją f(X), lygybinio ir nelygybinių apribojimų funkcijas gi(X) ir hi(X) taip, kad optimizavimo uždavinys būtų formuluojamas min f(X), gi(X)=0, hi(X)≤0.
2	Apskaičiuokite funkcijų f(X), gi(X), hi(X) reikšmes taškuose X0=(0,0,0), X1=(1,1,1) ir Xm=(a/10,b/10,c/10), čia a,b,c – studento knygelės numerio “1x1xabc” skaitmenys.
3	Aprašykite kvadratinę baudos funkciją, apimančią tikslo funkciją ir apribojimus.
4	Patyrinėkite baudos daugiklio įtaką baudos funkcijos reikšmėms.
5	Minimizuokite baudos funkciją praeitame laboratoriniame darbe sukurtu optimizavimo be apribojimų algoritmu sprendžiant optimizavimo uždavinių seką su mažėjančia parametro r seka, kai pirmasis sekos uždavinys optimizuojamas pradedant iš taškų X0, X1 ir Xm, o kiekvieno paskesnio uždavinio pradinis taškas yra ankstesnio uždavinio sprendinys.
6	Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.

 

2.	 ATASKAITA
2.1.	Aprašykite tikslo funkciją f(X), lygybinio ir nelygybinių apribojimų funkcijas gi(X) ir hi(X) taip, kad optimizavimo uždavinys būtų formuluojamas min f(X), gi(X)=0, hi(X)≤0.
2.1.1.	Tikslo funkcija
Žemiau galite matyti mano tikslo funkciją. Kadangi uždavinyje buvo nurodomi taškai su trimis koordinatėmis, stačiakampio gretasienio tūrį skaičiavau kitaip, negu antrame laboratoriniame darbe – dabar tūris yra išreiškiamas per tris briaunas a, b ir c, skaičiuojamas labai paprastai V = a * b * c. Kadangi ieškome funkcijos minimumo, ieškome neigiamo tūrio.
def tikslo_funkcija(taskas):
    a = taskas[0]
    b = taskas[1]
    c = taskas[2]
    f = a*b*c 
    return -f
2.1.2.	Lygybinio apribojimo funkcija gi(x)
Žemiau galite matyti lygybinio apribojimo funkciją. Kadangi sąlyga sako, kad stačiakampio gretasienio paviršiaus plotas yra vienetinis, ši funkcija apskaičiuoja paviršiaus plotą ir atima iš jo vienetą. Tai praverčia ateityje, kai skaičiuojame baudos funkciją – jeigu taškas yra gana arti apribojimų ribos, skiriama mažesnė bauda, nes ši funkcija grąžina reikšmę artimą nuliui.
def gi(taskas):
    a = taskas[0]
    b = taskas[1]
    c = taskas[2]
    return 2*(a*b+b*c+a*c) - 1
2.1.3.	Nelygybinio apribojimo funkcija hi(x)
Žemiau galite matyti nelygybinio apribojimo funkciją, t. y. visos kraštinės negali būti mažesnės už nulį. Tai pravers ateityje skaičiuojant baudos funkciją lygiai taip pat kaip ir lygybinis funkcijos apribojimas.
def hi(taskas):
    return [-taskas[0], -taskas[1], -taskas[2]]
 

2.2.	Apskaičiuokite funkcijų f(X), gi(X), hi(X) reikšmes taškuose X0=(0,0,0), X1=(1,1,1) ir Xm=(a/10,b/10,c/10), čia a,b,c – studento knygelės numerio “1x1xabc” skaitmenys.
Žemiau pateikiamos tikslo funkcijos reikšmės nurodytuose taškuose (žiūrėti pav. 1)
Mano a = 9, b = 8, c = 0.
 
pav. 1 Tikslo funkcijos reikšmės nurodytuose taškuose
2.3.	Aprašykite kvadratinę baudos funkciją, apimančią tikslo funkciją ir apribojimus.
Žemiau galite matyti baudos funkciją, kuri paskaičiuoja lygybinius bei nelygybinius apribojimus, tada tikrina, ar hi (nelygybiniai apribojimai) yra didesni už nulį ar ne, jei didesni, juos kelia kvadratu ir sumuoja, gauname tarpinę reikšmę b, jei nėra didesni, prideda nulį, kas visiškai nekeičia b reikšmės. Kitas žingsnis – prie tarpinės reikšmės b yra pridedamas gi (lygybinis apribojimas) pakeltas kvadratu. Galiausiai – prie tikslo funkcijos reiksmės pridedamas 1 / r * b, kur r yra iš anksčiau paduodama reikšmė, kuri daro įtaką, kaip smarkiai yra baudžiama už ribų nesilaikymą.
def bauda(taskas, r):
    g = gi(taskas)
    h = hi(taskas)
    b = sum((max(0, x))**2 for x in h)
    b += g**2
    return tikslo_funkcija(taskas) + 1.0 / r * b
 

2.4.	Patyrinėkite baudos daugiklio įtaką baudos funkcijos reikšmėms.
Kaip pradinį tašką visur pasirinkau tašką [1.0, 1.0, 1.0] (žiūrėti XX), o r vis mažinau. Kaip matote, kuo mažesnis r, tuo labiau funkcija yra „baudžiama“.
 
2 pav. Baudos daugiklio įtaka baudos funkcijos reikšmėms
2.5.	Minimizuokite baudos funkciją praeitame laboratoriniame darbe sukurtu optimizavimo be apribojimų algoritmu sprendžiant optimizavimo uždavinių seką su mažėjančia parametro r seka, kai pirmasis sekos uždavinys optimizuojamas pradedant iš taškų X0, X1 ir Xm, o kiekvieno paskesnio uždavinio pradinis taškas yra ankstesnio uždavinio sprendinys.
Minimumo taškui skaičiuoti pasirinkau greičiausio nusileidimo metodą, kuris buvo optimizuotas naudojant aukso pjūvio algoritmą.
Kodo veikimo principas:
1.	Žemiau galite matyti funkciją „optimumas“, kuriai yra paduodamos trijų taškų koordinatės. Tai yra pagrindinė funkcija, kuri kviečia visas kitas jai reikiamas funkcijas. Iš pradžių yra nustatoma artima nuliui reikšmė epsilon bei baudos daugiklių masyvas. Toliau užsukamas ciklas, kol nebus pereita per visus baudos daugiklius r. Kiekvienam taškui yra kviečiama funkcija „greiciausiasNusileidimas“, kuri apskaičiuoja optimalią reikšmę su atitinkamu daugikliu einant nuo nurodyto taško. Kai ciklas užbaigiamas, paimami visi trys optimalūs taškai ir paskaičiuojamos jų reikšmės. Taškas su mažiausia reikšme yra atrenkamas kaip optimalus uždavinio sprendinys.
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
2.	Žemiau matote funkciją „greiciausiasNusileidimas“, kuri priima tašką ir baudos daugiklį ir su jais atlieka veiksmus. Pirmiausiai yra kviečiama funkcija „baudosGradientas“, kuri apskaičiuoja funkcijos ir baudos gradientą kartu. Užsukamas ciklas: kol gradiento norma bus didesnė už epsilon, tol bus sukamas ciklas. Cikle pirmas žingsnis yra apskaičiuoti optimalų žingsnį, kurį galima žengti geros krypties link, todėl yra kviečiama funkcija „aksoPjuvis“, kuri būtent tai ir padaro. Toliau yra paskaičiuojamas naujas taškas, iš senojo taško koordinatės atėmus gamma (žingsnio ilgį) padaugintą iš koordinatės gradiento. Toliau seka labai svarbi dalis – patikrinimai. Pirmas patikrinimas: apskaičiuojamos baudos funkcijos senam ir naujam taškui ir žiūrima, kuris iš jų labiau pažeidžia apribojimus. Jei naujasis taškas „nubaustas“ labiau, sukame ciklą tol, kol naujasis pradės tenkinti apribojimus. Cikle po truputį mažiname žingsnį, kuriuo buvo eita. Antras patikrinimas: tikriname, ar skirtumas tarp seno ir naujo taško yra reikšmingas – didesnis už epsilon. Jei ne – išeiname iš ciklo. Trečias patikrinimas: tikriname, ar gamma yra reikšminga – didesnė už epsilon. Jei ne, išeiname iš ciklo. Galiausiai – skaičiuojamas gradientas naujame taške ir ciklas sukasi toliau.
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

3.	Funkcija, kurią matote žemiau tikrina, ar atitinkamame taške, yra tenkinami lygybiniai ir nelygybiniai apribojimai
def tenkina_apribojimus(taskas):
    return gi(taskas) <= 0 and all(x >= 0 for x in taskas)
4.	Funkcija, kurią matote žemiau, skaičiuoja gradiento (vektoriaus) normą (ilgį). Funkcija paimta iš jau įdiegtos python bibliotekos, tačiau jos principas yra labai paprastas – skaičiuojami kiekvienos koordinatės kvadratai, jie sudedami ir iš sumos ištraukiama šaknis.

def norma(v):
    return np.linalg.norm(v)
5.	Žemiau matote funkciją „auksoPjuvis“. Principas toks pats, kaip ir praeitame laboratoriniame darbe, tik čia yra priimamos trys, o ne dvi koordinatės. Taip pat, vietoj tikslo funkcijos kvietimų, mes turime baudos funkcijos kvietimus.
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
`		taskas[0] - x2 * grad[0],
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
2.6.	Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.
2.6.1.	Programos rezultatai
Žemiau galite matyti programos rezultatus (žiūrėti 3 pav.) 
 
3 pav. Programos rezultatai
Taškas	{0, 0, 0}	{1, 1, 1}	{0.9, 0.8, 0.0}
Sprendinys	{0, 0, 0}	{0.408, 0.408, 0.408}	{0.409, 0.408, 0.408}
Iteracijų kiekis	0	19	57
Tikslo funkcijos kvietimų keikis	1	723	2167

2.6.2.	Išvados
Kaip matote, minimumo taškas buvo rastas tik antro ir trečio taškų, iš pirmojo taško funkcija „neišlipa“. Ši programa yra gana „brangi“, nes tam, kad surasti minimumo tašką, tikslo funkcija buvo kviečiama net 723 ir 2167 kartus. 



