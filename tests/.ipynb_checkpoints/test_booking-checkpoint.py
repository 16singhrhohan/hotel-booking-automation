import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_setup import init_driver
from pages.booking_page import BookingPage

def test_guest_contact_form_submission():
    driver = init_driver()
    driver.get("https://automationintesting.online")

    # Wait for the form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))

    booking = BookingPage(driver)
    booking.submit_contact_form(
        name="Your Name",
        email="yourname@example.com",
        phone="98765432100",
        subject="Test Booking",
        message="I'd like to book a room for automation testing."
    )

    time.sleep(3)
    assert "Thanks for getting in touch" in driver.page_source
    driver.quit()
