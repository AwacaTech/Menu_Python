import time
import sys
from datetime import datetime, date

# Función para escribir progresivamente el texto
def escribir_progresivamente(texto, intervalo=0.025):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()  # Asegura que se muestre inmediatamente
        time.sleep(intervalo)
    sys.stdout.write("\n")  # Para añadir el salto de línea al final

# Sobrescribir el comportamiento de print para usar la función progresiva
def print_progresivo(*args, sep=' ', end='\n', intervalo=0.025):
    texto = sep.join(map(str, args)) + end  # Crear la cadena de texto completa
    escribir_progresivamente(texto, intervalo)

# Sobrescribimos la función print original por la nueva
print = print_progresivo

# Función genérica para obtener entrada validada
def obtener_entrada(mensaje, tipo=None, validacion=None, intervalo=0.025):
    while True:
        escribir_progresivamente(mensaje, intervalo)  # Mostrar el mensaje de forma progresiva
        entrada = input()
        if tipo:
            try:
                entrada = tipo(entrada)
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un valor correcto.")
                time.sleep(1)
                continue
        if validacion and not validacion(entrada):
            print("Entrada no válida. Por favor, ingresa un valor que cumpla con los requisitos.")
            time.sleep(1)
            continue
        return entrada

# Ejemplos de validación personalizada
def es_alfabetico(texto):
    return texto.isalpha()

def es_s_n(texto):
    return texto.lower() in ['s', 'n']

# Uso para números
# precio = obtener_entrada("¿Cuál es el precio del producto? (Solo en números): ", float)

# Uso para letras
# nombre = obtener_entrada("¿Cuál es tu nombre?: ", validacion=es_alfabetico)

# Uso para letras con una validación personalizada (s/n)
# volver_menu = obtener_entrada("¿Quieres volver al menú? (s/n): ", validacion=es_s_n)

# Función de saludo con hora actual
def saludo():
    hora_actual = datetime.now()
    nombre = obtener_entrada("¿Cómo te llamas?: ")
    time.sleep(0.5)
    print(f"\nBuenos días {nombre}. Son las {hora_actual.hour:02d}:{hora_actual.minute:02d}")
    time.sleep(0.5)

# Calculadora de precio
def descuento(precio, desc):
    return precio - (precio * 0.01 * desc)

def aplicar_descuento():
    precio = obtener_entrada("¿Cuál es el precio del producto? (Solo en números): ", float)
    desc = obtener_entrada("¿Cuánto es el descuento a aplicar? (Solo en números): ", float)
    precio_final = descuento(precio, desc)
    print(f"El precio final del producto con un {desc}% de descuento es de {precio_final}€")

# Calculadora IMC
def IMC(peso, estatura):
    return peso / (estatura ** 2)

def calcular_IMC():
    peso = obtener_entrada("Escribe tu peso en Kg: ", float)
    estatura = obtener_entrada("Escribe tu estatura en metros: ", float)
    resultado_IMC = IMC(peso, estatura)
    print(f"\nTu IMC es: {resultado_IMC}")
    return peso, estatura, resultado_IMC

# Calcular estado nutricional según el IMC
def calcular_estado_nutricional(peso, estatura):
    resultado_IMC = IMC(peso, estatura)
    if resultado_IMC < 18.5:
        estado = "Peso bajo"
    elif resultado_IMC < 25:
        estado = "Peso normal"
    elif resultado_IMC < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    return estado

# Función para leer lista de números
def lee_numeros():
    n = obtener_entrada("¿Cuántos números deseas ingresar?: ", int)
    lista = []
    for i in range(n):
        numero = obtener_entrada(f"Número {i+1}: ", int)
        lista.append(numero)
    
    # Mostrar resultados
    print("\nLista ingresada:", lista)
    time.sleep(1)
    
    # Número mayor
    numero_mayor = max(lista)
    print("Número mayor:", numero_mayor)
    time.sleep(0.5)

    # Valor medio
    if len(lista) > 0:
        media = sum(lista) / len(lista)
    else:
        media = None
    print("Media de los números:", media)
    time.sleep(0.5)

    # Contar pares
    pares = [numero for numero in lista if numero % 2 == 0]
    print(f"Hay {len(pares)} números pares: {pares}")
    time.sleep(0.5)

    # Números mayores de 10
    mayores_10 = [numero for numero in lista if numero > 10]
    print(f"Hay {len(mayores_10)} números mayores de 10: {mayores_10}")
    time.sleep(1)

# Función para calcular el día de la semana
def calcular_dia_semana(fecha):
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    dia = fecha.weekday()
    return dias[dia]

def calcular_dia_nacimiento():
    dia = obtener_entrada("¿Cuál fue tu día de nacimiento?: ", int)
    mes = obtener_entrada("¿Y el mes?: ", int)
    año = obtener_entrada("¿Y el año?: ", int)
    fecha = date(año, mes, dia)
    nombre_dia = calcular_dia_semana(fecha)
    print(f"Naciste un {nombre_dia}")

# Menú
def menu():
    options = [
        "Calculadora de precios",
        "Calculadora de IMC",
        "Lista de números",
        "Calcular día de la semana de nacimiento"
    ]

    while True:
        print("¿Qué quieres hacer?")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}", end="")
            
            
        time.sleep(0.5)
        sys.stdout.write("\n")
        choice = obtener_entrada("Escribe el número de la acción: ", int)

        if 1 <= choice <= len(options):
            print(f"\nSeleccionaste: {options[choice - 1]}")
            if choice == 1:
                aplicar_descuento()
            elif choice == 2:
                peso, estatura, _ = calcular_IMC()
                estado = calcular_estado_nutricional(peso, estatura)
                print(f"Tu estado nutricional es: {estado}")
            elif choice == 3:
                lee_numeros()
            elif choice == 4:
                calcular_dia_nacimiento()

            while True:
                volver_menu = obtener_entrada("\n¿Quieres volver al menú? (s/n): ", validacion=es_s_n)
                if volver_menu == 's':
                    print("Volviendo al menú...")
                    time.sleep(1)
                    break
                elif volver_menu == 'n':
                    print("Saliendo del programa...")
                    time.sleep(1)
                    return
                else:
                    print("Entrada no válida. Ingrese 's' para sí o 'n' para no.")
        else:
            print("\nElección no válida. Por favor introduzca un número entre 1 y 4.")

if __name__ == "__main__":
    saludo()  # Saludo inicial
    menu()
