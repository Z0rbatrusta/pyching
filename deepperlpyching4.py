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
    "111111": 1,  # Ch'ien / Lo Creativo
    "000000": 2,  # Kun / Lo Receptivo
    "100010": 3,  # Chun / La Dificultad Inicial
    "010001": 4,  # Meng / La Necedad Juvenil
    "111010": 5,  # Hsu / La Espera
    "010111": 6,  # Sung / El Conflicto
    "010000": 7,  # Shih / El Ejército
    "000010": 8,  # Pi / La Solidaridad
    "110111": 9,  # Hsiao Ch'u / La Fuerza Domesticadora de lo Pequeño
    "111011": 10, # Lü / El Porte
    "000111": 11, # T'ai / La Paz
    "111000": 12, # Pi / El Estancamiento
    "101111": 13, # T'ung Jen / Comunidad con los Hombres
    "111101": 14, # Ta Yu / La Posición de lo Grande
    "001000": 15, # Ch'ien / La Modestia
    "000100": 16, # Yü / El Entusiasmo
    "011001": 17, # Sui / El Seguimiento
    "100110": 18, # Ku / El Trabajo en lo Echado a Perder
    "000011": 19, # Lin / El Acrecimiento
    "110000": 20, # Kuan / La Contemplación
    "101001": 21, # Shih Ho / La Mordedura Tajante
    "100101": 22, # Pi / La Gracia
    "000001": 23, # Po / La Desintegración
    "100000": 24, # Fu / El Retorno
    "111001": 25, # Wu Wang / La Inocencia
    "100111": 26, # Ta Ch'u / La Fuerza Domesticadora de lo Grande
    "100001": 27, # I / Las Comisuras de la Boca
    "011110": 28, # Ta Kuo / La Preponderancia de lo Grande
    "010010": 29, # Kan / Lo Abismal, El Agua
    "101101": 30, # Li / Lo Adherente, El Fuego
    "001110": 31, # Hsien / El Influjo
    "011100": 32, # Heng / La Duración
    "001111": 33, # Tun / La Retirada
    "111100": 34, # Ta Chuang / El Poder de lo Grande
    "000101": 35, # Chin / El Progreso
    "101000": 36, # Ming I / El Oscurecimiento de la Luz
    "100011": 37, # Chia Jen / El Clan
    "110001": 38, # Kuei / El Antagonismo
    "000110": 39, # Chien / El Impedimento
    "011000": 40, # Hsieh / La Liberación
    "110110": 41, # Sun / La Merma
    "011011": 42, # I / El Aumento
    "110010": 43, # Kuai / El Desbordamiento
    "010110": 44, # Kou / El Ir al Encuentro
    "101011": 45, # Ts'ui / La Reunión
    "110101": 46, # Sheng / La Subida
    "010011": 47, # Kun / La Desazón
    "001010": 48, # Ching / El Pozo de Agua
    "011101": 49, # Ko / La Revolución
    "101110": 50, # Ting / El Caldero
    "100100": 51, # Chen / Lo Suscitativo
    "001001": 52, # Ken / El Aquietamiento
    "110011": 53, # Chien / La Evolución
    "001100": 54, # Kuei Mei / La Muchacha que se Casa
    "101111": 55, # Feng / La Plenitud
    "111101": 56, # Lü / El Andariego
    "011010": 57, # Sun / Lo Suave
    "001011": 58, # Tui / Lo Sereno, El Lago
    "100110": 59, # Huan / La Disolución
    "011001": 60, # Chieh / La Restricción
    "101010": 61, # Chung Fu / La Verdad Interior
    "010101": 62, # Hsiao Kuo / La Preponderancia de lo Pequeño
    "101100": 63, # Chi Chi / Después de la Consumación
    "001101": 64  # Wei Chi / Antes de la Consumación
}

