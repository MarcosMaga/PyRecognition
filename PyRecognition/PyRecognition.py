import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = './chromedriver.exe'
option = Options()

option.add_experimental_option("prefs", {\
    "profile.default_content_setting_values.media_stream_mic": 1
    })

option.headless = False;
driver = webdriver.Chrome(path,0,option)
driver.set_window_position(0,0)
driver.set_window_size(200,200)


def recognition(language):
    
    engine = os.getcwd() + '/Engines/' + str(language) + '.html'  
    driver.get(engine)
    time.sleep(5)

    while True:
        speech = driver.find_element_by_id("resultSpeak").text

        if speech != 'error' and speech != 'on' and speech != '':
            return speech




