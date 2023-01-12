codigo = 2000

def total(usuarios):
    acu = 0
    for i in range(0,len(usuarios)):
        acu = acu + usuarios[i][4]
    print("El total a pagar es ",acu)

def promedio(usuarios):
    genero = int(input("Digite su genero: 1. Masculino, 2. Femenino: "))
    g = False
    if genero ==1:
        g = True
    else:
        g = False
    contador = 0
    acu = 0
    for i in range(0,len(usuarios)):
        if usuarios[i][3] ==g:
            contador = contador+1
            acu = acu + usuarios[i][4]

    if contador>0:
        promedio = acu/contador
        texto = ""
        if g == True:
            texto = "Los hombres"
        else:
            texto = "Las mujeres"
        print("El promedio de los que deben ",texto,"es",promedio)
    else:
        print("No se encontro el genero")

def modificar(usuarios):
    codigo = int(input("Digite el codigo a modificar: "))

    for i in range(0,len(usuarios)):
        if usuarios[i][0] == codigo:
            nombre = input("Digite el nombre: ")
            edad= int(input("Digite su edad: "))
            genero = int(input("Digite su genero: 1. Masculino, 2. Femenino: "))
            g = False
            if genero ==1:
                g = True
            else:
                g = False
            pagar = float(input("Digite el valor a pagar: "))
            usuarios[i][1] = nombre
            usuarios[i][2] = edad
            usuarios[i][3] = g
            usuarios[i][4] = pagar
            
    return usuarios
            
                 
    

def imprimir(usuarios):

    filas = len(usuarios)
    print("CODIGO   NOMBRE    EDAD   GENERO   DEUDA")
    for i in range(0,filas):
        for j in range(0,5):
            if j ==3:
                if usuarios[i][3] == True:
                    print("Masculino",end="   ")
                else:
                    print("Femenino",end="   ")
            else:
                print(usuarios[i][j],end = "   ")
        print()

def crear(usuarios):
    global codigo
    nombre = input("Digite el nombre: ")
    edad= int(input("Digite su edad: "))
    genero = int(input("Digite su genero: 1. Masculino, 2. Femenino: "))
    g = False
    if genero ==1:
        g = True
    else:
        g = False
    pagar = float(input("Digite el valor a pagar: "))

    datos = []
    datos.append(codigo)
    datos.append(nombre)
    datos.append(edad)
    datos.append(g)
    datos.append(pagar)

    usuarios.append(datos)
    
    codigo = codigo+1
    return usuarios
def menu():
    usuarios = []
    opc = 1
    while opc>0 and opc<6:

        print("Menu")
        print("1. Crear usuario")
        print("2. Mostrar ususarios")
        print("3. Modificar usuario")
        print("4. promedio segun genero")
        print("5. Total a pagar")
        print("6. Salir")
        print("")
        opc = int(input("Digite una opcion: "))

        if opc ==1:
            usuario = crear(usuarios)

        if opc == 2:
            imprimir(usuario)
            
        if opc == 3:
            usuario = modificar(usuarios)
        if opc == 4:
            promedio(usuarios)

        if opc ==5:
            total(usuarios)
            

menu()
