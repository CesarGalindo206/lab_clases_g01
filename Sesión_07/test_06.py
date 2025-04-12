"""Uso de la librería JSON para tratar datos de tipo JSON"""

import json

date_python = {'nombre': 'Milagros', 'edad' : 32, 'distrito' : 'Jesus Maria'}

#Convirtiendo a un dato tipo JSON

python_to_json = json.dumps(date_python)
print(python_to_json)
print(type(python_to_json))