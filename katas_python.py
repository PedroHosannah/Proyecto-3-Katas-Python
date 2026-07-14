"""Proyecto 3 - Katas Python
Autor: Pedro Hosannah
"""

from functools import reduce
from math import pi


# EJERCICIO 1: Escribe una función que reciba una cadena de texto y devuelva un diccionario con la frecuencia de cada letra. Los espacios no se consideran.
def contar_frecuencia_letras(texto):
    # Uso un diccionario para contar cada letra.
    frecuencias = {}
    for letra in texto:
        if not letra.isspace():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


# EJERCICIO 2: Dada una lista de números, obtén una nueva lista con el doble de cada valor usando map().
def duplicar_numeros(numeros):
    # map() aplica el doble a toda la lista.
    return list(map(lambda numero: numero * 2, numeros))


# EJERCICIO 3: Recibe una lista de palabras y una palabra objetivo, y devuelve las palabras que contengan esa palabra.
def buscar_palabras(palabras, objetivo):
    # Recorro la lista y guardo las coincidencias.
    resultado = []

    for palabra in palabras:
        if objetivo.lower() in palabra.lower():
            resultado.append(palabra)

    return resultado


# EJERCICIO 4: Calcula la diferencia entre los valores de dos listas usando map().
def diferencia_listas(lista_1, lista_2):
    # map() resta las dos listas por parejas.
    return list(map(lambda a, b: a - b, lista_1, lista_2))


# EJERCICIO 5: Calcula la media de una lista y devuelve una tupla con la media y el estado aprobado o suspenso.
def calcular_media_estado(notas, nota_aprobado=5):
    # Compruebo la lista antes de calcular la media.
    if not notas:
        raise ValueError('La lista no puede estar vacía.')
    media = sum(notas) / len(notas)

    # Uso un condicional para decidir el estado.
    if media >= nota_aprobado:
        estado = 'aprobado'
    else:
        estado = 'suspenso'

    return media, estado


# EJERCICIO 6: Calcula el factorial de un número de forma recursiva.
def factorial(numero):
    # Uso recursividad hasta llegar al caso base.
    if not isinstance(numero, int):
        raise TypeError('El número debe ser entero.')
    if numero < 0:
        raise ValueError('El número no puede ser negativo.')
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)


# EJERCICIO 7: Convierte una lista de tuplas en una lista de strings usando map().
def tuplas_a_strings(tuplas):
    # map() convierte cada tupla con str().
    return list(map(str, tuplas))


# EJERCICIO 8: Pide dos números, intenta dividirlos y controla valores no numéricos y divisiones entre cero.
def dividir_numeros_usuario():
    # try/except controla los posibles errores.
    try:
        numero_1 = float(input('Introduce el primer número: '))
        numero_2 = float(input('Introduce el segundo número: '))
        resultado = numero_1 / numero_2
    except ValueError:
        print('Debes introducir valores numéricos.')
        return None
    except ZeroDivisionError:
        print('No se puede dividir entre cero.')
        return None
    else:
        print(f'División realizada correctamente: {resultado}')
        return resultado


# EJERCICIO 9: Filtra una lista de mascotas excluyendo Mapache, Tigre, Serpiente Pitón, Cocodrilo y Oso usando filter().
def filtrar_mascotas(mascotas):
    # filter() deja solamente las mascotas permitidas.
    prohibidas = ['mapache', 'tigre', 'serpiente pitón', 'cocodrilo', 'oso']

    return list(
        filter(
            lambda mascota: mascota.lower() not in prohibidas,
            mascotas
        )
    )


# EJERCICIO 10: Calcula el promedio de una lista y lanza una excepción personalizada si está vacía.
class ListaVaciaError(Exception):
    # Excepción propia para una lista vacía.
    pass


def calcular_promedio(numeros):
    # Evito calcular el promedio sin datos.
    if not numeros:
        raise ListaVaciaError('No se puede calcular el promedio de una lista vacía.')
    return sum(numeros) / len(numeros)


def mostrar_promedio(numeros):
    try:
        promedio = calcular_promedio(numeros)
        print(f'El promedio es: {promedio}')
        return promedio
    except ListaVaciaError as error:
        print(error)
        return None


