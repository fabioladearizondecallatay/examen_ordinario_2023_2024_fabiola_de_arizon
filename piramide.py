def piramide(nivel):
    for i in range(1, nivel * 2, 2): #bucle del numero de filas
        espacios = (nivel * 2 - i) // 2 #para construir las filas 
        print(' ' * espacios + '*' * i + ' ' * espacios)


def main():
    #solo acepta numeros enteros
    nivel = int(input("Chose a level of lines * :"))
    while True: #bucle para crear las condiciones de la talla de la pyramide
        try :
            if 1<= nivel <= 5:
                break
            else:
                print("The number of stars is not a number bigger than 1")
        except ValueError: 
            print("Please chose a number!")

    piramide(nivel)


if __name__ == "__main__":
    main()


       