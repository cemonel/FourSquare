from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(SearchTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SearchTestCase, self).tearDown()

    def test_search(self):
        selenium = self.selenium
        selenium.get("http://127.0.0.1:8000")
        search_location = selenium.find_element_by_id("id_location")
        search_food = selenium.find_element_by_id('id_food')

        submit = selenium.find_element_by_name('search-button')

        search_location.send_keys('istanbul')
        search_food.send_keys('pizza')

        submit.send_keys(Keys.RETURN)

        assert "Results" in selenium.page_source
