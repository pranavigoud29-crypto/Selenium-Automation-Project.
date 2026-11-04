
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    # Open demo website
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Find text box and enter text
    textbox = driver.find_element(By.NAME, "my-text")
    textbox.send_keys("Hello Selenium")

    # Find Submit button using its tag
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()

    # Wait until the result appears
    message = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "message")
    )

    # Check result
    if message.text == "Received!":
        print("TEST PASSED: Form submitted successfully!")
    else:
        print("TEST FAILED")

finally:
    driver.quit()
