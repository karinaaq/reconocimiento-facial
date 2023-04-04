# Aplicación de Reconocimiento Facial
Esta aplicación desarrollada en Python utiliza técnicas de reconocimiento facial para identificar a las personas que aparecen en el marco de la cámara. Además, distinguir entre clientes y empleados, si una persona no es reconocida, se puede registrar en el sistema para futuras referencias. Y, para los empleados registrados, el sistema puede registrar la hora de entrada y salida en una base de datos para el seguimiento del tiempo de trabajo.

 ##  Partes de la aplicación:
 ![screen1](https://user-images.githubusercontent.com/67199946/229819409-92b04d83-38d2-46da-a648-e473ba1b3f9b.png)

**1. Main:**
      Al correr la aplicación, se abre la cámara y se queda abierta reconociendo a las personas que entran en el marco de la camara hasta que el usuario decida hacer alguna de las siguientes partes expuestas en esta sección.
**2. Registrar Personas:** 
      En primer lugar, se deben completar los datos de la persona (Nombre y si es Empleado o Cliente), luego, abre la cámara y toma fotografías de la persona, para luego entrenar el modelo y guardarlo en el directorio donde está el código fuente.
      
**3. Registrar Entrada/Salida:** 
      Se pide presionar **Tab** en la ventana de la camara para obtener el nombre del empleado reconocido, luego se debe ingresar si quiere registrar una entrada o una salida y el programa inserta en una base de datos dicha información.
      
