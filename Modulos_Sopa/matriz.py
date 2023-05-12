import random
import string

"""Este modulo va a contenes la matriz 
   que se va a utiliza en el programa

    Las funcion del modulo es : 

    matriz

    En el programa principal se renombra el 
    modulo como M, un ejemplo de esto :

        mx = M.matriz(dicc, matr, caps, cantS, cantV, cantA)
    """
def matriz(dicc, m, caps, cs, cv, ca):
    """Esta funcion va a realizar los 
       calculos del juego utilizando la matriz

    Args:
        dicc ([type]): [description]
        m ([type]): [description]
        caps ([type]): [description]
        cs ([type]): [description]
        cv ([type]): [description]
        ca ([type]): [description]

    Returns:
        [int]: [description]
    """
    aux = []
    mx = 0
    for elem in dicc.values():
        for x in elem:
            aux.append([x[0]])
    for elem in range(len(aux)):
        if len(aux[elem][0]) > mx:
            mx = len(aux[elem][0])
    elem = 0
    aux2 = []
    while elem != cs:
        aux = []
        pal = random.choice(dicc['Sustantivo'])
        if pal[0] not in aux2:
            aux2.append(pal[0])
            for l in pal[0]:
                aux.append(l.upper()) if caps else aux.append(l.lower())
            m.append(aux)
            elem += 1
    elem = 0
    aux2 = []
    while elem != cv:
        aux = []
        pal = random.choice(dicc['Verbo'])
        if pal[0] not in aux2:
            aux2.append(pal[0])
            if pal not in m:
                for l in pal[0]:
                    aux.append(l.upper()) if caps else aux.append(l.lower())
                m.append(aux)
                elem += 1
    elem = 0
    aux2 = []
    while elem != ca:
        aux = []
        pal = random.choice(dicc['Adjetivo'])
        if pal[0] not in aux2:
            aux2.append(pal[0])
            if pal not in m:
                for l in pal[0]:
                    aux.append(l.upper()) if caps else aux.append(l.lower())
                m.append(aux)
                elem += 1
    return mx
