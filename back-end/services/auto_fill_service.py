from services.browser_service import BrowserService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import os
import time

class AutoFillService:
    def __init__(self):
        self.form_data = {}
        self.number_of_fill = 0

    def _prepare_form_data(self):
        print("Preparing form data for auto-fill...")
        for list in self.form_data['lists']:
            for question in list['questions']:
                for option in question['options']:
                    option['count'] = option['percent'] * self.number_of_fill / 100
        print("Form data prepared successfully.")

    def auto_fill(self, form_data, number_of_fill):
        self.form_data = form_data
        self.number_of_fill = number_of_fill
        self._prepare_form_data()
        try:
            while self.number_of_fill > 0:
                print("Config browser")
                browser_service = BrowserService()
                driver = browser_service.get_driver()
                print("Open browser: " + self.form_data['url'])
                driver.get(self.form_data['url'])
                time.sleep(3)
                print(f"Starting auto-fill for {self.number_of_fill} times...  " + time.strftime("%H:%M:%S", time.localtime()))
                retries = 0
                while retries < 3:
                    try:
                        self._fill_form(driver)
                        break
                    except WebDriverException as e:
                        print(f"Error during auto-fill: {str(e)}. Retrying...")
                        retries += 1
                        time.sleep(2)
                    except Exception as e:
                        print(f"An unexpected error occurred: {str(e)}. Retrying...")
                        retries += 1
                        time.sleep(2)
                
                time.sleep(3)
                driver.quit()
                os.system("taskkill /f /im chromedriver.exe")
                self.number_of_fill -= 1

        except Exception as e:
            print(f"An error occurred during auto-fill: {str(e)}")
        finally:
            print("Closing browser...")

    def _fill_form(self, driver):
        try:
            backup_data = self.form_data.copy()
            for list in backup_data['lists']:
                if len(list['questions']) == 0:
                    continue
                list_element = driver.find_element(By.XPATH, list['xpath'])
                question_elements = list_element.find_elements(By.XPATH, "./div[@role='listitem']")
                questions = list['questions']
                for question_element, question in zip(question_elements, questions):
                    time.sleep(0.5)
                    if len(questions) <= 0:
                        break
                    question['element'] = question_element
                    self._fill_question(question)
                button_element = list_element.find_element(By.XPATH, list['button']['xpath'])
                button_element.click()
                time.sleep(2)
                if list['button']['value'] == "Submit":
                    print('-----------------------------------------------')
                    print("Form submitted successfully.")
                    print('-----------------------------------------------')
                    self.form_data = backup_data
                    break
                else:
                    print('-----------------------------------------------')
                    print(f"Moving to next page")
                    print('-----------------------------------------------')
            driver.quit()
            time.sleep(2)
        except WebDriverException as e:
            print(f"Error filling form: {str(e)}")
            driver.quit()
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            driver.quit()
                
    def _fill_question(self, question):
        rows = question['rows']
        try:
            print('-----------------------------------------------')
            print(f"Question: {question['heading']}")
            print('-----------------------------------------------')
            for option in question['options']:
                time.sleep(0.5)
                if option['count'] < 1:
                    continue
                if question['type'] in ["Date", "Short answer", "Paragraph"]:
                    option_element = question['element'].find_element(By.XPATH, option['xpath'])
                    option_element.send_keys(option['value'])
                    time.sleep(0.3)
                    option['count'] -= 1
                    print(f"\t Option: {option['value']}")
                    break
                if question['type'] == "Checkboxes":
                    option_element = question['element'].find_element(By.XPATH, option['xpath'])
                    if self._is_enough_options(question, option):
                        if option['label'] == '__other_option__':
                            print(f"\t Option: {option['value']}")
                            option_element.send_keys(option['value'])
                            time.sleep(0.3)
                            option['count'] -= 1
                            break
                        else:
                            option_element.click()
                            time.sleep(0.3)
                            option['count'] -= 1
                            print(f"\t Option: {option['label']}")
                    else:
                        break
                    continue
                if question['type'] in ["Multiple choice", "Rating", "Linear scale"]:
                    option_element = question['element'].find_element(By.XPATH, option['xpath'])
                    if option['label'] == '__other_option__':
                        print(f"\t Option: {option['value']}")
                        option_element.send_keys(option['value'])
                        time.sleep(0.3)
                        option['count'] -= 1
                    else:
                        option_element.click()
                        time.sleep(0.3)
                        print(f"\t Option: {option['label']}")
                        option['count'] -= 1
                    break
                if question['type'] == "Drop-down":
                    presentation_element = question['element'].find_element(By.XPATH, '''.//div[@role="presentation"]''')
                    presentation_element.click()
                    time.sleep(0.5)
                    option_element = question['element'].find_element(By.XPATH, option['xpath'])
                    option_element.click()
                    time.sleep(0.3)
                    print(f"\t Option: {option['label']}")
                    option['count'] -= 1
                    break
                if question['type'] == "Multiple-choice grid":
                    for row in rows:
                        if option['label'].startswith(row):
                            option_element = question['element'].find_element(By.XPATH, option['xpath'])
                            option_element.click()
                            time.sleep(0.3)
                            option['count'] -= 1
                            rows = [r for r in rows if r != row]
                            print(f"\t Option: {option['label']}")
                            break
                    continue
                if question['type'] == "Tick box grid":
                    option_element = question['element'].find_element(By.XPATH, option['xpath'])
                    if self._is_enough_options(question, option):
                        option_element.click()
                        time.sleep(0.3)
                        option['count'] -= 1  
                        print(f"\t Option: {option['label']}")
                    else:
                        continue
        except WebDriverException as e:
            print(f"Error filling question: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred while filling question: {str(e)}")

    def _is_enough_options(self, question, option):
        if question['type'] == "Checkboxes":
            total_count = sum(option['count'] for option in question['options'])
            return total_count >= self.number_of_fill
        if question['type'] == "Tick box grid":
            option_row = option['label'].split(" - ")[0]
            total_count = sum(
                opt['count'] for opt in question['options'] 
                if opt['label'].startswith(option_row)
            )
            return total_count >= self.number_of_fill
        

        
                
