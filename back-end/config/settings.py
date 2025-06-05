import os
from dotenv import load_dotenv
# Load from environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Other configuration settings
DEFAULT_WAIT_TIMEOUT = 10
BROWSER_OPTIONS = {
    "language": "en-US",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
}
TARGET_VERSION = 85
MAX_RETRIES = 3