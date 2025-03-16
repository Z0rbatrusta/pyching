#!/usr/bin/python3
# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------##
##
## pyching -- a Python program to cast and interpret I Ching hexagrams
##
## Copyright (C) 2020 Zorbatrusta
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be of some
## interest to somebody, but WITHOUT ANY WARRANTY; without even the
## implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING or COPYING.txt. If not,
##  write to the Free Software Foundation, Inc.,
## 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
## The license can also be found at the GNU/FSF website: http://www.gnu.org
##
import time
from random import seed, randint
from time import sleep
from datetime import datetime

cadenaiching = "I Ching"
cadenawilhem = "Richard H. Wilhem"
print (cadenaiching.center(70, "="))
print (" Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?.")
print (" El Libro de las Mutaciones es la obra mediante la cual los sabios")
print (" santos elevaron su modo de ser y ampliaron su campo de acción.")
print (cadenawilhem.center(70, "="))
print ("")
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
print (yoda)
sleep(3)

TIEMPO_ESPERA_PREGUNTA = 13
TIEMPO_ESPERA_ENTRE_TIRADAS = 1

HEXAGRAMAS = {
    "111111": 1, "000000": 2, "010001": 3, "100010": 4, "010111": 5, "111010": 6,
    "000010": 7, "010000": 8, "110111": 9, "111011": 10, "000111": 11, "111000": 12,
    "101110": 13, "011101": 14, "001000": 15, "000100": 16, "100110": 17, "011001": 18,
    "110000": 19, "000011": 20, "100101": 21, "101001": 22, "000001": 23, "100000": 24,
    "100111": 25, "111001": 26, "100001": 27, "011110": 28, "010010": 29, "101101": 30,
    "011100": 31, "001110": 32, "111100": 33, "001111": 34, "101000": 35, "000101": 36,
    "100011": 37, "110001": 38, "011000": 39, "000110": 40, "011011": 41, "110110": 42,
    "011010": 43, "010110": 44, "110101": 45, "101011": 46, "010011": 47, "110010": 48,
    "101110": 49, "011101": 50, "001101": 51, "101100": 52, "110011": 53, "001100": 54,
    "011111": 55, "111110": 56, "001011": 57, "110100": 58, "011001": 59, "100110": 60,
    "010101": 61, "101010": 62, "110011": 63, "001100": 64
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
    return "".join(["1" if linea in [7, 9] else "0" for linea in reversed(lineas)])

def obtener_numero_hexagrama(binario):
    return HEXAGRAMAS.get(binario, "Desconocido")

def imprimir_hexagrama(lineas):
    hexagrama = []
    for linea in reversed(lineas):
        if linea in [9, 7]:
            hexagrama.append("_______")  # Yang
        elif linea in [6, 8]:
            hexagrama.append("___ ___")  # Yin
    return hexagrama

def mutar_lineas(lineas):
    return [7 if x == 9 else 8 if x == 6 else x for x in lineas]

def convertir_a_binario_mutado(lineas):
    return "".join(["1" if linea in [6, 8] else "0" for linea in reversed(lineas)])

def obtener_numero_hexagrama_mutado(binario):
    return HEXAGRAMAS.get(binario, "Desconocido")

def imprimir_hexagrama_mutado(lineas):
    hexagrama_mutado = []
    for linea in reversed(lineas):
        if linea == 9:
            hexagrama_mutado.append("___ ___")  # Yang muta a Yin
        elif linea == 6:
            hexagrama_mutado.append("_______")  # Yin muta a Yang
        elif linea == 7:
            hexagrama_mutado.append("_______")  # Yang no cambia
        elif linea == 8:
            hexagrama_mutado.append("___ ___")  # Yin no cambia
    return hexagrama_mutado

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Archivo {nombre_archivo} no encontrado."
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

    lineas = generar_hexagrama()
    
    binario_principal = convertir_a_binario(lineas)
    numero_hexagrama_principal = obtener_numero_hexagrama(binario_principal)
    
    hexagrama = imprimir_hexagrama(lineas)
    
    print("\nTu hexagrama principal es:\n")
    for linea in hexagrama:
        print(linea)

    # Generar hexagrama mutado
    lineas_mutadas = mutar_lineas(lineas)
    binario_mutado = convertir_a_binario(lineas_mutadas)
    numero_hexagrama_mutado = obtener_numero_hexagrama_mutado(binario_mutado)

    hexagrama_mutado = imprimir_hexagrama_mutado(lineas)
    
    print("\nTu hexagrama mutado (futuro o devenir) es:\n")
    for linea in hexagrama_mutado:
        print(linea)

print(f"\nNúmero del hexagrama principal: {numero_hexagrama_principal}")
print("")
print(f"Número del hexagrama mutado: {numero_hexagrama_mutado}\n")

mostrar_info_hexagrama_y_lineas(lineas, numero_hexagrama_principal)

if __name__ == "__main__":
    main()