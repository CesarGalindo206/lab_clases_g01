from datetime import datetime

str_date = "2/6/2025"

# Formato correcto: día/mes/año
conversion = datetime.strptime(str_date, '%d/%m/%Y')
print(conversion)

"Traer el mes de la fecha con formato string: strftime de datetime"

conversion_mes = conversion.strftime('%d %b del %y')
print(conversion_mes)

"""
b: reemplaza al "m" para mostrar el mes de forma literal
"""