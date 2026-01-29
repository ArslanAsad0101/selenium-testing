import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Open Chrome browser with matching ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open login page
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click login button
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Wait for result
time.sleep(2)

# Verify login success
message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("✅ Login Test Passed")
else:
    print("❌ Login Test Failed")

# Close browser
time.sleep(2)
driver.quit()
