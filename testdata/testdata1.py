import pytest
import softest
import conftest
from pytest import fixture
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import ddt

# v2
# v33
# v34
from pages.yatra_first_page import FirstPage
from selenium.webdriver.common.keys import Keys
from utilities.utils import utils
from ddt import ddt, data, unpack, file_data

@pytest.mark.usefixtures("setup")
#@ddt
class Testyatra(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.fp = FirstPage(self.driver)
    #@file_data("C:\\Users\\ISHAN CHARDE\\PycharmProjects\\E2E_Make_My_Trip\\testdata\\data.csv")

    #@data("22/02/2023","Delhi","Mumbai")
    #@unpack
    # @unpack
    def test_search_flight_verify(self):
        sp = self.fp.flightsearch("22/02/2023","Delhi","Mumbai")
        time.sleep(10)
        sp.verify_flight_detils("Delhi","Mumbai")



