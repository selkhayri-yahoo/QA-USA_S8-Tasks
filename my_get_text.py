from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "https://cnt-973d0748-9f73-4d75-a50a-9c00bda19eb0.containerhub.tripleten-services.com"
driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get(URL)

time.sleep(2)

input_from = driver.find_element(By.ID, "from")
input_to = driver.find_element(By.ID, "to")

input_from.send_keys("East")
input_to.send_keys("1300")

time.sleep(3)

default = driver.find_element(By.CSS_SELECTOR, "div[class='mode active']").text

# Assert that the text of the default variable is "Fastest"
try:
    assert default == "Fastest"
    print("Fastest")
except:
    print("Not Fastest")



driver.quit()