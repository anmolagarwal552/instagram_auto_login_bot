from selenium import webdriver
import time

driver = webdriver.Firefox()

def login(usr,pss):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    usr_ent.clear()
    usr_ent.send_keys(usr)
    time.sleep(2)

    pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    pss_ent.clear()
    pss_ent.send_keys(pss)
    time.sleep(2)

    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
    login.click()
    time.sleep(2)

login("beelogger386","PowerisPower")