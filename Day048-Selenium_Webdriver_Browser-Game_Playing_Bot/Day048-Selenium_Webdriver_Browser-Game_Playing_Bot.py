# Selenium Webdriver Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# With Chrome
service = Service("C:\\SeleniumDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# With Brave
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
service = Service("C:\\SeleniumDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service, chrome_options=option)

# With Firefox
service = Service("C:\\SeleniumDrivers\\geckodriver.exe")
driver = webdriver.Firefox(service=service)

# With Edge
service = Service("C:\\SeleniumDrivers\\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Scraping Amazon
driver.get("https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=lp_16225009011_1_2")

# Find an element by ID
price = driver.find_element(By.ID, "priceblock_ourprice")
print(price.text)

# Scraping Python
driver.get("https://www.python.org/")

# Find an element by NAME
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# Find an element by CLASS_NAME
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

# Find an element by CSS_SELECTOR
documentation_link = driver.find_elements(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link[0].text)

# Find an element by XPATH
issue_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(issue_link.text)

# Find multiple elements
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

# Scraping Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find an element by LINK_TEXT
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
all_portals.click()

# Click on a link
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
article_count.click()

# Type text into an input field and send a keyboard key
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys("werwer")
last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.send_keys("werwer")
email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.send_keys("werwer@sdfsdf.com")
sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.click()

# Day 48 Project - Game Playing Bot
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\SeleniumDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
timeout = time.time() + 9
five_min = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in items[::-1]:
            try:
                if not item.get_attribute("class"):
                    item.click()
            except StaleElementReferenceException:
                items = driver.find_elements(By.CSS_SELECTOR, "#store div")

        timeout = time.time() + 9

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()
