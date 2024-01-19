import pyautogui
from PIL import Image
import pytesseract
import time

import Graphics


Topics = [
    "Automatizacion Industrial",
    "Automatizacion del Hogar",
    "Automatizacion de Procesos Empresariales",
    "Automatizacion de Marketing",
    "Automatizacion de la Cadena de Suministro",
    "Automatizacion de Tareas Cotidianas",
    "Automatizacion de Procesos de TI",
    "Automatizacion en la Agricultura",
    "Automatizacion en la Salud",
    "Automatizacion en la Educacion",
    "Automatizacion en la Robotica",
    "Automatizacion en la Inteligencia Artificial",
    "Automatizacion de Procesos Quimicos",
    "Automatizacion en la Energia Renovable",
    "Automatizacion en la Construccion",
    "Automatizacion en el Transporte",
    "Automatizacion en la Logistica",
    "Automatizacion en la Gestión de Residuos",
    "Automatizacion en la Impresion 3D",
    "Automatizacion en la Manufactura Aditiva",
    "Automatizacion en la Seguridad",
    "Automatizacion en la Domotica",
    "Automatizacion en la Agricultura de Precision",
    "Automatizacion en la Mineria"
]

Archive = "AutomatizacionData"

# Puedes acceder a cada tipo de video utilizando tipos_de_videos_youtube[index]

pytesseract.pytesseract.tesseract_cmd = r'D:'

print("inicio del progama")

time.sleep(6)

def WriteData(TopicCSV):
    nombre_archivo = 'Data/' + Archive + '.csv'
    # Abre el archivo en modo agregar ('a')
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(TopicCSV + '\n')
        time.sleep(0.5)

def ControlChrome(Topic):

    pyautogui.click(x=1163, y=128)

    pyautogui.typewrite(Topic)

    pyautogui.press("enter")

    time.sleep(2)

    #pyautogui.click(x=1163, y=128)

def GetData(Topic):

    for _ in range(3):  # Intentar hasta 5 veces

        X1 = 1531
        Y1 = 707
        X2 = 1654
        Y2 = 777
    
        region = (X1, Y1, X2 - X1, Y2 - Y1)
        screenshot = pyautogui.screenshot(region=region)
    
        screenshot.save('screenshotscore.png')
    
        text1 = pytesseract.image_to_string(Image.open('screenshotscore.png'))
    
        print(text1)
    
        #----------------------------------------------------------------------------------------
    
        X1 = 1438
        Y1 = 837
        X2 = 1858
        Y2 = 870
    
        region = (X1, Y1, X2 - X1, Y2 - Y1) 
        screenshot = pyautogui.screenshot(region=region)
    
        screenshot.save('screenshotvolumen.png')
    
        text2 = pytesseract.image_to_string(Image.open('screenshotvolumen.png'))
    
        print(text2)
    
        #----------------------------------------------------------------------------------------
    
        X1 = 1415
        Y1 = 898
        X2 = 1867
        Y2 = 947
    
        region = (X1, Y1, X2 - X1, Y2 - Y1)
        screenshot = pyautogui.screenshot(region=region)
    
        screenshot.save('screenshotcompetencia.png')
    
        text3 = pytesseract.image_to_string(Image.open('screenshotcompetencia.png'))
    
        print(text3)
    
        #----------------------------------------------------------------------------------------
    
        text1 = text1.replace(" ", "").replace("\n", "")
        text2 = text2.replace(" ", "").replace("\n", "")
        text3 = text3.replace(" ", "").replace("\n", "")
    
        if text1.isdigit() and len(text1) == 2 and text2.isdigit() and len(text2) == 2:
            texto_final = f"{Topic},{text1},{text2},{text3}"
            print(texto_final)
            WriteData(texto_final)
            break 
        else:
            print(f"Los valores de text1 y text2 no son números de 2 dígitos. Intento {_ + 1}")
            ControlChrome(Topic)
            time.sleep(5)



#GetData("ESP32")

for Topic in Topics:
    #print(Topic+VideoGame)
    print(Topic)
    time.sleep(10)

    #ControlChrome(Topic+VideoGame)
    ControlChrome(Topic)
    time.sleep(12)

    #GetData(Topic+VideoGame)
    GetData(Topic)


Graphics.Graficar(Archive)