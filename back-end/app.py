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
        "value": "Tiếp",
        "xpath": "//div[@role='button'][contains(., 'Tiếp')]"
      },
      "questions": [],
      "xpath": "//div[@role='list']"
    },
    {
      "button": {
        "value": "Tiếp",
        "xpath": "//div[@role='button'][contains(., 'Tiếp')]"
      },
      "questions": [
        {
          "columns": [],
          "heading": "PERSONAL INFORMATION",
          "options": [],
          "rows": [],
          "scale": [],
          "type": "Title",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What is your gender?",
          "options": [
            {
              "count": 0,
              "label": "Male",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Male\") or contains(@data-value, \"male\"))]"
            },
            {
              "count": 0,
              "label": "Female",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Female\") or contains(@data-value, \"female\"))]"
            },
            {
              "count": 0,
              "label": "Khác",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Khác\") or contains(@data-value, \"khác\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What is your age? ",
          "options": [
            {
              "count": 0,
              "label": "Under 18",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Under 18\") or contains(@data-value, \"under 18\"))]"
            },
            {
              "count": 0,
              "label": "18 - 24",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"18 - 24\") or contains(@data-value, \"18 - 24\"))]"
            },
            {
              "count": 0,
              "label": "25 - 34",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"25 - 34\") or contains(@data-value, \"25 - 34\"))]"
            },
            {
              "count": 0,
              "label": "Above 35",
              "percent": 0,
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
          "heading": "Where you from ? ",
          "options": [
            {
              "count": 0,
              "label": "USA",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"USA\") or contains(@data-value, \"usa\"))]"
            },
            {
              "count": 0,
              "label": "Canada",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Canada\") or contains(@data-value, \"canada\"))]"
            },
            {
              "count": 0,
              "label": "France",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"France\") or contains(@data-value, \"france\"))]"
            },
            {
              "count": 0,
              "label": "Germany",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Germany\") or contains(@data-value, \"germany\"))]"
            },
            {
              "count": 0,
              "label": "Italy",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Italy\") or contains(@data-value, \"italy\"))]"
            },
            {
              "count": 0,
              "label": "Spain",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Spain\") or contains(@data-value, \"spain\"))]"
            },
            {
              "count": 0,
              "label": "United Kingdom",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"United Kingdom\") or contains(@data-value, \"united kingdom\"))]"
            },
            {
              "count": 0,
              "label": "Netherlands",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Netherlands\") or contains(@data-value, \"netherlands\"))]"
            },
            {
              "count": 0,
              "label": "New Zealand",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"New Zealand\") or contains(@data-value, \"new zealand\"))]"
            },
            {
              "count": 0,
              "label": "Singapore",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Singapore\") or contains(@data-value, \"singapore\"))]"
            },
            {
              "count": 0,
              "label": "Japan",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Japan\") or contains(@data-value, \"japan\"))]"
            },
            {
              "count": 0,
              "label": "South Korea",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"South Korea\") or contains(@data-value, \"south korea\"))]"
            },
            {
              "count": 0,
              "label": "China",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"China\") or contains(@data-value, \"china\"))]"
            },
            {
              "count": 0,
              "label": "Thailand",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Thailand\") or contains(@data-value, \"thailand\"))]"
            },
            {
              "count": 0,
              "label": "Malaysia",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Malaysia\") or contains(@data-value, \"malaysia\"))]"
            },
            {
              "count": 0,
              "label": "__other_option__",
              "percent": 100,
              "value": "Việt Nam",
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
              "label": "1- 3 year",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"1- 3 year\") or contains(@data-value, \"1- 3 year\"))]"
            },
            {
              "count": 0,
              "label": "> 3 year",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"> 3 year\") or contains(@data-value, \"> 3 year\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What is your current occupation?",
          "options": [
            {
              "count": 0,
              "label": "Student",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Student\") or contains(@data-value, \"student\"))]"
            },
            {
              "count": 0,
              "label": "Office staff",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Office staff\") or contains(@data-value, \"office staff\"))]"
            },
            {
              "count": 0,
              "label": "Self-employed/Business",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Self-employed/Business\") or contains(@data-value, \"self-employed/business\"))]"
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
          "heading": "Have you ever used or heard of a biodegradable batch bowl?",
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
        }
      ],
      "xpath": "//div[@role='list']"
    },
    {
      "button": {
        "value": "Tiếp",
        "xpath": "//div[@role='button'][contains(., 'Tiếp')]"
      },
      "questions": [
        {
          "columns": [],
          "heading": " CONSUMER BEHAVIOR ",
          "options": [],
          "rows": [],
          "scale": [],
          "type": "Title",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "What do you think of when you heard of a <span>biodegradable areca palm bowl</span>?",
          "options": [
            {
              "count": 0,
              "label": "Environmentally friendly, nature-friendly",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Environmentally friendly, nature-friendly\") or contains(@data-answer-value, \"environmentally friendly, nature-friendly\"))]"
            },
            {
              "count": 0,
              "label": "Perishable, not durable",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Perishable, not durable\") or contains(@data-answer-value, \"perishable, not durable\"))]"
            },
            {
              "count": 0,
              "label": "Product for single use only",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Product for single use only\") or contains(@data-answer-value, \"product for single use only\"))]"
            },
            {
              "count": 0,
              "label": "More expensive than conventional product",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"More expensive than conventional product\") or contains(@data-answer-value, \"more expensive than conventional product\"))]"
            },
            {
              "count": 0,
              "label": "Vgreen Kombucha",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Vgreen Kombucha\") or contains(@data-answer-value, \"vgreen kombucha\"))]"
            },
            {
              "count": 0,
              "label": "Other",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Other\") or contains(@data-answer-value, \"other\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Checkboxes",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "When do you think this product is suitable for use? ",
          "options": [
            {
              "count": 0,
              "label": "Picnic",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Picnic\") or contains(@data-value, \"picnic\"))]"
            },
            {
              "count": 0,
              "label": "Home party",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Home party\") or contains(@data-value, \"home party\"))]"
            },
            {
              "count": 0,
              "label": "Green gift",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Green gift\") or contains(@data-value, \"green gift\"))]"
            },
            {
              "count": 0,
              "label": "Use in homestay, resort",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Use in homestay, resort\") or contains(@data-value, \"use in homestay, resort\"))]"
            },
            {
              "count": 0,
              "label": "Not suitable",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Not suitable\") or contains(@data-value, \"not suitable\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Do you have any concerns about using this type? ",
          "options": [
            {
              "count": 0,
              "label": "Not sure if it's food-safe",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Not sure if it's food-safe\") or contains(@data-answer-value, \"not sure if it's food-safe\"))]"
            },
            {
              "count": 0,
              "label": "Not durable, easily breaks or leaks",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Not durable, easily breaks or leaks\") or contains(@data-answer-value, \"not durable, easily breaks or leaks\"))]"
            },
            {
              "count": 0,
              "label": "More expensive than regular tableware",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"More expensive than regular tableware\") or contains(@data-answer-value, \"more expensive than regular tableware\"))]"
            },
            {
              "count": 0,
              "label": "Not widely available",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Not widely available\") or contains(@data-answer-value, \"not widely available\"))]"
            },
            {
              "count": 0,
              "label": "Other",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Other\") or contains(@data-answer-value, \"other\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Checkboxes",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "Would you be willing to try a bowl/plate product made from 100% areca leaf spathe – environmentally friendly, no chemicals, no microplastics ?",
          "options": [
            {
              "count": 0,
              "label": "Yes, if it is easy to buy and reasonably priced",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Yes, if it is easy to buy and reasonably priced\") or contains(@data-value, \"yes, if it is easy to buy and reasonably priced\"))]"
            },
            {
              "count": 0,
              "label": "Maybe, if there is a promotion/trial",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Maybe, if there is a promotion/trial\") or contains(@data-value, \"maybe, if there is a promotion/trial\"))]"
            },
            {
              "count": 0,
              "label": "No, I am not interested",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"No, I am not interested\") or contains(@data-value, \"no, i am not interested\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Multiple choice",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "If this product were available at the following places, where would be the most convenient for you to buy it in Vietnam? \n<p></p>",
          "options": [
            {
              "count": 0,
              "label": "Online platforms (TikTok, Shopee, Lazada, etc.)",
              "percent": 100,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Online platforms (TikTok, Shopee, Lazada, etc.)\") or contains(@data-answer-value, \"online platforms (tiktok, shopee, lazada, etc.)\"))]"
            },
            {
              "count": 0,
              "label": "Facebook community groups",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Facebook community groups\") or contains(@data-answer-value, \"facebook community groups\"))]"
            },
            {
              "count": 0,
              "label": "Supermarkets",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Supermarkets\") or contains(@data-answer-value, \"supermarkets\"))]"
            },
            {
              "count": 0,
              "label": "Local markets / Convenience stores",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Local markets / Convenience stores\") or contains(@data-answer-value, \"local markets / convenience stores\"))]"
            },
            {
              "count": 0,
              "label": "Eco-friendly specialty stores",
              "percent": 50,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Eco-friendly specialty stores\") or contains(@data-answer-value, \"eco-friendly specialty stores\"))]"
            },
            {
              "count": 0,
              "label": "Fairs or exhibitions",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Fairs or exhibitions\") or contains(@data-answer-value, \"fairs or exhibitions\"))]"
            },
            {
              "count": 0,
              "label": "Other",
              "percent": 0,
              "value": "",
              "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Other\") or contains(@data-answer-value, \"other\"))]"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Checkboxes",
          "xpath": "./div[@role='listitem']"
        }
      ],
      "xpath": "//div[@role='list']"
    },
    {
      "button": {
        "value": "Submit",
        "xpath": "//div[@role='button' and contains(@aria-label, 'Submit')]"
      },
      "questions": [
        {
          "columns": [],
          "heading": "THANK YOU 💖",
          "options": [],
          "rows": [],
          "scale": [],
          "type": "Title",
          "xpath": "./div[@role='listitem']"
        },
        {
          "columns": [],
          "heading": "If you have any additional sharing or contributions, do not hesitate to leave a comment below!",
          "options": [
            {
              "count": 0,
              "label": "textarea",
              "percent": 0,
              "value": "",
              "xpath": ".//textarea"
            }
          ],
          "rows": [],
          "scale": [],
          "type": "Paragraph",
          "xpath": "./div[@role='listitem']"
        }
      ],
      "xpath": "//div[@role='list']"
    }
  ],
  "url": "https://forms.gle/LHPFYvz3M8Wjp9p37"
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