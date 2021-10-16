from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

searchTerms = "Tuscan Chicken Pasta"
service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.maximize_window()
browser.get("https://www.yummly.com/recipes")
searchBar = browser.find_element(By.XPATH, "//input[@id='searchbox-input']")
searchBar.send_keys(searchTerms)
searchBar.send_keys(Keys.ENTER)
