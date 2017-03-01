from selenium.webdriver.common.keys import Keys

class Framework:

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field_by_id(self, elem_id, input_value):
        elem = self.driver.find_element_by_id(elem_id)
        elem.clear()
        elem.send_keys(input_value)

    def press_enter(self, elem_id):
        elem = self.driver.find_element_by_id(elem_id)
        elem.send_keys(Keys.RETURN)

    def click_on_elem(self, elem_id):
        elem = self.driver.find_element_by_id(elem_id)
        elem.click()

