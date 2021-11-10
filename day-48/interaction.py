from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



chrome_driver_path = r"ํ"
chrome_service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service)
driver.get("http://secure-retreat-92358.herokuapp.com/")


# article_count = driver.find_element(by="css selector", value="#articlecount a")
# # article_count.click()
#
#
# all_portals = driver.find_element(by="link text", value="All portals")
# # all_portals.click()


# search = driver.find_element(by="name", value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
FIRST_NAME = "*****"
LAST_NAME = "****"
EMAIL = "***@***.com"

f_name = driver.find_element(by="name", value="fName")
f_name.send_keys(FIRST_NAME)

l_name = driver.find_element(by="name", value="lName")
l_name.send_keys(LAST_NAME)

email = driver.find_element(by="name", value="email")
email.send_keys(EMAIL)


submit = driver.find_element(by="css selector", value="form button")
submit.click()