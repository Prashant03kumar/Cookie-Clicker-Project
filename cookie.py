import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# Add a User-Agent header
chrome_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# 1 TODO  "Click continuously on cookie"

cookie_button=driver.find_element(By.CSS_SELECTOR,"#cookie")

# 2 TODO "Check right hand panel for every five seconds "

# Get upgrade item ids.
# string ids of all item to buy
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout=time.time()+5   # Current time + 5
five_min=time.time()+60*5 # 5mins more in cureent time

while True:
    cookie_button.click()

    #Every 5 seconds
    if time.time()>timeout: # Current time is greater then 5 seconds

        # Get all upgarde <b> tags
        # These all prices are store in <b> in store id
        all_prices=driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_prices=[]

        # Converting all value of prices in integer
        for price in all_prices:
            element_text=price.text
            if element_text!="":
                cost=int(element_text.split("-")[1].strip().replace(",",""))
                #Strip to remove trail or leading spaces from 50 and replace remove , from 1,00
                item_prices.append(cost)\
        
        #Create dictionary of store items and prices 

        cookie_upgrade={}
        for n in range(len(item_prices)):
            # Prices will key and "ids" will "value"
            cookie_upgrade[item_prices[n]]=item_ids[n]

        # Get current cookie count
        money_element=driver.find_element(By.CSS_SELECTOR,value="#money").text #It will return current money

        if "," in money_element:
            money_element=money_element.replace(",","")
        cookie_count=int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades={}
        for cost,id in cookie_upgrade.items():
            if cookie_count>cost:
                # It wil store all ids whose prices or count are low then current count
                affordable_upgrades[cost]=id
        
        #Purchase most expensive affordable upgrades
        highest_affordable_price_upgrades=max(affordable_upgrades)

        print(highest_affordable_price_upgrades)
        #Which we have to purchase
        to_purchase_id=affordable_upgrades[highest_affordable_price_upgrades]

        driver.find_element(By.ID,value=to_purchase_id).click()

        # Adding more 5 seconds to current time and set new timeout until the next check
        timeout=time.time()+5

    # After 5minutes stop the bot and check the cookies per seconds count
    if time.time()>five_min:
        cookie_per_sec=driver.find_element(By.ID,value="cps").text
        print(cookie_per_sec)
        break



