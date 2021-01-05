from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/@10.0288971,76.3058324,14z?authuser=1')
time.sleep(3)
driver.get('https://www.google.com/maps/@10.0288971,76.3058324,14z?authuser=2')
time.sleep(3)
driver.get('https://www.google.com/maps/@10.0288971,76.3058324,14z?authuser=3')
time.sleep(3)
driver.get('https://www.google.com/maps/@10.0288971,76.3058324,14z?authuser=4')
fn.send_keys('abhilash')
ln = driver.find_element_by_id("lastName")
ln.send_keys('james')
gid = driver.find_element_by_id("username")
gid.send_keys('aj904848')
pas = driver.find_element_by_name('Passwd')
pas.send_keys('abhi@123')
cpas = driver.find_element_by_name('ConfirmPasswd')
cpas.send_keys('abhi@123')
bt = driver.find_element_by_class_name("VfPpkd-RLmnJb")
bt.click()
ph = driver.find_element_by_id("phoneNumberId")
ph.send_keys('8129451866')
bt = driver.find_element_by_class_name("VfPpkd-RLmnJb")
bt.click()
