import random
import string


def matriz(dicc, m, caps, CS, CV, CA):
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
    while elem != CS:
        aux = []
        pal = random.choice(dicc['Sustantivo'])
        if pal[0] not in aux2:
            aux2.append(pal[0])
            for l in pal[0]:
                if caps:
                    aux.append(l.upper())
                else:
                    aux.append(l.lower())
            m.append(aux)
            elem += 1
    elem = 0
    aux2 = []
    while elem != CV:
        aux = []
        pal = random.choice(dicc['Verbo'])
        print(pal)
        if pal[0] not in aux2:
            aux2.append(pal[0])
            if pal not in m:
                for l in pal[0]:
                    if caps:
                        aux.append(l.upper())
                    else:
                        aux.append(l.lower())
                m.append(aux)
                elem += 1
    elem = 0
    aux2 = []
    while elem != CA:
        aux = []
        pal = random.choice(dicc['Adjetivo'])
        if pal[0] not in aux2:
            aux2.append(pal[0])
            if pal not in m:
                for l in pal[0]:
                    if caps:
                        aux.append(l.upper())
                    else:
                        aux.append(l.lower())
                m.append(aux)
                elem += 1
    print(m)
    return mx