import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

server_url = "https://cnt-657fe76b-56e2-4a78-b3a4-e482b23ea038.containerhub.tripleten-services.com"

driver = webdriver.Chrome()

driver.get(server_url)

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

urban_routes_page = UrbanRoutesPage(driver)

urban_routes_page.enter_from_location("East")
urban_routes_page.enter_to_location("1300")

time.sleep(2)

urban_routes_page.click_custom_option()

urban_routes_page.click_scooter_icon()

expected_text = "Duration"

actual_text = urban_routes_page.get_duration_text()
print(f"actual_text: {actual_text}")

assert expected_text in actual_text, f"{expected_text} not in {actual_text}"

driver.quit()