# Diccionario de nombres de hexagramas
NOMBRES_HEXAGRAMAS = {
    1: "Ch'ien / Lo Creativo",
    2: "Kun / Lo Receptivo",
    3: "Chun / La Dificultad Inicial",
    4: "Meng / La Necedad Juvenil",
    5: "Hsu / La Espera",
    6: "Sung / El Conflicto",
    7: "Shih / El Ejército",
    8: "Pi / La Solidaridad",
    9: "Hsiao Ch'u / La Fuerza Domesticadora de lo Pequeño",
    10: "Lü / El Porte",
    11: "T'ai / La Paz",
    12: "Pi / El Estancamiento",
    13: "T'ung Jen / Comunidad con los Hombres",
    14: "Ta Yu / La Posición de lo Grande",
    15: "Ch'ien / La Modestia",
    16: "Yü / El Entusiasmo",
    17: "Sui / El Seguimiento",
    18: "Ku / El Trabajo en lo Echado a Perder",
    19: "Lin / El Acrecimiento",
    20: "Kuan / La Contemplación",
    21: "Shih Ho / La Mordedura Tajante",
    22: "Pi / La Gracia",
    23: "Po / La Desintegración",
    24: "Fu / El Retorno",
    25: "Wu Wang / La Inocencia",
    26: "Ta Ch'u / La Fuerza Domesticadora de lo Grande",
    27: "I / Las Comisuras de la Boca",
    28: "Ta Kuo / La Preponderancia de lo Grande",
    29: "Kan / Lo Abismal, El Agua",
    30: "Li / Lo Adherente, El Fuego",
    31: "Hsien / El Influjo",
    32: "Heng / La Duración",
    33: "Tun / La Retirada",
    34: "Ta Chuang / El Poder de lo Grande",
    35: "Chin / El Progreso",
    36: "Ming I / El Oscurecimiento de la Luz",
    37: "Chia Jen / El Clan",
    38: "Kuei / El Antagonismo",
    39: "Chien / El Impedimento",
    40: "Hsieh / La Liberación",
    41: "Sun / La Merma",
    42: "I / El Aumento",
    43: "Kuai / El Desbordamiento",
    44: "Kou / El Ir al Encuentro",
    45: "Ts'ui / La Reunión",
    46: "Sheng / La Subida",
    47: "Kun / La Desazón",
    48: "Ching / El Pozo de Agua",
    49: "Ko / La Revolución",
    50: "Ting / El Caldero",
    51: "Chen / Lo Suscitativo",
    52: "Ken / El Aquietamiento",
    53: "Chien / La Evolución",
    54: "Kuei Mei / La Muchacha que se Casa",
    55: "Feng / La Plenitud",
    56: "Lü / El Andariego",
    57: "Sun / Lo Suave",
    58: "Tui / Lo Sereno, El Lago",
    59: "Huan / La Disolución",
    60: "Chieh / La Restricción",
    61: "Chung Fu / La Verdad Interior",
    62: "Hsiao Kuo / La Preponderancia de lo Pequeño",
    63: "Chi Chi / Después de la Consumación",
    64: "Wei Chi / Antes de la Consumación"
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
    for linea in reversed(lineas):  # Invertir el orden para mostrar de abajo hacia arriba
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
    for linea in reversed(lineas):  # Invertir el orden para mostrar de abajo hacia arriba
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

    # Mostrar el nombre del hexagrama principal
    nombre_hexagrama_principal = NOMBRES_HEXAGRAMAS.get(numero_hexagrama_principal, "Desconocido")
    print(f"\nNombre del hexagrama principal: {nombre_hexagrama_principal}\n")

    # Generar el hexagrama mutado
    lineas_mutadas = mutar_lineas(lineas)
    binario_mutado = convertir_a_binario(lineas_mutadas)
    numero_hexagrama_mutado = obtener_numero_hexagrama(binario_mutado)

    # Imprimir el hexagrama mutado
    hexagrama_mutado = imprimir_hexagrama_mutado(lineas_mutadas)
    print("\nTu hexagrama mutado (futuro o devenir) es:\n")
    for linea in hexagrama_mutado:
        print(linea)

    # Mostrar el nombre del hexagrama mutado
    nombre_hexagrama_mutado = NOMBRES_HEXAGRAMAS.get(numero_hexagrama_mutado, "Desconocido")
    print(f"\nNombre del hexagrama mutado: {nombre_hexagrama_mutado}\n")

    # Mostrar información del hexagrama principal
    mostrar_info_hexagrama_y_lineas(lineas, numero_hexagrama_principal)

    # Mostrar información del hexagrama mutado
    mostrar_info_hexagrama_y_lineas(lineas_mutadas, numero_hexagrama_mutado)

if __name__ == "__main__":
    main()