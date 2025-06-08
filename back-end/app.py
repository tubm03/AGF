from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from types import SimpleNamespace

from services.crawl_service import CrawlService
from services.auto_fill_service import AutoFillService

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

data = {
  "lists": [
    {
      "button": {
        "value": "Submit",
        "xpath": "//div[@role='button' and contains(@aria-label, 'Submit')]"
      },
      "questions": [
        {
          "columns": [],
          "heading": "Where are you from?",
          "options": [
            {
              "count": 0,
              "label": "Your answer",
              "percent": 60,
              "value": "Ha noi",
              "xpath": ".//input[@type='text']"
            },
            {
              "label": "input text",
              "percent": 40,
              "count": 0,
              "xpath": ".//input[@type='text']",
              "value": "Nam Dinh"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Short answer",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What is your age?",
          "options": [
            {
              "count": 0,
              "label": "18- 24",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"18- 24\") or contains(@data-value, \"18- 24\"))]"
            },
            {
              "count": 0,
              "label": "25 - 34",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"25 - 34\") or contains(@data-value, \"25 - 34\"))]"
            },
            {
              "count": 0,
              "label": "Above 35",
              "percent": 20,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Above 35\") or contains(@data-value, \"above 35\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What is your gender?",
          "options": [
            {
              "count": 0,
              "label": "Male",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Male\") or contains(@data-value, \"male\"))]"
            },
            {
              "count": 0,
              "label": "Female",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Female\") or contains(@data-value, \"female\"))]"
            },
            {
              "count": 0,
              "label": "Other",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Other\") or contains(@data-value, \"other\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "How long have you lived in Vietnam?",
          "options": [
            {
              "count": 0,
              "label": "< 1 month",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"< 1 month\") or contains(@data-value, \"< 1 month\"))]"
            },
            {
              "count": 0,
              "label": "1 - 3 years",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"1 - 3 years\") or contains(@data-value, \"1 - 3 years\"))]"
            },
            {
              "count": 0,
              "label": "> 3 years",
              "percent": 90,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"> 3 years\") or contains(@data-value, \"> 3 years\"))]"
            },
            {
              "count": 0,
              "label": "__other_option__",
              "percent": 10,
              "value": "5 month",
              "xpath": ".//input[@type='text']"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Do you use eco-friendly products like biodegradable plates or bowls?",
          "options": [
            {
              "count": 0,
              "label": "Daily",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Daily\") or contains(@data-value, \"daily\"))]"
            },
            {
              "count": 0,
              "label": "Weekly",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Weekly\") or contains(@data-value, \"weekly\"))]"
            },
            {
              "count": 0,
              "label": "Occasionally (events, parties...)",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Occasionally (events, parties...)\") or contains(@data-value, \"occasionally (events, parties...)\"))]"
            },
            {
              "count": 0,
              "label": "Rarely or never",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Rarely or never\") or contains(@data-value, \"rarely or never\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Which of the following disposable products do you usually use?",
          "options": [
            {
              "count": 0,
              "label": "Plastic plates/bowls",
              "percent": 60,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Plastic plates/bowls\") or contains(@data-value, \"plastic plates/bowls\"))]"
            },
            {
              "count": 0,
              "label": "Paper plates/bowls",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Paper plates/bowls\") or contains(@data-value, \"paper plates/bowls\"))]"
            },
            {
              "count": 0,
              "label": "Plates/bowls made from natural materials (leaves, bamboo, areca spathe, etc.)",
              "percent": 10,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Plates/bowls made from natural materials (leaves, bamboo, areca spathe, etc.)\") or contains(@data-value, \"plates/bowls made from natural materials (leaves, bamboo, areca spathe, etc.)\"))]"
            },
            {
              "count": 0,
              "label": "__other_option__",
              "percent": 0,
              "value": "",
              "xpath": ".//input[@type='text']"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Have you ever heard of disposable tableware products made from  areca spathe?",
          "options": [
            {
              "count": 0,
              "label": "Yes",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Yes\") or contains(@data-value, \"yes\"))]"
            },
            {
              "count": 0,
              "label": "No",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"No\") or contains(@data-value, \"no\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [
            "Strongly disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree"
          ],
          "heading": "What do you think about tableware products made from areca spathe? ",
          "options": [
            {
              "count": 0,
              "label": "Do you find the product attractive - Strongly disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Do you find the product attractive\") and contains(@aria-label, \"Strongly disagree\")]"
            },
            {
              "count": 0,
              "label": "Do you find the product attractive - Disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Do you find the product attractive\") and contains(@aria-label, \"Disagree\")]"
            },
            {
              "count": 0,
              "label": "Do you find the product attractive - Neutral",
              "percent": 10,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Do you find the product attractive\") and contains(@aria-label, \"Neutral\")]"
            },
            {
              "count": 0,
              "label": "Do you find the product attractive - Agree",
              "percent": 20,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Do you find the product attractive\") and contains(@aria-label, \"Agree\")]"
            },
            {
              "count": 0,
              "label": "Do you find the product attractive - Strongly agree",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Do you find the product attractive\") and contains(@aria-label, \"Strongly agree\")]"
            },
            {
              "count": 0,
              "label": "The product can replace conventional disks and plastic products. - Strongly disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"The product can replace conventional disks and plastic products.\") and contains(@aria-label, \"Strongly disagree\")]"
            },
            {
              "count": 0,
              "label": "The product can replace conventional disks and plastic products. - Disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"The product can replace conventional disks and plastic products.\") and contains(@aria-label, \"Disagree\")]"
            },
            {
              "count": 0,
              "label": "The product can replace conventional disks and plastic products. - Neutral",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"The product can replace conventional disks and plastic products.\") and contains(@aria-label, \"Neutral\")]"
            },
            {
              "count": 0,
              "label": "The product can replace conventional disks and plastic products. - Agree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"The product can replace conventional disks and plastic products.\") and contains(@aria-label, \"Agree\")]"
            },
            {
              "count": 0,
              "label": "The product can replace conventional disks and plastic products. - Strongly agree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"The product can replace conventional disks and plastic products.\") and contains(@aria-label, \"Strongly agree\")]"
            },
            {
              "count": 0,
              "label": "You feel that areca bowls and plates are suitable for the green living trend and environmental protection. - Strongly disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"You feel that areca bowls and plates are suitable for the green living trend and environmental protection.\") and contains(@aria-label, \"Strongly disagree\")]"
            },
            {
              "count": 0,
              "label": "You feel that areca bowls and plates are suitable for the green living trend and environmental protection. - Disagree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"You feel that areca bowls and plates are suitable for the green living trend and environmental protection.\") and contains(@aria-label, \"Disagree\")]"
            },
            {
              "count": 0,
              "label": "You feel that areca bowls and plates are suitable for the green living trend and environmental protection. - Neutral",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"You feel that areca bowls and plates are suitable for the green living trend and environmental protection.\") and contains(@aria-label, \"Neutral\")]"
            },
            {
              "count": 0,
              "label": "You feel that areca bowls and plates are suitable for the green living trend and environmental protection. - Agree",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"You feel that areca bowls and plates are suitable for the green living trend and environmental protection.\") and contains(@aria-label, \"Agree\")]"
            },
            {
              "count": 0,
              "label": "You feel that areca bowls and plates are suitable for the green living trend and environmental protection. - Strongly agree",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"You feel that areca bowls and plates are suitable for the green living trend and environmental protection.\") and contains(@aria-label, \"Strongly agree\")]"
            }
          ],
          "rows": [
            "Do you find the product attractive",
            "The product can replace conventional disks and plastic products.",
            "You feel that areca bowls and plates are suitable for the green living trend and environmental protection."
          ],
          "scale": [],
          "type": "Multiple-choice grid",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [
            "1",
            "2",
            "3",
            "4"
          ],
          "heading": "Please select all your learning schedule",
          "options": [
            {
              "count": 0,
              "label": "Monday - 1",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Monday\") and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "Monday - 2",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Monday\") and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "Monday - 3",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Monday\") and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "Monday - 4",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Monday\") and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "Tuesday - 1",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Tuesday\") and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "Tuesday - 2",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Tuesday\") and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "Tuesday - 3",
              "percent": 80,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Tuesday\") and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "Tuesday - 4",
              "percent": 90,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Tuesday\") and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "Wenesday - 1",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Wenesday\") and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "Wenesday - 2",
              "percent": 60,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Wenesday\") and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "Wenesday - 3",
              "percent": 60,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Wenesday\") and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "Wenesday - 4",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Wenesday\") and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "Thursday - 1",
              "percent": 80,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Thursday\") and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "Thursday - 2",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Thursday\") and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "Thursday - 3",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Thursday\") and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "Thursday - 4",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Thursday\") and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "Friday - 1",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Friday\") and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "Friday - 2",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Friday\") and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "Friday - 3",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Friday\") and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "Friday - 4",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Friday\") and contains(@aria-label, \"4\")]"
            }
          ],
          "rows": [
            "Monday",
            "Tuesday",
            "Wenesday",
            "Thursday",
            "Friday"
          ],
          "scale": [],
          "type": "Tick box grid",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Do you have any concerns when using dishes made from areca spathe?",
          "options": [
            {
              "count": 0,
              "label": "Durability",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Durability\") or contains(@data-answer-value, \"durability\"))]"
            },
            {
              "count": 0,
              "label": "Price",
              "percent": 80,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Price\") or contains(@data-answer-value, \"price\"))]"
            },
            {
              "count": 0,
              "label": "Health safety",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Health safety\") or contains(@data-answer-value, \"health safety\"))]"
            },
            {
              "count": 0,
              "label": "__other_option__",
              "percent": 0,
              "value": "",
              "xpath": ".//input[@type='text']"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Checkboxes",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "In what context would you consider using areca spathe products?",
          "options": [
            {
              "count": 0,
              "label": "Travel, picnic",
              "percent": 70,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Travel, picnic\") or contains(@data-answer-value, \"travel, picnic\"))]"
            },
            {
              "count": 0,
              "label": "Restaurant/cafe",
              "percent": 10,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Restaurant/cafe\") or contains(@data-answer-value, \"restaurant/cafe\"))]"
            },
            {
              "count": 0,
              "label": "Everyday at home",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Everyday at home\") or contains(@data-answer-value, \"everyday at home\"))]"
            },
            {
              "count": 0,
              "label": "I don't care",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"I don't care\") or contains(@data-answer-value, \"i don't care\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Checkboxes",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Are you willing to pay more for environmentally and health-friendly products?",
          "options": [
            {
              "count": 0,
              "label": "Yes",
              "percent": 60,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Yes\") or contains(@data-value, \"yes\"))]"
            },
            {
              "count": 0,
              "label": "No",
              "percent": 10,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"No\") or contains(@data-value, \"no\"))]"
            },
            {
              "count": 0,
              "label": "Depends on the quality",
              "percent": 30,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Depends on the quality\") or contains(@data-value, \"depends on the quality\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Do you feel this product is suitable in the country you live in?",
          "options": [
            {
              "count": 0,
              "label": "Your answer",
              "percent": 100,
              "value": "yes",
              "xpath": ".//input[@type='text']"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Short answer",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Would you be willing to try this product if given the chance?",
          "options": [
            {
              "count": 0,
              "label": "Yes",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Yes\") or contains(@data-value, \"yes\"))]"
            },
            {
              "count": 0,
              "label": "No",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"No\") or contains(@data-value, \"no\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Bạn có sẵn sàng trải nghiệm thử sản phẩm khi chúng tôi mở bán không?",
          "options": [
            {
              "count": 0,
              "label": "1",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "2",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "3",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "4",
              "percent": 10,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "5",
              "percent": 90,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"5\")]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Linear scale",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "您如何評價這次填表體驗？",
          "options": [
            {
              "count": 0,
              "label": "1",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"1\")]"
            },
            {
              "count": 0,
              "label": "2",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"2\")]"
            },
            {
              "count": 0,
              "label": "3",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"3\")]"
            },
            {
              "count": 0,
              "label": "4",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"4\")]"
            },
            {
              "count": 0,
              "label": "5",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"5\")]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Rating",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Quando você planeja viajar?",
          "options": [
            {
              "count": 0,
              "label": "input date",
              "percent": 20,
              "value": "2025-06-14",
              "xpath": ".//input[@type='date']"
            },
            {
              "label": "input date",
              "percent": 30,
              "count": 0,
              "xpath": ".//input[@type='date']",
              "value": "2025-06-12"
            },
            {
              "label": "input date",
              "percent": 50,
              "count": 0,
              "xpath": ".//input[@type='date']",
              "value": "2025-05-29"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Date",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Che ore sono nella tua zona adesso?",
          "options": [
            {
              "label": "input time",
              "percent": 0,
              "count": 0,
              "xpath": ".//input[@type='time']",
              "value": ""
            },
            {
              "label": "input time",
              "percent": 0,
              "count": 0,
              "xpath": ".//input[@type='time']",
              "value": ""
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Time",
          "xpath": "./div[@role='listitem']"
        }
      ],
      "xpath": "//div[@role='list']"
    }
  ],
  "url": "https://forms.gle/kRrps3n2m5pLaPZP8"
}
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify server status."""
    return jsonify({"status": "Server is running"}), 200

@app.route('/api/crawl', methods=['POST'])
def crawl():
    global data
    """Endpoint to handle crawling requests."""
    url = request.json.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        # Start the crawling process
        crawl_service = CrawlService()
        if data is None:
            data = crawl_service.crawl(url)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/autofill', methods=['POST'])
def autofill():
    """Endpoint to handle auto-fill requests."""
    form_data = request.json.get('formData')
    number_of_fill = request.json.get('numberOfFill')
    
    if not form_data or not isinstance(number_of_fill, int):
        return jsonify({"error": "Invalid form data or number of fills"}), 400
    
    try:
        auto_service = AutoFillService()
        auto_service.auto_fill(form_data,number_of_fill)
        return jsonify({
            "message": f"Auto-filled {number_of_fill} times",
            "formData": form_data
        }), 200
    except Exception as e:
        print(f"An error occurred during auto-fill: {str(e)}")
        return jsonify({"error": str(e)}), 500

def dict_to_obj(d):
    return json.loads(json.dumps(d), object_hook=lambda d: SimpleNamespace(**d))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True,)