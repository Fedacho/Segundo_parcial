import pygame
from pygame.locals import *
import json



def respuesta_correcta(lista:list, numero_pregunta:list,texto_puntaje,contador:list,puntaje:list,opcion:str,font,sonido_correcta,sonido_incorrecta1,sonido_incorrecta2,a:list,b:list,c:list):
    """
    Se le pasa por parametro:
    * La lista con las preguntas a revisar
    * Una lista con un indice para manipular el numero de pregunta
    * el texto del puntaje
    * Una lista con un indice para manipular el contador
    * Una lista con un indice para manipular el puntaje
    * La opcion la cual vamos a utilizar (a,b,c)
    * La fuente que vamos a utilizar
    * Los sonidos de cuando se elige una opcion correcta
    * Los dos sonidos de cuando se elige una incorrecta por primera y segunda vez
    * Las 3 lista donde queramos manipular el primer indice con un valor booleano.

    La funcion va a verificar si la opcion elegida es correcta, si fue correcta cuantos intentos
    nos llevo y va a reproducir un sonido en base a esto.
    """
    if lista[numero_pregunta[0]]["correcta"] == opcion:
        if contador[0] == 0:
            numero_pregunta[0] += 1
            puntaje[0] = int(puntaje[0]) + 10
            texto_puntaje = font.render(str(puntaje[0]), True, (252, 186, 3))
            contador[0] = 0
            sonido_correcta.play()
        elif contador[0] == 1:
            numero_pregunta[0] += 1
            puntaje[0] = int(puntaje[0]) + 5
            texto_puntaje = font.render(str(puntaje[0]), True, (252, 186, 3))
            contador[0] = 0
            reiniciar_incorrectas(a,b,c)
            sonido_correcta.play()
    else:
        if contador[0] == 0:
            contador[0] += 1
            sonido_incorrecta1.play()
            if opcion == "a":
                a[0] = True
            elif opcion == "b":
                b[0] = True
            else:
                c[0] = True
        else:
            numero_pregunta[0] += 1
            contador[0] = 0
            sonido_incorrecta2.play()
            reiniciar_incorrectas(a,b,c)
    return texto_puntaje

def reinicio_valores(puntaje:list, numero_pregunta:list, contador:list):
    """
    Se le pasan 3 listas con un solo indice.

    Se asigna el valor 0 a cada indice

    """
    puntaje[0] = "0"
    numero_pregunta[0] = 0
    contador[0] = 0

def pasar_json(lista:list):
    """
    Recibe una lista por parametro.

    La cual pasa a un archivo JSON.
    """
    with open(f"Parcial_juego/lista_jugadores.json", "w") as archivo:
        json.dump(lista, archivo, indent= 4,ensure_ascii= False)
    
def carga_archivo() -> list:
    """
    Carga el archivo json

    Retorna la lista del archivo
    """
    with open("Parcial_juego/lista_jugadores.json", "r") as archivo:
        data_json = json.load(archivo)
    return data_json 

def ordenar_lista(lista: list,clave:str,criterio:str):
     """
     Se le pasa una lista con diccionarios dentro.

     Un criterio el cual va a ser Ascendente si queremos que ordene de menor a mayor o 
     Descedente si queremos que ordene de mayor a menor 

     Una clave la cual va a ser la variable por la cual vamos a ordenar la lista.

     Realiza los cambios en la lista haciendo el ordenamiento


     """

     for i in range(len(lista) -1):
          for j in range(i+1, len(lista)):
                if (criterio == "asc" and lista[i][clave] < lista[j][clave]) or (criterio == "desc" and lista[i][clave] < lista[j][clave]):
                    aux = lista[i]
                    lista[i] = lista[j] 
                    lista[j] = aux

