from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

searchTerms = "Tuscan Chicken Pasta"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.get("https://www.yummly.com/")
# searchToggle = browser.find_element_by_id("search-modal-searchbox-input")
'''
searchBar = browser.find_element_by_id("search-modal-searchbox-input")
searchBar.send_keys(searchTerms)
searchBar.send_keys(Keys.ENTER)
'''
wait = WebDriverWait(browser, 5)
print(browser.title)