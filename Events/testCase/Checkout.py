import time
import pyautogui
from selenium.common import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from EventAutomationBaseClass import EventAutomation
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


class Checkout(EventAutomation):

    def __init__(self):
        super().__init__()

    def eve_200(self, url):
        self.request_func(url)
        # Add To Cart
        add_to_cart = "//*[@id='eve_38']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        # Live Chat
        self.chat_box_close()
        # CheckOut Option
        click_On_Checkout = "(//*[@id='eve_294'])"
        self.finds_elements(click_On_Checkout)
        # Shipping Information

        # Email Adress
        email_Address = "(//*[@id='customer-email'])"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # FirstName
        first_Name = "(//*[@id='Q4IMHXH'])"
        self.finds_elements(first_Name, 'xyz')
        # lastName
        last_Name = "(//*[@id='Q9QAKNJ'])"
        self.finds_elements(last_Name, 'kumar')
        # CompanyName
        company_Name = "(//*[@id='KA9R6BD'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@id='PBXV0M4'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@id='NPE9FI7'])"
        self.finds_elements(city_Name, 'abc')
        # Country_Name
        country_Name = "(//*[@id='GWREGT5'])"
        self.finds_elements(city_Name, 'abc')
        # PostalCode
        postal_Code = "(//*[@id='FQG53BW'])"
        self.finds_elements(postal_Code, 123456)
        # Phone_Number
        phone_number = "(//*[@id='NETQR7E'])"
        self.finds_elements(phone_number, 1234567890)
        # ContinueButton
        click_On_continue = "(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)

        self.print_visitor_id()
        con = "BPN"
        val1 = 'Email'
        val2 = ''
        eve_id = '200'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)

    def eve_202(self, url):
        self.request_func(url)
        # Add To Cart
        add_to_cart = "//*[@id='eve_38']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        # Live Chat
        self.chat_box_close()
        # CheckOut Option
        click_On_Checkout = "(//*[@id='eve_294'])"
        self.finds_elements(click_On_Checkout)
        # Shipping Information
        # Email Adress
        email_Address = "(//*[@id='customer-email'])"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # FirstName
        first_Name = "(//*[@id='Q4IMHXH'])"
        self.finds_elements(first_Name, 'xyz')
        # lastName
        last_Name = "(//*[@id='Q9QAKNJ'])"
        self.finds_elements(last_Name, 'kumar')
        # CompanyName
        company_Name = "(//*[@id='KA9R6BD'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@id='PBXV0M4'])"
        self.finds_elements(address, 'UK')
        # City_Name
        city_Name = "(//*[@id='NPE9FI7'])"
        self.finds_elements(city_Name, 'abc')
        # Country_Name
        country_Name = "(//*[@id='GWREGT5'])"
        self.finds_elements(city_Name, 'abc')
        # PostalCode
        postal_Code = "(//*[@id='FQG53BW'])"
        self.finds_elements(postal_Code, 123456)
        # Phone_Number
        phone_number = "(//*[@id='NETQR7E'])"
        self.finds_elements(phone_number, 1234567890)
        # ContinueButton
        click_On_continue = "(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        # Express_Option
        express_Clicking = "(//*[@class='row shipping_info_label rpt-radio'])"
        self.finds_elements(express_Clicking)
        # Process_Payment
        self.print_visitor_id()
        con = "BP"
        val1 = '#Freight Amount'
        val2 = ''
        eve_id = '201'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)


def run_program():
    program_dict = {

        'eve_200': 'eve_200("https://stage.raptorsupplies.com/pd/morse-drum/91")',
        'eve_202': 'eve_200("https://stage.raptorsupplies.com/pd/morse-drum/91")',

    }

    testing = Checkout()
    # keys = list(program_dict.keys())
    # start_index = 19
    # for i, key in enumerate(keys[start_index:], start_index):
    #     print(i, ">>>>>>>>>>> Working Template >>>>>>>>>", key), eval(f"testing.{program_dict[key]}")
    for key in keys_to_run:
        if key in program_dict:
            print(">>>>>>>>>>> Working Template >>>>>>>>>", key)
            eval(f"testing.{program_dict[key]}")
    # eval(f"testing.{program_dict['eve_192']}")
    testing.driver_quit()


keys_to_run = ['eve_179']

run_program()