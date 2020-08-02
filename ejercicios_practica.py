#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Pablo"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.2"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))

    diferencia = numero_1 - numero_2

    if diferencia < 0:
        print('Resultado de la resta {} es negativo' .format(diferencia))
    elif diferencia == 0:
        print('Resultado de la resta es cero')
    else:
        print('Resultado de la resta {} es positivo' .format(diferencia))


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''

    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el segundo número:\n'))
    numero_3 = int(input('Ingrese el tercer número:\n'))

    if numero_1 % 2 == 0:
      print('El numero {} es par' .format(numero_1))
    else:
      print('El numero {} es impar' .format(numero_1))
    
    if  numero_2 % 2 == 0:
      print('El numero {} es par' .format(numero_2))
    else:
      print('El numero {} es impar' .format(numero_2))

    if numero_3 % 2 == 0:
      print('El numero {} es par' .format(numero_3))
    else:
      print('El numero {} es impar' .format(numero_3))


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''

    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input('Ingrese el segundo número:\n'))
    operacion = str(input('Ingrese la operacion a ejecutar:\n + -> suma \n - -> resta \n * -> multiplicacion \n / -> division \n ** -> potenciacion \n'))

    if operacion == '+':
      print('La suma es {}' .format(numero_1 + numero_2))
    elif operacion == '-':
      print('La resta es {}' .format(numero_1 - numero_2))
    elif operacion == '*':
      print('La multiplicacion es {}' .format(numero_1 * numero_2))
    elif operacion == '/':
      print('La division es {}' .format(numero_1 / numero_2))
    elif operacion == '**':
      print('{} a la potencia de {} es {}' .format(numero_1, numero_2, numero_1 ** numero_2))
    else:
      print('Operacion matematica no existente.')


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
  '''

    texto_1 = str(input('Ingrese primera palabra:\n'))
    texto_2 = str(input('Ingrese segunda palabra:\n'))
    texto_3 = str(input('Ingrese tercera palabra:\n'))
    operacion_txt = str(input('Ingrese accion a realizar: \n > -> Orden alfabetico \n Lon -> Cantidad de letras \n'))

    if operacion_txt == '>':
      if (texto_1 > texto_2 and texto_1 > texto_3 and texto_2 > texto_3):
        print(texto_3, ' ', texto_2, ' ', texto_1)
      elif (texto_1 > texto_2 and texto_1 > texto_3 and texto_2 < texto_3):
        print(texto_2, ' ', texto_3, ' ', texto_1)
      elif (texto_2 > texto_1 and texto_2 > texto_3 and texto_1 > texto_3):
        print(texto_3, ' ', texto_1, ' ', texto_2)
      elif (texto_2 > texto_1 and texto_2 > texto_3 and texto_1 < texto_3):
        print(texto_1, ' ', texto_3, ' ', texto_2)
      elif (texto_3 > texto_1 and texto_3 > texto_2 and texto_1 > texto_2):
        print(texto_2, ' ', texto_1, ' ', texto_3)
      elif (texto_3 > texto_1 and texto_3 > texto_2 and texto_1 < texto_2):
        print(texto_1, ' ', texto_2, ' ', texto_3)
      else:
        print('Las tres palabras son iguales alfabeticamente')      
    elif operacion_txt == 'Lon':
      if (len(texto_1) > len(texto_2) and len(texto_1) > len(texto_3) and len(texto_2) > len(texto_3)):
        print(' ', texto_1, '\n', texto_2, '\n', texto_3)
      elif (len(texto_1) > len(texto_2) and len(texto_1) > len(texto_3) and len(texto_2) < len(texto_3)):
        print(' ', texto_1, '\n', texto_3, '\n', texto_2)
      elif (len(texto_2) > len(texto_1) and len(texto_2) > len(texto_3) and len(texto_1) > len(texto_3)):
        print(' ', texto_2, '\n', texto_1, '\n', texto_3)
      elif (len(texto_2) > len(texto_1) and len(texto_2) > len(texto_3) and len(texto_1) < len(texto_3)):
        print(' ', texto_2, '\n', texto_3, '\n', texto_1)
      elif (len(texto_3) > len(texto_1) and len(texto_3) > len(texto_2) and len(texto_1) > len(texto_2)):
        print(' ', texto_3, '\n', texto_1, '\n', texto_2)
      elif (len(texto_3) > len(texto_1) and len(texto_3) > len(texto_2) and len(texto_1) < len(texto_2)):
        print(' ', texto_3, '\n', texto_2, '\n', texto_2)
      else:
        print('Las tres palabras son iguales de largas')
    else:
      print('Accion no existente.')



def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    temp_1 = float(input('Ingrese 1er temperatura \n'))
    temp_2 = float(input('Ingrese 2da temperatura \n'))
    temp_3 = float(input('Ingrese 3er temperatura \n'))

    if (temp_1 > temp_2 and temp_1 > temp_3):
      print('{} es la temperatura maxima' .format(temp_1))
    elif (temp_2 > temp_1 and temp_2 > temp_3):
      print('{} es la temperatura maxima' .format(temp_2))
    elif (temp_3 > temp_1 and temp_3 > temp_2):
      print('{} es la temperatura maxima' .format(temp_3))

    if (temp_1 < temp_2 and temp_1 < temp_3):
      print('{} es la temperatura minima' .format(temp_1))
    elif (temp_2 < temp_1 and temp_2 < temp_3):
      print('{} es la temperatura minima' .format(temp_2))
    elif (temp_3 < temp_1 and temp_3 < temp_2):
      print('{} es la temperatura minima' .format(temp_3))

    print('El promedio entre las temperaturas es {}' .format((temp_1 + temp_2 + temp_3) / 3))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
