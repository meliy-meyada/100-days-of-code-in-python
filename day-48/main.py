from selenium import webdriver
from selenium.webdriver.chrome.service import Service



chrome_driver_path = r"Your Driver Chrome Location PATH"
chrome_service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.python.org/")

# price = driver.find_element(by="class name" value="a-offscreen")
# print(price.text)

# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(by="class name", value="python-logo")
# print(logo.size)

# documentation_link = driver.find_element(by="css selector", value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(by="xpath", value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

event_times = driver.find_element(by="css selector", value=".event-widget time")
event_names = driver.find_element(by="css selector", value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

# driver.close()
driver.quit()
