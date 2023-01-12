n = int(input("Ingrese el numero tipo HLTAAL: "))

#HL T AL G

g = n%10
q = n//10
al = q%100
f = n//1000
t = f%10
hl = n//10000
#generos
gen =""
if g==1:
    gen = "MASCULINO"
    tipo = "hombre"
else:
    gen= "FEMENINO"
    tipo = "mujer"

#categorias
cat = 0
if al<9: #menores que 9
    cat = 1
else:
    if al<19: #mayores a 9 y menores de 19
        cat = 2
    else:
        cat = 3 #mayores e 19

#turno
tur = 0
if cat==1:
    vh = 15000
    tur = "MAÑANA"
else:
    if cat==2:
        vh = 20000
        tur = "TARDE"
    else:
        if cat==3:
            vh = 25000
            tur = "NOCHE"
#valor horas extras
he = 0          
vhe = 0
if hl>40:
    he = hl-40
    horas = hl-he
    if g == 1:
        if cat == 1:
            vhe = 17000
        else:
            if cat == 2:
                vhe = 22000
            else:
                if cat==3:
                    vhe = 27000
    else:
        if g ==2:
            if cat == 1:
                vhe = 20000
            else:
                if cat == 2:
                    vhe = 25000
                else:
                    if cat == 3:
                        vhe = 30000
else:
    horas = 40



print("Horas laboradas en una semana: ",hl)
print("Horas extras: ",he)
print("Turno: ",tur)
print("Años laborados: ",al)
print("Categoria: ",cat)
print("Genero: ",gen)
print("Valor hora extra",tipo,": ",vhe)
print()
print("Valor horas laboradas",horas,"*",vh,"=",(horas*vh))
print("Valor horas extra: ",he,"*",vhe,"=",(he*vhe))
print("Toatal a pagar",(horas*vh)+(he*vhe))
