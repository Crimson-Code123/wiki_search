from selenium import webdriver
import logging
import selenium

options = webdriver.ChromeOptions()
options.add_argument("headless")
# options.add_argument("window-size=0,0")
service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")

browser = webdriver.Chrome(options=options, service=service)
# browser = webdriver.Chrome(service=service)
# logger = logging.getLogger("selenium")
# logger.log(level=logging.DEBUG)
try:
    browser.get('https://google.com')
    # input = browser.find_element_by_id('kw')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    # print(browser.page_source)
finally:
    pass
    # browser.close()

