from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

searchTerms = "pizza"
service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.maximize_window()
browser.get("https://www.yummly.com/recipes")
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "searchbox-input")))
searchBar = browser.find_element(By.ID, "searchbox-input")
searchBar.send_keys(searchTerms)
searchBar.send_keys(Keys.ENTER)

WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='recipe-card-img-wrapper']")))
firstItem = browser.find_element(By.XPATH, "//div[@class='recipe-card-img-wrapper']").find_element(By.TAG_NAME, "a")
browser.execute_script("arguments[0].click();", firstItem)
