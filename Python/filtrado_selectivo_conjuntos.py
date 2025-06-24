"""
Reconstructor de Elementos por Filtrado Progresivo de Conjuntos, creado por Rodolfo Casan.

Este sistema utiliza un método de filtrado progresivo de subconjuntos para adivinar elementos indexados por enteros dentro de un rango o colección.
El algoritmo genera subconjuntos basados en la representación posicional de índices y, mediante preguntas simples sobre la presencia del elemento en estos subconjuntos, puede determinar exactamente qué índice está pensando el usuario.

Características:
- Soporta rangos personalizados de índices enteros (positivos, negativos o mixtos).
- Trabaja exclusivamente con índices enteros para mapear cualquier elemento.
- Algoritmo optimizado para minimizar el número de preguntas necesarias.

Es ideal para demostraciones de teoría de la información aplicada, entretenimiento educativo o
como base para sistemas de selección interactiva de elementos mediante filtrado progresivo.
"""





'''
>>> Funciones de algortímo
'''
def generar_subconjuntos_filtrado_progresivo(limite_inferior, limite_superior):
    """
    Genera subconjuntos para el Reconstructor de Elementos por Filtrado Progresivo de Conjuntos
    para un rango personalizado de índices enteros.
    
    Argumentos:
        limite_inferior (int): El índice entero más pequeño del rango.
        limite_superior (int): El índice entero más grande del rango.
    
    Retorna:
        list: Lista de listas, donde cada lista contiene índices que tienen un bit específico activado en su representación posicional ajustada al rango.
    """
    # Asegurar que los límites sean enteros
    limite_inferior = int(limite_inferior)
    limite_superior = int(limite_superior)

    # Calcular el número de elementos en el rango (tamaño del dominio)
    num_puntos = limite_superior - limite_inferior + 1  # tamaño del conjunto discreto
    num_bits = 0
    
    temp = num_puntos - 1  # para determinar cuántos bits son necesarios
    
    # Determinar cuántos bits se necesitan para cubrir todas las posiciones
    while temp > 0:
        temp >>= 1  # desplazar bits a la derecha: equivalente a dividir entre 2
        num_bits += 1  # incrementar contador de bits
    
    # Inicializar lista de subconjuntos, uno por cada posición de bit
    subconjuntos = []
    for _ in range(num_bits):
        subconjuntos.append([])  # cada subconjunto agrupa índices con bit i activo

    # Iterar sobre cada índice en el rango y asignarlo a subconjuntos según bits activos
    for indice in range(limite_inferior, limite_superior + 1):
        indice_ajustado = indice - limite_inferior  # mapear rango a 0..(num_puntos-1)
        for i in range(num_bits):
            
            # Verificar si el bit i está activo en la representación de indice_ajustado
            if indice_ajustado & (1 << i):  # operación AND para comprobar la presencia del bit
                subconjuntos[i].append(indice)
    
    # Filtrar subconjuntos vacíos: no aportan información
    resultado = []
    for s in subconjuntos:
        
        # Si el subconjunto no está vacío lo agregamos al resultado
        if len(s) > 0:
            resultado.append(s)
    return resultado  # devolver lista de subconjuntos relevantes


def reconstruir_elemento_por_filtrado(subconjuntos, respuestas, limite_inferior):
    """
    Reconstruye el índice basado en las respuestas del usuario a los subconjuntos.
    
    Argumentos:
        subconjuntos (list): Los subconjuntos generados.
        respuestas (list): Lista de booleanos indicando si el elemento está en cada subconjunto.
        limite_inferior (int): El índice más pequeño del rango.
    
    Returna:
        int: El índice adivinado.
    """
    # Validar consistencia entre subconjuntos y respuestas
    if len(subconjuntos) != len(respuestas):
        raise ValueError("El número de respuestas debe coincidir con el número de subconjuntos")
    
    # Asegurar que el límite inferior sea entero
    limite_inferior = int(limite_inferior)
    valor_binario = 0  # acumulador para reconstruir posición relativa en el dominio
    
    # Sumar potencias de 2 según respuestas afirmativas
    for i, respuesta in enumerate(respuestas):
        # Cada respuesta True indica que el bit i en la posición ajustada es 1
        if respuesta:
            valor_binario += (1 << i)  # agregar valor posicional 2^i
    
    # Convertir posición relativa a índice real en el dominio original
    indice_adivinado = limite_inferior + valor_binario
    return indice_adivinado  # devolver índice reconstruido







