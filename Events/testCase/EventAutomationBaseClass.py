import time
import json
from selenium.common import exceptions
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from passcode import password
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pymysql
import csv

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


class EventAutomation:

    def __init__(self):
        # self.test_url = test_url
        self.option = options
        self.driver = Chrome(service=Service(), options=self.option)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.exceptions = exceptions

    def logs(self):
        return
        logs = self.driver.get_log('performance')
        # res_dict = dict(logs)
        # data = json.loads(logs)
        # print(log)
        perf = {'e': []}
        for i, en in enumerate(logs):
            # print(en)
            if 'event_name' in str(en):
                j = json.loads(en['message'])
                k = j["message"]['params']['request']['postData']
                print(k.split('&'))

    def finds_elements(self, xpath, key=''):
        try:
            if key != '':
                self.driver.find_element(By.XPATH, xpath).send_keys(key)
                self.logs()
                time.sleep(3)
            else:
                try:
                    self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
                    self.logs()
                except (BaseException, NoSuchElementException, ElementClickInterceptedException):
                    self.element_hover(xpath)
                    self.driver.execute_script(f"window.scrollBy(0, {500});")
                    self.logs()
                    self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
                    self.logs()
                time.sleep(5)
        except (BaseException, NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            print("Element Not Clicked .........", xpath)
            pass

    def request_func(self, url):
        self.driver.get(url)
        time.sleep(3)

    def mobile_screen_request(self, url):
        try:
            self.driver.set_window_size(360, 640)
            self.driver.get(url)
            time.sleep(3)
        except (BaseException, Exception) as ex:
            print("Mobile View request failed .............", ex)
            pass

    def find_multi_elements(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def switch_to_frame(self, xpath):
        frame = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.switch_to.frame(frame)
        time.sleep(3)

    def element_hover(self, xpath, drag=False):
        try:
            pop_up_element1 = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(pop_up_element1)
            actions.perform()
            if drag:
                actions.drag_and_drop_by_offset(pop_up_element1, -100,
                                                -200)  # Move the element by 100 pixels horizontally and vertically
                # Execute the action chain
                actions.perform()
        except (BaseException, Exception) as ex:
            print(ex)
            pass

    def tagmanager_popup_move(self):
        self.switch_to_frame("//iframe[@class='__TAG_ASSISTANT_BADGE']")
        self.finds_elements('/html/body/debug-badge/frame-auto-resize/div/div/div[2]/i')
        self.element_hover('/html/body/debug-badge/frame-auto-resize/div/div[1]/div[1]/i', drag=True)
        self.driver.switch_to.default_content()

    def robot_click(self, xpath):
        self.switch_to_frame(xpath)
        self.finds_elements('//*[@id="recaptcha-anchor"]/div[1]')
        self.driver.switch_to.default_content()

    def chat_box_close(self):
        try:
            self.switch_to_frame('//*[@id="webWidget"]')
            self.finds_elements("//button[@aria-label='Minimize widget']")
            self.driver.switch_to.default_content()
        except TimeoutException:
            print("chatbox time out error")
            pass
        except ElementClickInterceptedException:
            print('Retry chat box closing')
            self.chat_box_close()

    def trust_pilot_click(self, xpath):
        # self.element_hover(By.XPATH, xpath)
        # trust_pilot_frame = xpath
        # self.switch_to_frame(trust_pilot_frame)
        # trust_pilot_click = '//*[@id="tp-widget-wrapper"]'
        # self.finds_elements(xpath)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        try:
            # Wait for element to be clickable
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

            # Perform hover action
            ActionChains(self.driver).move_to_element(element).perform()

            # Click on the element
            element.click()

            # Switch to the new window
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Close the new window
            self.driver.close()

            # Switch back to the original window
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except NoSuchElementException as e:
            print("Element not found:", e)
        except TimeoutException as e:
            print("Timeout waiting for element to be clickable:", e)

    def send_key(self, key):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(key)
        except exceptions as ex:
            print(ex)
        pass


    def save_output(self, filename='output'):
        self.driver.switch_to.window(self.driver.window_handles[1])
        file = open(f'{filename}.txt', 'a+', encoding='utf-8')
        fire_tags = self.driver.find_elements(By.XPATH, '//*[@id="gtm-debug-id-has-tags"]/div[1]/div/div[1]')
        fire_tags_number = self.driver.find_elements(By.XPATH, '//*[@id="gtm-debug-id-has-tags"]/div[1]/div/div[2]')
        for tags, number in zip(fire_tags, fire_tags_number):
            print(tags.text, ">>>>>>>>>", number.text, ">>>>>>>>>>>", datetime.now())
            file.write('\n' + tags.text + "\t" + number.text + "\t" + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        file.close()

    def driver_quit(self):
        self.driver.quit()
        # self.driver.close()

    def print_visitor_id(self):
        time.sleep(5)
        visitor_id = self.driver.find_element(By.XPATH, '//*[@id="rpt_com_visitor_id"]').get_attribute('value')

        print("Visitor ID >>>>>>>>>>>>> ", visitor_id)
        return visitor_id

    def report_genrate(self, visitor_id, con, val1, val2, eve_id):
        conn = pymysql.connect(host="development-uk.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
                               user="raptoradmin",
                               password="Raptorpwa2020",
                               database='rpt_events'
                               )

        cursor = conn.cursor()

        visitor_id = visitor_id
        print(visitor_id)
        condition = con
        value1 = val1
        value2 = val2
        eve_id = eve_id
        cursor.execute("SELECT * FROM `raptor_browser_fingerprinting_transaction_2024_04_05` WHERE visitor_id = %s",
                       (visitor_id,))
        results = cursor.fetchall()
        a = 0
        for x in results:
            a += 1
            print(a)
            if x[-2] == eve_id:
                if condition == 'BPN' and value1 == '' and value2 == '':
                    if (x[9] != '' and x[11] != '') or x[10] != '':
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                if condition == 'BP' and value1 == '' and value2 == '':
                    if x[9] != '' or x[10] != '':
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()

                if condition == 'BPN' and value1 != '' and value2 == '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[11] != '' and x[5] != '') or x[10] != '':
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                if condition == '' and value1 != '' and value2 == '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[5] != ''):
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                if condition == 'BP' and value1 != '' and value2 == '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[5] != ''):
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                if condition == 'BPN' and value1 != '' and value2 != '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[11] != '' and x[5] != '' and x[6] != ''):
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                if condition == 'BP' and value1 != '' and value2 != '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[5] != '' and x[6] != ''):
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()

                if condition == 'BPN' and value1 == '' and value2 != '':
                    print("yesssssssssss", x[5])
                    if (x[9] != '' and x[11] != '' and x[6] != ''):
                        print("Working")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Working',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()
                    else:
                        print("Error")
                        cursor.execute(
                            "UPDATE rpt_automation_qa.event_file SET status_mark = 'Error',base_origin_url = '" + x[
                                9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[
                                5] + "',value2='" + x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                        conn.commit()
                        conn.close()

            elif x[-2] == '90':
                print("page view event")
            elif x[-2] == '90' and a == 1:
                print("status 0")
                cursor.execute(
                    "UPDATE rpt_automation_qa.event_file SET status_mark = 'Event not trigger',base_origin_url = '" + x[
                        9] + "',prev_url = '" + x[10] + "',next_url = '" + x[11] + "',value1='" + x[5] + "',value2='" +
                    x[6] + "' WHERE Event_ID ='" + 'eve_' + eve_id + "' ")
                conn.commit()
                conn.close()
            else:
                print("Extra event trigger")

            # if

        # current_date = datetime.now().strftime("%Y-%m-%d")

        # csv_filename = f"report_{current_date}.csv"

        # with open(csv_filename, 'w', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)

        #     csv_writer.writerow([i[0] for i in cursor.description])

        #     csv_writer.writerows(results)

        # print(f"Data saved to {csv_filename}")

        # cursor.close()
        # conn.close()