# EJERCICIO 11: Pide la edad del usuario y controla valores no numéricos o fuera del rango de 0 a 120.
def pedir_edad():
    # Convierto y valido la edad introducida.
    try:
        edad = int(input('Introduce tu edad: '))
        if edad < 0 or edad > 120:
            raise ValueError('La edad debe estar entre 0 y 120 años.')
    except ValueError as error:
        print(f'Edad no válida: {error}')
        return None
    else:
        print(f'Edad válida: {edad}')
        return edad


# EJERCICIO 12: Recibe una frase y devuelve una lista con la longitud de cada palabra usando map().
def longitud_palabras(frase):
    # map() aplica len() a cada palabra.
    return list(map(len, frase.split()))


# EJERCICIO 13: Recibe un conjunto de caracteres y devuelve tuplas con cada letra en mayúscula y minúscula usando map().
def mayusculas_minusculas(caracteres):
    # map() crea una tupla por cada carácter del conjunto.
    return list(
        map(
            lambda letra: (letra.upper(), letra.lower()),
            caracteres
        )
    )


# EJERCICIO 14: Devuelve las palabras de una lista que comiencen por una letra concreta usando filter().
def palabras_por_inicial(palabras, inicial):
    # filter() conserva las palabras con esa inicial.
    if not inicial:
        return []
    return list(filter(lambda palabra: palabra.lower().startswith(inicial[0].lower()), palabras))


# EJERCICIO 15: Crea una función lambda que sume 3 a cada número de una lista.
# map() aplica la lambda a toda la lista.
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# EJERCICIO 16: Devuelve las palabras de un texto que sean más largas que n usando filter().
def palabras_mas_largas(texto, n):
    # filter() conserva las palabras más largas que n.
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# EJERCICIO 17: Convierte una lista de dígitos en el número correspondiente usando reduce().
def digitos_a_numero(digitos):
    # Compruebo que todos los valores sean dígitos.
    if not digitos:
        raise ValueError('La lista no puede estar vacía.')

    for digito in digitos:
        if type(digito) is not int or digito < 0 or digito > 9:
            raise ValueError('Todos los valores deben ser dígitos entre 0 y 9.')

    # reduce() va formando un único número.
    return reduce(lambda total, digito: total * 10 + digito, digitos)


# EJERCICIO 18: Filtra una lista de estudiantes y devuelve los que tengan una calificación mayor o igual a 90.
def estudiantes_destacados(estudiantes):
    # filter() conserva notas de 90 o más.
    return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))


# EJERCICIO 19: Crea una función lambda que filtre los números impares de una lista.
# filter() conserva los números con resto distinto de cero.
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# EJERCICIO 20: De una lista con integers y strings, devuelve solamente los valores de tipo int usando filter().
def filtrar_enteros(elementos):
    # Compruebo el tipo exacto de cada valor.
    return list(filter(lambda elemento: type(elemento) is int, elementos))


# EJERCICIO 21: Crea una función que calcule el cubo de un número mediante una función lambda.
# La lambda devuelve el número elevado al cubo.
calcular_cubo = lambda numero: numero ** 3


# EJERCICIO 22: Dada una lista numérica, obtén el producto total de sus valores usando reduce().
def producto_total(numeros):
    # reduce() multiplica todos los valores.
    return reduce(lambda total, numero: total * numero, numeros, 1)


# EJERCICIO 23: Concatena una lista de palabras usando reduce().
def concatenar_palabras(palabras):
    # Compruebo la lista antes de usar reduce().
    if not palabras:
        return ''

    # reduce() va uniendo todas las palabras.
    return reduce(lambda texto, palabra: texto + ' ' + palabra, palabras)


# EJERCICIO 24: Calcula la diferencia total de los valores de una lista usando reduce().
def diferencia_total(numeros):
    # reduce() resta cada valor al acumulado.
    if not numeros:
        raise ValueError('La lista no puede estar vacía.')
    return reduce(lambda total, numero: total - numero, numeros)


# EJERCICIO 25: Crea una función que cuente el número de caracteres de una cadena de texto.
def contar_caracteres(texto):
    # len() devuelve la cantidad de caracteres.
    return len(texto)


# EJERCICIO 26: Crea una función lambda que calcule el resto de la división entre dos números.
# El operador % devuelve el resto de la división.
calcular_resto = lambda numero_1, numero_2: numero_1 % numero_2


# EJERCICIO 27: Crea una función que calcule el promedio de una lista de números.
def promedio_lista(numeros):
    # Divido la suma entre la cantidad de números.
    if not numeros:
        raise ValueError('La lista no puede estar vacía.')
    return sum(numeros) / len(numeros)


