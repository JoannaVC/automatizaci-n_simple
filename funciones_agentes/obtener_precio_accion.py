# importar la función By de selenium.webdriver.common.by,
# misma que permite seleccionar elementos de una página web
# por medio de selectores CSS.
from selenium.webdriver.common.by import By
import time

# Función para obtener el precio de una acción
# Parámetros:
# - driver: objeto de Selenium WebDriver
# - consulta: cadena de texto que contiene la consulta del usuario
def obtener_precio_accion(driver, consulta):
    partes = consulta.split(maxsplit=1)

    if len(partes) < 2:
        return "Debes escribir por ejemplo: accion Tesla"

    empresa_input = partes[1]
    driver.get(f"https://www.google.com/search?q=precio+acción+{empresa_input}")
    time.sleep(2)

    # Variables inicializadas
    empresa = ""
    precio = ""
    divisa = ""
    ticker = ""

    try:
        # Obtener el nombre completo de la empresa
        empresa = driver.find_element(By.CSS_SELECTOR, "span[class='ilUpNd d6Ejqe aSRlid']").text

        # Obtener el precio de la acción
        precio = driver.find_element(By.CSS_SELECTOR, "div[class='ilUpNd nB7Pqb aSRlid']").text

        # Obtener la divisa de la acción
        divisa = driver.find_element(By.CSS_SELECTOR, "div[class='ilUpNd An9Aqc aSRlid']").text
        partes = divisa.split("·")

        for parte in partes:
            if "Moneda en" in parte:
                divisa = parte.replace("Moneda en", "").strip()


        # Obtener el ticker de la acción
        ticker = driver.find_element(By.CSS_SELECTOR, "div[class='ilUpNd d6Ejqe aSRlid']").text
        
    except Exception as e:
        print(f"DEBUG - Excepción capturada: {e}")

    # Return FUERA del try-except
    if empresa and precio:
        return f"{empresa} ({ticker}): {precio} {divisa}"
    else:
        return "No se pudo obtener el precio de la acción en este momento."