from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/vreed/Documents/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://www.amazon.com")
# driver.close()
driver.quit()