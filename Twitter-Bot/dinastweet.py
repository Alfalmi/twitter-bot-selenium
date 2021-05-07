# importing all modules/packages
import csv
import selenium
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def get_tweet_data(pack_tweet):
    """Extract data from tweet data"""
    user_name = card.find_element_by_xpath(".// span").text
    handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text

    try:
        post_date = card.find_element_by_xpath('//time').get_attribute('datetime')
    except NoSuchElementException:
        return

    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    resp = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    reply = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    likes = card.find_element_by_xpath('.//div[@data-testid="like"]').text

    cnt_text = comment + resp

    tweet = (user_name, handle, post_date, cnt_text, reply, retweet, likes)
    return tweet


# creating an instane of our webdriver and applying options
options = Options()
options.add_argument("start-maximized")
driver = selenium.webdriver.Chrome(options=options)


# creating a function to read from our text file which returns our email and password
def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password


# storing email and password
email, password = account_info()

# opens Chrome on Twitter's login page
driver.get("https://twitter.com/login")

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'

time.sleep(3)

# interacts with Twitter's login page, logs in and search
# LOGIN

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(1)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(1.5)

# search text input
search_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input'
time.sleep(.5)
driver.find_element_by_xpath(search_xpath).send_keys('#KeepWalking')
time.sleep(.5)
driver.find_element_by_xpath(search_xpath).send_keys(Keys.RETURN)
time.sleep(2)

# interact with the result page

driver.find_element_by_link_text('Latest').click()
time.sleep(2)

page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')


driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div').click()

