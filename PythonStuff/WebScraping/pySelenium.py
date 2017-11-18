from selenium import webdriver
import time


browser = webdriver.Chrome()
# browser.get('https:i-out.io')
# browser.close()
browser.get('http://inventwithpython.com')
link = browser.find_element_by_link_text('Read It Online')
link.click()
# browser.close()

# submitting form
browser.get('https://mail.yahoo.com')
email = browser.find_element_by_id('login-username')
email.send_keys('chhatrachhorm@yahoo.com')
email.submit()

time.sleep(30)
password = browser.find_element_by_id('login-passwd')
password.send_keys('i-out-team')
password.submit()
