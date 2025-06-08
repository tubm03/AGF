from services.browser_service import BrowserService
from services.form_service import FormService
from model.form import Form
class CrawlService:
    def crawl(self, url: str):
        try:
        # Initialize services
            browser_service = BrowserService()
            form = Form(url)
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
        return data