# EJERCICIO 28: Crea una función que busque y devuelva el primer elemento duplicado de una lista.
def primer_duplicado(elementos):
    # Un set permite saber si un valor ya apareció.
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# EJERCICIO 29: Convierte una variable en texto y enmascara con # todos los caracteres excepto los últimos cuatro.
def enmascarar_dato(dato):
    # Oculto todo excepto los últimos cuatro caracteres.
    texto = str(dato)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]


# EJERCICIO 30: Determina si dos palabras son anagramas, es decir, si tienen las mismas letras en diferente orden.
def son_anagramas(palabra_1, palabra_2):
    # Ordeno las letras para poder compararlas.
    primera = palabra_1.replace(' ', '').lower()
    segunda = palabra_2.replace(' ', '').lower()
    return primera != segunda and sorted(primera) == sorted(segunda)


# EJERCICIO 31: Solicita una lista de nombres y un nombre para buscar; si no se encuentra, lanza una excepción.
class NombreNoEncontradoError(Exception):
    # Excepción propia para un nombre no encontrado.
    pass


def buscar_nombre_usuario():
    # Separo los nombres introducidos por comas.
    texto_nombres = input('Introduce nombres separados por comas: ')
    nombres_sin_limpiar = texto_nombres.split(',')
    nombres = []

    for nombre in nombres_sin_limpiar:
        nombres.append(nombre.strip())

    nombre_buscado = input('Introduce el nombre que quieres buscar: ').strip()

    try:
        if nombre_buscado not in nombres:
            raise NombreNoEncontradoError(
                f'{nombre_buscado} no está en la lista.'
            )

        print(f'{nombre_buscado} fue encontrado.')
        return nombre_buscado

    except NombreNoEncontradoError as error:
        print(error)
        return None


# EJERCICIO 32: Busca un nombre completo en una lista de empleados y devuelve su puesto o indica que no trabaja aquí.
def buscar_puesto(nombre_completo, empleados):
    # Recorro los empleados hasta encontrar el nombre.
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre_completo.lower():
            return empleado['puesto']
    return 'La persona no trabaja aquí.'


# EJERCICIO 33: Crea una función lambda que sume los elementos correspondientes de dos listas.
# map() suma los elementos de las listas por parejas.
sumar_listas = lambda lista_1, lista_2: list(map(lambda a, b: a + b, lista_1, lista_2))


# EJERCICIO 34: Crea la clase Arbol con un tronco, ramas y métodos para crecer, añadir, quitar y mostrar información.
class Arbol:
    def __init__(self):
        # El árbol empieza con tronco 1 y sin ramas.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumento el tronco en una unidad.
        self.tronco += 1

    def nueva_rama(self):
        # Cada rama nueva empieza con longitud 1.
        self.ramas.append(1)

    def crecer_ramas(self):
        # Recorro las ramas para aumentar su longitud.
        for posicion in range(len(self.ramas)):
            self.ramas[posicion] += 1

    def quitar_rama(self, posicion):
        # Compruebo la posición antes de eliminar.
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError('La posición de la rama no es válida.')

        return self.ramas.pop(posicion)

    def info_arbol(self):
        # Devuelvo los datos del árbol en un diccionario.
        informacion = {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitud_ramas': self.ramas.copy()
        }

        return informacion


# EJERCICIO 35: Crea la clase UsuarioBanco con nombre, saldo, cuenta corriente y métodos para retirar, transferir y agregar dinero.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # Guardo los datos principales del usuario.
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        # Compruebo la cantidad antes de sumarla.
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser mayor que cero.')

        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        # Compruebo la cantidad y el saldo.
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser mayor que cero.')

        if cantidad > self.saldo:
            raise ValueError('Saldo insuficiente.')

        self.saldo -= cantidad

    def transferir_dinero(self, destinatario, cantidad):
        # Las dos personas deben tener cuenta corriente.
        if not self.cuenta_corriente or not destinatario.cuenta_corriente:
            raise ValueError('Los dos usuarios deben tener cuenta corriente.')

        self.retirar_dinero(cantidad)
        destinatario.agregar_dinero(cantidad)


