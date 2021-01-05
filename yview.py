import time
import random
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)


videos = [
    'https://gestyy.com/erOJjz',
    'http://gestyy.com/er4PZD',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZV',
    'http://gestyy.com/er4PZ7',
    'http://gestyy.com/er4PXw',
    'http://gestyy.com/er4PXu',
    'http://gestyy.com/er4PXu',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
    'http://gestyy.com/er4PZK',
]

sleep_time = 0

for i in range(1000):
    print("Watching for {} time".format(i))
    for j in range(25):
        random_video=j
        driver.get(videos[random_video])
        time.sleep(7)
        skip = driver.find_element_by_xpath("//span[@id='skip_button']")
        skip.click()
     # Let the user actually see something!
        driver.quit()
        time.sleep(6) # Let the user actually see something!
