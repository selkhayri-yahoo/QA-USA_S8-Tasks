import time
# Import selenium webdriver
from selenium import webdriver
# Import the UrbanRoutesPage class
from urban_routes_main_page import UrbanRoutesPage

delay = 4

# Instantiate the Chrome webdriver and get page to examine
driver = webdriver.Chrome()
driver.get('https://cnt-0569e1ad-c33d-4b23-a70f-2beabb6cccdd.containerhub.tripleten-services.com')

# Instantiate the UrbanRoutesPage
urban_routes_page = UrbanRoutesPage(driver)

# Set the from and to locations
urban_routes_page.enter_from_location("East")
urban_routes_page.enter_to_location("1300")

# Click the Custom button
urban_routes_page.click_custom_option()

# Click the Drive button
urban_routes_page.click_drive_icon()

time.sleep(delay)

# Click the Book button
urban_routes_page.click_book_button()

time.sleep(delay)

urban_routes_page.click_camping_card()

time.sleep(delay)

urban_routes_page.click_licence_add_button()

time.sleep(delay)

urban_routes_page.set_licence_first_name("Rex")
urban_routes_page.set_licence_last_name("Tillerson")
urban_routes_page.set_licence_birth_date('24.04.1898')
urban_routes_page.set_licence_licence_number("01 01 123456")

time.sleep(delay)

urban_routes_page.click_add_button()

time.sleep(delay)

expected_text = "Thank you!"
actual_text = urban_routes_page.get_popup_window_text()

try:
    assert expected_text in actual_text
    print("Thank you!")
except:
    print("No. thank you!")


driver.quit()
