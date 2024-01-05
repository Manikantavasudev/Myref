import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tirumala.org/Home.aspx")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present in the website", len(links))
for link in links:
    print(link.text)

# driver.find_element(By.LINK_TEXT, "Online Services").click()
# print("clicked on online services")
driver.find_element(By.PARTIAL_LINK_TEXT, "Online").click()
print("clicked on online services")


time.sleep(5)
driver.close()