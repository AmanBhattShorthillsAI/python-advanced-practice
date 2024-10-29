from os import chdir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://tumblershop.com/")

# title = driver.title
# print(title)

try:
    driver.implicitly_wait(30)

    # to get to the Tumbler page
    header_items = driver.find_elements(By.CSS_SELECTOR, ".navlink.navlink--toplevel")
    for item in header_items:
        span_element = item.find_element(By.TAG_NAME, "span")
        # print(span_element.text)
        if span_element.text == "TUMBLERS":
            span_element.click()
            break

    ## Both for loop and xpath can do the same thing

    # Use XPath to directly locate the span with text "Tumblers" inside the desired class
    tumblers_span = driver.find_element(
        By.XPATH,
        "//a[contains(@class, 'navlink navlink--toplevel')]//span[text()='Tumblers']",
    )
    # Click on the span element
    tumblers_span.click()
    links = []
    names = []
    info = []
    ## get the products list
    products = driver.find_elements(By.CLASS_NAME, "product__grid__info.text-left")
    for product in products:
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        product_name = product.find_element(
            By.CSS_SELECTOR, ".product__grid__title"
        ).text
        price_info = product.find_element(
            By.CLASS_NAME, "product__grid__price.product__grid__price--nowrap"
        )

        # Get price details
        price_text = " ".join(
            [span.text for span in price_info.find_elements(By.TAG_NAME, "span")]
        )

        # Append details to lists
        links.append(link)
        names.append(product_name)
        info.append(price_text)

    df = pd.DataFrame(
        {"Product Name": names, "Product Link": links, "Price Info": info}
    )

    df.to_csv("tumblers.csv", index=False)
    print("saved to csv file")

except Exception as e:
    print(e)
finally:
    driver.quit()
