from bs4 import BeautifulSoup
import requests
print("Informacion precios Hostal Asuncion \n\n")
#Fecha de ingreso
check_in = input("Ingrese fecha de ingreso en el formato yyyy-mm-dd, ejm 2017-11-12: ")
#fecha de salida
check_out = input("Ingrese fecha de salida en el formato yyyy-mm-dd, ejm 2017-11-13: ")
direccion = 'https://www.booking.com/searchresults.es.html?dest_id=12082&dest_type=hotel&checkin_year_month_monthday='+check_in+'&checkout_year_month_monthday='+check_out
#importante los headers en el request.get, si no se usan la respuesta es diferente a la que se obtiene en un browser
pagina = requests.get(direccion, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
paginaHtml = pagina.text
soup = BeautifulSoup(paginaHtml, 'html.parser')
#busqueda del hostal asuncion aprovechando que es el primero de la lista
hotel = soup.find_all("strong", class_="price")
#precio dentro del tag
precio = soup.find('b')
print("\nPrecio por estadia desde "+check_in+" hasta: "+check_out+" en hotel Asuncion: "+precio.string)