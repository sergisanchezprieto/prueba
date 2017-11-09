def comprobartiempo():

    dato = False
    while dato == False:
        try:

            tiempo = int(input("introduce el incremento en cada paso de tiempo(s): "))
            dato = True

        except:
            print("Intente introducir otro dato")
def comprobardias():
    dato = False
    while dato == False:
        try:

            dias = int(input("introduce el tiempo total de simulacion (Dias): "))
            dato = True

        except:
            print("Intente introducir otro dato")
def main():


    comprobardias()
    comprobartiempo()

if __name__ == '__main__':
    main()
