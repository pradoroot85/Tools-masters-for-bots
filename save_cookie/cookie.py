from selenium import webdriver
import os
import time
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}".format(profile))

browser = webdriver.Chrome("./chromedriver", chrome_options=options)

browser.get("https://web.whatsapp.com")

