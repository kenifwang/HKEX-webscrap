from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def load_button():
    while True:
        try:
            load_more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.loadmore .load')))
            driver.execute_script("arguments[0].click();", load_more_button)
            time.sleep(0.2)
        except Exception as e:
            print("All data loaded or an error occurred:", e)
            exit