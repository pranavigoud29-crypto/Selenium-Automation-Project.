
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_web_form_submission():

    driver = webdriver.Chrome()

    try:
        # Open demo website
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        # Enter text
        textbox = driver.find_element(By.NAME, "my-text")
        textbox.send_keys("Hello Selenium")

        # Click Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")
        submit_button.click()

        # Wait for success message
        message = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, "message")
        )

        # Verify result
        assert message.text == "Received!"

    finally:
        driver.quit()
