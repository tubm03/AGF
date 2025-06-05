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
import requests
import csv
import json

from Model.list_question import List
from Model.answer import Answer
from Model.question import ListItem

def is_valid_json(text):
    try:
        json.loads(text[7:-3])
        return True
    except json.JSONDecodeError:
        return False
    
def get_type(html):
    prompt = """
    
    Analyze the provided HTML snippet of a Google Form question to determine its question type, based on the following valid list:
    ["Title", "Short answer", "Paragraph", "Multiple choice", "Checkboxes", "Drop-down", "Linear scale", "Rating", "Multiple-choice grid", "Tick box grid", "Date", "Time"].

    If the question type includes selectable options (e.g., "Multiple choice", "Checkboxes", "Drop-down", "Linear scale", "Multiple-choice grid", "Tick box grid"), extract all visible options, including “Other” if present.

    Returns the correct result in JSON format with two properties:

    "type": the exact question type (must match one of the valid values).

    "options": a list of options (if applicable); omit this field if there are no options.

    Make sure to:

    Identify the question type accurately based on text or HTML structure.

    Extract options in the correct visual order.

    Exclude unrelated or duplicate elements.

    Example output:

    {"type": "Multiple choice", "options": ["Option 1", "Option 2", "Other"]}

    """
    client = genai.Client(api_key="AIzaSyAg6QdqkgO_wzJmdfci86QI9Pm0eY65wpc")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents= html + prompt
    )

    if is_valid_json(response.text):
        return json.loads(response.text[7:-3])
    else:
        print("Invalid JSON response:", response.text)
        return None
    
options = uc.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
uc.TARGET_VERSION = 85
driver = uc.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdv4ZC_qTN5XdSG4fKwcUODPwzLqsSQ6qxoolfeXHIKOu1VAw/viewform")

list = List(driver.find_element(By.CSS_SELECTOR, "div[role='list']"))

list_items = list.element.find_elements(By.XPATH, "./div[@role='listitem']")
print(str(len(list_items)))

for item in list_items:
    list_item = ListItem(item)
    list_item.xpath = "./div[@role='listitem']"
    list_item.type = get_type(item.get_attribute("outerHTML"))
    list.child.append(list_item)