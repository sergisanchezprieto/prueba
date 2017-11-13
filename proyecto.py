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
    print('Xx-TEMPORAL-xX: Número de calculos a realizar: ', calculos)
    return calculos


def calcular_Dvelocidad(a, t):
    Dvel = a * t
    print('Xx-TEMPORAL-xX: Diferencia de velocidad: ', Dvel)
    return Dvel

def calcular_fuerza(Dr):
    masas = 5.9722e+24 * 7.348e+22
    constante = 6.674e-11
    fuerza = masas * constante * (-1) / Dr
    print('Xx-TEMPORAL-xX: Fuerza: ', fuerza)
    return fuerza

def calcular_radio(posicion):
    radio = posicion[0] ** 2 + posicion[1] ** 2
    radio = math.sqrt(radio)

def datos():
        constante = 6.674e-11
        fuerza_inicio = [0.0e+00, -1.98201e+20]
        posicion_inicio = [0.0e+00, 3.84402e+08]
        masa_tierra = 5.9722e+24
        masa_luna = 7.348e+22
        velocidad_lunar = [1023.055, 0.0]

# # # P R I N C I P A L # # #
def main():
    dias = comprobardias()
    tiempo = comprobartiempo()
    fasesdiarias = calculartiempodia(tiempo)
    diferencia_radio = 
    fuerza = calcular_fuerza(diferencia_radio)
    aceleracion = calcular_aceleracion(fuerza)
    Diferencia_velocidad = calcular_Dvelocidad(aceleracion, tiempo)



if __name__ == '__main__':
    main()
