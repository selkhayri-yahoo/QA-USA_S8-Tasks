from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "https://cnt-973d0748-9f73-4d75-a50a-9c00bda19eb0.containerhub.tripleten-services.com"
driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get(URL)

time.sleep(2)

# Gets the element's text
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Assert that the text of the discalimer variable is "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()