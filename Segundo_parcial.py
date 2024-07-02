from datos import lista
import pygame
from pygame.locals import *
from biblioteca_juego import *

pygame.init() #Se inicializa pygame
config_pantalla = [1280, 720]
pantalla = pygame.display.set_mode(config_pantalla)
running = True
ubicacion_rectangulo = [225, 225]
tamanio_rectangulo = [50, 50]
color_rectangulo = [0,0,0]
pantalla_inicio = True
numero_pregunta = [0]
contador = [0]
a_incorrecta = [False]
b_incorrecta = [False]
c_incorrecta = [False]
primera_pregunta = False
jugando = False
agrego_jugador = False
scoreboard = False
lista_jugadores = carga_archivo()

#Imagenes
fondo_pantalla_inicio = pygame.image.load("Parcial_juego\preguntados.jpg")
corona = pygame.image.load("Parcial_juego/corona.webp")
corona = pygame.transform.scale(corona, (50, 50))
medalla_bronce = pygame.image.load("Parcial_juego/medalla_bronce.png")
medalla_bronce = pygame.transform.scale(medalla_bronce, (50, 50))
medalla_plata = pygame.image.load("Parcial_juego/medalla_plata.png")
medalla_plata = pygame.transform.scale(medalla_plata, (50, 50))

#COLORES
blanco = [255,255,255]
amarillo = [252, 186, 3]
violeta_fondo = [96, 49, 176]
violeta_botones = [55, 39, 145]

#TEXTO
font = pygame.font.SysFont("Impact", 35)
texto_inicio = font.render("Empezar a jugar", True, (violeta_fondo))
texto_salida = font.render("Salir del juego",True, (violeta_fondo))
texto_scoreboard = font.render("Puntaje", True,(violeta_fondo))
palabra_puntaje = font.render("Puntaje:", True, (amarillo))
puntaje = ["0"]
texto_puntaje = font.render(puntaje[0], True, (amarillo))
texto_preguntar = font.render("Siguiente pregunta", True, (blanco))
texto_reiniciar = font.render("Reinicar", True, (blanco))
texto_pregunta = font.render(f"{lista[numero_pregunta[0]]["pregunta"]}", True, (blanco))
texto_opcion_a = font.render(f"{lista[numero_pregunta[0]]["a"]}", True,(blanco))
texto_opcion_b = font.render(f"{lista[numero_pregunta[0]]["b"]}", True,(blanco))
texto_opcion_c = font.render(f"{lista[numero_pregunta[0]]["c"]}", True,(blanco))
texto_menu = font.render("Volver al menu",True,(blanco))
nombre = ""
texto_nombre = font.render(f"Ingrese su nickname: ",True,(252, 186, 3))

#PANTALLA INICIO BOTONES
boton_inicio = pygame.Rect(126,217,300,70)
boton_puntaje = pygame.Rect(860,217,300,70)
boton_salida = pygame.Rect(490,525,300,70)
boton_menu = pygame.Rect(490,525,300,70)

#PANTALLA JUEGO BOTONES
boton_opcion_a = pygame.Rect(39,311,350,70)
boton_opcion_b = pygame.Rect(39,410,350,70)
boton_opcion_c = pygame.Rect(39,510,350,70)
boton_pregunta = pygame.Rect(878,326,350,70)
boton_reiniciar = pygame.Rect(878,525,350,70)
boton_borde_a = pygame.Rect(35,305,360,80)
boton_borde_b = pygame.Rect(35,404,360,80)
boton_borde_c = pygame.Rect(35,504,360,80)
boton_borde_pregunta = pygame.Rect(874,322,360,80)
boton_borde_reiniciar = pygame.Rect(874,521,360,80)

#SONIDOS
sonido_menu = pygame.mixer.Sound("Parcial_juego\musica_menu.mp3")
sonido_menu.set_volume(0.5)
sonido_opcion_correcta = pygame.mixer.Sound("Parcial_juego/correcta.mp3")
sonido_opcion_incorrecta1 = pygame.mixer.Sound("Parcial_juego/incorrecta_1.mp3")
sonido_opcion_incorrecta2 = pygame.mixer.Sound("Parcial_juego/incorrecta_2.mp3")

