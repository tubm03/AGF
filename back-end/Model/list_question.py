from selenium.webdriver.common.by import By
from model.question import Question
class ListQuestion:
    def __init__(self, element):
        self.element = element
        self.xpath = ''
        self.button = None
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

    def __json__(self):
        return {
            "xpath": self.xpath,
            "questions": [question.__json__() for question in self.questions],
            "button": self.button.__json__() if self.button else None
        }