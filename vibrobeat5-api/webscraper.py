from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route("/")
def up():
    return "Flask API is up!"

@app.route("/getbpm")
def getbpm():
    #getting song title
    song = request.args.get("song")

    #setting up webscraper
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    driver.get('https://tunebat.com/')

    driver.implicitly_wait(1)

    search_box = driver.find_element(By.TAG_NAME, 'input')
    search_btn = driver.find_element(By.TAG_NAME, 'button')

    search_box.send_keys(song)
    search_btn.click()

    driver.implicitly_wait(1)

    bpm_result = driver.find_elements(By.TAG_NAME, 'p')
    bpm_value = int(bpm_result[2].text)

    driver.quit()

    return jsonify([{"bpm": bpm_value}])