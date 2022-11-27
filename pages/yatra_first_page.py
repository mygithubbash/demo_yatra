import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.yatra_second_page import SecondPage


class FirstPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    DEPART_FROM_LOCATOR="//input[@id='BE_flight_origin_city']"
    GOING_TO_LOCATOR="//input[@id='BE_flight_arrival_city']"
    LIST_OF_GOING_TO="//div[@class='viewport']//li/div/p[@class='ac_cityname']"
    CLICK_ON_DATE_FIELD="//input[@id='BE_flight_origin_date']"
    ALLDATES="//div[@id='monthWrapper']//tbody/tr/td[@class!='inActiveTD' and @class!='inActiveTD weekend']"

    def depart(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.DEPART_FROM_LOCATOR)
    def goingto(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.GOING_TO_LOCATOR)
    def listofgoingto(self):
        return self.wait_for_precence_of_all_elements(By.XPATH, self.LIST_OF_GOING_TO)
    def clickondatefield(self):
        return self.driver.find_element(By.XPATH, self.CLICK_ON_DATE_FIELD)
    def getalldates(self):
        return self.wait_until_element_to_be_clickable(By.XPATH,self.ALLDATES).find_elements(By.XPATH, self.ALLDATES)

    def depart_from(self):
        self.depart().click()
        self.depart().send_keys('Delhi')
        self.depart().send_keys(Keys.ENTER)
        time.sleep(2)

    def going_to(self):
        self.goingto().click()
        self.goingto().send_keys('New')
        for i in self.listofgoingto():
            if "New York (NYC)" in i.text:
                i.click()
                break

    def all_dates(self, departdate):
        self.clickondatefield().click()
        for dt in self.getalldates():
            if dt.get_attribute("data-date") == departdate:
                dt.click()
                time.sleep(5)
                break
        time.sleep(5)

    def select_recent_flight(self, frm, to):
        elem=self.driver.find_element(By.XPATH, "//div[@class='VueCarousel-inner']//a[@class='VueCarousel-slide items' and @title='" + frm + " to " + to + "']")
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def flightsearch(self, departdate, frm, to):
        self.depart()
        self.goingto()
        self.all_dates(departdate)
        self.select_recent_flight(frm, to)
        searchresult=SecondPage(self.driver)
        return searchresult




