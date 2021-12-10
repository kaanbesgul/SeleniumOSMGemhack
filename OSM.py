from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException,ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome(r"C:\Users\kaanb\OneDrive\Masaüstü\Programlar\eclipse\selenium\drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
wait=WebDriverWait(driver,180)

username = "SeleniumExample"
password = "SeleniumExample11"

def login(username,password):

    driver.get("https://en.onlinesoccermanager.com/Login?nextUrl=%2FCareer%3FnextUrl%3D%2FLogin")
    driver.find_element_by_class_name("btn-new").click()
    driver.find_element_by_class_name("btn-alternative").click()
    driver.find_element_by_id("manager-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login").click()
    time.sleep(5)
    driver.refresh()

def watchad():

    driver.find_element_by_css_selector("div.wallet-container.bosscoin-wallet.btn-new.btn-success").click()
    driver.find_element_by_class_name("green-product").click()

    for i in range(5):
        driver.find_element_by_xpath('//*[@id="product-category-free"]/div[2]/div[1]/div').click()
        if len(driver.find_elements_by_id("modal-dialog-alert")) > 0:
            driver.refresh()
            break
        else:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="product-category-free"]/div[2]/div[1]/div')))
            print("First Ads now watched")

def freeFunds():
    driver.find_element_by_css_selector(".wallet-container.clubfunds-wallet.btn-new").click()

    all=driver.find_elements_by_css_selector(".slidee.clearfix>li>div>div")
    for i in all:
        try:
            i.click()
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.col-xs-12.col-h-xs-8.finances-multistep-container')))
        except ElementClickInterceptedException:
            pass

def watchad2():
    driver.get("https://en.onlinesoccermanager.com/BusinessClub")
    for i in range(5):
        driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div').click()
        if len(driver.find_elements_by_css_selector(".row.row-h-xs-24.no-padding.modal-scrollable-content-container")) > 0:
            driver.get("https://en.onlinesoccermanager.com/Dashboard")
            break
        else:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="body-content"]/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div')))
            print("One AD watched")

login(username,password)
watchad()
freeFunds()
watchad2()


