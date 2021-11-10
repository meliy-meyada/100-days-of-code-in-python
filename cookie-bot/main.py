from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



chrome_driver_path = r"Your Driver Chrome Location PATH"
chrome_service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


game_time = time.time() + 5 * 60
buy_time = time.time() + 5

cookie_click = driver.find_element(by="id", value="cookie")

upgrade_items = driver.find_element(by="id", value="store")
upgrades_list = {}
upgrades_list = [item.text.split(sep=" - ") for item in upgrade_items.find_elements_by_css_selector("b")]

while True:
    cookie_click.click()

    if time.time() >= buy_time:
        money = int(driver.find_element(by="id", value="money").text.replace(",", ""))

        for price in range(len(upgrades_list) - 1):
            item_price = int(upgrades_list[price][1].replace(",", ""))
            if money >= item_price:
                upgrade = upgrades_list[price][0]

        if upgrade != "":
            selected_upgrade = driver.find_element(by="id", value=f"buy{upgrade}")
            selected_upgrade.click()

        buy_time += 5

    if time.time() > game_time:
        results = driver.find_element(by="id", value="cps").text
        print(results)
        break
