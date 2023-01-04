#!/bin/bash

#ingresar a ruta donde esta el script python
cd ruta
# Ejecutar el script de Python y guardar la salida en una variable
output=$(python3 bot-telegram-jf-d.py)

# Enviar la salida a Telegram utilizando el bot de Telegram y el ID de chat

# notificacion telegram
##
TOKEN="TOKEN"
ID="CHAT_ID"
MENSAJE="$output"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"

###
#La información que se presenta a continuación ha sido recopilada mediante el uso de tecnologías de inteligencia artificial y scraping de datos públicos. TEPUY no es responsable por la exactitud o integridad de esta información y se exime de toda responsabilidad en caso de cualquier error o imprecisión. Además, TEPUY no se hace responsable por el uso indebido de esta información por parte de terceros. Esta información se proporciona únicamente con fines educativos y no debe utilizarse para ningún propósito comercial o ilegal. TEPUY se reserva el derecho a realizar cambios o correcciones a esta información en cualquier momento sin previo aviso.
###
