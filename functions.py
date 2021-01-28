from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess as sp

sp.Popen('cmd', shell=True)

driver = webdriver.Chrome(executable_path='C:\\bin\\chromedriver.exe')
driver.get("https://10fastfingers.com/typing-test/portuguese")


def digita(qnt_ppm, tempo):
    u = 1
    while u <= int(qnt_ppm):
        target2 = driver.find_element_by_xpath("//*[@id='timer']").text
        if target2 == "0:00":
            break
        else:
            x = "//*[@id='row1']/span[" + str(u) + "]"
            target = driver.find_element_by_xpath(x).text
            target1 = driver.find_element_by_xpath("//*[@id='inputfield']")
            target1.send_keys(target)
            target1.send_keys(Keys.SPACE)
            u += 1
            sleep(float(tempo))


def close():
    driver.close()

