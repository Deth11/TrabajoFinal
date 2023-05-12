import PySimpleGUI as sg
import random
import string

"""Este modulo tiene dos funciones que se van a invocar en el prog_principal.

    Las funciones del modulo son : 

    hacer_grafico_horizontal
    hacer_grafico_vertical

    En el programa principal se renombra el modulo como g, un ejemplo de esto:

    if orientacion:
        g.hacer_grafico_horizontal(matr, mx, caps, dicc, cantS, cantV, cantA,
            ColSus, ColVer, ColAdj, definiciones, cantPalIngresadas, fuente)
"""

def hacer_grafico_horizontal(m, 
                             l, 
                             caps, 
                             dicc, 
                             cs, 
                             cv, 
                             ca, 
                             col_s, 
                             col_v, 
                             col_a, 
                             defi, 
                             cant_p, 
                             fuente):
    """Esta funcion va a emplear la vista del grafico horizontal

    Args:
        m ([type]): [description]
        l ([type]): [description]
        caps ([type]): [description]
        dicc ([type]): [description]
        cs ([type]): [description]
        cv ([type]): [description]
        ca ([type]): [description]
        col_s ([type]): [description]
        col_v ([type]): [description]
        col_a ([type]): [description]
        defi ([type]): [description]
        cant_p ([type]): [description]
        fuente ([type]): [description]
    """
    BOX_SIZE = 25
    a = []
    cont = 0
    a.append(sg.Text('                                                                       '))
    if defi:
        a.append(sg.Button('Definiciones'))
        defs = []
        auxx = []
        for x in range(len(m)):
            pla = ''
            for y in m[x]:
                pla = pla + y
            auxx.append(pla)
        for x in dicc.keys():
            for y in range(len(dicc[x])):
                if dicc[x][y][0].upper() in auxx:
                    defs.append([dicc[x][y][1]])
        layout_def = [[sg.Text('Definiciones: ')], 
                      [sg.Listbox(defs, auto_size_text=False, size=(50, 5))], 
                      [sg.Button('Salir')]]
    if cant_p:
        a.append(sg.Button('Palabras'))
        layout_pal = [[sg.Text('Palabras')], 
                      [sg.Listbox(m, size=(None, len(m)))]]

    layout = [
        [sg.Button('Verbo', button_color=('black', col_v)),
         sg.Button('Adjetivo', button_color=('black', col_a)),
         sg.Button('Sustantivo', button_color=('black', col_s))], a,
        [sg.Text(('Cant. Verbos: ' + str(cv)), key='_VERB_'),
         sg.Text(('Cant. Adj: ' + str(ca)), key='_ADJT_'),
         sg.Text(('Cant. Sust: ' + str(cs)), key='_SUST_')],
        [sg.Graph((l * 70, l * 70), (0, l * 55), (l * 55, 0), 
                  key='_GRAPH_',
                  change_submits=True, 
                  drag_submits=False)],
        [sg.Button('Verificar'), 
         sg.Button('Salir'), 
         sg.Text('                                  '), 
         sg.Button('Ayuda')]
    ]
    window = sg.Window('Sopa de Letras').Layout(layout).Finalize()
    g = window.FindElement('_GRAPH_')
    a = window.FindElement('_ADJT_')
    v = window.FindElement('_VERB_')
    s = window.FindElement('_SUST_')
    for row in range(l * 2):
        for col in range(l * 2):
            g.DrawRectangle((col * BOX_SIZE + 5, 
                             row * BOX_SIZE + 3),
                            (col * BOX_SIZE + BOX_SIZE + 5, 
                             row * BOX_SIZE + BOX_SIZE + 3), 
                             line_color='black',
                             fill_color='white')
    aux = {}
    i = random.randrange(0, l * 2)
    for row in range(l * 2):
        j = random.randrange(0, l)
        for col in range(l * 2):
            try:
                g.DrawText(text=m[row][col], 
                           location=(j * BOX_SIZE + 18, 
                                     i * BOX_SIZE + 17), 
                           font=fuente)
                aux[j, i] = m[row][col]
                j += 1
            except IndexError:
                if caps:
                    let = random.choice(string.ascii_uppercase)
                    g.DrawText(text=let,
                               location=(j * BOX_SIZE + 18, 
                                         i * BOX_SIZE + 17), 
                               font=fuente)
                else:
                    let = random.choice(string.ascii_lowercase)
                    g.DrawText(text=let,
                               location=(j * BOX_SIZE + 18, 
                                         i * BOX_SIZE + 17), 
                               font=fuente)
                aux[j, i] = let
                j += 1 if j < (l * 2) - 1 else 0

            i+= 1 if i < (l * 2) - 1 else 0
    tipo = None
    locc = None
    ing = []
    while True:  # Event Loop
        event, values = window.Read()
        if event == 'Verbo':
            tipo = 'Verbo'
        elif event == 'Sustantivo':
            tipo = 'Sustantivo'
        elif event == 'Adjetivo':
            tipo = 'Adjetivo'
        if event is None or event == 'Salir':
            break
        if event == 'Definiciones':
            wndow = sg.Window('Definiciones').Layout(layout_def)
            wndow.Read()
            wndow.Close()
        if event == 'Palabras':
            wndw = sg.Window('Palabras').Layout(layout_pal)
            wndw.Read()
            wndw.Close()
        mouse = values['_GRAPH_']
        if event == 'Ayuda':
            sg.Popup('Primero seleccione el tipo de palabra a buscar, luego '
                     'seleccione\n las palabras letra por letra ' +
                     'y luego haga click en verificar', 
                     title='Ayuda')
        if event == '_GRAPH_':
            if mouse == (None, None):
                continue
            box_x = mouse[0] // BOX_SIZE
            box_y = mouse[1] // BOX_SIZE
            letter_location = (box_x * BOX_SIZE + 18, 
                               box_y * BOX_SIZE + 17)
            if letter_location != locc:
                if tipo == 'Verbo':
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color=col_v)
                elif tipo == 'Sustantivo':
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color=col_s)
                else:
                    fill_color= col_a if tipo =='Adjetivo' else 'white'
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color= fill_color)
            else:
                g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                          box_y * BOX_SIZE + 3.5),
                                bottom_right=(box_x * BOX_SIZE + 30, 
                                              box_y * BOX_SIZE + 28), 
                                              fill_color='white')
            locc = letter_location
            ing.append(aux[box_x, box_y])
            g.DrawText(aux[box_x, box_y], letter_location, font=fuente)
        if event == 'Verificar':
            if not tipo:
                continue
            for k in range(len(dicc[tipo][0])):
                if ing in m:
                    cont += 1
                    if cont >= len(m):
                        window.Close()
                        sg.Popup('Felicidades, ganaste!', no_titlebar=True)
                    else:
                        if tipo == 'Verbo':
                            cv -= 1
                            v.Update('Cant. Verbos: ' + str(cv))
                        if tipo == 'Adjetivo':
                            ca -= 1
                            a.Update('Cant. Adj: ' + str(ca))
                        if tipo == 'Sustantivo':
                            cs -= 1
                            s.Update('Cant. Sust.: ' + str(cs))
                        sg.Popup('Correcto ' + 
                                 'te faltan ' + 
                                 str(len(m) - cont) + 
                                 ' palabras',
                                 auto_close=True, 
                                 auto_close_duration=5, 
                                 no_titlebar=True)
                    break
                else:
                    sg.Popup('Selecciona de nuevo la plabra', no_titlebar=True)
                    break
            ing = []


