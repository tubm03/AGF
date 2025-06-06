from config import settings
from utils.json_utils import clean_json_response, is_valid_json
import json
from google import genai

class AIService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.client = genai.Client(api_key=self.api_key)
        
        
    def classify_question_type(self, outerHTML):
        # Your classification logic here
        prompt = self._build_classification_prompt(outerHTML)
        
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = clean_json_response(response.text)
        return json.loads(text) if is_valid_json(text) else None
    
    def _build_classification_prompt(self, outerHTML):
        short_answer = '{"block": "1", "type": "Short answer", "heading": "Where are you from?"}'
        multiple_choice = '{"block": "2", "type": "Multiple choice", "heading": "What is your favorite color?", "options": ["Red", "Blue", "Green"]}'
        paragraph = '{"block": "3", "type": "Paragraph", "heading": "Describe your experience with the product."}'
        multiple_choice_grid = '{"block": "4", "type": "Multiple-choice grid", "heading": "Rate the following features:", "rows": ["Feature A", "Feature B"], "columns": ["1", "2", "3"]}'
        tick_box_grid = '{"block": "5", "type": "Tick box grid", "heading": "Select your preferred options:", "rows": ["Option 1", "Option 2"], "columns": ["Choice A", "Choice B"]}'
        checkboxes = '{"block": "6", "type": "Checkboxes", "heading": "Select all that apply:", "options": ["Option 1", "Option 2", "Option 3"]}'
        date = '{"block": "7", "type": "Date", "heading": "Select a date:"}'
        time = '{"block": "8", "type": "Time", "heading": "Select a time:"}'
        linear_scale = '{"block": "9", "type": "Linear scale", "heading": "Rate your satisfaction from 1 to 5.", "option": "1", "2", "3", "4", "5"}'
        rating = '{"block": "10", "type": "Rating", "heading": "Rate the product quality from 1 to 5 stars.", "option": "1", "2", "3", "4", "5"}'
        title = '{"block": "11", "type": "Title", "heading": "Welcome to the survey!"}'

        example = f"""[{title}, {short_answer}, {multiple_choice}, {paragraph}, {multiple_choice_grid}, {tick_box_grid}, {checkboxes}, {date}, {time}, {linear_scale}, {rating}]"""

        prompt = f"""
        You are given a block of HTML that represents a single question from a Google Form. Your task is to analyze the HTML structure and classify the question into one of the following types:

        {outerHTML}

        ["Title", "Short answer", "Paragraph", "Multiple choice", "Checkboxes", "Drop-down", "Linear scale", "Rating", "Multiple-choice grid", "Tick box grid", "Date", "Time"]

        If the question type includes selectable options (e.g., "Multiple choice", "Checkboxes", "Drop-down", "Linear scale", "Multiple-choice grid", "Tick box grid"), extract all visible options, including “Other” if present.

        Use the following rules to classify:

        - "Title": <div>, <h1>, or <h2> containing descriptive text only (no inputs).
        - "Short answer": <input type="text"> with placeholder or text like "Your answer".
        - "Paragraph": <textarea> with placeholder "Your answer".
        - "Multiple choice": div[role="radio"] inside label.docssharedWizToggleLabeledContainer.
        - "Checkboxes": div[role="checkbox"] inside label.docssharedWizToggleLabeledContainer.
        - "Drop-down": div[role="listbox"] with div[role="option"] inside.
        - "Linear scale": div[role="radio"] with numeric labels (e.g., 1–5), and polar ends (e.g., "bad" to "good").
        - "Rating": label[data-ratingscale] with div[role="radio"] representing stars or numbers.
        - "Multiple-choice grid": div[role="radiogroup"][aria-label] (each row is a set of radio buttons).
        - "Tick box grid": div[role="group"] (each row has multiple div[role="checkbox"]).
        - "Date": <input type="date"> or fields for day/month/year.
        - "Time": input[type="text"][max="23"] or [max="59"] or fields for hour/minute.

        Returns the correct result in JSON format with two properties:
        
        "block": the HTML structure you analyzed,
        "type": the exact question type (must match one of the valid values).
        "heading": the question's title or description if available.
        "options": an array of options if applicable (only for multiple choice, checkboxes, linear scale, rating etc.).
        "rows": an array of row labels if applicable (only for multiple-choice grid, tick box grid).
        "columns": an array of column labels if applicable (only for multiple-choice grid, tick box grid).

        Make sure to:

        Identify the question type accurately based on text or HTML structure.
        Provide all relevant options, scales, or labels in the JSON response.
        Return the JSON response without any additional text or formatting.
        Get other options from the example output below to help you classify the question type.

        Example output:

        {example}

        """
        return prompt.strip()