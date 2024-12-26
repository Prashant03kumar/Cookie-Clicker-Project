from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(article_count.text)
# for clicking on a particular element 
# article_count.click()

# Like if i want search with given text in search box
try:
    # Wait for the search box to be interactable
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "search"))
    )

    # Interact with the search box
    search.send_keys("Python")  # Input search term
    search.send_keys(Keys.RETURN)  # Press Enter to search

    print("Search performed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Optional: Close the driver after some time (comment out to keep the browser open)
    # driver.quit()
    pass
