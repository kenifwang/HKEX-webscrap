from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Firefox()
driver.get('https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities?sc_lang=en')
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.table_equities')))

rows = driver.find_elements(By.CSS_SELECTOR, 'table.table_equities tbody tr.datarow')

# Iterating the "Load More" button
while True:
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.loadmore .load')))
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(0.2)
    except Exception as e:
        print("All data loaded or an error occurred:", e)
        break

stock_data = []
for row in rows:
    stock_code = row.find_element(By.CSS_SELECTOR, 'td.code').text
    stock_name = row.find_element(By.CSS_SELECTOR, 'td.name').text
    stock_data.append([stock_code, stock_name])

with open('hk_stocks.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['Stock Code', 'Name'])
    writer.writerows(stock_data)

driver.quit()
