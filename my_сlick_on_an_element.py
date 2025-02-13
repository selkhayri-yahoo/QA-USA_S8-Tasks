import time

from selenium.webdriver.common.by import By
from selenium import webdriver

server_url = "https://cnt-dcae0ea6-4b25-4db8-a474-7fca81c90d83.containerhub.tripleten-services.com"

driver = webdriver.Chrome()

driver.get(server_url)

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

element1 = driver.find_element(By.XPATH, "//div/input[@id='from']/../button[@class='close-button input-close-button']")
print(f"from cross element: {element1}")

element1.click()

time.sleep(15)

driver.quit()
