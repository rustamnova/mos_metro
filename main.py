from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up Chrome driver and navigate to website
driver = webdriver.Chrome()
driver.get('https://www.moscowmap.ru/metro.html')

try:
    # Wait for the departure input field to appear and enter text
    departure_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/form[2]/div/div[3]/input')))
    departure_input.clear()
    departure_input.send_keys('Медведково')

    # Wait for the arrival input field to appear and enter text
    arrival_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/form[2]/div/div[6]/input')))
    arrival_input.clear()
    arrival_input.send_keys('Марксистская')

    # Wait for the search button to appear and click it
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Найти маршрут"]')))
    search_button.click()

    # Wait for the search results to appear
    search_results = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="search-page-block"]')))
    print(search_results.text)

except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

except NoSuchElementException:
    print("Element not found")
    driver.quit()

finally:
    driver.quit()
