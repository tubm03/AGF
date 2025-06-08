import undetected_chromedriver as uc
from config import settings

class BrowserService:
    def __init__(self):
        self.options = self._configure_options()
        
    def _configure_options(self):
        options = uc.ChromeOptions()
        
        # Apply settings from config
        options.add_argument(f"--lang={settings.BROWSER_OPTIONS['language']}")
        options.add_argument(f"user-agent={settings.BROWSER_OPTIONS['user_agent']}")

        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument("--incognito")
        
        # Thêm các tham số ẩn danh
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")

        # Thêm các tham số ngẫu nhiên giống trình duyệt thật
        options.add_argument("--flag-switches-begin")
        options.add_argument("--flag-switches-end")

        # chạy trong nền 
        options.add_argument('--headless')  # Run in background
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Thiết lập profile
        options.add_argument("--user-data-dir=/tmp/chrome_profile")
        options.add_argument("--profile-directory=Default")
        
        return options
    
    def get_driver(self):
        uc.TARGET_VERSION = settings.TARGET_VERSION
        driver = uc.Chrome(options=self.options)
        self._remove_automation_traces(driver)
        return driver
    
    def _remove_automation_traces(self, driver):
        # Xóa traces của automation
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_script("window.navigator.chrome = {runtime: {}, etc: {}};")