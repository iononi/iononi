#!/usr/bin/env python3

#Programa que convierte de DECIMAL a BINARIO y viceversa
#Acepta numeros binarios con punto binario
#Falta incorporar capacidad para convertir numero decimales con punto decimal a binario

import re
import math

def decimal_to_binary(decimal):
    """Convierte un número decimal entero positivo a binario."""
    try:
        
        #Obtengo el cociente y la parte fraccionaria del numero decimal
        fraccion, cociente = math.modf(decimal)

        if cociente == 0 and fraccion == 0:
            return True, "0"

        #Trato al cociente como entero
        cociente = int(cociente)

        cociente_rest_list = []
        bit = ""

        #Aplica el método de división sucesiva entre 2 al número decimal y a los cocientes
        
        if cociente > 0:
            while (cociente > 0):
                residuo = cociente % 2
                cociente //= 2
                cociente_rest_list.append(residuo)

            #Itero sobre la lista en reversa para obtener el resultado de la conversión
            
            for i in range(len(cociente_rest_list) - 1, -1, -1):
                bit += str(cociente_rest_list[i])

        #Obtengo los bits equivalentes a la parte decimal
        if fraccion > 0:
            bit += "."
            for i in range(0, 11):
                result = fraccion * 2
                fraccion, cociente = math.modf(result)
                bit += str(int(cociente))
                fraccion = fraccion

        #Si se pudo convertir, devuelvo True y el resultado de la conversión
        return True, bit
    except ValueError:
        #Devuelvo que no se pudo convertir si el numero decimal no es entero
        return False, ""

def binary_to_decimal(binary):
    """Convierte un número binario(con o sin punto binario) a su equivalente decimal."""
    #Verifico que el numero ingresado esté conformado por 0's y 1's
    check = re.search(r"([01]*).?([01]*)", binary)

    #Si no, retorno que no se pudo convertir
    if len(check[1]) == 0 and len(check[2]) == 0:
        return False, "Compruebe que ha ingresado un numero binario valido."

    e = 0   #Un exponente que simboliza la máxima potencia de 2 para el número en cuestión
    decimal_number = 0      #Variable donde se almacenará el resultado de la conversión

    if len(check[1]) > 0:
        e = len(check[1]) - 1
        #Comienzo desde el MSB
        for bit in check[1]:
            decimal_number += int(bit) * 2 ** e
            e -= 1  #Decremento el valor del exponente hasta llegar a 0
        
    if len(check[2]) > 0:
        #Comienzo desde el primer bit después del punto binario
        e = 1
        for bit in check[2]:
            decimal_number += int(bit) * 2 ** (-e)
            e += 1
    
    #Devuelvo que se pudo convertir y el resultado
    return True, decimal_number

def main():
    """Función principal"""
    print("[1] - Convertir de DECIMAL a BINARIO.")
    print("[2] - Convertir de BINARIO a DECIMAL.")

    option = 0
    
    while(option <= 0 or option > 2):
        try:
            option = int(input("Ingrese una opcion: "))
        except ValueError:
            continue

    
    if option == 1:
        decimal_number = float(input("Ingrese el numero decimal que desea convertir a binario: "))

        converted, result = decimal_to_binary(decimal=decimal_number)

        if not converted:
            print("El numero decimal ingresado no esta soportado actualmente.")
        else:
            print("El numero decimal {} equivale al binario {}.".format(decimal_number, result))

    if option == 2:
        binary_number = input("Ingrese el numbero binario que desea convertir a decimal: ")

        converted, result = binary_to_decimal(binary=binary_number.strip())

        if not converted:
            print(result)
        else:
            print("El numero binario {} equivale a {} en decimal.".format(binary_number, result))

main()