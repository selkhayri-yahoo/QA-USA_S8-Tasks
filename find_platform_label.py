import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() # create Chrome driver

driver.get('https://cnt-24fbf32f-d55e-46a1-a0ae-7108c778de3a.containerhub.tripleten-services.com/')  #navigate to the url

# Task 1
# ======
# Find the logo element using its CSS Selector
element = driver.find_element(By.CLASS_NAME, 'logo-disclaimer');

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Print the found element to the console
print("Task 1")
print(element)

# Task 2
# ======
elements = driver.find_elements(By.CLASS_NAME, 'dst-picker-marker')

print("\nTask 2")
try:
    assert(len(elements) > 1)
    print("More than one element found")
except Exception as e:
    print(len(elements))

# Task 3
# ======

print("\nTask 3")
element_from = driver.find_element(By.ID, "from")
placeholder_from = "East 2nd Street, 601"

try:
    assert(element_from.get_attribute("placeholder") == placeholder_from)
    print(f"Placeholder for 'from' field is '{placeholder_from}'")
except:
    print(element_from.get_attribute("placeholder"))
    print(f"Placeholder for 'from' field is not '{placeholder_from}'")

element_to = driver.find_element(By.ID, "to")
placeholder_to = "1300 1st St"

try:
    assert(element_to.get_attribute("placeholder") == placeholder_to)
    print(f"Placeholder for 'to' field is '{placeholder_to}'")
except:
    print(element_to.get_attribute("placeholder"))
    print(f"Placeholder for 'to' field is not '{placeholder_to}'")

driver.quit()