def hacer_grafico_vertical(m, 
                           l, 
                           caps, 
                           dicc, 
                           cs, 
                           cv, 
                           ca, 
                           col_s, 
                           col_v, 
                           col_a, 
                           defi, 
                           cant_p, 
                           fuente):
    """Esta funcion va a emplear la vista del grafico horizontal

    Args:
        m ([type]): [description]
        l ([type]): [description]
        caps ([type]): [description]
        dicc ([type]): [description]
        cs ([type]): [description]
        cv ([type]): [description]
        ca ([type]): [description]
        col_s ([type]): [description]
        col_v ([type]): [description]
        col_a ([type]): [description]
        defi ([type]): [description]
        cant_p ([type]): [description]
        fuente ([type]): [description]
    """
    BOX_SIZE = 25
    a = []
    cont = 0
    a.append(sg.Text('                                                                       '))
    if defi:
        a.append(sg.Button('Definiciones'))
        defs = []
        auxx = []
        for x in range(len(m)):
            pla = ''
            for y in m[x]:
                pla = pla + y
            auxx.append(pla)
        for x in dicc.keys():
            for y in range(len(dicc[x])):
                if dicc[x][y][0].upper() in auxx:
                    defs.append([dicc[x][y][1]])
        layout_def = [[sg.Text('Definiciones: ')], 
                      [sg.Listbox(defs, auto_size_text=False, size=(50, 5))],
                     [sg.Button('Salir')]]
    if cant_p:
        a.append(sg.Button('Palabras'))
        layout_pal = [[sg.Text('Palabras')], 
                      [sg.Listbox(m, size=(None, len(m)))]]

    layout = [[sg.Button('Verbo', button_color=('black', col_v)),
         sg.Button('Adjetivo', button_color=('black', col_a)),
         sg.Button('Sustantivo', button_color=('black', col_s))], a,
        [sg.Text(('Cant. Verbos: ' + str(cv)), key='_VERB_'),
         sg.Text(('Cant. Adj: ' + str(ca)), key='_ADJT_'),
         sg.Text(('Cant. Sust: ' + str(cs)), key='_SUST_')],
        [sg.Graph((l * 70, l * 70), (0, l * 55), (l * 55, 0), 
                  key='_GRAPH_',
                  change_submits=True, 
                  drag_submits=False)],
        [sg.Button('Verificar'), 
         sg.Button('Salir'), 
         sg.Text('                                  '), 
         sg.Button('Ayuda')]]
    window = sg.Window('Window Title', ).Layout(layout).Finalize()

    g = window.FindElement('_GRAPH_')
    a = window.FindElement('_ADJT_')
    v = window.FindElement('_VERB_')
    s = window.FindElement('_SUST_')
    for row in range(l * 2):
        for col in range(l * 2):
            g.DrawRectangle((col * BOX_SIZE + 5, 
                             row * BOX_SIZE + 3),
                            (col * BOX_SIZE + BOX_SIZE + 5, 
                             row * BOX_SIZE + BOX_SIZE + 3), 
                             line_color='black',
                            fill_color='white')
    aux = {}
    i = random.randrange(0, l * 2)
    for row in range(l * 2):
        j = random.randrange(0, l)
        for col in range(l * 2):
            try:
                g.DrawText(text=m[row][col], 
                           location=(i * BOX_SIZE + 18, j * BOX_SIZE + 17), 
                           font='Helvetica 10')
                aux[i, j] = m[row][col]
                j += 1
            except IndexError:
                if caps:
                    let = random.choice(string.ascii_uppercase)
                    g.DrawText(text=let,
                               location=(i * BOX_SIZE + 18, j * BOX_SIZE + 17), 
                               font='Helvetica 10')
                else:
                    let = random.choice(string.ascii_lowercase)
                    g.DrawText(text=let,
                               location=(i * BOX_SIZE + 18, j * BOX_SIZE + 17), 
                               font='Helvetica 10')
                aux[i, j] = let

                j+=1 if j < (l * 2) - 1 else 0
        i+= 1 if i < (l * 2) - 1 else 0

    tipo = None
    locc = None
    ing = []
    while True:  # Event Loop
        event, values = window.Read()
        if cont >= len(m):
            window.Close()
            sg.Popup('Felicidades, ganaste!')
            break
        if event == 'Verbo':
            tipo = 'Verbo'
        elif event == 'Sustantivo':
            tipo = 'Sustantivo'
        elif event == 'Adjetivo':
            tipo = 'Adjetivo'
        if event is None or event == 'Salir':
            break
        if event == 'Definiciones':
            wndow = sg.Window('Definiciones').Layout(layout_def)
            wndow.Read()
            wndow.Close()
        if event == 'Palabras':
            wndw = sg.Window('Palabras').Layout(layout_pal)
            wndw.Read()
            wndw.Close()
        mouse = values['_GRAPH_']
        if event == 'Ayuda':
            sg.Popup('Primero seleccione el tipo de palabra a buscar, luego '
                     'seleccione\n las palabras letra por letra ' + 
                     'y luego haga click en verificar', title="Ayuda")
        if event == '_GRAPH_':
            if mouse == (None, None):
                continue
            box_x = mouse[0] // BOX_SIZE
            box_y = mouse[1] // BOX_SIZE
            letter_location = (box_x * BOX_SIZE + 18, 
                               box_y * BOX_SIZE + 17)
            if letter_location != locc:
                if tipo == 'Verbo':
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color='green')
                elif tipo == 'Sustantivo':
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color='red')
                else:
                    fill_color= col_a if tipo =='Adjetivo' else 'white'
                    g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                              box_y * BOX_SIZE + 3.5),
                                    bottom_right=(box_x * BOX_SIZE + 30, 
                                                  box_y * BOX_SIZE + 28), 
                                                  fill_color= fill_color)
            else:
                g.DrawRectangle(top_left=(box_x * BOX_SIZE + 5, 
                                          box_y * BOX_SIZE + 3.5),
                                bottom_right=(box_x * BOX_SIZE + 30, 
                                              box_y * BOX_SIZE + 28), 
                                              fill_color='white')
            locc = letter_location
            ing.append(aux[box_x, box_y])
            g.DrawText(aux[box_x, box_y], letter_location, 
                       font='Courier 13')
        if event == 'Verificar':
            if not tipo:
                continue
            for k in range(len(dicc[tipo][0])):
                if ing in m:
                    cont += 1
                    if cont >= len(m):
                        window.Close()
                        sg.Popup('Felicidades, ganaste!', no_titlebar=True)
                    else:
                        if tipo == 'Verbo':
                            cv -= 1
                            v.Update('Cant. Verbos: ' + str(cv))
                        if tipo == 'Adjetivo':
                            ca -= 1
                            a.Update('Cant. Adj: ' + str(ca))
                        if tipo == 'Sustantivo':
                            cs -= 1
                            s.Update('Cant. Sust.: ' + str(cs))
                        sg.Popup('Correcto ' + 
                                 'te faltan ' + 
                                 str(len(m) - cont) + 
                                 ' palabras',
                                 auto_close=True, 
                                 auto_close_duration=5, 
                                 no_titlebar=True)
                    break
                else:
                    sg.Popup('Selecciona de nuevo la plabra', no_titlebar=True)
                    break
            ing = []
    window.Close()
