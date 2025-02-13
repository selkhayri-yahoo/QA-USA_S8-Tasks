import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

server_url = "https://cnt-973d0748-9f73-4d75-a50a-9c00bda19eb0.containerhub.tripleten-services.com"

driver = webdriver.Chrome()

driver.get(server_url)

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "from")))
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "to")))

input_from = driver.find_element(By.ID, 'from')
input_to = driver.find_element(By.ID, 'to')

input_from.send_keys("East")
input_to.send_keys("1300")

time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Call a taxi']").click()

WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "comment")))

msg = "Don't be late!"

driver.find_element(By.ID, "comment").send_keys(msg)

assert driver.find_element(By.ID, "comment").get_attribute("value") == msg

time.sleep(10)

driver.quit()
