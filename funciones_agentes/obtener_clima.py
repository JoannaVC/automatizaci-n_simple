from selenium.webdriver.common.by import By
import time

def obtener_clima(driver, consulta):
    partes = consulta.split(maxsplit=1)

    if len(partes) < 2:
        return "Debes escribir por ejemplo: clima Madrid"

    lugar = partes[1]
    driver.get(f"https://www.google.com/search?q=clima+{lugar}")
    time.sleep(2)

    # Variables inicializadas
    ciudad = ""
    temperatura = ""
    estado = ""

    try:
        # Obtener el nombre completo de la ciudad
        ciudad = driver.find_element(By.CSS_SELECTOR, "span[class='ilUpNd d6Ejqe aSRlid']").text

        # Obtener la temperatura
        temperatura = driver.find_element(By.CSS_SELECTOR, "div[class='ilUpNd nB7Pqb aSRlid']").text

        # Obtener el estado del clima
        estado = driver.find_element(By.CSS_SELECTOR, "div[class='ilUpNd d6Ejqe aSRlid']").text
        
    except Exception as e:
        print(f"DEBUG - Excepción capturada: {e}")

    # Return FUERA del try-except
    if ciudad and temperatura and estado:
        return f"{ciudad}: {temperatura}, {estado}"
    else:
        return "No se pudo obtener el clima en este momento."