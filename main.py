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
rounds = 0
bumps = 0


def clear(): return os.system('cls')


def main_menu():
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2 - Main Menu")
    print("@2leo Autobumper v1.2 - Main Menu\n\n\n")
    print("[1] Start")
    print("[2] Threads")
    print("[3] Mybbuser")
    print("[4] Chromedriver")


def thread_menu():
    global ogusersmybbuser, chromedriver
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2 - Thread Menu")
    print("@2leo Autobumper v1.2 - Thread Menu\n\n\n")
    data = json.load(open("config.json", "r"))
    ogusersmybbuser = (data["ogusersmybbuser"])
    chromedriver = (data["chromedriver"])
    threadurls = []
    threads = input("How many threads do you want to bump?: ")
    for x in range(int(threads)):
        threadurl = input("Thread URL " + str(x + 1) + ": ")
        threadurls.append(threadurl)
    data = {"threads": threads, "threadurls": threadurls,
            "ogusersmybbuser": ogusersmybbuser, "chromedriver": chromedriver}
    f = open("config.json", "w+")
    f.write(json.dumps(data))
    main_menu()


def mybbuser_menu():
    global threads, threadurls, chromedriver
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2 - Cookie Menu")
    print("@2leo Autobumper v1.2 - Cookie Menu\n\n\n")
    data = json.load(open("config.json", "r"))
    threads = (data["threads"])
    threadurls = (data["threadurls"])
    chromedriver = (data["chromedriver"])
    ogusersmybbuser = ""
    ogusersmybbuser = input("Your \"ogusersmybbuser\" cookie: ")
    data = {"threads": threads, "threadurls": threadurls,
            "ogusersmybbuser": ogusersmybbuser, "chromedriver": chromedriver}
    f = open("config.json", "w+")
    f.write(json.dumps(data))
    main_menu()


def chromedriver_menu():
    global threads, threadurls, ogusersmybbuser
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2 - Chromedriver Menu")
    print("@2leo Autobumper v1.2 - Chromedriver Menu\n\n\n")
    data = json.load(open("config.json", "r"))
    threads = (data["threads"])
    threadurls = (data["threadurls"])
    ogusersmybbuser = (data["ogusersmybbuser"])
    chromedriver = ""
    chromedriver = input(r'Path of your chrome driver (replace \ with \\)')
    data = {"threads": threads, "threadurls": threadurls,
            "ogusersmybbuser": ogusersmybbuser, "chromedriver": chromedriver}
    f = open("config.json", "w+")
    f.write(json.dumps(data))


def first_time_setup():
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2 - First Time Setup")
    print("@2leo Autobumper v1.2 - First Time Setup")
    print("\n\n\n")
    threads = input("How many threads do you want to bump?: ")
    for x in range(int(threads)):
        threadurl = input("Thread URL " + str(x + 1) + ": ")
        threadurls.append(threadurl)
    ogusersmybbuser = input("Your \"ogusersmybbuser\" cookie: ")
    chromedriver = input(r'Path of your chrome driver (replace \ with \\)')
    data = {"threads": threads, "threadurls": threadurls,
            "ogusersmybbuser": ogusersmybbuser, "chromedriver": chromedriver}
    f = open("config.json", "w+")
    f.write(json.dumps(data))


def get_info():
    global data, ogusersmybbuser, cookies, delay, threadurls, chromedriver, threads
    data = json.load(open("config.json", "r"))
    ogusersmybbuser = (data["ogusersmybbuser"])
    chromedriver = (data["chromedriver"])
    threadurls = (data["threadurls"])
    threads = (data["threads"])
    cookies = {
        'ogusersmybbuser': ogusersmybbuser}


def bump():
    global threadurls, delay, rounds, bumps, chromedriver
    get_info()
    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.get("https://ogusers.com/Leo")
    driver.add_cookie(
        {'name': 'mybbuser', 'value': str(ogusersmybbuser)})
    ctypes.windll.kernel32.SetConsoleTitleW(
        "@2leo Autobumper v1.2")
    print("@2leo Autobumper v1.2")
    while True:
        rounds += 1
        for i in range(int(threads)):
            driver.get(threadurls[i])
            randomno = random.randrange(1, 10000000000000)
            message = "Bumped by Leo's autobumper! " + str(randomno)
            try:
                messagebox = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable(
                        (By.ID, "message"))
                )
            except TimeoutException:
                print("Element not interactable")
                quit()
            if rounds == 1:
                messagebox.send_keys(message)
            sleep(5)
            driver.find_element_by_xpath(
                "//*[@id=\"quick_reply_submit\"]").click()
            print("Bumped " + threadurls[i] + "!")
            bumps += 1
            if bumps == int(threads) or bumps % int(threads) == 0:
                if not bumps == 0 or 1:
                    print("Waiting...")
                    bumps = 0
                    sleep(int(delay))
            else:
                sleep(60)


if not os.path.isfile("config.json"):
    first_time_setup()
else:
    get_info()
    main_menu()
    menu = input("")
    if menu == "1":
        delay = input("Delay for bumping in seconds (recommended 1920): ")
        bump()
    elif menu == "2":
        thread_menu()
    elif menu == "3":
        mybbuser_menu()
    elif menu == "4":
        chromedriver_menu()
