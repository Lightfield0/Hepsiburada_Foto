import traceback
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time,sys,os,random, csv, requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import threading
import time
import pandas as pd
import logging
import csv, random
import coloredlogs
import urllib.parse


def random_wait():
    wait_time = random.uniform(1, 2.8)
    time.sleep(wait_time)

def random_scroll(driver, scrolls=2):
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(scrolls):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(random.uniform(0.5, 1.5))  # sleep for a random time between 0.5 to 1.5 seconds
        body.send_keys(Keys.PAGE_UP)
        time.sleep(random.uniform(0.5, 1.5)) 

tüm_ürünler = []

options = ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
# options.add_argument('--disable-notifications')
# options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-save-password-bubble')
# options.add_argument('--headless')
options.add_argument('--disable-translate')
# options.add_argument('--disable-infobars')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')

driver_path = 'chromedriver.exe'
driver = Chrome(options=options, executable_path=driver_path, use_subprocess=True)
wait = WebDriverWait(driver,50)

for i in range(1,51)[0:2]:
    driver.get(f'https://www.hepsiburada.com/bayan-cantalari-c-60000163?sayfa={i}')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    ürünler = list(map(lambda link: 'https://www.hepsiburada.com'+link["href"], soup.select("a.moria-ProductCard-gyqBb")))

    tüm_ürünler.extend(ürünler)

for ürün in tüm_ürünler:
    # Parse the URL into components
    url_components = urllib.parse.urlparse(ürün)

    # Extract the query parameters
    params = urllib.parse.parse_qs(url_components.query)

    # The 'redirect' parameter contains the URL we're interested in, but it's URL-encoded
    try:
        encoded_url = params['redirect'][0]

        # Decode the URL
        decoded_url = urllib.parse.unquote(encoded_url).split('?')[0]

        print(decoded_url)
    except: pass

    while True:
        try:
            driver.get(ürün)
            element = driver.find_element(By.ID, "productReviewsTab")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            element.click()
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            for foto in soup.find_all("img", class_='product-image',attrs={"data-src": True}):
                    print(foto["data-src"])
            
            for foto in soup.find_all("img", class_='hermes-Image-module-rc3n_sPA6aus4S4MJcuo',attrs={"src": True}):
                print(foto["src"])
            break
        except Exception as e:
            # print("ERROR: ", e)
            print(f"Problematic URL: {ürün}")
            # Parse the URL into components
            url_components = urllib.parse.urlparse(ürün)

            # Extract the query parameters
            params = urllib.parse.parse_qs(url_components.query)

            # The 'redirect' parameter contains the URL we're interested in, but it's URL-encoded
            try:
                encoded_url = params['redirect'][0]

                # Decode the URL
                decoded_url = urllib.parse.unquote(encoded_url).split('?')[0]
                ürün = decoded_url
                print("yeni ürl: ", decoded_url)
            except: pass
            # break
            
driver.close()
