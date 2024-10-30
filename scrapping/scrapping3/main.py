from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.fullscreen_window()
time.sleep(2)

username_field = driver.find_element(By.NAME, "user-name")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.NAME, "login-button")
login_button.click()

time.sleep(2)

buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for button in buttons:
    # print(button.text)
    time.sleep(1)
    button.click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart.click()

time.sleep(2)

# cart_items = driver.find_elements(By.XPATH, "//div[@class='cart_list']//div")
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
# length = len(cart_items)-1
# print(len(cart_items))

names=[]
desc=[]
costs=[]
images=[]

# i=3
for i in range(3, 9):
    content = driver.find_element(
        By.XPATH, f"/html/body/div/div/div/div[2]/div/div[1]/div[{i}]/div[2]"
    )
    content.find_element(
        By.XPATH, f"/html/body/div/div/div/div[2]/div/div[1]/div[{i}]/div[2]/a"
    ).click()
    time.sleep(2)

    ## scrap the data of each item
    product_name = driver.find_element(
        By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[1]"
    )
    # print(product_name.text)
    product_description = driver.find_element(
        By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[2]"
    )
    # print(product_description.text)
    product_cost = driver.find_element(
        By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[3]"
    )
    # print(product_cost.text)
    product_image = driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[1]/img").get_attribute('src')
    # print(product_image)
    
    names.append(product_name.text)
    desc.append(product_description.text)
    costs.append(product_cost.text)
    images.append(product_image)

    # i=i+1
    back_to_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    back_to_cart.click()

    # driver.back()
    time.sleep(2)


df = pd.DataFrame({
    'name': names,
    'description': desc,
    'cost': costs,
    'image': images
})

df.to_csv('products.csv', index=False)

input("Press enter to continue...")
driver.close()
