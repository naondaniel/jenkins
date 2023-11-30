from selenium import webdriver
from time import sleep
mydriver = webdriver.Chrome()
mydriver.get("file:///C:/Users/kovia/PycharmProjects/TipCalc/index.html")
billamt = mydriver.find_element("id", "billamt").send_keys("100")
service = mydriver.find_element("id", "serviceQual").send_keys(30)
numOfPeople = mydriver.find_element("id", "peopleamt").send_keys(3)
music = mydriver.find_element("id", "music").send_keys(2)
calculate = mydriver.find_element("id", "calculate").click()
# mydriver.find_element("xpath", "//*[@id=\"serviceQual\"]").click()
# Testing:
expected = "14.00"
actual = mydriver.find_element("id", "tip").text
assert expected == actual

sleep(5)