while running:
    pressed_keys = pygame.key.get_pressed()
    #EVENTOS DEL JUEGO
    for event in pygame.event.get():  #pygame.even.get(): se obtienen los eventos que suceden

        if jugando == False and pantalla_inicio == False and scoreboard == False:
            asignar_frases_puntaje(pantalla,puntaje,lista,font)
            pantalla.blit(texto_nombre,(351,292))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    agrego_jugador = True
                    pantalla_inicio = True
                nombre += event.unicode
                nombre_escrito = font.render(f"Ingrese su nickname: {nombre}",True,(amarillo))
                pantalla.blit(nombre_escrito,(351,292))
                
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if pantalla_inicio == True:
                if boton_inicio.collidepoint(event.pos):
                    pantalla_inicio = False
                    jugando = True
                if boton_salida.collidepoint(event.pos):
                    running = False
                if boton_puntaje.collidepoint(event.pos):
                    scoreboard = True
                    pantalla_inicio = False

            elif jugando == True:
                if boton_pregunta.collidepoint(event.pos) and primera_pregunta == True:
                    numero_pregunta[0] += 1
                    reiniciar_incorrectas(a_incorrecta,b_incorrecta,c_incorrecta)

                if boton_pregunta.collidepoint(event.pos) and primera_pregunta == False:
                    primera_pregunta = True

                if boton_reiniciar.collidepoint(event.pos):
                    reiniciar_incorrectas(a_incorrecta,b_incorrecta,c_incorrecta)
                    reinicio_valores(puntaje,numero_pregunta,contador)
                    texto_puntaje = font.render(str(puntaje[0]), False, (amarillo))

                if primera_pregunta == True:
                    if boton_opcion_a.collidepoint(event.pos) and a_incorrecta[0] == False:
                        texto_puntaje = respuesta_correcta(lista,numero_pregunta,texto_puntaje,contador,puntaje,"a",font,sonido_opcion_correcta,sonido_opcion_incorrecta1,sonido_opcion_incorrecta2,a_incorrecta,b_incorrecta,c_incorrecta)

                    if boton_opcion_b.collidepoint(event.pos) and b_incorrecta[0] == False:
                        texto_puntaje = respuesta_correcta(lista,numero_pregunta,texto_puntaje,contador,puntaje,"b",font,sonido_opcion_correcta,sonido_opcion_incorrecta1,sonido_opcion_incorrecta2,a_incorrecta,b_incorrecta,c_incorrecta)
                        
                    if boton_opcion_c.collidepoint(event.pos) and c_incorrecta[0] == False:
                        texto_puntaje = respuesta_correcta(lista,numero_pregunta,texto_puntaje,contador,puntaje,"c",font,sonido_opcion_correcta,sonido_opcion_incorrecta1,sonido_opcion_incorrecta2,a_incorrecta,b_incorrecta,c_incorrecta)
            else:
                if boton_menu.collidepoint(event.pos) and scoreboard == True:
                    pantalla_inicio = True 
                    scoreboard = False
                elif boton_menu.collidepoint(event.pos) and scoreboard == False:
                    agrego_jugador = True
                    pantalla_inicio = True 

    if numero_pregunta[0] == len(lista):
        primera_pregunta = False
        jugando = False
        pantalla.fill(violeta_fondo)
        pantalla.blit(texto_puntaje, (650,100))
        pantalla.blit(palabra_puntaje, (516,100))
        pygame.draw.rect(pantalla, (violeta_botones), (boton_menu), border_radius= 15)
        pantalla.blit(texto_menu,(520,544))
        numero_pregunta[0] = 0
        contador[0] = 0
        aux = int(puntaje[0])
        
    if agrego_jugador == True:
        agrego_jugador = agregar_jugador(aux,nombre,lista_jugadores)
        nombre = ""
        puntaje[0] = "0"
        texto_puntaje = font.render(str(puntaje[0]), True, (amarillo))
    
    if scoreboard == True:
        mostrar_tabla_puntaje(pantalla,lista_jugadores,font,sonido_menu,boton_menu,texto_menu,violeta_fondo,blanco,corona,medalla_bronce,medalla_plata)
        
        
    #PANTALLA DE INICIO
    if pantalla_inicio == True:
        mostrar_pantalla_inicio(sonido_menu,pantalla,amarillo,boton_inicio,boton_salida,boton_puntaje,fondo_pantalla_inicio,texto_inicio,texto_salida,texto_scoreboard)
        reiniciar_incorrectas(a_incorrecta,b_incorrecta,c_incorrecta)
            
    #PANTALLA DE JUEGO
    elif jugando == True:
        pantalla.fill(violeta_fondo)
        pygame.draw.rect(pantalla, (amarillo), (boton_borde_pregunta), border_radius= 15)
        pygame.draw.rect(pantalla, (amarillo), (boton_borde_reiniciar), border_radius= 15)
        pygame.draw.rect(pantalla, (violeta_botones), (boton_pregunta), border_radius= 15)
        pygame.draw.rect(pantalla, (violeta_botones), (boton_reiniciar), border_radius= 15)
        sonido_menu.stop()
        pantalla.blit(texto_puntaje, (650,100))
        pantalla.blit(palabra_puntaje, (516,100))
        pantalla.blit(texto_preguntar,(915,340))
        pantalla.blit(texto_reiniciar,(985, 540))
        if primera_pregunta == True:
            texto_pregunta = font.render(f"{lista[numero_pregunta[0]]["pregunta"]}", True, (blanco))
            texto_opcion_a = font.render(f"{lista[numero_pregunta[0]]["a"]}", True,(blanco))
            texto_opcion_b = font.render(f"{lista[numero_pregunta[0]]["b"]}", True,(blanco))
            texto_opcion_c = font.render(f"{lista[numero_pregunta[0]]["c"]}", True,(blanco))
            pantalla.blit(texto_pregunta,(60,195))
            if a_incorrecta[0] == False:
                pygame.draw.rect(pantalla,(amarillo),(boton_borde_a), border_radius= 15)
                pygame.draw.rect(pantalla, (violeta_botones), (boton_opcion_a), border_radius= 15)
                pantalla.blit(texto_opcion_a, (60, 330))
            if b_incorrecta[0] == False:
                pygame.draw.rect(pantalla,(amarillo),(boton_borde_b), border_radius= 15)
                pygame.draw.rect(pantalla, (violeta_botones), (boton_opcion_b), border_radius= 15)
                pantalla.blit(texto_opcion_b, (60, 428))
            if c_incorrecta[0] == False:
                pygame.draw.rect(pantalla,(amarillo),(boton_borde_c), border_radius= 15)
                pygame.draw.rect(pantalla, (violeta_botones), (boton_opcion_c), border_radius= 15)
                pantalla.blit(texto_opcion_c, (60, 530))

    pygame.display.flip()
pygame.quit() # Fin