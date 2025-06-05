from services.browser_service import BrowserService
from services.form_service import FormService
from config import settings

def main():
    try:
        # Initialize services
        browser_service = BrowserService()
        form_service = FormService()
        
        # Get browser instance
        driver = browser_service.get_driver()
        
        # Process form
        form_service.process_form(driver, "https://forms.gle/qFkBDjWP1HCVDM2V8")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()