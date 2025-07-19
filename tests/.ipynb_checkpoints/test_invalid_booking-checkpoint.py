import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_setup import init_driver
from pages.booking_page import BookingPage

def test_empty_fields_should_not_submit():
    driver = init_driver()
    driver.get("https://automationintesting.online")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))

    booking = BookingPage(driver)
    booking.submit_contact_form("", "", "", "", "")

    time.sleep(2)
    assert "Thanks for getting in touch" not in driver.page_source
    driver.quit()

def test_invalid_email_should_not_submit():
    driver = init_driver()
    driver.get("https://automationintesting.online")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))

    booking = BookingPage(driver)
    booking.submit_contact_form(
        name="Your Name",
        email="invalid-email",  # missing '@'
        phone="9876543210",
        subject="Invalid Email Test",
        message="This email should fail."
    )

    time.sleep(2)
    assert "Thanks for getting in touch" not in driver.page_source
    driver.quit()
