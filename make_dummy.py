import domain
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sign_up(driver, id, pw):
	sign_up_url = "/bbs/lo_join.php?mb_id="+ id +"&mb_password="+ pw
	driver.get(domain.do4 + sign_up_url)
	#WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mbskin")))
	WebDriverWait(driver, 100).until(EC.alert_is_present())
	alert = driver.switch_to.alert
	alert.accept()

def login(driver,id, pw):
	driver.get(domain.do4)
	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mbskin")))
	driver.find_element_by_name("mb_id").send_keys(id)
	driver.find_element_by_name("mb_password").send_keys(pw)
	driver.find_element_by_css_selector('input.btn_submit').click()

def charge_req(driver, name, price):
	driver.get(domain.do4 + domain.charge)
	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.charging_top")))
	driver.find_element_by_name("mb_name").clear()
	driver.find_element_by_name("mb_name").send_keys(name)
	driver.find_element_by_name("price").send_keys(price)
	driver.find_element_by_css_selector('div.charging_footer').click()
	WebDriverWait(driver, 100).until(EC.alert_is_present())
	alert = driver.switch_to.alert
	alert.accept()

def munsang_req(driver, price, number):
	driver.get(domain.do4 + domain.munsang)
	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.charging_top")))
	driver.find_element_by_name("price").send_keys(price)
	driver.find_element_by_name("munsang1[]").send_keys(number[0])
	driver.find_element_by_name("munsang2[]").send_keys(number[1])
	driver.find_element_by_name("munsang3[]").send_keys(number[2])
	driver.find_element_by_name("munsang4[]").send_keys(number[3])
	driver.find_element_by_css_selector('div.charging_footer').click()
	WebDriverWait(driver, 100).until(EC.alert_is_present())
	alert = driver.switch_to.alert
	alert.accept()