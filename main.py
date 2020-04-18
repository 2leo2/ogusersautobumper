from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import ctypes
import json
import os
import random
from time import sleep

threadurls = []
delay = ""


def first_time_setup():
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.0 - First Time Setup")
    print("@2leo Autobumper v1.0 - First Time Setup")
    threads = input("How many threads do you want to bump? [Max 5]: ")
    for x in range(int(threads)):
        threadurl = input("Thread URL " + str(x + 1) + ": ")
        threadurls.append(threadurl)
    ogusersmybbuser = input("Your \"ogusersmybbuser\" cookie: ")
    chromedriver = input("Path of your chrome driver: ")
    data = {"threads": threads, "threadurls": threadurls,
            "ogusersmybbuser": ogusersmybbuser, "chromedriver": chromedriver}
    f = open("config.json", "w+")
    f.write(json.dumps(data))


def get_info():
    global data, ogusersmybbuser, cookies, delay, threadurls, chromedriver
    data = json.load(open("config.json", "r"))
    ogusersmybbuser = (data["ogusersmybbuser"])
    chromedriver = (data["chromedriver"])
    threadurls = (data["threadurls"])
    cookies = {
        'ogusersmybbuser': ogusersmybbuser}


def bump():
    global threadurls, delay
    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.get("https://ogusers.com/Leo")
    driver.add_cookie(
        {'name': 'mybbuser', 'value': str(ogusersmybbuser)})
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.0")
    print("@2leo Autobumper v1.0")
    while True:
        for x in threadurls:
            driver.get(x)
            randomno = random.randrange(1, 10000000000000)
            message = "Bumped by Leo's autobumper! " + str(randomno)
            try:
                messagebox = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.ID, "message"))
                )
            except TimeoutException:
                print("Element not interactable")
                quit()
            messagebox.send_keys(message)
            sleep(5)
            driver.find_element_by_xpath(
                "//*[@id=\"quick_reply_submit\"]").click()
            print("Bumped " + x + "!")
            sleep(60)
    print("Waiting...")
    sleep(delay)


if not os.path.isfile("config.json"):
    first_time_setup()
else:
    get_info()
delay1 = input("Delay for bumping in minutes: ")
delay = int(delay1)*60
print(delay)
bump()
