# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import keyboard
import os
from dotenv import load_dotenv

load_dotenv()

EXECUTABLE_PATH = os.getenv("EXECUTABLE_PATH")
optionsChrome = Options()
driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH, chrome_options=optionsChrome)
driver.maximize_window()

driver.get("https://www.aparat.com/v/XzVJu")
keyboard.press_and_release('space')
wait1 = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("xpath", "//span[contains(.,'رد کردن')]")))
wait1 = driver.find_element(By.XPATH, "//span[contains(.,'رد کردن')]")
button1 = driver.find_element(By.XPATH, "//span[contains(.,'رد کردن')]")
button1.click()
time.sleep(5)
wait2 = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("css selector", ".romeo-play-toggle > svg")))
wait2 = driver.find_element(By.CSS_SELECTOR, ".romeo-play-toggle > svg")
button2 = driver.find_element(By.XPATH, "//video")
button2.click()
button3 = driver.find_element(By.CSS_SELECTOR, ".romeo-fullscreen > svg")
button3.click()
