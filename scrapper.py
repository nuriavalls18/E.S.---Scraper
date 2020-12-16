import os
import random
import re
from datetime import datetime
from time import sleep
from common import *

from selenium.webdriver import ActionChains

import settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import bleach
import codecs

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
             " Chrome/78.0.3904.97 Safari/537.36"

previus_page_count = 0

browser = configure_driver(settings, user_agent)

# Ir a la URL en cuestión url inicio de settings
browser.get(settings.url_inicio)
print ("Entra") ###AporteNuria: print("Loading url automatically.")
browser.find_element_by_id("numcontacontrato").send_keys(settings.num_contrato)
print ("Valor de contrato asignado") ###AporteNuria: print("'Numero da conta contrato' assigned.")
solve_wait_recaptcha(browser)
print ("Recaptcha resuelto") ###AporteNuria: print("Sucessfully ReCaptcha solved.")
browser.switch_to.default_content()
print ("Move out of any frame") ###AporteNuria: print("Moving out of any frame.")
browser.implicitly_wait(5)
print ("Esperamos") ###AporteNuria: print("Just a few seconds.")
browser.find_element_by_id("cmdEnviar").click()
print ("Click en entrar")  ###AporteNuria: print("Clicking automatically.")

	
	