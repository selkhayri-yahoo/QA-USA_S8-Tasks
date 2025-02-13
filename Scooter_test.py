from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "https://cnt-a29f906b-ac44-411f-af64-c87d9e2b418d.containerhub.tripleten-services.com"
driver = webdriver.Chrome()
driver.get(URL)

time.sleep(2)

# Gets the From and To fields
input_from = driver.find_element(By.ID, "from")
input_to = driver.find_element(By.ID, "to")

input_from.send_keys("East")
input_to.send_keys("1300")

button_custom = driver.find_element(By.XPATH, "//div[text()='Custom']")
button_custom.click()

time.sleep(2)

scooter_img_src = "/static/media/scooter.cf9bb57e.svg"
scooter_div_xpath = "//img[@src='" + scooter_img_src + "']/.."

button_scooter = driver.find_element(By.XPATH, scooter_div_xpath)
button_scooter.click()

displayed_text = driver.find_element(By.CSS_SELECTOR, "div.results-container>div.results-text>div.text").text

try:
    assert displayed_text.startswith("Scooter")
    print("Scooter displayed")
except:
    print("Scooter not displayed ")

time.sleep(5)

driver.quit()