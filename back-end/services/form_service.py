import time
from Model.option import Option
from selenium.webdriver.common.by import By
from Model.list_question import ListQuestion
from Model.question import Question
from services.ai_service import AIService
from selenium.common.exceptions import WebDriverException

class FormService:
    def __init__(self):
        self.url = ''
        self.driver = None
        self.page = []

    def _restart_driver(self):
        """Restart the browser driver"""
        try:
            self.driver.quit()
        except:
            pass
        self.driver.get(self.url)

    def add_options(self, question):
        if question.type in self.options:
            self.options[question.type](question)

    def add_option_multiple_choice(self, question, options):
        for op in options:
            xpath = f".//div[@role='radio' and contains(translate(@data-value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{op.lower()}')]" 
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            print(option.xpath)
            option.label = option
            question.options.append(option)
            
    def add_option_checkboxes(self, question, options):
        for op in options:
            xpath = f".//div[@role='checkbox' and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{op.lower()}')]" 
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            print(option.xpath)
            option.label = option
            question.options.append(option)

    def add_option_dropdown(self, question, options):
        time.sleep(1)
        presentation_element = question.element.find_element(By.XPATH, ".//div[@role='presentation']")
        for op in options:
            presentation_element.click()
            time.sleep(1)
            xpath = f".//div[@role='option' and contains(translate(@data-value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{op.lower()}')]" 
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            print(option.xpath)
            option.label = option
            question.options.append(option)

    def add_option_linear_scale_or_rating(self, question, options):
        for op in options:
            xpath = f".//div[@role='radio' and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{op.lower()}')]" 
            option = Option(question.element.find_element(By.XPATH, xpath))
            option.xpath = xpath
            time.sleep(0.5)
            option.element.click()
            print(option.xpath)
            option.label = option
            question.options.append(option)

    def add_option_multiple_choice_grid(self, question, rows, columns):
        for row in rows:
            for column in columns:
                xpath = f".//div[@role='radio' and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{row.lower()}') and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{column.lower()}')]" 
                option = Option(question.element.find_element(By.XPATH, xpath))
                option.xpath = xpath
                time.sleep(0.5)
                option.element.click()
                print(option.xpath)
                option.label = option
                question.options.append(option)

    def add_option_tick_box_grid(self, question, rows, columns):
        for row in rows:
            for column in columns:
                xpath = f".//div[@role='checkbox' and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{row.lower()}') and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{column.lower()}')]" 
                option = Option(question.element.find_element(By.XPATH, xpath))
                option.xpath = xpath
                time.sleep(0.5)
                option.element.click()
                print(option.xpath)
                option.label = option
                question.options.append(option)

    def add_option_date(self, question):
        xpath = ".//input[@type='date']"
        option = Option(question.element.find_element(By.XPATH, xpath))
        option.xpath = xpath
        option.element.clear()  # Clear any existing value
        time.sleep(0.5)
        option.element.send_keys('12/11/2003')
        print(option.xpath)
        option.label = option
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
        print(option.xpath)
        option.label = option
        question.options.append(option)

    def add_option_paragraph(self, question):
        xpath = ".//textarea"
        option = Option(question.element.find_element(By.XPATH, xpath))
        option.xpath = xpath
        option.element.clear()  # Clear any existing value
        option.element.send_keys('Test')
        time.sleep(1)
        print(option.xpath)
        option.label = option
        question.options.append(option)

    def process_form(self, driver, url):
        self.url = url
        self.driver = driver
        self.driver.get(url)
        time.sleep(5)

        self.get_list_question()


    def get_list_question(self):
        #get list question
        list_question = ListQuestion(self.driver.find_element(By.XPATH, "//div[@role='list']"))        

        #get questions element in list
        questions_element = list_question.element.find_elements(By.XPATH, "./div[@role='listitem']")
        print(str(len(questions_element)))

        index = 1
        html =''
        for element in questions_element:
            question = Question(element)
            question.xpath = "./div[@role='listitem']"
            outerHTML = element.get_attribute("outerHTML")
            html += "{'block': '" + str(index) + "', 'html': '" + outerHTML + "'}"
            index += 1
            list_question.questions.append(question)

        result = self.get_classify_question_type(html)

        retries = 0
        success = False
        while not success and retries < 3:
            try:
                result = self.add_option(result, list_question)
                success = True
            except Exception as e:
                print(f"Error during classification: {e}")
                retries += 1
                list_question.refresh_elements()
                time.sleep(2)

        self.page.append(list_question)

    def get_classify_question_type(self, outerHTML):
        ai_service = AIService()
        return ai_service.classify_question_type(outerHTML)
    
    def add_option(self, result, list_question):
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
                self.add_option_multiple_choice_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])
            if result[i]['type'] == "Tick box grid":
                self.add_option_tick_box_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])
            if result[i]['type'] == "Date":
                self.add_option_date(list_question.questions[i])
            # if result[i]['type'] == "Time":
            #     add_option_time(list_question.questions[i])
            if result[i]['type'] == "Short answer":
                self.add_option_short_answer(list_question.questions[i])
            if result[i]['type'] == "Paragraph":
                self.add_option_paragraph(list_question.questions[i])
    
        
        



