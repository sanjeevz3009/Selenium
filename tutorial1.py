from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element(By.NAME, "s").send_keys("test" + Keys.ENTER)

wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

main = wait.until(EC.presence_of_element_located((By.ID, "main")))
print(main.text)


driver.quit()