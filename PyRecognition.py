import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class PyRecognition:
    driver = ''
    last = ''

    def __init__(self, language):
        path = './chromedriver.exe'
        option = Options()

        option.add_experimental_option("prefs", {\
            "profile.default_content_setting_values.media_stream_mic": 1
            })

        option.headless = False;
        self.driver = webdriver.Chrome(path,0,option)
        self.driver.set_window_position(0,0)
        self.driver.set_window_size(200,200)
        engine = os.getcwd() + '/Engine/engine.html'  
        self.driver.get(engine)
        time.sleep(5)
        self.driver.execute_script("document.getElementById('lg').innerHTML = '" + language + "';")

    def recognition(self):
        while True:
            speech = self.driver.find_element("id", "resultSpeak").text

            if speech != 'error' and speech != 'on' and speech != '' and speech != self.last:
                self.last = speech
                return speech

            self.last = speech