def mostrar_tabla_puntaje(pantalla, lista_jugadores:list,font,sonido_menu,boton_menu,texto_menu,color_1:list,color_2:list,corona,bronce,plata):
    """
    Se le pasan por parametro:
    * Pantalla donde vamos a mostrar
    * Lista de jugadores que vamos a manipular
    * Fuente de letra que vamos a usar
    * Sonido del menu para deshabilitarlo
    * Valores asignados en variables para hacer un boton (boton y texto)
    * Color_1 = Color de fondo de pantalla 
    * Color_2 = Color de las letras 
    * Imagenes de corona (1er puesto), plata (2do puesto) y bronce (3er puesto)

    La funcion va a blitear en pantalla tanto las imagenes como el texto.
    Analiza la lista y blitea los primeros 3 jugadores en la lista.
    En caso de no haber jugadores lo nombres se reemplazan por la palabra: VACIO y el puntaje por el valor: 0.

    """
    sonido_menu.stop()
    pantalla.fill((color_1))
    pantalla.blit(corona,(450,185))
    pantalla.blit(plata,(450,320))
    pantalla.blit(bronce,(450,430))
    if len(lista_jugadores) >= 1:
        nombre_primer_jugador = font.render(f"{lista_jugadores[0]["nombre"]}",True,(color_2))
        puntaje_primer_jugador = font.render(f"{lista_jugadores[0]["puntaje"]}",True,(color_2))
        pantalla.blit(nombre_primer_jugador, (500, 193))
        pantalla.blit(puntaje_primer_jugador, (700, 193))
    else:
        nombre_primer_jugador = font.render("VACIO",True,(color_2))
        puntaje_primer_jugador = font.render("0",True,(color_2))
        pantalla.blit(nombre_primer_jugador, (500, 193))
        pantalla.blit(puntaje_primer_jugador, (700, 193))
    if len(lista_jugadores) >= 2:
        nombre_segundo_jugador = font.render(f"{lista_jugadores[1]["nombre"]}",True,(color_2))
        puntaje_segundo_jugador = font.render(f"{lista_jugadores[1]["puntaje"]}",True,(color_2))
        pantalla.blit(nombre_segundo_jugador, (500, 315))
        pantalla.blit(puntaje_segundo_jugador, (700, 315))
    else:
        nombre_segundo_jugador = font.render("VACIO",True,(color_2))
        puntaje_segundo_jugador = font.render("0",True,(color_2))
        pantalla.blit(nombre_segundo_jugador, (500, 315))
        pantalla.blit(puntaje_segundo_jugador, (700, 315))
    if len(lista_jugadores) >= 3:
        nombre_tercer_jugador = font.render(f"{lista_jugadores[2]["nombre"]}",True,(color_2))
        puntaje_tercer_jugador = font.render(f"{lista_jugadores[2]["puntaje"]}",True,(color_2))
        pantalla.blit(nombre_tercer_jugador, (500, 423))
        pantalla.blit(puntaje_tercer_jugador, (700, 423))
    else:
        nombre_tercer_jugador = font.render("VACIO",True,(color_2))
        puntaje_tercer_jugador = font.render("0",True,(color_2))
        pantalla.blit(nombre_tercer_jugador, (500, 423))
        pantalla.blit(puntaje_tercer_jugador, (700, 423))
    pygame.draw.rect(pantalla, (55, 39, 145), (boton_menu), border_radius= 15)
    pantalla.blit(texto_menu,(520,544))

def reiniciar_incorrectas(a:list,b:list,c:list):
    """
    Se le pasa por parametro 3 listas.

    El primer indice de estas listas se reemplaza por el valor booleano False.
    """
    a[0] = False
    b[0] = False
    c[0] = False

def mostrar_pantalla_inicio(sonido_menu,pantalla,color_rectangulo,boton_1,boton_2,boton_3,fondo_pantalla_inicio,texto_1,texto_2,texto_3):
    """
    Por parametro se le pasa: 
    * Sonido para el menu
    * Pantalla donde vamos a blitear
    * Color que queramos para los botones
    * Las variables de 3 botones con pygame.Rect
    * Fondo de pantalla 
    * Los font.render que queramos para los botones
    
    La funcion va a blitear en pantalla tanto los botones como el texto que le pasamos,
    con la musica de fondo, para que asemeje a un menu de un juego.
    """
    sonido_menu.play()
    pantalla.blit(fondo_pantalla_inicio, (0,0))
    pygame.draw.rect(pantalla, (color_rectangulo), (boton_1), border_radius= 15)
    pygame.draw.rect(pantalla, (color_rectangulo), (boton_2), border_radius= 15)
    pygame.draw.rect(pantalla, (color_rectangulo), (boton_3), border_radius= 15)
    pantalla.blit(texto_1,(140,230))
    pantalla.blit(texto_2,(508,540))
    pantalla.blit(texto_3,(944,233))
    

def asignar_frases_puntaje(pantalla,puntaje:list,lista:list,fuente):
    """
    Se le pasa por parametro:
    * Pantalla donde vamos a blitear
    * Puntaje 
    * Lista 
    * Fuente para el texto que vamos a blitear

    La funcion pregunta si el jugador sobrepaso la mitad de los puntos posibles,
    si no los alcanzo o si alcanzo la maxima posible (para esto la lista a analizar,
    es donde se encuentran las preguntas).
    Y en base a esto se le asigna un mensaje.
    """
    puntaje[0] = int(puntaje[0])
    if puntaje[0] >= (len(lista) / 2) * 10:
        frase = fuente.render("Felicitaciones usted obtuvo mas de la mitad de los puntos posibles",True,(252, 186, 3))
        coordenadas = [160,200]
    if puntaje[0] <= (len(lista) / 2) * 10:
        frase = fuente.render("Mas suerte la proximo obtuvo menos de la mitad de los puntos posibles",True,(252, 186, 3))
        coordenadas = [150,200]
    if puntaje[0] == (len(lista) * 10):
        frase = fuente.render("OBTUVISTE LA PUNTUACION MAXIMA!!!!",True,(252, 186, 3))
        coordenadas = [350,200]
    pantalla.blit(frase,(coordenadas))

def agregar_jugador(puntaje:int,nombre:str,lista_jugadores:list):
    """
    La funcion va a agregar un jugador (con formato de diccionario) a la lista con su nombre y puntaje correspondiente.
    Dentro de esta la lista ya se ordena de mayor a menor y se pasa a un archivo json con la ayuda
    de otras funciones.
    
    Retorna False (valor booleano).

    Se le pasa por parametro:
    * Puntaje es el valor que se le asigna a la clave puntaje
    * Nombre es el valor que se le asigna a la clave nombre
    * Lista_jugadores es la lista donde se agrega el jugador
    
    """
    nuevo_jugador = {}
    nuevo_jugador["nombre"] = nombre
    nuevo_jugador["puntaje"] = puntaje
    lista_jugadores.append(nuevo_jugador)
    ordenar_lista(lista_jugadores,"puntaje","asc")
    pasar_json(lista_jugadores)
    agrego_jugador = False
    return agrego_jugador
    