"""

Uso de librerias de fecha y tiempo
Conversion de fechas
"""

from datetime import datetime

"""Uso del método timestamp"""

time_now = datetime.strptime("2025/05/02 20:30:00",
                             "%Y/%m/%d %H:%M:%S").timestamp()
#.timestamp() devuelve en los segundos totales todo el tiempo actual

print(time_now)