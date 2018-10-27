from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
def test_home ():
    #binary = FirefoxBinary('/usr/bin/firefox')
    #driver = webdriver.Firefox(firefox_binary=binary)
    driver = webdriver.Firefox()
    driver.get("http://162.246.157.132:8000")
    name = driver.find_element_by_id("name")
    about = driver.find_element_by_id("about")
    edu = driver.find_element_by_id("education")
    skills = driver.find_element_by_id("skills")
    work = driver.find_element_by_id("work")
    contact = driver.find_element_by_id("contact")
    assert name != None
    assert about != None
    assert edu != None
    assert skills != None
    assert work != None
    assert contact != None

	
test_home()