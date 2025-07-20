from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Try to use system PATH first, fall back to explicit path if needed
try:
    # Attempt with system PATH (no explicit path)
    driver = webdriver.Chrome()
except Exception as e:
    # If that fails, use the explicit ChromeDriver path
    chromedriver_path = r"C:\Users\Anju\Downloads\chromedriver-win64" 
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find search bar, type query, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("chatgpt")
    search_box.send_keys(Keys.RETURN)
    
    # Wait to see results
    time.sleep(2)
    print("Search completed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    print("Check ChromeDriver path, Chrome version, or internet connection.")
    
finally:
    # Ensure driver is closed only if it was created
    if 'driver' in locals():
        driver.quit()