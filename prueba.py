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
def aceleracion(fuerza):
    acel = [fuerza[0]/7.348e+22 , fuerza[1]/7.348e+22]
    return acel
def calculartiempodia(tiempo):
    tiemp = 86400 / tiempo
    return tiemp
def Dvelocidad():

    Dvel = aceleracion * tiempo
def fuerza(vector):
    masas = 5.9722e+24 * 7.348e+22
    fuerza = masas /
def calcular_radio(posicion):
    radio = posicion[0] ** 2 + posicion[1] ** 2
    radio = math.sqrt(radio)  


def datos():
        fuerza_inicio = [0.0e+00 , -1.98201e+20]
        posicion_inicio = [0.0e+00 , 3.84402e+08]
        masa_tierra = 5.9722e+24
        masa_luna = 7.348e+22
        velocidad_lunar = [1023.055 , 0.0]
def main():
    dias = comprobardias()
    tiempo = comprobartiempo()
    fasesdiarias = calculartiempodia(tiempo)





if __name__ == '__main__':
    main()
