import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# URL de la página a hacer scraping
#url = 'https://www.getonbrd.com/empleos/programacion'

Topicos_ = ['programacion','diseno-ux','data-science-analytics']

# Antiguedad de las publicaciones
Antiguedad_ = 3

def Obtencion_Datos(Topico, Antiguedad):

    #response = requests.get(url)

    response = requests.get('https://www.getonbrd.com/empleos/' + Topico)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        empleos = soup.find_all('a', class_='gb-results-list__item')

        fecha_actual = datetime.now()

        for empleo in empleos:
            titulo = empleo.find('strong', class_='pr-3').text.strip()
            empresa = empleo.find('strong').text.strip()
            nivel = empleo.find('span', class_='opacity-half').text.strip()
            ubicacion = empleo.find('span', class_='location').text.strip()
            fecha_publicacion_str = empleo.find('div', class_='opacity-half').text.strip()

            fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%b %d')

            if fecha_actual.month < fecha_publicacion.month:
                fecha_publicacion = fecha_publicacion.replace(year=fecha_actual.year - 1)
            else:
                fecha_publicacion = fecha_publicacion.replace(year=fecha_actual.year)

            antiguedad = (fecha_actual - fecha_publicacion).days

            if antiguedad <= Antiguedad:
                print(f'Título: {titulo}\nEmpresa: {empresa}\nNivel y Modalidad: {nivel}\nFecha de Publicación: {fecha_publicacion_str}\nAntigüedad: {antiguedad} días\nUbicación: {ubicacion}\n{"="*30}\n')
            #print(f'Título: {titulo}\nEmpresa: {empresa}\nNivel y Modalidad: {nivel}\nFecha de Publicación: {fecha_publicacion}\nUbicación: {ubicacion}\n{"="*30}\n')

    else:
        print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')

#Obtencion_Datos(Topicos_, Antiguedad_)

for ElementosTopicos in Topicos_:
    Obtencion_Datos(ElementosTopicos, Antiguedad_)
    #print(ElementosTopicos)