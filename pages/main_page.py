from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium, pytest
from faker import Faker
import re
from pages.base_page import BasePage



class TestSteamHomePage(BasePage):
    TIMEOUT = 5

    MAIN_LOGO = (By.XPATH, "//div[@class='logo']//img")
    HEADER_NAVIGATION = (By.XPATH, "//div[@class='content']//div[@class='supernav_container']")
    HEADER_GLOBAL_ACTIONS = (By.XPATH, "//div[@*='global_actions']")
    STORE_NAV_DIV = (By.XPATH, "//div[@class='store_nav']")
    HOME_PAGE_MENU = (By.XPATH, "//div[@class='home_page_gutter']")
    RECOMMENDATION_TEXT = (By.XPATH, "//h2[@*='home_featured_and_recommended']")
    RECOMMENDATION_CAROUSEL = (By.XPATH, "//div[@class='carousel_container maincap']")
    RECOMMENDATION_IMAGE = (By.XPATH, "//div[@class='carousel_container maincap']")


    def get_image_url(self):
        element = self.browser.find_element(*self.RECOMMENDATION_IMAGE)
        style = element.get_attribute("style")

        # Достаем URL из background-image
        match = re.search(r'url\(["\']?(.*?)["\']?\)', style)
        if match:
            url = match.group(1)
            print(f"Image URL: {url}")
            return url
        else:
            print("No image found in style")
            return None

    def test_home_page(self, browser):
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.MAIN_LOGO))
        print("MAIN_LOGO element found")
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.HEADER_NAVIGATION))
        print("HEADER_NAVIGATION element found")
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.HEADER_GLOBAL_ACTIONS))
        print("HEADER_GLOBAL_ACTIONS element found")
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.STORE_NAV_DIV))
        print("STORE_NAV_DIV element found")

        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.HOME_PAGE_MENU))
        print("HOME_PAGE_MENU element found")
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.RECOMMENDATION_TEXT))
        print("RECOMMENDATION_TEXT element found")
        WebDriverWait(browser, self.TIMEOUT).until(EC.visibility_of_element_located(self.RECOMMENDATION_CAROUSEL))
        print("RECOMMENDATION_CAROUSEL element found")

        self.get_image_url(browser)



