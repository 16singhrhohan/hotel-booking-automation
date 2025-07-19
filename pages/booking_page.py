from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "name")
        self.email_input = (By.ID, "email")
        self.phone_input = (By.ID, "phone")
        self.subject_input = (By.ID, "subject")
        self.description_input = (By.ID, "description")
        self.submit_btn = (By.XPATH, "//button[contains(text(),'Submit')]")

    def submit_contact_form(self, name, email, phone, subject, message):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.subject_input).send_keys(subject)
        self.driver.find_element(*self.description_input).send_keys(message)

    # Scroll into view before clicking
        submit_button = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)
