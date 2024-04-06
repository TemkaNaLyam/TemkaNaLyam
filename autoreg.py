import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class AutoregClass:

    def __init__(self):
        self.webdriver = webdriver.Chrome()

    @staticmethod
    def remove_everything_after_at(email):
        # Find the position of '@' character in the string
        at_position = email.find('@')
        # If '@' does not exist in the string, return the original string
        if at_position == -1:
            return email
        # Cut and return the string part from the beginning to the '@' position
        return email[:at_position]

    def create_account(self):
        input_data = input("Enter the details in 'address_hotmail|pass_hotmail|name|last_name' format: ")
        address_hotmail, pass_hotmail, name, last_name = input_data.split('|')
        delay = random.uniform(0.2, 1)
        self.webdriver.get("https://login.live.com")
        time.sleep(2)  # Wait for the page to load

        # Step 2: Click on "Create one!"
        self.webdriver.find_element(By.ID, "signup").click()
        time.sleep(2)

        # Steps 3 - 5: Enter hotmail and click next
        hotmail_field = WebDriverWait(self.webdriver, 10).until(
            ec.visibility_of_element_located((By.NAME, "MemberName")))
        for char in address_hotmail:
            hotmail_field.send_keys(char)
            time.sleep(delay)
        self.webdriver.find_element(By.ID, "iSignupAction").click()
        time.sleep(5)

        # Steps 6 - 8: Enter password and click next
        pass_hotmail_field = WebDriverWait(self.webdriver, 10).until(
            ec.visibility_of_element_located((By.NAME, "Password")))
        for char in pass_hotmail:
            pass_hotmail_field.send_keys(char)
            time.sleep(delay)
        self.webdriver.find_element(By.ID, "iSignupAction").click()
        time.sleep(5)

        # Steps 9 - 11: Enter first name, last name and click next
        name_field = self.webdriver.find_element(By.NAME, "FirstName")
        lastname_field = self.webdriver.find_element(By.NAME, "LastName")
        for char in name:
            name_field.send_keys(char)
            time.sleep(delay)
        time.sleep(5)
        for char in last_name:
            lastname_field.send_keys(char)
            time.sleep(delay)
        time.sleep(5)
        self.webdriver.find_element(By.ID, "iSignupAction").click()
        time.sleep(5)

        # Step 12: Enter birthdate and click next
        # IDs for the dropdown menu of day, month, year
        day_select = Select(self.webdriver.find_element(By.ID, "BirthDay"))
        month_select = Select(self.webdriver.find_element(By.ID, "BirthMonth"))
        year_select = self.webdriver.find_element(By.ID, "BirthYear")

        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"]
        days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                "20", "21", "22", "23", "24", "25", "26", "27", "28"]
        years = ["1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982",
                 "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995",
                 "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005"]
        # Select a value from the dropdown menu.
        self.webdriver.find_element(By.ID, "BirthMonth").click()
        time.sleep(5)
        month_select.select_by_visible_text(random.choice(month))
        time.sleep(5)
        self.webdriver.find_element(By.ID, "BirthDay").click()
        time.sleep(5)
        day_select.select_by_visible_text(random.choice(days))
        time.sleep(5)
        year_select.send_keys(random.choice(years))
        time.sleep(1)  # Wait for the dropdown to update
        self.webdriver.find_element(By.ID, "iSignupAction").click()
        input("Enter when done! ")
        time.sleep(9999999)


autoreg_instance = AutoregClass()

autoreg_instance.create_account()
