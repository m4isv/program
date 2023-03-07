import pytz
from datetime import datetime

fuso_horario = pytz.timezone('Brazil/East')
horario_br = datetime.now(fuso_horario)
print(horario_br.strftime('%d/%m/%Y %H:%M:%S'))