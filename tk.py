import tkinter as tk
from selenium import webdriver
import time


def englishtotamilapi(s):
   op = webdriver.ChromeOptions()
   op.add_argument('headless')
   driver = webdriver.Chrome(options=op)
   driver.get('http://www.google.com/');
   time.sleep(1) # Let the user actually see something!
   search_box = driver.find_element_by_name('q')
   search_box.send_keys(str(s)+" meaning in tamil")
   search_box.submit()
   search_box = driver.find_element_by_class_name("hrcAhc")
   r = search_box.text
   driver.quit()
   return r
    
   

t = englishtotamilapi("rich")
print(t)

