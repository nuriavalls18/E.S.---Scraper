
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import random

#INSTANCE DRIVER

def configure_driver(settings, user_agent):

    options = webdriver.ChromeOptions()

    #Options to try to fool the site we are a normal browser.
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", {
        "download.default_directory": settings.files_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    options.add_argument('--incognito')
    options.add_argument("start-maximized") 
    options.add_argument('user-agent={user_agent}') 
    options.add_argument('disable-blink-features') 
    options.add_argument('disable-blink-features=AutomationControlled') 
    
    driver = webdriver.Chrome(options=options, executable_path=settings.chromedriver_path)

    #Overwrite the webdriver property
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    
    driver.execute_cdp_cmd("Network.enable", {})

    #Overwrite the User-Agent header
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": user_agent}})

    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    return driver


#SOLVENTAR CAPTCHA
def solve_wait_recaptcha(driver):

    ###### Move to reCAPTCHA Iframe
    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")
    ))

    check_selector = "span.recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox"

    captcha_check = driver.find_element_by_css_selector(
        check_selector
    )

    ###### Random delay before hover & click the checkbox
    sleep(random.uniform(3, 6))
    ActionChains(driver).move_to_element(captcha_check).perform()

    ###### Hover it
    sleep(random.uniform(0.5, 1))
    hov = ActionChains(driver).move_to_element(captcha_check).perform()

    ######  Random delay before click the checkbox
    sleep(random.uniform(0.5, 1))
    driver.execute_script("arguments[0].click()", captcha_check)

    ######  Wait for recaptcha to be in solved state
    elem = None
    while elem is None:
        try:
            elem = driver.find_element_by_class_name("recaptcha-checkbox-checked")
        except:
            pass
        sleep(5)