"""
Uso de librerías de fecha y tiempo
"""

from datetime import datetime, date

fecha = date.today()

print(fecha)

tiempo = datetime.now()
print(tiempo)

año = tiempo.year
mes= tiempo.month
dia = tiempo.day

print("Año actual :{}".format(año))
print("Mes actual :{}".format(mes))
print("Dia actual :{}".format(dia))

"""Uso de datetime para extraer la hora, minuto y segundo"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("Hora actual :{}".format(hora))
print("Minuto actual :{}".format(minuto))
print("Segundo actual :{}".format(segundo))