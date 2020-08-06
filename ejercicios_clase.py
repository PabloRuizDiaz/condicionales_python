#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pablo"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos

    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print('1er numero ingresado {} es mayor al 2do ingresado {}' .format(numero_1, numero_2))
    else:
        print('2do numero ingresado {} es mayor al 1ro ingresado {}' .format(numero_2, numero_1))
        
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 < 0:
        print('1er numero ingresado {} es negativo' .format(numero_1))
    elif numero_1 == 0:
        print('1er numero ingresado es cero')
    else:
        print('1er numero ingresado {} es positivo' .format(numero_1))

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 > 0 and numero_1 < 100):
        print('El 1er numero {} esta en el rango (0;100)' .format(numero_1))
    else:
        print('El 1er numero {} esta fuera del rango (0:100)' .format(numero_1))

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10 or numero_2 > -2):
        print('El 1er numero es menor a 10, o el 2do numero es mayor a -2')
    else:
        print('El 1er numero es mayor a 10, o el 2do es menor a -2')


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas

    texto_1 = str(input('Ingrese la primera palabra:\n'))
    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print('El texto 1 "{}" es mayor alfabeticamente' .format(texto_1))
    else:
        print('El texto 2 "{}" es mayor alfabeticamente' .format(texto_2))

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    if len(texto_1) > len(texto_2):
        print('El texto 1 "{}" es mas largo que el texto 2 "{}"' .format(texto_1, texto_2))
    else:
        print('El texto 2 "{}" es mas largo que el texto 1 "{}"' .format(texto_2, texto_1))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if texto_1[0] > texto_2[0]:
        print('La 1er letra de "{}" es mas grande que la 1ra de "{}"' .format(texto_1, texto_2))
    elif texto_1[0] < texto_2[0]:
        print('La 1er letra de "{}" es mas grande que la 1ra de "{}"' .format(texto_2, texto_1))
    else:
        print('la 1ra letra de las palabras "{}" y "{}" son iguales' .format(texto_1, texto_2))

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    print('Se realizo correctamente la copia de Texto 1?', copia_texto_1 == texto_1)

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    print('La copia de Texto 1 es igual a Texto 2?', copia_texto_1 == texto_2)
    if copia_texto_1 == texto_2:
        print('La copia de Texo 1 es igual a Texto 2')
    else:
        print('La copia de Texo 1 NO es igual a Texto 2')


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados

    numero_1 = float(input('Ingrese un numero \n'))
    numero_2 = float(input('Ingrese un numero \n'))

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print('Resp=1')
        else:
            print('Resp=2')
    else:
        if numero_2 > 5:
            print('Resp=3')
        else:
            print('Resp=4')

    # Modificacion ejercicio 3 con elif

    if (numero_1 > 5 and numero_2 > 0):
        print('Resp=1')
    elif (numero_1 > 5 and numero_2 <= 0):
        print('Resp=2')
    elif (numero_1 <= 5 and numero_2 > 5):
        print('Resp=3')
    elif (numero_1 <= 5 and numero_2 <= 5):
        print('Resp=4')
    
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen

    puntaje = int(input('Ingrese calificacion \n'))

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 60:
        if puntaje >= 70:
            if puntaje >= 80:
                if puntaje >= 90:
                    print('A')
                else:
                    print('B')
            else:
                print('C')
        else:
            print('D')
    else:
        print('F')


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print('El texto "{}" es mayor al "{}"' .format(texto_1, texto_2))
    else:
        print('El texto "{}" es mayor al "{}"' .format(texto_2, texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    
    numero_1 = int(texto_1)
    numero_2 = int(texto_2)

    if numero_1 > numero_2:
        print('Numericamente el numero "{}" es mayor a "{}"' .format(numero_1, numero_2))
    else:
        print('Numericamente el numero "{}" es mayor a "{}"' .format(numero_2, numero_1))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
