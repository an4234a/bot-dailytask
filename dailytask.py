from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.notifications": 1 
  })
driver = webdriver.Chrome(chrome_options=opt, executable_path='/Users/alannurcahyo/Documents/Documents/chromedriver')
driver.get("https://office.kemenkeu.go.id/index/index")
driver.find_element_by_id('Username').send_keys('198803022009121002')
driver.find_element_by_id('Password').send_keys('198803022009121002')
driver.find_element_by_xpath("//input[@type='submit' and @value='Log in / Registrasi']").click()
driver.get("https://office.kemenkeu.go.id/nadine/mytask/add")
time.sleep(2)
driver.find_element_by_id("mat-radio-32").click()
driver.find_element_by_id("mat-input-0").send_keys('belajar')
driver.find_element_by_id("mat-input-1").send_keys('belajar mandiri')
driver.find_element_by_xpath("//span[@class='ngx-timepicker-control__arrow'][1]").click()
driver.find_element_by_xpath("(//span[@class='ngx-timepicker-control__arrow'][1])[3]").click()
driver.find_element_by_xpath("(//span[@class='ngx-timepicker-control__arrow'][1])[3]").click()
driver.find_element_by_id("mat-input-2").send_keys('360')
time.sleep(1)
driver.find_element_by_xpath("//button[@class='save mat-flat-button mat-accent']").click()
driver.get("https://office.kemenkeu.go.id/nadine/mytask/add")
time.sleep(5)
driver.find_element_by_xpath("//button[@class='send mat-raised-button mat-accent']").click()


