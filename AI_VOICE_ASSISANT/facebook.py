from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

usr="gowthamanspear420@gmail.com"
pwd="!gowthaman@#420!"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element(By.ID,'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element(By.ID,'pass') #find_element(By.XPATH, ‘xpath’)
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element(By.NAME,'login')
login_box.click()
#type="search"
#search = driver.find_element(By.TYPE,'search')
#search=driver.find_element(By.CSS_SELECTOR,"h1>span")
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
