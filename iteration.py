from collatz_functions import *
import csv
import numpy as np
import math
from tqdm import tqdm
import os

#----------------------------------------------- Parámetros de la ejecución ----------------------------------------------------------------

funcion_iterar = 'C' # C (mayúscula) para usar C(x), T (mayúscula) para iterar T(x)

guardar = True # True si queremos guardar los cálculos en un fichero .csv. False en caso contrario. 
nombre_archivo = 'prueba.csv' # Nombre del archivo que crearemos. PRECAUCIÓN: si guardar = False y el nombre del archivo 
                              # coincide con uno existente, este se borrará
 
rango = True # True si queremos hacer el cálculo para un intervalo entre dos valores, por ejemplo, [1, 10^7]. False si queremos elegir qué
             # valores queremos iterar, por ejemplo, [10, 4, 7564, 2345346]
# Si hemos elegido rango = True, elegir los valores iniciales y finales del intervalo. Si rango = False estos valores no intervienen en el programa
valor_inicial = 1
valor_final = pow(10, 3)
# Si hemos elegido rango = False, elegir los valores que queremos iterar introduciéndolos en el siguiente vector. Si rango = True, el vector
# no interviene en ningún cálculo
vector_iterar = [1346, pow(10, 50) - 1, pow(10, 500) + 1]

random = False # True si queremos escoger número aleatorios en el intervalo que hemos elegido
num_random = 10000 # Número de elementos aleatorios que queremos seleccionar del intervalo


if rango is True and random is True:
    vector_iterar = np.random.randint(valor_inicial, valor_final, num_random)
elif rango is True and random is False:
    vector_iterar = np.arange(valor_inicial, valor_final + 1)

precision = 3  # número decimales para la notación científica
error_modelo = 0
orden_magnitud = 0
aux = 0

#--------------------------------------------------- Bucle de ejecución -------------------------------------------------------------------

ruta_completa = os.path.join('Data', nombre_archivo)

if os.path.isdir('Data') == False:
            os.makedirs('Data')
            print('Se ha creado la carpeta "Data"')

with open(ruta_completa, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    encabezado = ['Número', 'secuencia'] # Primero fila del .csv
    #encabezado  = ['secuencia']
    escritor_csv.writerow(encabezado)

    # La siguiente línea es el bucle for. Para rangos muy grande, la línea (1) puede dar problemas de memoria. Si es así, 
    # simplemente comentarla y descomanetar la línea (2)
    #for n in tqdm(vector_iterar, desc=f'Iterando {funcion_iterar}(x)', unit=" elemento"):   # (1)
    for n in tqdm(range(valor_inicial, valor_final + 1), desc=f'Iterando {funcion_iterar}(x)', unit=" elemento"): # (2)

        # Parámetros que iremos actualizando y luego guardaremos
        n_inicial = n
        numero_iteraciones = 0
        tiempo_parada = 0
        secuencia = []
        secuencia.append(n)

        # Contamos si el número inicial es par o impar para llevar bien la cuenta de estos
        if n % 2 == 0:
            numero_pares = 1
        else:
            numero_pares = 0

        # Iteramos cada valor con la función elegida. También contamos los números pares e impares
        while n != 1:
            n = collatz_function(n, funcion_iterar)
            secuencia.append(n)
            numero_iteraciones += 1

            if n % 2 == 0:
                numero_pares += 1

            if n < n_inicial and tiempo_parada == 0:
                tiempo_parada = numero_iteraciones

        
        # Calculamos algunos parámetros que luego guardaremos
        pico_maximo = max(secuencia)
        s = max(secuencia) / n_inicial
        proporcion_pares = numero_pares / len(secuencia)
        aux = aux + proporcion_pares
        error_modelo += np.abs(len(secuencia) - 6.952 * math.log(n_inicial)) / len(secuencia) * 100

        

        if guardar is True:
            # Elegimos qué cantidades queremos guardar. Si se cambia, acordarse de cambiar el encabezado del archivo
            #guardar_vector = [secuencia]
            
            guardar_vector = [n_inicial,
                              secuencia]
            
            escritor_csv.writerow(guardar_vector)

        # Si queremos ir mostrando algunos datos para los números que vamos calculando, descomentar las siguientes líneas
        '''
        print(f'Proporción de número pares en la secuencia: {proporcion_pares}')
        print(f'Secuencia: {secuencia}')
        print(f'Número de iteraciones: {numero_iteraciones}\nTiempo de parada: {tiempo_parada}')
        print(f'Pico máximo: {pico_maximo}')
        print(f'Factor de expansión: {s}')
        print('--------------------------------------------------------------------------')
        '''

    proporcion_pares_total = aux / len(vector_iterar)
    print(f'Proporción total de números pares: {proporcion_pares_total}')
