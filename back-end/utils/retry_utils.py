import time
from functools import wraps
from selenium.common.exceptions import WebDriverException

def retry_on_driver_error(max_retries=3, delay=1, backoff=2):
    """
    Decorator to retry a function when WebDriverException occurs
    :param max_retries: Maximum number of retries
    :param delay: Initial delay between retries in seconds
    :param backoff: Multiplier for delay between retries
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            last_exception = None
            
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except WebDriverException as e:
                    last_exception = e
                    retries += 1
                    if retries < max_retries:
                        print(f"Attempt {retries} failed. Retrying in {current_delay} seconds...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                        # Reinitialize driver if needed
                        if hasattr(args[0], 'driver'):
                            args[0]._restart_driver()
            raise Exception(f"Failed after {max_retries} attempts") from last_exception
        return wrapper
    return decorator