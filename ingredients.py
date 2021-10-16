from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

searchTerms = "Lemon Shrimp Pasta"
browser = webdriver.Chrome
browser.get("https://www.allrecipes.com/")
search = browser.find_element_by_id("primary-search")
search.send_keys(searchTerms)
searchButton = browser.find_element_by_title("Search")
searchButton.click()
wait = WebDriverWait(browser, 5)
print(browser.title)