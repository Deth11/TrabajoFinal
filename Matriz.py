def matriz_horizontal(dicc, m, caps):
    for elem in dicc.values():
        for x in elem:
            if caps:
                m.append([x[0].upper()])
            else:
                m.append([x[0].lower()])


def matriz_vertical(dicc, m, mx, caps):
    aux = []
    for elem in dicc.values():
        for x in elem:
            aux.append([x[0]])
    for elem in range(len(aux)):
        if len(aux[elem][0]) > mx:
            mx = len(aux[elem][0])
    print(mx)
    for i in range(0, mx):
        m.append([])
    #print(m)
    i = 0
    while i < len(aux):
        x = 0
        while x < len(aux[i]):
            y = 0
            while y < len(aux[i][x]):
                if caps:
                    m[y].append(aux[i][x][y].upper())
                else:
                    m[y].append(aux[i][x][y].lower())
                y += 1
            x += 1
        i += 1
    #print(m)

'''
matr = []
dicc = {'Sustantivo': [('Futbol', 0), ('Computadora', 0)],
        'Adjetivo': [('Lindo', 0), ('Lento', 0)],
        'Verbo': [('Correr', 0), ('Masturbar', 0)]}
matriz_vertical(dicc, matr)
print(matr)
'''