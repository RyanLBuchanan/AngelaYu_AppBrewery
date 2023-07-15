from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\ChromeWebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# Get Python
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")

print(search_bar.get_attribute("placeholder"))



driver.quit()


# Get Amazon.com price
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/")
# values = driver.find_element(By.ID, "attach-base-product-price")
# print(values.get_attribute('value'))

"""PIECED TOGETHER FROM DR. ANGELA"S CODE"""
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# chrome_driver_path = "C:/Users/vreed/Documents/Development/chromedriver"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)
#
#
# driver.get("https://www.amazon.com/COMFEE-Electric-Pressure-Presets-Non-Stick/dp/B0BZS1D9R9/ref=sr_1_1_sspa?crid=C9UQK8EWN3CA&keywords=instant+pot+duo+evo&qid=1689448240&sprefix=instant+pot+duo+evo%2Caps%2C140&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
# # driver.close()
# price_element = driver.find_element("css selector", "#priceblock_ourprice")
#
#
#
# price = price_element.text
#
# print(price)
#
# driver.quit()