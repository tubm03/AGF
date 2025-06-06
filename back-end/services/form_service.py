import time
from Model.option import Option
from selenium.webdriver.common.by import By
from Model.list_question import ListQuestion
from Model.question import Question
from services.ai_service import AIService
from selenium.common.exceptions import WebDriverException
from Model.button import Button
from Model.form import Form
class FormService:
    def __init__(self, form):
        self.driver = None
        self.form = form

    def _restart_driver(self):
        """Restart the browser driver"""
        try:
            self.driver.quit()
        except:
            pass
        self.driver.get(self.form.url)

    def add_options(self, question):
        if question.type in self.options:
            self.options[question.type](question)

    def add_option_multiple_choice(self, question, options):
        for op in options:
            xpath = f'''.//div[@role="radio" and (contains(@data-value, "{op}") or contains(@data-value, "{op.lower().strip(":")}"))]'''
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            option.label = op
            question.options.append(option)
            if "other" in op.lower():
                try:
                    xpath = ".//input[@type='text']"
                    input_element = question.element.find_element(By.XPATH, xpath)
                    option = Option(input_element)
                    option.xpath = xpath
                    option.label = "__other_option__"
                    input_element.clear()  # Clear any existing value
                    input_element.send_keys('Test')
                    time.sleep(1)
                    question.options.append(option)
                except WebDriverException as e:
                    return
            
    def add_option_checkboxes(self, question, options):
        for op in options:
            xpath = f'''.//div[@role="checkbox" and (contains(@data-answer-value, "{op}") or contains(@data-answer-value, "{op.lower().strip(":")}"))]'''
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            option.label = op
            question.options.append(option)
            if "other" in op.lower():
                try:
                    xpath = ".//input[@type='text']"
                    input_element = question.element.find_element(By.XPATH, xpath)
                    option = Option(input_element)
                    option.xpath = xpath
                    option.label = "__other_option__"
                    input_element.clear()  # Clear any existing value
                    input_element.send_keys('Test')
                    time.sleep(1)
                    question.options.append(option)
                except WebDriverException as e:
                    return
            
    def add_option_dropdown(self, question, options):
        time.sleep(1)
        presentation_element = question.element.find_element(By.XPATH, '''.//div[@role="presentation"]''')
        for op in options:
            presentation_element.click()
            time.sleep(1)
            xpath = f'''.//div[@role="option" and contains(@data-value, "{op}")]'''
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            option.label = op
            question.options.append(option)

    def add_option_linear_scale_or_rating(self, question, options):
        for op in options:
            xpath = f'''.//div[@role="radio" and contains(@aria-label, "{op}")]'''
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            option.label = op
            question.options.append(option)

    def add_option_multiple_choice_grid(self, question, rows, columns):
        for row in rows:
            for column in columns:
                xpath = f'''.//div[@role="radio" and contains(@aria-label, "{row}") and contains(@aria-label, "{column}")]'''
                option = Option(question.element.find_element(By.XPATH, xpath))
                option.xpath = xpath
                time.sleep(0.5)
                option.element.click()
                option.label = row + ' - ' + column
                question.options.append(option)

    def add_option_tick_box_grid(self, question, rows, columns):
        for row in rows:
            for column in columns:
                xpath = f'''.//div[@role="checkbox" and contains(@aria-label, "{row}") and contains(@aria-label, "{column}")]'''
                option = Option(question.element.find_element(By.XPATH, xpath))
                option.xpath = xpath
                time.sleep(0.5)
                option.element.click()
                option.label = row + ' - ' + column
                question.options.append(option)

    def add_option_date(self, question):
        xpath = ".//input[@type='date']"
        option = Option(question.element.find_element(By.XPATH, xpath))
        option.xpath = xpath
        option.element.clear()  # Clear any existing value
        time.sleep(0.5)
        option.element.send_keys('12/11/2003')
        option.label = 'input date'
        question.options.append(option)

    def add_option_time(self, question):
        xpath_hour = ".//input[@type='text' and @max='12']"
        xpath_minute = ".//input[@type='text' and @max='59']"
        xpath_presentation = ".//div[@role='presentation']"

        hour_element = question.element.find_element(By.XPATH, xpath_hour)
        minute_element = question.element.find_element(By.XPATH, xpath_minute)
        presentation_element = question.element.find_element(By.XPATH, xpath_presentation)

        hour_element.clear()  # Clear any existing value
        hour_element.send_keys('12')

        time.sleep(0.3)

        minute_element.clear()  # Clear any existing value
        minute_element.send_keys('00')
        time.sleep(0.3)

    def add_option_short_answer(self, question):
        xpath = ".//input[@type='text']"
        option = Option(question.element.find_element(By.XPATH, xpath))
        option.xpath = xpath
        option.element.clear()  # Clear any existing value
        option.element.send_keys('Test')
        time.sleep(1)
        option.label = "Your answer"
        question.options.append(option)

    def add_option_paragraph(self, question):
        xpath = ".//textarea"
        option = Option(question.element.find_element(By.XPATH, xpath))
        option.xpath = xpath
        option.element.clear()  # Clear any existing value
        option.element.send_keys('Test')
        time.sleep(1)
        option.label = "Your answer"
        question.options.append(option)

    def process_form(self, driver):
        self.driver = driver
        self.driver.get(self.form.url)
        time.sleep(5)
        is_next = True
        page_number = 1
        while is_next:
            print(f"Processing page {page_number}")

            self.get_list_question()
            time.sleep(2)
            try:
                button_submit_xpath = "//div[@role='button' and contains(@aria-label, 'Submit')]"
                summit_button_element = self.driver.find_element(By.XPATH, button_submit_xpath)
                button = Button('Submit', button_submit_xpath)
                self.form.lists[-1].button = button
                #summit_button_element.click()
                self.driver.quit()
            except WebDriverException:
                print("Submit button not found, continuing to next page.")
                try:
                    button_element = self.driver.find_elements(By.XPATH,'//div[@role="button"]')
                    print(f"Number of buttons found: {len(button_element)}")

                    button_next = button_element[0] if len(button_element) == 2 else button_element[1]
                    value = button_next.get_attribute('innerText')
                    button_next_xpath = "//div[@role='button'][contains(., '{value}')]"

                    button = Button(value, button_next_xpath)

                    self.form.lists[page_number - 1].button = button
                    button_next.click()
                    time.sleep(3)
                    page_number += 1
                except WebDriverException as e:
                    print(f"Error clicking next button: {e}")
                    is_next = False
                except Exception as e:
                    print(f"Error finding next button: {e}")
                    is_next = False
            except Exception as e:
                print(f"Error getting button: {e}")
                

                
        
        print("Finished processing all pages.")
        
        print("Submitting the form...")
        

    def get_list_question(self):
        #get list question
        list_question = ListQuestion(self.driver.find_element(By.XPATH, "//div[@role='list']"))        
        list_question.xpath = "//div[@role='list']"
        
        #get questions element in list
        questions_element = list_question.element.find_elements(By.XPATH, "./div[@role='listitem']")
        print('Number of question: ' + str(len(questions_element)))
        if len(questions_element) == 0:
            print("No questions found on this page.")
            self.form.lists.append(list_question)
            return
        index = 1
        html =''
        for element in questions_element:
            question = Question(element)
            question.xpath = "./div[@role='listitem']"
            outerHTML = element.get_attribute("outerHTML")
            html += "{'block': '" + str(index) + "', 'html': '" + outerHTML + "'}"
            index += 1
            list_question.questions.append(question)

        is_result_getted = False
        retries = 0
        while not is_result_getted and retries < 3:
            try:
                result = self.get_classify_question_type(html)
                is_result_getted = True
            except Exception as e:
                retries += 1
                print(f"Error during get classification: {e}")
                print("Retrying classification...")
                time.sleep(retries * 15)
        

        for i in range(len(result)):
            print(result[i])

        retries = 0
        success = False
        while not success and retries < 3:
            try:
                for i in range(len(result)):
                    list_question.questions[i].type = result[i]['type']
                    list_question.questions[i].heading = result[i]['heading']

                    if result[i]['type'] == "Multiple choice":
                        time.sleep(0.5)
                        self.add_option_multiple_choice(list_question.questions[i], result[i]['options'])

                    if result[i]['type'] == "Checkboxes":
                        time.sleep(0.5)
                        self.add_option_checkboxes(list_question.questions[i], result[i]['options'])

                    if result[i]['type'] == "Drop-down":
                        time.sleep(0.5)
                        self.add_option_dropdown(list_question.questions[i], result[i]['options'])
                        
                    if result[i]['type'] == "Linear scale" or result[i]['type'] == "Rating":
                        time.sleep(0.5)
                        self.add_option_linear_scale_or_rating(list_question.questions[i], result[i]['options'])

                    if result[i]['type'] == "Multiple-choice grid":
                        list_question.questions[i].rows = result[i]['rows']
                        list_question.questions[i].columns = result[i]['columns']
                        self.add_option_multiple_choice_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])

                    if result[i]['type'] == "Tick box grid":
                        list_question.questions[i].rows = result[i]['rows']
                        list_question.questions[i].columns = result[i]['columns']
                        self.add_option_tick_box_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])

                    if result[i]['type'] == "Date":
                        self.add_option_date(list_question.questions[i])

                    # if result[i]['type'] == "Time":
                    #     add_option_time(list_question.questions[i])

                    if result[i]['type'] == "Short answer":
                        self.add_option_short_answer(list_question.questions[i])

                    if result[i]['type'] == "Paragraph":
                        self.add_option_paragraph(list_question.questions[i])
                success = True
            except Exception as e:
                print(f"Error during classification: {e}")
                retries += 1
                list_question.refresh_elements()
                time.sleep(2)

        self.form.lists.append(list_question)

    def get_classify_question_type(self, outerHTML):
        ai_service = AIService()
        return ai_service.classify_question_type(outerHTML)


    
        
        



