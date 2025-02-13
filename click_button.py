import time

from selenium.webdriver.common.by import By
from selenium import webdriver

server_url = "https://cnt-ad8f5d70-4128-441e-986a-96eee59bd48c.containerhub.tripleten-services.com"

driver = webdriver.Chrome()

driver.get(server_url)

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

# driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()
element1 = driver.find_element(By.XPATH, "//button[@title='Toggle fullscreen view']")
element2 = driver.find_element(By.XPATH, "//button[@aria-label='Toggle fullscreen view']")
element1.click()

print(element1, "\n", element2)

time.sleep(5)

driver.quit()