# Import Selenium WebDriver
from selenium import webdriver

# Create a driver
driver = webdriver.Chrome()

# Open a page
driver.get('https://cnt-f05ceeab-c1ca-459b-8880-6e657ceae66b.containerhub.tripleten-services.com/')

assert "tripleten-services.com" in driver.current_url

driver.quit()
