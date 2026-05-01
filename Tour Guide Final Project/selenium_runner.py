from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time

def open_map():
    path = os.path.abspath("templates/map.html")
    
    options = Options()
    # options.add_argument("--headless")  # uncomment = no window
    
    driver = webdriver.Chrome(options=options)
    driver.get(f"file:///{path}")
    time.sleep(3)  # let map load
    print("Map opened in browser")
    # driver.quit()  # keep open for demo