#enviando mensaje whatsapp
import WSPBOT

numero = input("Introduzca numero de telefono:")
mensaje = input("Introduzca mensaje:")
hora = int(input("hora de envio:"))
minuto =int(input("minuto de envio:"))

WSPBOT.sendwhatmsg(numero,mensaje,hora, minuto)