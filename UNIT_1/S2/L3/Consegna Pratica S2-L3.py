
figure = input("scegli una figura geometrica tra quadrato, cerchio o rettangolo: ")

while True:
    if figure == "quadrato":
        lato = float(input("inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print("il perimetro del quadrato è: " + str(perimetro))

    elif figure == "cerchio":
        raggio = float(input("inserisci il raggio del cerchio: "))
        circonferenza = 2 * 3.14 * raggio
        print("la circonferenza del cerchio è: " + str(circonferenza))

    elif figure == "rettangolo":
        base = float(input("inserisci la base del rettangolo: "))
        altezza = float(input("inserisci l'altezza del rettangolo: "))
        perimetro = (base + altezza) * 2
        print("il perimetro del rettangolo è: " + str(perimetro))

    else: print("figura geometrica non valida")

    while True:
        risposta = input("vuoi scegliere un'altra figura? rispondi con sì o no: ")

        if risposta == "sì":
            figure = input("scegli una figura geometrica tra quadrato, cerchio o rettangolo: ")
            break

        elif risposta == "no": break

        else: print("risposta non valida")

    if risposta == "no": break


