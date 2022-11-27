from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class yatra:
    def window_one(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #driver.implicitly_wait(5)
        driver.get('https://www.yatra.com')
        #explicite wait
        wait = WebDriverWait(driver, 10)
        ac=ActionChains(driver)
        driver.maximize_window()
        time.sleep(2)

        frm='Delhi'
        to='Mumbai'

        #elem = driver.find_element(By.XPATH, "//a[@title='Delhi to Mumbai']//div[@class='origin_destination']")
        elem=driver.find_element(By.XPATH,"//div[@class='VueCarousel-inner']//a[@class='VueCarousel-slide items' and @title='"+frm+" to "+to+"']")
        driver.execute_script("arguments[0].scrollIntoView();", elem)
        driver.execute_script("arguments[0].click();", elem)


        #wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Delhi to Mumbai']//div[@class='origin_destination']"))).click()

        time.sleep(10)
        totalflight=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')]")))
        totalflight=len(totalflight)
        for i in range(1,totalflight+1):
            time.sleep(1)
            flightname=wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')]["+str(i)+"]//div/span[@class='i-b text ellipsis']")))
            driver.execute_script("arguments[0].scrollIntoView();", flightname)
            #flightname = wait.until(EC.presence_of_element_located((By.XPATH, "
            fromdtl = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flightItem border-shadow pr')]["+str(i)+"]//div[@class='grid']//div[@class='i-b col-4 no-wrap text-right dtime col-3']//p[@class='fs-10 font-lightgrey no-wrap city ellipsis']")))
            todtl= wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')]["+str(i)+"]//div[@class='grid']//div[@class='i-b pdd-0 text-left atime col-5']//p[@class='fs-10 font-lightgrey no-wrap city ellipsis']")))
            flightfair= wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')]["+str(i)+"]//div[@class='i-b tipsy fare-summary-tooltip fs-18']")))
            ac.move_to_element(flightfair).perform()
            time.sleep(1)
            if frm in fromdtl.text and to in todtl.text:
                test= 'Pass'
            else:
                test='Fail'
            print(str(i)+")       "+flightname.text+"       "+fromdtl.text+"       "+todtl.text+"       "+flightfair.text+"       "+test)
call = yatra()
call.window_one()