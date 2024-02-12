import numpy as np
import pandas as pd
from tqdm import tqdm
import ast
import matplotlib.pyplot as plt


encodings = ['utf-8', 'latin1', 'ISO-8859-1']

for encoding in encodings:
    try:
        datos = pd.read_csv('prueba.csv', encoding=encoding, index_col = 0)
        print(f"CSV file read successfully with encoding: {encoding}")
        break  # Break out of the loop if successful
    except UnicodeDecodeError:
        print(f"Failed to read with encoding: {encoding}")

print('Conviertiendo secuencias (esto puede tardar un rato)')
datos['secuencia'] = datos['secuencia'].apply(ast.literal_eval) # para que las secuancias las interprete como números y no como strings

secuencias = np.array(datos['secuencia'].values)
for secuencia in tqdm(secuencias, desc='Formateando secuencias', unit='secuencia'):
    secuencia.reverse()
    del secuencia[0]

vector_colores = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque',
    'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue',
    'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
    'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen',
    'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
    'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue',
    'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink',
    'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite',
    'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod',
    'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred',
    'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon',
    'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray',
    'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen',
    'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow',
    'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine',
    'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue',
    'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
    'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive',
    'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen',
    'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink',
    'plum', 'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue',
    'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver',
    'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue',
    'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white',
    'whitesmoke', 'yellow', 'yellowgreen'
]

x = []
y = []


denominador_par = 100
denominador_impar = 100
angulo_par = np.pi / denominador_par
angulo_impar = - np.pi / denominador_impar



for secuencia in tqdm(secuencias, desc=f'Obteniendo vectores para hacer el gráfico', unit=" secuencia"):
    y_singular = []
    x_singular = []
    y_singular.append(1)
    x_singular.append(1)
    angulo_total = 0
    for i in range(1, len(secuencia) - 1):
        if secuencia[i] % 2 == 0:
            angulo_total += angulo_par
            x_singular.append(x_singular[i - 1] + np.cos(angulo_total))
            y_singular.append(y_singular[i - 1] + np.sin(angulo_total))
        else:
            angulo_total += angulo_impar
            x_singular.append(x_singular[i - 1] + np.cos(angulo_total))
            y_singular.append(y_singular[i - 1] + np.sin(angulo_total))

    x.append(x_singular)
    y.append(y_singular)



color_grafico = 'seagreen'
plt.figure(figsize=(11.69, 8.26), facecolor='black')
plt.axis('off')  # Elimina los ejes
for i in tqdm(range(len(x)), desc=f'Pintando', unit=" secuencia"):
    plt.plot(x[i], y[i], alpha = 0.02, color = color_grafico, linewidth=0.5)

print('Generando imagen (esto puede tardar un rato)')
plt.savefig(f'Figures/visualization_color_{color_grafico}_len_{len(secuencias)}_par_{denominador_par}_impar_{denominador_impar}.pdf', bbox_inches='tight')
print('pdf generaddo')
plt.savefig(f'Figures/visualization_color_{color_grafico}_len_{len(secuencias)}_par_{denominador_par}_impar_{denominador_impar}.png', dpi=600, bbox_inches='tight')  # Guardar el gráfico con una resolución de 300 dpi
print('png generado')
plt.close()
print('Finalizado')