# EJERCICIO 36: Crea procesar_texto para contar palabras, reemplazar una palabra o eliminarla según la opción elegida.
def contar_palabras(texto):
    # Uso un diccionario para contar las palabras.
    resultado = {}
    for palabra in texto.split():
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Recorro las palabras y cambio las coincidencias.
    palabras = texto.split()
    resultado = []

    for palabra in palabras:
        if palabra == palabra_original:
            resultado.append(palabra_nueva)
        else:
            resultado.append(palabra)

    return ' '.join(resultado)


def eliminar_palabra(texto, palabra_eliminar):
    # Creo una lista sin la palabra indicada.
    palabras = texto.split()
    resultado = []

    for palabra in palabras:
        if palabra != palabra_eliminar:
            resultado.append(palabra)

    return ' '.join(resultado)


def procesar_texto(texto, opcion, *argumentos):
    # *argumentos cambia según la opción elegida.
    if opcion == 'contar':
        return contar_palabras(texto)
    if opcion == 'reemplazar':
        if len(argumentos) != 2:
            raise ValueError('Debes indicar la palabra original y la nueva.')
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    if opcion == 'eliminar':
        if len(argumentos) != 1:
            raise ValueError('Debes indicar la palabra que quieres eliminar.')
        return eliminar_palabra(texto, argumentos[0])
    raise ValueError('La opción debe ser contar, reemplazar o eliminar.')


# EJERCICIO 37: Genera un programa que indique si es de noche, de día o de tarde según la hora introducida.
def momento_del_dia(hora):
    # Uso rangos horarios para elegir el momento.
    if hora < 0 or hora > 23:
        raise ValueError('La hora debe estar entre 0 y 23.')
    if 6 <= hora < 12:
        return 'día'
    if 12 <= hora < 21:
        return 'tarde'
    return 'noche'


def consultar_momento_del_dia():
    try:
        hora = int(input('Introduce una hora entre 0 y 23: '))
        resultado = momento_del_dia(hora)
        print(f'Es de {resultado}.')
        return resultado
    except ValueError as error:
        print(f'Valor no válido: {error}')
        return None


# EJERCICIO 38: Determina la calificación en texto de un alumno según su calificación numérica.
def calificacion_texto(calificacion):
    # Clasifico la nota mediante rangos.
    if calificacion < 0 or calificacion > 100:
        raise ValueError('La calificación debe estar entre 0 y 100.')
    if calificacion <= 69:
        return 'insuficiente'
    if calificacion <= 79:
        return 'bien'
    if calificacion <= 89:
        return 'muy bien'
    return 'excelente'


# EJERCICIO 39: Calcula el área de un rectángulo, círculo o triángulo a partir de una tupla con sus datos.
def calcular_area(figura, datos):
    # Aplico la fórmula según la figura recibida.
    figura = figura.lower()
    if figura == 'rectangulo':
        if len(datos) != 2:
            raise ValueError('El rectángulo necesita base y altura.')
        return datos[0] * datos[1]
    if figura == 'circulo':
        if len(datos) != 1:
            raise ValueError('El círculo necesita el radio.')
        return pi * datos[0] ** 2
    if figura == 'triangulo':
        if len(datos) != 2:
            raise ValueError('El triángulo necesita base y altura.')
        return datos[0] * datos[1] / 2
    raise ValueError('La figura debe ser rectangulo, circulo o triangulo.')


# EJERCICIO 40: Calcula el precio final de una compra aplicando un cupón de descuento válido cuando el usuario lo indique.
def calcular_precio_final(precio, tiene_cupon, descuento=0):
    # Compruebo el precio antes de calcular.
    if precio < 0:
        raise ValueError('El precio no puede ser negativo.')

    precio_final = precio

    # El cupón resta una cantidad al precio.
    if tiene_cupon and descuento > 0:
        precio_final = precio - descuento

        if precio_final < 0:
            precio_final = 0

    return precio_final


def compra_tienda_online():
    try:
        precio = float(input('Introduce el precio original: '))
        respuesta = input('¿Tienes un cupón de descuento? (sí/no): ').strip().lower()
        if respuesta in ('sí', 'si'):
            descuento = float(input('Introduce el valor del cupón: '))
            precio_final = calcular_precio_final(precio, True, descuento)
        else:
            precio_final = calcular_precio_final(precio, False)
        print(f'El precio final es: {precio_final:.2f} €')
        return precio_final
    except ValueError as error:
        print(f'Dato no válido: {error}')
        return None


