# Proyecto final de programación 2 robot traductor arandubot
# Importación de librerias necesarias

import event, time, cyberpi, mbuild
import time
import matplotlib.pyplot as plt

# Definición de diagrama
def diagrama_de_uso(diccionario, color):
    # Obtener las palabras y los contadores del diccionario
    palabras = list(diccionario.keys())
    contadores = list(diccionario.values())

    # Crear gráfico de barras
    plt.figure(figsize=(15, 8))
    plt.barh(palabras, contadores, color=color)
    plt.xlabel('Contadores')
    plt.title('Contadores de Palabras')
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.show()

#Iniciamos las variables para el contador de los usos de las palabras
contador_hola = 0
contador_adios = 0
contador_personaje = 0
contador_palabra = 0
contador_imagen = 0
contador_cuento = 0
contador_narracion = 0
contador_amigo = 0
contador_leer = 0
contador_escribir = 0
contador_escuela = 0
contador_hospital = 0
contador_plaza = 0
contador_casa = 0
contador_familia = 0
contador_madre = 0
contador_padre = 0
contador_hermana = 0
contador_hermano = 0
contador_abuela = 0
contador_hambre = 0
contador_comer = 0
contador_dolor = 0
contador_sueno = 0
contador_agua = 0
contador_pan = 0
contador_historia = 0
contador_pais = 0
contador_paraguay = 0
contador_indigena = 0
contador_hoja = 0
contador_lapiz = 0
contador_tarea = 0
contador_juguete = 0
contador_pelota = 0
contador_brazo = 0
contador_hombre = 0
contador_mujer = 0
contador_perro = 0
contador_gato = 0
contador_conejo = 0
contador_anillo = 0
contador_abeja = 0
contador_bailar = 0
contador_blanco = 0
contador_caballo = 0
contador_calabaza = 0
contador_cantar = 0
contador_cantaro = 0
contador_cerdo = 0


# Conexion a la base de datos

cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")

#La base de datos utilizada es microsoft azure y en el caso que deseamos realizar un cambio en el proyecto
#El token de acceso es generado de manera automatica por medio de nuestra cuenta
#Para brindarle mayores posibilidades se podría cambiar el motor de base por otro como GTP o la base de datos de google
#No es posible cambar debido a que es una conexión directa entre la marca makeblock y el servidor.
#Si deseamos realizar este programa deberiamos utilizar un sistema libre como Arduino o rasberrypi

@event.start #llamamos una funcion de inicio de nuestra librería event para poder iniciar la lectura del código desde la placa
#Se realiza el inicio de lectura del programa mediante la placa
#Iniciamos la placa del robot solicitando el acceso a la red de wifi local, debe ser la misma que la de la computadora


def on_start():  #definimos una función por medio de la cual, una vez la placa se encienda esta pueda realizar la siguiente acción
    global boton
    mbuild.speaker.set_volume(100, 1)
    cyberpi.led.show('green black black black black')
    time.sleep(1)
    cyberpi.led.move(1)
    time.sleep(1)
    cyberpi.led.move(1)
    time.sleep(1)
    cyberpi.led.move(1)
    time.sleep(1)
    cyberpi.led.move(1)
    time.sleep(1)
    cyberpi.led.show('green green green green green')
    cyberpi.wifi.connect("IDT-ADMINISTRACION", "idtsa@admin22")
    while not cyberpi.wifi.is_connect():

      pass

    cyberpi.led.play('rainbow')

#Si la red se conecta de manera exitosa debe encender la luz led en forma de arcoiris

@event.is_press('a')

#por medio de una interacción se da inicio a la fase de escucha para la traducción


