from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Navigate to url

driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)


#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Navigate to url

driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page

webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()


#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Navigate to url

driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page

webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()


#


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url

driver.get("http://www.google.com")
# Store 'SearchInput' element

SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
# Clears the entered text

SearchInput.clear()
