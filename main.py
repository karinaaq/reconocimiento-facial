import threading
import asistencias, registrar, reconocimiento
import time
import json 
def opciones():
    print('Bienvenido/a')

    print('1. Registrar persona')

    print('2. Marcaciones de Asistencia (para Empleados)')

    seleccion = int(input())

    if seleccion==1:
        print('Cierre la ventana de webcam')
        time.sleep(4)
        registrar.datos_persona()


    if seleccion==2:
        print('Presione Tab en la ventana de la camara para extraer nombre de empleado')
        print('Registrar 1. Entrada o 2. Salida: ')
        tipoRegistro= int(input())
        with open("identificacion.json", "r") as f:
            nombreEmpleado = json.load(f)
        print(asistencias.registrar_asistencia(nombreEmpleado, 'Entrada' if tipoRegistro==1 else 'Salida'))

hilo1 = threading.Thread(target=reconocimiento.abre_webcam)
hilo2 = threading.Thread(target=opciones)

hilo1.start()
hilo2.start()

hilo2.join()
hilo1.join()