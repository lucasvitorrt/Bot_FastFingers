from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\bin\\chromedriver.exe')
driver.get("https://10fastfingers.com/typing-test/portuguese")
sleep(7)

t = 1
u = 1
x = ''

while t <= 305:
    x = "//*[@id='row1']/span[" + str(u) + "]"
    target = driver.find_element_by_xpath(x).text
    target1 = driver.find_element_by_xpath("//*[@id='inputfield']")
    target1.send_keys(target)
    target1.send_keys(Keys.SPACE)
    u += 1
    t += 1
