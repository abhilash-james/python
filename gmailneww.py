from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--private")
driver = webdriver.Firefox(firefox_options=firefox_options)

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S353055271%3A1607697975194007&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
time.sleep(3)
fn = driver.find_element_by_class_name("whsOnd.zHQkBf")
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
ph.send_keys('8848901330')
bt = driver.find_element_by_class_name("VfPpkd-RLmnJb")
bt.click()
