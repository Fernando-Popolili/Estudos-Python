from datetime import datetime, date

agora = datetime.now()
print(agora.strftime("Hoje é dia %d do mês %m do ano %Y"))
print(agora.strftime("Agora são %H horas e %M minutos"))

print(agora)
print(agora.day)
print(agora.month)

aniversario = date(2004,12,29)
print(aniversario)

data_str = "29-12-2005"
data_convertida = date.strptime(data_str, "%d-%m-%Y")
print(data_convertida)





