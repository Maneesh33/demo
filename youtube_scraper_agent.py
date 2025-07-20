from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()  # Try system PATH
except:
    chromedriver_path = r"C:\Users\Anju\Downloads\chromedriver-win64"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.youtube.com")
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("robotics tutorials")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    videos = driver.find_elements(By.ID, "video-title")[:5]
    if not videos: raise Exception("No titles found")
    with open("robotics_videos.txt", "w", encoding="utf-8") as f:
        for i, video in enumerate(videos, 1):
            title = video.text.strip()
            if title: f.write(f"{i}. {title}\n"); print(f"{i}. {title}")
    print("Scraping completed successfully!")
except Exception as e:
    print(f"Error: {e}")
    print("Check ChromeDriver path, Chrome version, or internet connection.")
finally:
    if 'driver' in locals(): driver.quit()