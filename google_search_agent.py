from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

try:
    # Specify ChromeDriver path (update this to your exact location)
    chromedriver_path = "C:\Users\Anju\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    
    # Set up Chrome driver
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Find search bar, type query, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("robotics")
    search_box.send_keys(Keys.RETURN)
    
    # Wait to see results
    time.sleep(2)
    print("Search completed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    print("Check ChromeDriver path, Chrome version, or internet connection.")
    
finally:
    # Close browser
    driver.quit()