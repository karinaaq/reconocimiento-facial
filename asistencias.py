import mysql.connector
from datetime import datetime
def registrar_asistencia(nombreEmpleado, tipoRegistro):
  '''
  Registra en la base de datos las horas de entrada y salida de los empleados (fecha incluída)
  Args:
    string nombreEmpleado: Nombre del Empleado en cuestion
    string tipoRegistro: Entrada o Salida
  Returns:
    string: Confirmacion de exito o falla.
  '''
  conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="registros"
  )
  cursor = conexion.cursor()
  try:
    if (tipoRegistro == 'Entrada'):
      sql = f"INSERT INTO asistencias (empleado, hora_entrada) VALUES ('{nombreEmpleado}', NOW())" 
      info = 'Entrada registrada con exito.'
    else:
      cursor.execute(f"SELECT MAX(id) FROM asistencias where empleado='{nombreEmpleado}'")
      result = cursor.fetchone()
      ultimo_id = result[0]
      sql = f"UPDATE asistencias SET hora_salida=NOW() WHERE id={ultimo_id}"
      info = 'Salida registrada con exito.'
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()
  except Exception as e:
      info = f'Ocurrio un error en el registro. {e}'
  
  return info