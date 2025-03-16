#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 
# pyching -- a Python program to cast and interpret I Ching hexagrams
# 
# Copyright (C) 2020 Zorbatrusta
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be of some
# interest to somebody, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING or COPYING.txt. If not,
#  write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# The license can also be found at the GNU/FSF website: http://www.gnu.org
# 
import time
from random import seed, randint
from time import sleep
from datetime import datetime

cadenaiching = "I Ching"
cadenawilhem = "Richard H. Wilhem"
print(cadenaiching.center(70, "="))
print(" Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?.")
print(" El Libro de las Mutaciones es la obra mediante la cual los sabios")
print(" santos elevaron su modo de ser y ampliaron su campo de acción.")
print(cadenawilhem.center(70, "="))
print("")
sleep(9)
yoda = '''                   
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_DLC;-";.__
          .-j/'.;  ;""""  / .'!"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   |.
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  
                 "-.t-._:'
'''
print(yoda)
sleep(3)

TIEMPO_ESPERA_PREGUNTA = 13
TIEMPO_ESPERA_ENTRE_TIRADAS = 1

HEXAGRAMAS = {
    "111111": 1, "000000": 2, "100010": 3, "010001": 4, "111010": 5, "010111": 6,
    "010000": 7, "000010": 8, "111011": 9, "110111": 10, "111000": 11, "000111": 12,
    "101111": 13, "111101": 14, "001000": 15, "000100": 16, "011001": 17, "100110": 18,
    "000011": 19, "110000": 20, "101001": 21, "100101": 22, "000001": 23, "100000": 24,
    "111001": 25, "100111": 26, "100001": 27, "011110": 28, "010010": 29, "101101": 30,
    "001110": 31, "011100": 32, "001111": 33, "111100": 34, "000101": 35, "101000": 36,
    "110001": 37, "100011": 38, "000110": 39, "011000": 40, "110110": 41, "011011": 42,
    "110010": 43, "010110": 44, "101011": 45, "110101": 46, "010011": 47, "001010": 48,
    "011101": 49, "101110": 50, "100100": 51, "001001": 52, "110011": 53, "001100": 54,
    "101111": 55, "111101": 56, "011010": 57, "001011": 58, "100110": 59, "011001": 60,
    "101010": 61, "010101": 62, "101100": 63, "001101": 64
}

def generar_nombre_archivo():
    ahora = datetime.now()
    return f"consulta_iching_{ahora.strftime('%Y%m%d_%H%M%S')}.txt"

def guardar_pregunta(nombre_archivo):
    pregunta = input("Ingresa tu pregunta para el oráculo: ")
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Fecha y hora de la consulta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Pregunta: {pregunta}\n")
    return pregunta

def generar_hexagrama():
    ts = time.time()
    seed(ts)
    lineas = []
    for i in range(1, 7):
        print(f"{i}ª tirada...")
        linea = randint(6, 9)
        print(linea)
        lineas.append(linea)
        sleep(TIEMPO_ESPERA_ENTRE_TIRADAS)
    return lineas

def convertir_a_binario(lineas):
    """
    Convierte las líneas del hexagrama a binario.
    - Yang (7, 9) -> 1
    - Yin (6, 8) -> 0
    El orden es de abajo hacia arriba.
    """
    return "".join(["1" if linea in [7, 9] else "0" for linea in lineas])

def obtener_numero_hexagrama(binario):
    return HEXAGRAMAS.get(binario, "Desconocido")

def imprimir_hexagrama(lineas):
    hexagrama = []
    for linea in lineas:
        if linea in [9, 7]:
            hexagrama.append("_______")  # Yang
        elif linea in [6, 8]:
            hexagrama.append("___ ___")  # Yin
    return hexagrama

def mutar_lineas(lineas):
    """
    Mutar las líneas del hexagrama según las reglas del I Ching:
    - Línea 6 (Yin mutable) -> 7 (Yang).
    - Línea 9 (Yang mutable) -> 8 (Yin).
    - Líneas 7 y 8 no cambian.
    """
    return [7 if x == 6 else 8 if x == 9 else x for x in lineas]

def imprimir_hexagrama_mutado(lineas):
    hexagrama_mutado = []
    for linea in lineas:
        if linea == 7:
            hexagrama_mutado.append("_______")  # Yang
        elif linea == 8:
            hexagrama_mutado.append("___ ___")  # Yin
    return hexagrama_mutado

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Información no disponible para {nombre_archivo}."
    except Exception as e:
        return f"Error al leer el archivo: {e}"

def mostrar_info_hexagrama_y_lineas(lineas, numero_hexagrama):
    nombre_archivo_hexagrama = f"hexagramas/{numero_hexagrama}.txt"
    
    print(f"\nInformación del hexagrama {numero_hexagrama}:\n{leer_archivo(nombre_archivo_hexagrama)}\n")
    
    for i, linea in enumerate(lineas):
        if linea in [6, 9]:  # Solo mostrar líneas mutables
            nombre_archivo_linea = f"hexagramas/{numero_hexagrama}_{i+1}.txt"
            print(f"Línea {i+1} (valor {linea}):\n{leer_archivo(nombre_archivo_linea)}\n")

def main():
    nombre_archivo = generar_nombre_archivo()
    print("\nHaz una pregunta en voz alta al oráculo o piénsala.\n")
    pregunta = guardar_pregunta(nombre_archivo)
    print(f"Tienes {TIEMPO_ESPERA_PREGUNTA} segundos para meditar sobre tu pregunta: '{pregunta}'")
    sleep(TIEMPO_ESPERA_PREGUNTA)

    # Generar el hexagrama principal
    lineas = generar_hexagrama()
    
    # Convertir a binario y obtener el número del hexagrama principal
    binario_principal = convertir_a_binario(lineas)
    numero_hexagrama_principal = obtener_numero_hexagrama(binario_principal)
    
    # Imprimir el hexagrama principal
    hexagrama = imprimir_hexagrama(lineas)
    print("\nTu hexagrama principal es:\n")
    for linea in hexagrama:
        print(linea)

    # Generar el hexagrama mutado
    lineas_mutadas = mutar_lineas(lineas)
    binario_mutado = convertir_a_binario(lineas_mutadas)
    numero_hexagrama_mutado = obtener_numero_hexagrama(binario_mutado)

    # Imprimir el hexagrama mutado
    hexagrama_mutado = imprimir_hexagrama_mutado(lineas_mutadas)
    print("\nTu hexagrama mutado (futuro o devenir) es:\n")
    for linea in hexagrama_mutado:
        print(linea)

    # Mostrar los números de los hexagramas
    print(f"\nNúmero del hexagrama principal: {numero_hexagrama_principal}\n")
    print(f"Número del hexagrama mutado: {numero_hexagrama_mutado}\n")

    # Mostrar información del hexagrama principal
    mostrar_info_hexagrama_y_lineas(lineas, numero_hexagrama_principal)

    # Mostrar información del hexagrama mutado
    mostrar_info_hexagrama_y_lineas(lineas_mutadas, numero_hexagrama_mutado)

if __name__ == "__main__":
    main()