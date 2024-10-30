# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.get("https://leetcode.com/")

# explore = driver.find_element(
#     By.XPATH,
#     "//*[@id='landing-page-app']/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[2]/span",
# )
# explore.click()
# problem_set = driver.find_element(
#     By.XPATH, "//*[@id='product']/div/div/div[1]/div/a"
# ).get_attribute("href")
# driver.get(problem_set)

# time.sleep(2)  # wait for the page to load


# pages = driver.find_elements(
#     By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[3]/nav/button"
# )
# total_n_of_pages = pages[-2].text

# # print(len(pages))


# for i in range(int(total_n_of_pages)):

#     try:
#         # Wait until the page button is clickable
#         page_count = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, '//*[@id="headlessui-listbox-button-:ra:"]')
#             )
#         )
#         page_count.click()

#         # Wait for the options to load and become clickable
#         page_20_click = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[3]/div/ul/li[1]",
#                 )
#             )
#         )
#         # print(page_20_click.text)
#         # Uncomment to click if needed
#         page_20_click.click()

#     except Exception as e:
#         print(e)

#     time.sleep(3)

#     try:
#         # Using CSS_SELECTOR to handle compound class names
#         q = driver.find_elements(
#             By.CSS_SELECTOR,
#             ".odd\\:bg-layer-1.even\\:bg-overlay-1.dark\\:odd\\:bg-dark-layer-bg.dark\\:even\\:bg-dark-fill-4",
#         )
#         # q = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div')
#         print(len(q))
#     except Exception as e:
#         print(e)

#     # Using a for loop with error handling
#     for i in range(1, len(q) + 1):
#         try:
#             title_link = driver.find_element(
#                 By.XPATH,
#                 f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a',
#             ).get_attribute("href")
#             title = driver.find_element(
#                 By.XPATH,
#                 f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a',
#             ).text
#             solution = driver.find_element(
#                 By.XPATH,
#                 f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[3]/a',
#             ).get_attribute("href")
#             acceptance = driver.find_element(
#                 By.XPATH,
#                 f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[4]',
#             ).text
#             diff = driver.find_element(
#                 By.XPATH,
#                 f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[5]',
#             ).text
#             print(title, title_link, solution, acceptance, diff, "\n")

#         except Exception as e:
#             print(f"Element at index {i} not found: {e}")
#             continue  # Continue to the next iteration in case of an error

#     # click for next  page
#     pages[-1].click()
#     time.sleep(5)


# # Wait for user input before closing
# input("Press Enter to continue...")

# # Close the browser
# driver.quit()













from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Initialize the driver
driver = webdriver.Chrome()
driver.get("https://leetcode.com/")

# Navigate to the required page
explore = driver.find_element(
    By.XPATH,
    "//*[@id='landing-page-app']/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[2]/span",
)
explore.click()
problem_set = driver.find_element(
    By.XPATH, "//*[@id='product']/div/div/div[1]/div/a"
).get_attribute("href")
driver.get(problem_set)

time.sleep(2)  # Wait for the page to load

# Set up CSV file
with open("leetcode_problems.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Title Link", "Solution Link", "Acceptance", "Difficulty"])  # Header row

    pages = driver.find_elements(
        By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[3]/nav/button"
    )
    total_n_of_pages = pages[-2].text

    for page_num in range(int(total_n_of_pages)):
        try:
            # Wait until the page button is clickable
            page_count = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="headlessui-listbox-button-:ra:"]')
                )
            )
            page_count.click()

            # Wait for the options to load and become clickable
            page_20_click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[3]/div/ul/li[1]")
                )
            )
            page_20_click.click()
        except Exception as e:
            print(e)

        time.sleep(3)

        try:
            q = driver.find_elements(
                By.CSS_SELECTOR,
                ".odd\\:bg-layer-1.even\\:bg-overlay-1.dark\\:odd\\:bg-dark-layer-bg.dark\\:even\\:bg-dark-fill-4",
            )
            print(f"Number of problems on the page: {len(q)}")
        except Exception as e:
            print(e)

        # Loop through each problem on the current page
        for i in range(1, len(q) + 1):
            try:
                title_link = driver.find_element(
                    By.XPATH,
                    f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a',
                ).get_attribute("href")
                title = driver.find_element(
                    By.XPATH,
                    f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a',
                ).text
                solution = driver.find_element(
                    By.XPATH,
                    f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[3]/a',
                ).get_attribute("href")
                acceptance = driver.find_element(
                    By.XPATH,
                    f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[4]',
                ).text
                diff = driver.find_element(
                    By.XPATH,
                    f'//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[{i}]/div[5]',
                ).text

                # Write each row to the CSV
                writer.writerow([title, title_link, solution, acceptance, diff])
                print(title, title_link, solution, acceptance, diff, "\n")

            except Exception as e:
                print(f"Element at index {i} not found: {e}")
                continue

        # Click to go to the next page
        pages[-1].click()
        time.sleep(5)

# Close the browser after completion
driver.quit()