if __name__ == '__main__':
    print('Ejercicio 1:', contar_frecuencia_letras('Hola mundo'))
    print('Ejercicio 2:', duplicar_numeros([1, 2, 3]))
    print('Ejercicio 3:', buscar_palabras(['programa', 'Python', 'gramática'], 'gram'))
    print('Ejercicio 4:', diferencia_listas([10, 20, 30], [1, 2, 3]))
    print('Ejercicio 5:', calcular_media_estado([7, 6, 5]))
    print('Ejercicio 6:', factorial(5))
    print('Ejercicio 7:', tuplas_a_strings([(1, 2), ('a', 'b')]))
    print('Ejercicio 9:', filtrar_mascotas(['Perro', 'Mapache', 'Gato']))
    mostrar_promedio([8, 9, 7])
    print('Ejercicio 12:', longitud_palabras('Python es fácil'))
    print('Ejercicio 13:', mayusculas_minusculas({'a', 'B', 'c'}))
    print('Ejercicio 14:', palabras_por_inicial(['Python', 'Java', 'PHP'], 'p'))
    print('Ejercicio 15:', sumar_tres([1, 2, 3]))
    print('Ejercicio 16:', palabras_mas_largas('Python permite escribir código', 5))
    print('Ejercicio 17:', digitos_a_numero([5, 7, 2]))

    estudiantes = [
        {'nombre': 'Ana', 'edad': 22, 'calificacion': 95},
        {'nombre': 'Luis', 'edad': 24, 'calificacion': 82},
        {'nombre': 'Marta', 'edad': 21, 'calificacion': 90}
    ]
    print('Ejercicio 18:', estudiantes_destacados(estudiantes))
    print('Ejercicio 19:', filtrar_impares([1, 2, 3, 4, 5]))
    print('Ejercicio 20:', filtrar_enteros([1, 'dos', 3, True, 'cinco']))
    print('Ejercicio 21:', calcular_cubo(4))
    print('Ejercicio 22:', producto_total([2, 3, 4]))
    print('Ejercicio 23:', concatenar_palabras(['Hola', 'mundo', 'Python']))
    print('Ejercicio 24:', diferencia_total([20, 5, 3]))
    print('Ejercicio 25:', contar_caracteres('Hola Python'))
    print('Ejercicio 26:', calcular_resto(10, 3))
    print('Ejercicio 27:', promedio_lista([6, 8, 10]))
    print('Ejercicio 28:', primer_duplicado([1, 2, 3, 2, 4]))
    print('Ejercicio 29:', enmascarar_dato('123456789'))
    print('Ejercicio 30:', son_anagramas('Roma', 'amor'))

    empleados = [
        {'nombre': 'Ana López', 'puesto': 'Administradora de sistemas'},
        {'nombre': 'Luis Pérez', 'puesto': 'Desarrollador'}
    ]
    print('Ejercicio 32:', buscar_puesto('Ana López', empleados))
    print('Ejercicio 33:', sumar_listas([1, 2, 3], [4, 5, 6]))

    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print('Ejercicio 34:', arbol.info_arbol())

    alicia = UsuarioBanco('Alicia', 100, True)
    bob = UsuarioBanco('Bob', 50, True)
    bob.agregar_dinero(20)
    try:
        bob.transferir_dinero(alicia, 80)
    except ValueError as error:
        print(f'Ejercicio 35, transferencia no realizada: {error}')
    alicia.retirar_dinero(50)
    print('Ejercicio 35, saldos:', {'Alicia': alicia.saldo, 'Bob': bob.saldo})

    texto = 'python es fácil y python es útil'
    print('Ejercicio 36 contar:', procesar_texto(texto, 'contar'))
    print('Ejercicio 36 reemplazar:', procesar_texto(texto, 'reemplazar', 'python', 'Java'))
    print('Ejercicio 36 eliminar:', procesar_texto(texto, 'eliminar', 'es'))
    print('Ejercicio 37:', momento_del_dia(18))
    print('Ejercicio 38:', calificacion_texto(92))
    print('Ejercicio 39:', calcular_area('circulo', (3,)))
    print('Ejercicio 40:', calcular_precio_final(100, True, 15))

    # Para probar los ejercicios interactivos, descomenta las llamadas necesarias.
    # dividir_numeros_usuario()
    # pedir_edad()
    # buscar_nombre_usuario()
    # consultar_momento_del_dia()
    # compra_tienda_online()
