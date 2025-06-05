from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from google import genai

import undetected_chromedriver as uc
import time
import requests
import csv
import json

from Model.list_question import ListQuestion
from Model.answer import Answer
from Model.question import Question
from Model.option import Option


result = []
index = 1

list_question = ListQuestion(driver.find_element(By.XPATH, "//div[@role='list']"))
list_question.questions = []

questions_element = list_question.element.find_elements(By.XPATH, "./div[@role='listitem']")
print(str(len(questions_element)))

html =''
for element in questions_element:
    question = Question(element)
    question.xpath = "./div[@role='listitem']"
    outerHTML = element.get_attribute("outerHTML")
    html += "{'block': '" + str(index) + "', 'html': '" + outerHTML + "'}"
    index += 1
    list_question.questions.append(question)
print(html)

genai_result = get_type(html)
result = genai_result



for i in range(len(result)):
    list_question.questions[i].type = result[i]['type']
    list_question.questions[i].heading = result[i]['heading']
    if result[i]['type'] == "Multiple choice":
        time.sleep(0.5)
        add_option_multiple_choice(list_question.questions[i], result[i]['options'])
    if result[i]['type'] == "Checkboxes":
        time.sleep(0.5)
        add_option_checkboxes(list_question.questions[i], result[i]['options'])
    if result[i]['type'] == "Drop-down":
        time.sleep(0.5)
        add_option_dropdown(list_question.questions[i], result[i]['options'])
    if result[i]['type'] == "Linear scale" or result[i]['type'] == "Rating":
        time.sleep(0.5)
        add_option_linear_scale_or_rating(list_question.questions[i], result[i]['options'])
    if result[i]['type'] == "Multiple-choice grid":
        add_option_multiple_choice_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])
    if result[i]['type'] == "Tick box grid":
        add_option_tick_box_grid(list_question.questions[i], result[i]['rows'], result[i]['columns'])
    if result[i]['type'] == "Date":
        add_option_date(list_question.questions[i])
    # if result[i]['type'] == "Time":
    #     add_option_time(list_question.questions[i])
    if result[i]['type'] == "Short answer":
        add_option_short_answer(list_question.questions[i])
    if result[i]['type'] == "Paragraph":
        add_option_paragraph(list_question.questions[i])
        