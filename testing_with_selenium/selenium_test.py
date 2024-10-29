from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

# this is the resource -----> https://saucelabs.com/resources/blog/selenium-with-python-for-automated-testing

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("testing started")
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
sleep(5)

# get the page title
title = driver.title
print(title)
# test if the title is correct
assert "Swag Labs" in title
print("`title` test passed")

# find elements
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

# test if the login is successful
text = driver.find_element(By.CLASS_NAME, "title").text

assert "products" in text.lower()
print("login test is passed")

### this is the test case to test if the items are added to the cart ###
print("testing add to cart")
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# click three buttons to make the cart values to 3
for btns in add_to_cart_btns[:3]:
    btns.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert "3" in cart_value
print("test passed in adding to cart")

### this is the test case to test if the items are removed or not ###
print("testing to remove the item from cart")
remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in remove_btns[:2]:
    btns.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert "1" in cart_value
print("test passed to remove from the cart")

driver.quit()
