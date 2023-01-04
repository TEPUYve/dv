import requests
from lxml import html

# Hacer una solicitud HTTP a la página web y obtener el contenido HTML
url = 'https://exchangemonitor.net/dolar-venezuela'
page = requests.get(url)
tree = html.fromstring(page.content)

# Utilizar xpath para seleccionar la fecha, el valor del dólar paralelo y el valor del dólar del BCV
fecha_xpath = '//section[@class="light-bg"]/div[1]/div[1]/div[1]/p[1]'
paralelo_xpath = '//section[@class="light-bg"]/div[1]/div[6]/div[7]/div[1]/div[1]/div[2]/p[2]'
bcv_xpath = '//section[@class="light-bg"]/div[1]/div[6]/div[14]/div[1]/div[1]/div[2]/p[2]'
fecha = tree.xpath(fecha_xpath)[0].text
paralelo = tree.xpath(paralelo_xpath)[0].text
bcv = tree.xpath(bcv_xpath)[0].text

print(f'EL PRECIO DEL DOLAR HOY')
print(f'Dólar paralelo: {paralelo}')
print(f'Dólar BCV: {bcv}')
print(f'Copyright © 2023 - TEPUY') 

###
#La información que se presenta a continuación ha sido recopilada mediante el uso de tecnologías de inteligencia artificial y scraping de datos públicos. TEPUY no es responsable por la exactitud o integridad de esta información y se exime de toda responsabilidad en caso de cualquier error o imprecisión. Además, TEPUY no se hace responsable por el uso indebido de esta información por parte de terceros. Esta información se proporciona únicamente con fines educativos y no debe utilizarse para ningún propósito comercial o ilegal. TEPUY se reserva el derecho a realizar cambios o correcciones a esta información en cualquier momento sin previo aviso.
###

