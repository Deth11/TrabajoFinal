import PySimpleGUI as sg


def hacer_grafico(m, dicc, deff, cantP, cantTP):
    colum = [[sg.Button('Sustantivo', button_color=('black', 'red'))],
            [sg.Button('Adjetivo', button_color=('black', 'green'))],
            [sg.Button('Verbo', button_color=('black', 'yellow'))]]
    pistas = []

    if deff:
        for elem in dicc:
            for x in dicc[elem]:
                pistas.append(sg.Text(text=x[1]))
    print(pistas)


    def layout_g(col, pist=[sg.Text('')]):
        return [[sg.Column(col)],
                [sg.Graph(canvas_size=(500, 500), graph_bottom_left=(-500, -500), graph_top_right=(500, 500),
                      background_color='white', key='graph', enable_events=True)], pist]
    window = sg.Window('Sopa de Letras', layout_g(colum, pistas), grab_anywhere=False).Finalize()
    graph = window.Element('graph')

    x = -499
    x1 = 499
    y = -450
    y1 = 450
    i = 0
    r = 0
    while x1 > -500 and y1 > -550:
        while x < 500 and y < 550:
            graph.DrawRectangle(bottom_right=(x, x1), top_left=(y, y1))
            graph.DrawText(text=m[i][0][r], location=(x+25, x1-25))
            if r < len(m[i][0])-1:
                r += 1
            else:
                r = 0
                if i < len(m)-1:
                    i += 1
                else:
                    i = 0
            x += 50
            y += 50
        r = 0
        i -= 1
        if i < len(m)-1:
            i += 1
        else:
            i = 0
        x = -499
        y = -450
        x1 -= 50
        y1 -= 50
    event, values = window.Read()
    print(event)
    print(values)