'''
>>> Funciones de interacción
'''
def sistema_reconstructor_filtrado_progresivo(limite_inferior, limite_superior):
    """
    Sistema interactivo del Reconstructor de Elementos por Filtrado Progresivo de Conjuntos
    para adivinar un índice entero en un rango personalizado.
    
    Args:
        limite_inferior (int): El límite inferior del rango de índices.
        limite_superior (int): El límite superior del rango de índices.
    """
    # Conversión a enteros
    limite_inferior = int(limite_inferior)
    limite_superior = int(limite_superior)
    # Mensaje de cabecera con contexto del método
    print(f"\nReconstructor de Elementos por Filtrado Progresivo de Conjuntos")
    print(f"Piensa en un índice entero entre {limite_inferior} y {limite_superior}.")
    print("Responde 'sí' o 'no' a las siguientes preguntas sobre presencia en subconjuntos de filtrado.\n")

    # Generar subconjuntos de filtrado según representación posicional
    subconjuntos = generar_subconjuntos_filtrado_progresivo(limite_inferior, limite_superior)

    # Mostrar subconjuntos para depuración o análisis de información
    for i, sub in enumerate(subconjuntos, start=1):
        # Ordenar para presentación clara
        print(f"Subconjunto {i}: {sorted(sub)}")  # muestra elementos con bit i activo
        print(f"-Total: {len(sub)}")  # tamaño del subconjunto: cantidad de información
        print()

    respuestas = []  # lista para almacenar respuestas del usuario
    for i, sub in enumerate(subconjuntos, start=1):
        while True:
            # Preguntar si el índice pensado está en el subconjunto i
            respuesta = input(f"¿Tu índice aparece en el Subconjunto {i}? (sí/no): ").lower()
            if respuesta in ["sí", "si", "s", "yes", "y"]:
                respuestas.append(True)  # bit i = 1 en reconstrucción
                break
            elif respuesta in ["no", "n"]:
                respuestas.append(False)  # bit i = 0
                break
            else:
                print("Por favor, responde 'sí' o 'no'.")  # insistir hasta respuesta válida

    # Reconstruir índice basado en las respuestas binarias
    indice_adivinado = reconstruir_elemento_por_filtrado(subconjuntos, respuestas, limite_inferior)
    print(f"\n¡He adivinado! El índice pensado es {indice_adivinado}.")
    return indice_adivinado










'''
>>> Ejemplo de inicialización
'''
if __name__ == "__main__":
    try:
        # Encabezado general del programa
        print("=======================================================")
        print("  Reconstructor de Elementos por Filtrado Progresivo de Conjuntos")
        print("=======================================================")
        print("Este sistema puede adivinar cualquier índice entero que pienses dentro de un rango definido.\n")

        while True:
            try:
                # Solicitar límites del rango
                limite_inferior = int(input("Ingresa el límite inferior del rango (índice entero): "))
                limite_superior = int(input("Ingresa el límite superior del rango (índice entero): "))
                # Validar rango
                if limite_inferior >= limite_superior:
                    print("Error: El límite inferior debe ser menor que el límite superior.")
                    continue
                # Advertencia si el dominio es muy grande
                if limite_superior - limite_inferior > 10000:
                    print("Advertencia: Rango muy grande. Esto puede generar muchos subconjuntos.")
                    confirmacion = input("¿Deseas continuar de todos modos? (sí/no): ").lower()
                    if confirmacion not in ["sí", "si", "s", "yes", "y"]:
                        continue
                # Ejecutar sistema interactivo
                sistema_reconstructor_filtrado_progresivo(limite_inferior, limite_superior)
                break  # finalizar tras una ejecución completa
            except ValueError:
                print("Error: Por favor, ingresa solo números enteros.")
    except KeyboardInterrupt:
        # Manejo de interrupción por usuario
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        # Captura de errores inesperados
        print(f"Error inesperado: {e}")
