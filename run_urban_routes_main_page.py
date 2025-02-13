# Import selenium webdriver
from selenium import webdriver
# Import the UrbanRoutesPage class
from urban_routes_main_page import UrbanRoutesPage

# Instantiate the Chrome webdriver and get page to examine
driver = webdriver.Chrome()
driver.get('https://cnt-5d2a240b-567a-4bd2-81b6-38bda81db5b9.containerhub.tripleten-services.com')

# Instantiate the UrbanRoutesPage
urban_routes_page = UrbanRoutesPage(driver)

# Set the from and to locations
urban_routes_page.enter_from_location("East")
urban_routes_page.enter_to_location("1300")

# Click the Custom button
urban_routes_page.click_custom_option()

# Click the bike icon
urban_routes_page.click_bike_icon()

# Verify that the text value 'Bike' is displayed in the selected transportation mode
try:
    assert "Bike" in urban_routes_page.get_bike_text()
    print("Bike text is displayed")
except:
    print("Bike text is not displayed")

driver.quit()
