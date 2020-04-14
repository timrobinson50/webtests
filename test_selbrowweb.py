import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_1_connect():
    driver = webdriver.Chrome('/home/tarobin/projects/selen/chromedriver')  # Optional argument, if not specified will search path.

    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")
    driver.set_window_size(1400, height-100)

    driver.get('http://www.google.com/')

    try:
        element = WebDriverWait(driver, 15).until(EC.title_contains("Google"))
    except:
        print("Some sort of timeout exception")
        # try a restart
        driver.close()
        driver.get('http://www.google.com/')

    assert "Google" in driver.title
    
    #time.sleep(8) # Let the user actually see something!
    # note that name="q" is used on this page and is a popular usage
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!

    opstring = "got here. Width = {} Height = {} element = {}"
    print(opstring.format(width, height, element))

    driver.quit()

def test2_enter_text(): 
    driver = webdriver.Chrome('/home/tarobin/projects/selen/chromedriver')
    
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

    print("got here 2")

    driver.quit()
