import math
def comprobartiempo():
    dato = False
    while dato == False:
        try:
            tiempo = int(input("introduce el incremento en cada paso de tiempo(s): "))
            dato = True
        except:
            print("Intente introducir otro dato")
        return tiempo

def comprobardias():
    dato = False
    while dato == False:
        try:
            dias = int(input("introduce el tiempo total de simulacion (Dias): "))
            dato = True
        except:
            print("Intente introducir otro dato")
    return dias

def calcular_aceleracion(fuerza):
    acel = [fuerza[0]/7.348e+22 , fuerza[1]/7.348e+22]
    return acel

def calculartiempodia(t):
    calculos = 86400 / t      #un día = 86400s #tiempo de dia / tiempo introducido = numero de calculos
    print(calculos)
    hola = input("pilsa enter para continuar")
    return calculos



def calcular_Dvelocidad(a, t):
    Dvel = a * t
    return Dvel
def calcular_velocidad_nueva(Dv, v):
    velocidad_nueva = Dv + v
    return velocidad_nueva

def calcular_fuerza(Dr , distancia):
    masas = 5.9722e+24 * 7.348e+22
    constante = 6.674e-11

    fuerza_x = masas * constante * (-1) / Dr ** 3 * distancia[0]
    fuerza_y = masas * constante * (-1) / Dr ** 3 * distancia[1]

    return (fuerza_x, fuerza_y)

def calcular_posicion(v, x, t):
    s = x + v * t
    return s


def calcular_radio(posicion):
    radio = posicion[0] ** 2 + posicion[1] ** 2
    radio = math.sqrt(radio)

    return radio

def datos():
        constante = 6.674e-11
        fuerza_inicio = [0.0e+00, -1.98201e+20]
        posicion_inicio = [0.0e+00, 3.84402e+08]
        masa_tierra = 5.9722e+24
        masa_luna = 7.348e+22
        velocidad_lunar = [1023.055, 0.0]

def calcular_contador_segundos(contador):
    segundos = contador * 86400
    return segundos

# # # P R I N C I P A L # # #
def main():
    dias = comprobardias()
    tiempo = comprobartiempo()
    posicion = [0.0e+00, 3.84402e+08]
    fasesdiarias = calculartiempodia(tiempo)
    contador = 0
    contador1 = 0
    nueva_velocidad = [1023.055 , 0.0]
    contador_segundos = calcular_contador_segundos(contador)
    while contador <= dias:

        while contador1 <= fasesdiarias:

            diferencia_radio = calcular_radio(posicion)
            fuerza = calcular_fuerza(diferencia_radio, posicion)
            aceleracion = calcular_aceleracion(fuerza)
            Diferencia_velocidad = calcular_Dvelocidad(aceleracion, tiempo)
            nueva_velocidad = calcular_velocidad_nueva(Diferencia_velocidad, nueva_velocidad)
            posicion = calcular_posicion(nueva_velocidad, posicion, tiempo)
            contador1 = contador1 + 1
            print(posicion)
        print(fuerza)
        print(diferencia_radio)
        print(nueva_velocidad)
        contador1 = 0
        contador = contador + 1




if __name__ == '__main__':
    main()
