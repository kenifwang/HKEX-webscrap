from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get('https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities?sc_lang=en')
wait = WebDriverWait(driver, 20)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.table_equities')))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table_equities tbody tr.datarow')))

while(True):
    try:
            load_more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.loadmore .load')))
            driver.execute_script("arguments[0].click();", load_more_button)
            time.sleep(0.3)
    except Exception as e:
            print("All data loaded or an error occurred:", {e})
            break

stock_data = []
try:
    tbody = driver.find_element(By.XPATH, '//*[@id="lhkexw-equities"]/div/main/section/div[3]/table/tbody')
    for tr in tbody.find_elements(By.XPATH, './/tr[contains(@class, "datarow")]'):
        stock_code_element = tr.find_element(By.XPATH, './/td[contains(@class, "code")]')
        stock_name_element = tr.find_element(By.XPATH, './/td[contains(@class, "name")]')
        stock_code = stock_code_element.text.strip() if stock_code_element else ''
        stock_name = stock_name_element.text.strip() if stock_name_element else ''
        if stock_code and stock_name:
            stock_data.append([stock_code, stock_name])
except Exception as e:
    print(f"An error occurred: {e}")

with open('hk_stocks.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['Stock Code', 'Name'])
    writer.writerows(stock_data)

driver.quit()

data = pd.read_csv('hk_stocks.csv')
data['Stock Code'] = pd.to_numeric(data['Stock Code'], errors='coerce', downcast='integer')
data_sorted = data.sort_values(by='Stock Code', ascending=True).reset_index(drop=True)
data_sorted.to_csv('hk_stocks_sorted.csv', index=False)