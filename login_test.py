from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page(driver):
    driver.get("https://saucedemo.com")
    wait = WebDriverWait(driver, 20)

    # Wait for username field
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    # Use JavaScript to set username
    username_field.clear()
    username_field.send_keys("standard_user")

    # Wait for password field
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    # Use JavaScript to set password
    password_field.clear()
    password_field.send_keys("secret_sauce")

    # Click login button
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # Wait for URL redirection
    wait.until(EC.url_contains("inventory"))  # confirms redirect to Products (inventory) page

    print("Login test passed! Redirected to:", driver.current_url)

# Run the test
driver = webdriver.Chrome()
test_login_page(driver)
driver.quit()