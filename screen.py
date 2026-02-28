from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logging
import time

def main():
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")
	# browser = webdriver.Chrome(options=options, service=service)

	options = webdriver.FirefoxOptions()
	options.add_argument("--headless")
	service = webdriver.FirefoxService(executable_path="/usr/bin/geckodriver")
	browser = webdriver.Firefox(options=options, service=service)

	browser.implicitly_wait(10)
	# logger = logging.getLogger("selenium")
	# logger.log(level=logging.DEBUG)

	# i = input()
	i = "https://www.amazon.com/portable-ultrasound/s?k=portable+ultrasound"
	browser.get(i)
	
	page_load(5)
	# input = browser.find_element_by_id('kw')
	# input.send_keys('Python')
	# input.send_keys(Keys.ENTER)
	# wait = WebDriverWait(browser, 10)
	# wait.until(EC.presence_of_element_located((By.ID, "content_left")))
	# print(browser.current_url)
	# print(browser.get_cookies())
	# browser.save_screenshot("screen.png")
	browser.save_full_page_screenshot("screen.png")
	# save_file(browser.get_screenshot_as_png(), "screen.png")
	# print(browser.page_source)
	browser.close()

def page_load(t):
	time.sleep(t)

def save_file(data, name):
	f = open(name, "+bw")
	f.write(data)
	f.close()

if __name__ == "__main__":
	main()

