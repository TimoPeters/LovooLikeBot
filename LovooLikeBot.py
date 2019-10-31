from selenium import webdriver
import time
import json

with open('LoginData.json') as file:
    loginData = json.load(file)
login_email = loginData["email"]
login_password = loginData["password"]

# navigate to lovoo.com
driver = webdriver.Firefox()
driver.get("https://de.lovoo.com/")
print("navigate to Lovoo-Website")

# click "Einloggen"-Button
login_button_1 = driver.find_element_by_xpath('//button[text()="Einloggen"]')
login_button_1.click()
print("click login button")
time.sleep(3)

# fill in Email and Password text fields and submit to log in
email_text_field = driver.find_element_by_name("authEmail")
password_text_field = driver.find_element_by_name("authPassword")
login_button_2 = driver.find_element_by_xpath("//form[@id='form']/div/div/button")
email_text_field.send_keys(login_email)
print("fill Email")
password_text_field.send_keys(login_password)
print("fill Password")
login_button_2.click()
print("submit login formular")
time.sleep(3)

# navigate to game
driver.get("https://de.lovoo.com/match")
time.sleep(3)
print("navigate to game page")

accept_cookies_button = driver.find_element_by_css_selector("span[data-automation-id='vote-yes-button']")
#press vote yes button in a loop
while True:
    vote_yes_button = driver.find_element_by_css_selector("span[data-automation-id='vote-yes-button']")
    try:
        vote_yes_button = driver.find_element_by_css_selector("span[data-automation-id='vote-yes-button']")
        vote_yes_button.click()
        print("Like Profile")
        time.sleep(2)
    except:
        driver.get("https://de.lovoo.com/match")
        print("reloading match page")
        time.sleep(3)
