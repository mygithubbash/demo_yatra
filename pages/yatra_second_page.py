import time
import logging
logging.basicConfig(level=logging.DEBUG, filename="....\pages\demologs.log",filemode="w")
import softest
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SecondPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    TOTALFLIGHT="//div[contains(@class,'flightItem border-shadow pr')]"

    def totlflight(self):
        return self.wait_for_precence_of_all_elements(By.XPATH, self.TOTALFLIGHT)

    def verify_flight_detils(self, frm, to):
        for i in range(1, len(self.totlflight()) + 1):
            time.sleep(1)
            flightname= self.wait_for_precence_of_element(By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')][" + str(i) + "]//div/span[@class='i-b text ellipsis']")
            self.driver.execute_script("arguments[0].scrollIntoView();", flightname)
            fromdtl = self.wait_for_precence_of_element(By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')][" + str(i) + "]//div[@class='grid']//div[@class='i-b col-4 no-wrap text-right dtime col-3']//p[@class='fs-10 font-lightgrey no-wrap city ellipsis']")
            todtl = self.wait_for_precence_of_element(By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')][" + str(i) + "]//div[@class='grid']//div[@class='i-b pdd-0 text-left atime col-5']//p[@class='fs-10 font-lightgrey no-wrap city ellipsis']")
            flightfair = self.wait_for_precence_of_element(By.XPATH,"//div[contains(@class,'flightItem border-shadow pr')][" + str(i) + "]//div[@class='i-b tipsy fare-summary-tooltip fs-18']")
            time.sleep(1)
            #b1=self.soft_assert(self.assertEqual, fromdtl.text, frm)
            assert frm in fromdtl.text and to in todtl.text
            #b2 = self.soft_assert(self.assertEqual, todtl.text, to)

            test = 'Pass'

            print(str(i) + ")       " + flightname.text + "       " + fromdtl.text + "       " + todtl.text + "       " + flightfair.text + "       " + test)

