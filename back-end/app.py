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
    "url": "https://forms.gle/qFkBDjWP1HCVDM2V8",
    "lists": [
        {
            "xpath": "//div[@role='list']",
            "questions": [
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Title",
                    "heading": "Title",
                    "options": [],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Short answer",
                    "heading": "Short answer",
                    "options": [
                        {
                            "xpath": ".//input[@type='text']",
                            "label": "Your answer",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Paragraph",
                    "heading": "Paragraph",
                    "options": [
                        {
                            "xpath": ".//textarea",
                            "label": "Your answer",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Multiple choice",
                    "heading": "Multiple choice",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Option 1\") or contains(@data-value, \"option 1\"))]",
                            "label": "Option 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and (contains(@data-value, \"Option 2\") or contains(@data-value, \"option 2\"))]",
                            "label": "Option 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//input[@type='text']",
                            "label": "__other_option__",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Checkboxes",
                    "heading": "Checkboxes",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Option 1\") or contains(@data-answer-value, \"option 1\"))]",
                            "label": "Option 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and (contains(@data-answer-value, \"Option 2\") or contains(@data-answer-value, \"option 2\"))]",
                            "label": "Option 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//input[@type='text']",
                            "label": "__other_option__",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Drop-down",
                    "heading": "Drop-down",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"option\" and contains(@data-value, \"Option 1\")]",
                            "label": "Option 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"option\" and contains(@data-value, \"Option 2\")]",
                            "label": "Option 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"option\" and contains(@data-value, \"Option 3\")]",
                            "label": "Option 3",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Linear scale",
                    "heading": "Linear scale",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"1\")]",
                            "label": "1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"2\")]",
                            "label": "2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"3\")]",
                            "label": "3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"4\")]",
                            "label": "4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"5\")]",
                            "label": "5",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Rating",
                    "heading": "Rating",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"1\")]",
                            "label": "1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"2\")]",
                            "label": "2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"3\")]",
                            "label": "3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"4\")]",
                            "label": "4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"5\")]",
                            "label": "5",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Multiple-choice grid",
                    "heading": "Multiple-choice grid",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 1 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 1 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 1 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 1 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 1 - Column 5",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 2 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 2 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 2 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 2 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 2 - Column 5",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 3 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 3 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 3 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 3 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"radio\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 3 - Column 5",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [
                        "Row 1",
                        "Row 2",
                        "Row 3"
                    ],
                    "columns": [
                        "Column 1",
                        "Column 2",
                        "Column 3",
                        "Column 4",
                        "Column 5"
                    ]
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Tick box grid",
                    "heading": "Tick box grid",
                    "options": [
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 1 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 1 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 1 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 1 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 1\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 1 - Column 5",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 2 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 2 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 2 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 2 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 2\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 2 - Column 5",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 1\")]",
                            "label": "Row 3 - Column 1",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 2\")]",
                            "label": "Row 3 - Column 2",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 3\")]",
                            "label": "Row 3 - Column 3",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 4\")]",
                            "label": "Row 3 - Column 4",
                            "percent": 0,
                            "count": 0
                        },
                        {
                            "xpath": ".//div[@role=\"checkbox\" and contains(@aria-label, \"Row 3\") and contains(@aria-label, \"Column 5\")]",
                            "label": "Row 3 - Column 5",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [
                        "Row 1",
                        "Row 2",
                        "Row 3"
                    ],
                    "columns": [
                        "Column 1",
                        "Column 2",
                        "Column 3",
                        "Column 4",
                        "Column 5"
                    ]
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Date",
                    "heading": "Date",
                    "options": [
                        {
                            "xpath": ".//input[@type='date']",
                            "label": "input date",
                            "percent": 0,
                            "count": 0
                        }
                    ],
                    "scale": [],
                    "rows": [],
                    "columns": []
                },
                {
                    "xpath": "./div[@role='listitem']",
                    "type": "Time",
                    "heading": "Time",
                    "options": [],
                    "scale": [],
                    "rows": [],
                    "columns": []
                }
            ],
            "button": {
                "value": "Submit",
                "xpath": "//div[@role='button' and contains(@aria-label, 'Submit')]"
            }
        }
    ]
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