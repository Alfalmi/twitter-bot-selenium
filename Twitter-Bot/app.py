# importing all modules/packages
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from quoters import Quote
import time


# creating a function to read from our text file which returns our email and password
def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password


# storing email and password
email, password = account_info()

# creating an instane of our webdriver and applying options
options = Options()
options.add_argument("start-maximized")
driver = selenium.webdriver.Chrome(options=options)

# opens Chrome on Twitter's login page
driver.get("https://twitter.com/login")

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'

time.sleep(2)

# interacts with Twitter's login page and logs in

driver.find_element_by_xpath(email_xpath).send_keys(email)
# time.sleep(1)
driver.find_element_by_xpath(password_xpath).send_keys(password)
# time.sleep(1)
driver.find_element_by_xpath(login_xpath).click()

# specifying more xpaths

tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
post_tweet_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span'

qt_ant = ' '

for x in range(15):

    # posts a tweet

    qt = Quote.print()

    if qt != qt_ant:
        driver.find_element_by_xpath(tweet_xpath).click()
        # time.sleep(2)
        driver.find_element_by_xpath(message_xpath).send_keys(qt)
        # time.sleep(2)
        driver.find_element_by_xpath(post_tweet_xpath).click()
        time.sleep(1)
        qt_ant = qt
