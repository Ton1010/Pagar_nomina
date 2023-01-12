print("Bienvenido al programa que le dice cuanto pagarle a sus empleados")
print(" ")
ñ = int((input("Ingrese un numero de nueve digitos tipo VVVVTHEHS: ")))
#vvvv t he hs
#Valor de la hora turno hora de entrada hora de salida
vvvv = ñ//100000
w = ñ//10000
t = w%10
q = ñ//100
he = q%100
hs = ñ%100
hl = hs-he

vh = hl*vvvv
tu = ""
if t == 1:
    tu = "Turno de la MAÑANA"
else:
    if t==2:
        tu = "Turno de la TARDE"
    else:
        if t == 3:
            tu = "Turno de la NOCHE"
cat = 0
ad = 0
por = ""
#mañana
if t ==1:
    if hl<= 6:
        cat = 1
        ad = vh*0.05
        por = "5%"
    else:
        if hl<13:
            cat = 2
            ad = vh*0.10
            por = "10%"
        else:
            if hl>12:
                cat = 3
                ad = vh*0.15
                por = "15%"
#tare noche
if t ==2:
    if hl<= 6:
        cat = 1
        ad = vh*0.05
        por = "5%"
    else:
        if hl<10:
            cat = 2
            ad = vh*0.10
            por = "10%"
        else:
            if hl<12:
                cat = 3
                ad = vh*0.20
                por = "20%"
            if hl>11:
                cat = 4
                ad = vh*0.30
                por = "30%"
else:
    if t == 3:
        if hl<= 6:
            cat = 1
            ad = vh*0.05
            por = "5%"
        else:
            if hl<10:
                cat = 2
                ad = vh*0.10
                por = "10%"
            else:
                if hl<12:
                    cat = 3
                    ad = vh*0.20
                    por = "20%"
                if hl>11:
                    cat = 4
                    ad = vh*0.30
                    por = "30%"
tp = vh+ad
if he<hs:
    if he==hs:
        print("ERROR EN LAS HORAS")
    else:
        if he>0:
            if hs<23:
                if t<4:
                    print(" ")
                    print("Total a pagar:",tu,", categoria",cat,", $",int(tp))
                    print(" ")
                    print("Gracias por usar nuestro servicio")
                else:
                    print("NUMERO DE TURNO INCORRECTO")
            else:
                print("ERRO EN LAS HORAS")
        else:
            print("ERROR EN LAS HORAS")
else:
    print("ERROR EN LAS HORAS")
