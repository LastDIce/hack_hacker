from make_dummy import *
from make_random import *
from selenium import webdriver

def driver_load():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	options.add_argument("lang=ko_KR")
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
	driver = webdriver.Chrome('./chromedriver', chrome_options=options)
	driver.get('about:blank')
	driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
	driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
	driver.implicitly_wait(3)
	return driver

if __name__ == '__main__':
	for i in range(1,10000):
		try:
			driver = driver_load()
			print("############## " + str(i) + " 번째 ##############")
			fid = random_id_pw()
			fpw = random_id_pw()
			name = random_name()
			price = random_price()
			s_price = random_small_price()
			munsang_list = random_munsang()
			sign_up(driver, fid, fpw)
			login(driver, fid, fpw)
			flag = random.choice([0,1,2,3])
			if flag == 1 or flag == 3:
				charge_req(driver, name, price)
				print("1. 허위 입금 정보 주입!")
			if flag == 2 or flag == 3:
				munsang_req(driver, s_price, munsang_list)
				print("2. 허위 문상 충천 정보 주입!")
			driver.quit()
		except Exception as e:
			print("실패")
			print(e)
			continue
		finally:
			print("------------------------------------------")
			print("ID : [" + fid + "]")
			print("PW : [" + fpw + "]")
			print("가명 : [" + name + "]")
			print("충전가격 : [" + price + "]")
			print("문상충전가격 : [" + s_price + "]")
			print("문상번호 : [" + "-".join(munsang_list) + "]")
