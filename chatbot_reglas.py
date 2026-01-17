import time 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from funciones_agentes.obtener_clima import obtener_clima
from utils.sanitizar import sanitizar

# Configuración de Selenium
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# Inicialización del driver
driver = webdriver.Chrome(options=options)

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)
    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
    else:
        respuesta = funcion_agente(driver, user_input)
        print(f">>> {respuesta}")