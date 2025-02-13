import time
# Import selenium webdriver
from selenium import webdriver
# Import the UrbanRoutesPage class
from urban_routes_main_page import UrbanRoutesPage

# Instantiate the Chrome webdriver and get page to examine
driver = webdriver.Chrome()
driver.get('https://cnt-349292e0-73dd-474d-8be4-b10b13c2e9bc.containerhub.tripleten-services.com')

# Instantiate the UrbanRoutesPage
urban_routes_page = UrbanRoutesPage(driver)

# Set the from and to locations
urban_routes_page.enter_from_location("East")
urban_routes_page.enter_to_location("1300")

# Click the Custom button
urban_routes_page.click_custom_option()

# Click the Drive button
urban_routes_page.click_drive_icon()

time.sleep(5)

# Click the Book button
urban_routes_page.click_book_button()

time.sleep(5)

urban_routes_page.click_camping_card()

time.sleep(5)

expected_value = "Audi A3 Sedan"

try:
    assert expected_value in urban_routes_page.get_car_make()
    print(f"Actual camping car: {urban_routes_page.get_car_make()} make matches expected car make: {expected_value} ")
except:
    print(f"Actual camping car: {urban_routes_page.get_car_make()} does not make match expected car make: {expected_value} ")

driver.quit()