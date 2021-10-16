from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def getPrice(ingredients_to_input):
    # Initializes Chrome Driver
    service1 = webdriver.chrome.service.Service(ChromeDriverManager().install())
    chrome_options1 = webdriver.chrome.options.Options().add_experimental_option("detach", True)
    browser1 = webdriver.Chrome(service=service1, options=chrome_options1)

    browser1.maximize_window()
    browser1.get("https://www.loblaws.ca/")

    WebDriverWait(browser1, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "search-input__input")))
    price_list = []

    for ingredient in ingredients_to_input:
        search_item = ingredient

        # Enters ingredients
        searchBox = browser1.find_element(By.CLASS_NAME, "search-input__input")
        searchBox.send_keys(Keys.COMMAND + "a")
        searchBox.send_keys(Keys.DELETE)
        searchBox.send_keys(search_item)
        searchBox.send_keys(Keys.ENTER)

        # Extracts price
        WebDriverWait(browser1, 3).until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='price selling-price-list__item__price "
                       "selling-price-list__item__price--now-price']")))
        price = browser1.find_element(
            By.XPATH, "//span[@class='price selling-price-list__item__price "
                      "selling-price-list__item__price--now-price']").text
        price_list.append(price)

    return price_list


def getIngredients(search_terms):
    # Initializes Chrome Driver
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    chrome_options = webdriver.chrome.options.Options().add_experimental_option("detach", True)
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()

    # Loads webpage and searches for search_Term
    browser.get("https://www.yummly.com/recipes")
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "searchbox-input")))
    searchBar = browser.find_element(By.ID, "searchbox-input")
    searchBar.send_keys(search_terms)
    searchBar.send_keys(Keys.ENTER)

    # Waits until results appear then select the first one
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='recipe-card-img-wrapper']")))
    firstItem = browser.find_element(By.XPATH, "//div[@class='recipe-card-img-wrapper']") \
        .find_element(By.TAG_NAME, "a")
    browser.execute_script("arguments[0].click();", firstItem)

    # Waits until ingredients load then collects all of the ingredients
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ingredient']")))
    ingredients = browser.find_elements(By.XPATH, "//span[@class='ingredient']")
    ingredients_list = []
    for k in range(len(ingredients)):
        ingredients_list.append(ingredients[k].text)

    # Get name of food, time needed to make food, calories of food
    food_name = browser.find_element(By.TAG_NAME, "h1").text
    time = " ".join([k.text for k in browser.find_element(
        By.XPATH, "//div[@class='recipe-summary-item unit h2-text']").find_elements(By.TAG_NAME, "span")])
    nutrition = " ".join([k.text for k in browser.find_element(
        By.XPATH, "//div[@class='recipe-summary-item nutrition h2-text']").find_elements(By.TAG_NAME, "span")])

    # Generates dictionary to return
    info = {'name': food_name, 'time': time, 'nutrition': nutrition, 'ingredients': ingredients_list}

    # Closes browser
    browser.quit()

    return info
