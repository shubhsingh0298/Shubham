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



    def eve_207(self, url):
        self.request_func(url)
        # Add To Cart
        add_to_cart = "//*[@class='rpt_btn rpt_white_btn cart-btn']"
        self.element_hover(add_to_cart)
        self.finds_elements(add_to_cart)
        # Live Chat
        self.chat_box_close()
        # CheckOut Option
        click_On_Checkout = "(//*[@id='eve_294'])"
        self.finds_elements(click_On_Checkout)
        # Shipping Information
        # Email Id
        email_Address = "(//*[@id='customer-email'])"
        self.finds_elements(email_Address, 'shubham@raptorsupplies.co.uk')
        # First Name
        first_Name = "(//*[@name='firstname'])"
        self.finds_elements(first_Name, 'Automation')
        # Last Name
        last_Name = "(//*[@name='lastname'])"
        self.finds_elements(last_Name, 'Testing')
        # Company Name
        company_Name = "(//*[@name='company'])"
        self.finds_elements(company_Name, 'Raptor')
        # Address
        address = "(//*[@name='street[0]'])"
        self.finds_elements(address, 'India')
        # City_Name
        city_Name = "(//*[@name='city'])"
        self.finds_elements(city_Name, 'abc')
        # Country dropdown
        country_Dropdown = "(//*[@name='country_id'])"
        self.finds_elements(country_Dropdown, 'India')
        # State dropdown
        # state_Or_Province="(//*[@name='region_id'])"
        # self.finds_elements(state_Or_Province,'Goa')
        # Postal code
        postal_Code = "(//*[@name='postcode'])"
        self.finds_elements(postal_Code, 123456)
        # Contact number
        phone_number = "(//*[@name='telephone'])"
        self.finds_elements(phone_number, 1234567890)
        # Click on continue or submit
        click_On_continue = "(//*[@id='eve_200'])"
        self.finds_elements(click_On_continue)
        # Express 5 to 7 days
        express_Clicking = "(//*[@id='s_method_matrixrate_matrixrate_6175'])"
        self.finds_elements(express_Clicking)
        # Process_Payment
        click_On_Payment = "(//*[@id='proceed_payment'])"
        self.finds_elements(click_On_Payment)
        # select payment mode
        net_payment = "(//*[@id='tooltip_banktransfer'][1])"
        self.finds_elements(net_payment)
        purschase_no = "(//*[@id='eve_209'])"
        self.finds_elements(purschase_no, 6547685)
        net_payment_Checkbox = "(//*[@id='net_check'])"
        self.finds_elements(net_payment_Checkbox)
        # Click on Place order
        # place_Order="(//*[@id='net_real'])"
        # self.finds_elements(place_Order)
        print("Successfully done!!!!!")

        self.print_visitor_id()
        con = "BPN"
        val1 = 'Subtotal with Currency'
        val2 = ''
        eve_id = '207'
        self.report_genrate(self.print_visitor_id(), con, val1, val2, eve_id)


def run_program():
    program_dict = {

        'eve_200': 'eve_200("https://www.raptorsupplies.com/pd/morse-drum/91")',
        'eve_207': 'eve_207("https://www.raptorsupplies.com/pd/morse-drum/91")',

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


keys_to_run = ['eve_207']

run_program()
