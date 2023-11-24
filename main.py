import random
iloscoczek = " "
def rzut(x):
    punkty = 100
    for i in range(x):
        iloscoczek = random.randint(1, 6)
        if iloscoczek == 1:
            punkty = 1
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 2 or iloscoczek == 3:
            punkty = punkty / 2
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 4 or iloscoczek == 5:
            punkty = punkty * 2
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 100:
            punkty = punkty
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
rzut(3)



