import time
from selenium import webdriver
from selenium.webdriver.common.by import By

service = webdriver.ChromeService("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome(service=service)
query = "laptops"
file = 1
for i in range(1, 20):
    driver.get(
        f"https://www.amazon.in/s?k={query}&page={i}&crid=3KHNT4HXJ08W6&sprefix=laptops%2Caps%2C524&ref=nb_sb_noss_2"
    )
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(len(elems))
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1

time.sleep(5)
driver.close()
