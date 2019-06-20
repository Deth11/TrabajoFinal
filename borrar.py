import Grafico
import Matriz

matr = []
dicc = {'Sustantivo': [('Futbol', 0), ('Computadora', 0)],
        'Adjetivo': [('Lindo', 0), ('Lento', 0)],
        'Verbo': [('Correr', 0), ('Masturbar', 0)]}
mx = 0
caps = False
Matriz.matriz_vertical(dicc, matr, mx, caps)
print(mx)
d = True
tp = False
p = False
Grafico.hacer_grafico(matr, dicc, d, p, tp)
