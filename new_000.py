import time
import random
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

videos = [
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
    'https://www.youtube.com/watch?v=id0ctEN-7Q0',
]

sleep_time = 0

for i in range(1000):
    print("Watching for {} time".format(i))
    random_video = random.randint(0,5)
    driver.get(videos[random_video])
    time.sleep(sleep_time) # Let the user actually see something!
    sleep_time = random.randint(11, 13)

    time.sleep(5) # Let the user actually see something!
driver.quit()