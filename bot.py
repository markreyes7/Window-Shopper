import selenium
import Item
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/Users/mark/chromedriver"
driver = webdriver.Chrome(PATH)

websites = ["https://www.target.com/"]
items = ["pokemon cards", "chips", "ice cream", "tartar sauce"]


class Bot:

    def get_website(self):
        global websites
        websites = websites[0]
        return websites

    def visit_website(self, url):
        driver.get(url)

    def search(self):
        search = driver.find_element_by_id("search")
        print("Here are your last searches: ")
        for i in items:
            print(i, end=' ')
        user_input = input("What would you like to search for?")
        if user_input.lower() in items:
            search.send_keys(user_input, Keys.ENTER)

    def is_in_Stock(self):
        try:
            is_green_text = driver.find_element_by_class_name("h-text-greenDark h-text-bold")
        except:
            print("Not in stock")
