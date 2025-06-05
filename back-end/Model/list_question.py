from selenium.webdriver.common.by import By
from Model.question import Question
class ListQuestion:
    def __init__(self, element):
        self.element = element
        self.xpath = ''
        self.questions = []

    def _init_questions(self):
        """Initialize questions from the element"""
        questions_element = self.element.find_elements(By.XPATH, "./div[@role='listitem']")
        for element in questions_element:
            question = Question(element)
            question.xpath = "./div[@role='listitem']"
            self.questions.append(question)
    
    def refresh_elements(self):
        """Refresh all elements after driver restart"""
        self.questions = []
        self._init_questions()