def is_btn_press(): #definimos una funcion de interación mediante por medio de que el botón de la placa sea prosionada este realiza la segunda parte del programa
    global boton
    cyberpi.led.on(208, 2, 27, "all")
    cyberpi.cloud.listen('spanish', 2) #por medio de la siguiente función la placa nos escucha por medio de su micronofono incorporado, previamente confugurado para un idioma en especifico durante un tiempo especificado
    #La placa escucha y envia la información de audio a la base de datos para procesar y recibir el audio en formato texto
    cyberpi.led.off("all")
    if str(cyberpi.cloud.listen_result()).find(str('inicio')) > -1:  #Para la primaera condicional utilizamos un si entonces sino
      mbuild.speaker.play_melody_until_done("0099", 1)

    else: #Si no se cumple la condicion inicial se pasa al siguiente conjunto de condicionales para su verificación
      if str(cyberpi.cloud.listen_result()).find(str('hola')) > -1:
        mbuild.speaker.play_melody_until_done("0001", 1)
        contador_hola=contador_hola+1

      if str(cyberpi.cloud.listen_result()).find(str('adios')) > -1:
        mbuild.speaker.play_melody_until_done("0002", 1)
        contador_adios=contador_adios+1

      if str(cyberpi.cloud.listen_result()).find(str('personaje')) > -1:
        mbuild.speaker.play_melody_until_done("0003", 1)
        contador_personaje=contador_personaje+1

      if str(cyberpi.cloud.listen_result()).find(str('palabra')) > -1:
        mbuild.speaker.play_melody_until_done("0004", 1)
        contador_palabra=contador_palabra+1

      if str(cyberpi.cloud.listen_result()).find(str('imagen')) > -1:
        mbuild.speaker.play_melody_until_done("0005", 1)
        contador_imagen=imagen+1

      if str(cyberpi.cloud.listen_result()).find(str('cuento')) > -1:
        mbuild.speaker.play_melody_until_done("0006", 1)
        contador_cuento=contador_cuento+1

      if str(cyberpi.cloud.listen_result()).find(str('narracion')) > -1:
        mbuild.speaker.play_melody_until_done("0007", 1)
        contador_narracion=contador_narracion+1

      if str(cyberpi.cloud.listen_result()).find(str('amigo')) > -1:
        mbuild.speaker.play_melody_until_done("0008", 1)
        contador_amigo=contador_amigo+1

      if str(cyberpi.cloud.listen_result()).find(str('leer')) > -1:
        mbuild.speaker.play_melody_until_done("0009", 1)
        contador_leer=contador_leer+1

      if str(cyberpi.cloud.listen_result()).find(str('escribir')) > -1:
        mbuild.speaker.play_melody_until_done("0010", 1)
        contador_escribir=contador_escribir+1

      if str(cyberpi.cloud.listen_result()).find(str('escuela')) > -1:
        mbuild.speaker.play_melody_until_done("0011", 1)
        contador_escuela=contador_escuela+1

      if str(cyberpi.cloud.listen_result()).find(str('hospital')) > -1:
        mbuild.speaker.play_melody_until_done("0012", 1)
        contador_hospital=contador_hospital+1

      if str(cyberpi.cloud.listen_result()).find(str('plaza')) > -1:
        mbuild.speaker.play_melody_until_done("0013", 1)
        contador_plaza=contador_plaza+1

      if str(cyberpi.cloud.listen_result()).find(str('casa')) > -1:
        mbuild.speaker.play_melody_until_done("0014", 1)
        contador_casa=contador_casa+1

      if str(cyberpi.cloud.listen_result()).find(str('familia')) > -1:
        mbuild.speaker.play_melody_until_done("0015", 1)
        contador_familia=contador_familia+1

      if str(cyberpi.cloud.listen_result()).find(str('madre')) > -1:
        mbuild.speaker.play_melody_until_done("0016", 1)
        contador_madre=contador_madre+1

      if str(cyberpi.cloud.listen_result()).find(str('padre')) > -1:
        mbuild.speaker.play_melody_until_done("0017", 1)
        contador_padre=contador_padre+1

      if str(cyberpi.cloud.listen_result()).find(str('hermana')) > -1:
        mbuild.speaker.play_melody_until_done("0018", 1)
        contador_hermana=contador_hermana+1

      if str(cyberpi.cloud.listen_result()).find(str('hermano')) > -1:
        mbuild.speaker.play_melody_until_done("0019", 1)
        contador_hermano=contador_hermano+1

      if str(cyberpi.cloud.listen_result()).find(str('abuela')) > -1:
        mbuild.speaker.play_melody_until_done("0020", 1)
        contador_abuela=contador_abuela+1

      if str(cyberpi.cloud.listen_result()).find(str('hambre')) > -1:
        mbuild.speaker.play_melody_until_done("0021", 1)
        contador_hambre_contador_hambre+1

      if str(cyberpi.cloud.listen_result()).find(str('comer')) > -1:
        mbuild.speaker.play_melody_until_done("0022", 1)
        contador_comer=contador_comer+1

      if str(cyberpi.cloud.listen_result()).find(str('dolor')) > -1:
        mbuild.speaker.play_melody_until_done("0023", 1)
        contador_dolor=contador_dolor+1

      if str(cyberpi.cloud.listen_result()).find(str('sueño')) > -1:
        mbuild.speaker.play_melody_until_done("0024", 1)
        contador_sueño=contador_sueño+1

      if str(cyberpi.cloud.listen_result()).find(str('agua')) > -1:
        mbuild.speaker.play_melody_until_done("0025", 1)
        contador_agua=contador_agua+1

      if str(cyberpi.cloud.listen_result()).find(str('pan')) > -1:
        mbuild.speaker.play_melody_until_done("0026", 1)
        contador_pan=contador_pan+1

      if str(cyberpi.cloud.listen_result()).find(str('historia')) > -1:
        mbuild.speaker.play_melody_until_done("0027", 1)
        contador_historia=contador_historia+1

      if str(cyberpi.cloud.listen_result()).find(str('pais')) > -1:
        mbuild.speaker.play_melody_until_done("0028", 1)
        contador_pais=contador_pais+1

      if str(cyberpi.cloud.listen_result()).find(str('paraguay')) > -1:
        mbuild.speaker.play_melody_until_done("0029", 1)
        contador_paraguay=contador_paraguay+1

      if str(cyberpi.cloud.listen_result()).find(str('indigena')) > -1:
        mbuild.speaker.play_melody_until_done("0030", 1)
        contador_indigena=contador_indigena+1

      if str(cyberpi.cloud.listen_result()).find(str('hoja')) > -1:
        mbuild.speaker.play_melody_until_done("0031", 1)
        contador_hoja=contador_hoja+1

      if str(cyberpi.cloud.listen_result()).find(str('lapiz')) > -1:
        mbuild.speaker.play_melody_until_done("0032", 1)
        contador_lapiz=contador_lapiz+1

      if str(cyberpi.cloud.listen_result()).find(str('tarea')) > -1:
        mbuild.speaker.play_melody_until_done("0033", 1)
        contador_tarea=contador_tarea+1

      if str(cyberpi.cloud.listen_result()).find(str('juguete')) > -1:
        mbuild.speaker.play_melody_until_done("0034", 1)
        contador_juguete=contador_juguete+1

      if str(cyberpi.cloud.listen_result()).find(str('pelota')) > -1:
        mbuild.speaker.play_melody_until_done("0035", 1)
        contador_pelota=contador_pelota+1

      if str(cyberpi.cloud.listen_result()).find(str('brazo')) > -1:
        mbuild.speaker.play_melody_until_done("0036", 1)
        contador_brazo=contador_brazo+1

      if str(cyberpi.cloud.listen_result()).find(str('hombre')) > -1:
        mbuild.speaker.play_melody_until_done("0037", 1)
        contador_hombre=contador_hombre+1

      if str(cyberpi.cloud.listen_result()).find(str('mujer')) > -1:
        mbuild.speaker.play_melody_until_done("0038", 1)
        contador_mujer=contador_mujer+1

      if str(cyberpi.cloud.listen_result()).find(str('perro')) > -1:
        mbuild.speaker.play_melody_until_done("0039", 1)
        contador_perro=contador_perro+1

      if str(cyberpi.cloud.listen_result()).find(str('gato')) > -1:
        mbuild.speaker.play_melody_until_done("0040", 1)
        contador_gato=contador_gato+1

      if str(cyberpi.cloud.listen_result()).find(str('conejo')) > -1:
        mbuild.speaker.play_melody_until_done("0041", 1)
        contador_conejo=contador_conejo+1

      if str(cyberpi.cloud.listen_result()).find(str('anillo')) > -1:
        mbuild.speaker.play_melody_until_done("0042", 1)
        contador_anillo=contador_anillo+1

      if str(cyberpi.cloud.listen_result()).find(str('abeja')) > -1:
        mbuild.speaker.play_melody_until_done("0043", 1)
        contador_abeja=contador_abeja+1

      if str(cyberpi.cloud.listen_result()).find(str('bailar')) > -1:
        mbuild.speaker.play_melody_until_done("0044", 1)
        contador_bailar=contador_bailar+1

      if str(cyberpi.cloud.listen_result()).find(str('blanco')) > -1:
        mbuild.speaker.play_melody_until_done("0045", 1)
        contador_blanco=contador_blanco+1

      if str(cyberpi.cloud.listen_result()).find(str('caballo')) > -1:
        mbuild.speaker.play_melody_until_done("0046", 1)
        contador_caballo=contador_caballo+1

      if str(cyberpi.cloud.listen_result()).find(str('calabaza')) > -1:
        mbuild.speaker.play_melody_until_done("0047", 1)
        contador_calabaza=contador_calabaza+1

      if str(cyberpi.cloud.listen_result()).find(str('cantar')) > -1:
        mbuild.speaker.play_melody_until_done("0048", 1)
        contador_cantar=contador_cantar+1

      if str(cyberpi.cloud.listen_result()).find(str('cantaro')) > -1:
        mbuild.speaker.play_melody_until_done("0049", 1)
        contador_cantaro=contador_cantaro+1

      if str(cyberpi.cloud.listen_result()).find(str('cerdo')) > -1:
        mbuild.speaker.play_melody_until_done("0050", 1)
        contador_cerdo=contador_contador_cerdo+1

    cantidad_palabras = {
      "hola": contador_hola,
      "adios": contador_adios,
      "personaje": contador_personaje,
      "palabra": contador_palabra,
      "imagen": contador_imagen,
      "cuento": contador_cuento,
      "narracion": contador_narracion,
      "amigo": contador_amigo,
      "leer": contador_leer,
      "escribir": contador_escribir,
      "escuela": contador_escuela,
      "hospital": contador_hospital,
      "plaza": contador_plaza,
      "casa": contador_casa,
      "familia": contador_familia,
      "madre": contador_madre,
      "padre": contador_padre,
      "hermana": contador_hermana,
      "hermano": contador_hermano,
      "abuela": contador_abuela,
      "hambre": contador_hambre,
      "comer": contador_comer,
      "dolor": contador_dolor,
      "sueno": contador_sueno,
      "agua": contador_agua,
      "pan": contador_pan,
      "historia": contador_historia,
      "pais": contador_pais,
      "paraguay": contador_paraguay,
      "indigena": contador_indigena,
      "hoja": contador_hoja,
      "lapiz": contador_lapiz,
      "tarea": contador_tarea,
      "juguete": contador_juguete,
      "pelota": contador_pelota,
      "brazo": contador_brazo,
      "hombre": contador_hombre,
      "mujer": contador_mujer,
      "perro": contador_perro,
      "gato": contador_gato,
      "conejo": contador_conejo,
      "anillo": contador_anillo,
      "abeja": contador_abeja,
      "bailar": contador_bailar,
      "blanco": contador_blanco,
      "caballo": contador_caballo,
      "calabaza": contador_calabaza,
      "cantar": contador_cantar,
      "cantaro": contador_cantaro,
      "cerdo": contador_cerdo,
    }
    
# Color elegido
color_elegido = 'skyblue'
diagrama_de_uso(cantidad_palabras, color_elegido)
