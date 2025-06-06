from services.browser_service import BrowserService
from services.form_service import FormService
from model.form import Form
import json

def main():
    url1 = "https://forms.gle/LHPFYvz3M8Wjp9p37" # chuẩn
    url2 = "https://forms.gle/kRrps3n2m5pLaPZP8" # khong có tiêu đề
    url3 = "https://forms.gle/qFkBDjWP1HCVDM2V8" # test agf

    try:
        # Initialize services
        browser_service = BrowserService()
        form = Form(url2)
        form_service = FormService(form)
        
        # Get browser instance
        driver = browser_service.get_driver()
        
        # Process form
        form_service.process_form(driver)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("Closing browser...")

    data = form.to_dict()
    json_data = json.dumps(data, indent=4)
    with open('url2.json', 'w') as f:
        f.write(json_data)
    print(json_data)

def get_form_data(url):
    pass
if __name__ == "__main__":
    main()

