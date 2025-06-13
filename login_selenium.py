from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_turnitin(username, password):
    """Returns True if login successful, False otherwise."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    try:
        driver.get("https://www.turnitin.com/login_page.asp")
        time.sleep(2)

        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        email_field.send_keys(username)
        password_field.send_keys(password)

        password_field.submit()
        time.sleep(5)

        if "login_page" not in driver.current_url:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False
    finally:
        driver.quit()

