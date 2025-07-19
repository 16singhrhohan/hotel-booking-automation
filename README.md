# Hotel Booking Automation

This project demonstrates end-to-end automation testing of a real-world hotel booking platform using Selenium, Pytest, and Python. It focuses on simulating user actions such as submitting a booking form, validating input fields, and ensuring appropriate responses are handled effectively.

## Project Objectives

- Automate a functional guest booking flow
- Validate form behavior with invalid or missing data
- Use the Page Object Model (POM) for better test maintenance
- Structure tests for clarity, scalability, and real-life application

## Technologies Used

- Python 3.11+
- Selenium WebDriver
- Pytest
- Chrome WebDriver

## Folder Structure

hotel-booking-automation/
├── pages/
│ └── booking_page.py # Page Object for contact/booking form
├── tests/
│ ├── test_booking.py # Valid booking test
│ └── test_invalid_booking.py # Negative test scenarios
├── utils/
│ └── browser_setup.py # WebDriver initialization
├── .gitignore
├── requirements.txt
└── README.md


## How to Run the Project

1. Clone this repository: git clone https://github.com/16singhrhohan/hotel-booking-automation.git
cd hotel-booking-automation


2. (Optional) Set up a virtual environment:
python -m venv venv
venv\Scripts\activate


3. Install the required packages:
pip install -r requirements.txt


4. Execute the test suite:
pytest



## Test Scenarios Covered

### 1. Valid Booking Submission

- Fills out the booking form with valid details
- Verifies successful submission message on screen

### 2. Invalid Booking Scenarios

- Attempts to submit the form with all fields empty
- Attempts to submit the form with an improperly formatted email
- Ensures that no success message appears and the form is not submitted

## Additional Notes

- Tests are executed on [https://automationintesting.online](https://automationintesting.online)
- Test results are printed directly in the terminal
- Pytest and Selenium are used without any third-party frameworks to maintain simplicity
