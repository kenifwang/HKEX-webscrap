from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get('https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities?sc_lang=en')


time.sleep(5)

# find the elements containing stock codes and names and update the selectors based on the actual page structure
stocks = driver.find_elements(By.CSS_SELECTOR, 'css_selector_for_stocks')

# extract stock codes and name
stock_data = []
for stock in stocks:
    # stock_code = stock.find_element(By.CSS_SELECTOR, 'css_selector_for_stock_code').text
    # stock_name = stock.find_element(By.CSS_SELECTOR, 'css_selector_for_stock_name').text
    stock_data.append([stock_code, stock_name])

with open('hk_stocks_selenium.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stock Code', 'Name'])
    writer.writerows(stock_data)

driver.quit()
