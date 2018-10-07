from selenium import webdriver
from bs4 import BeautifulSoup


def start_typing(driver):
    inputField = driver.find_element_by_id("inputfield")

    words= driver.find_element_by_id('words')
    for i in words.find_elements_by_tag_name('span'):
        word=str(i.get_attribute('innerHTML'))
        inputField.send_keys(word)
        inputField.send_keys(' ')

if __name__ == '__main__':
    driver = webdriver.Chrome('./drivers/chromedriver.exe')
    driver.set_page_load_timeout(10)
    driver.get("https://10fastfingers.com/typing-test/english")
    html=driver.page_source
    soup=BeautifulSoup(html,"lxml")
    print soup.prettify()

    start_typing(driver)
    #add this feed back form
script=int(input("RATE YOUR EXPERIANCE FROM 1-5 : "))
print()
if (script == 1 ):
    print("we will try to imporve please tell us where are we lacking behind")
if (script == 2 ):
    print("we will try to imporve please tell us where are we lacking behind")
if (script == 3):
    print("thankyou have nice day ")
if (script == 4 ):
    print("i am glat you had a great experian thank you so much")
if (script == 5 ):
    print("i am glat you had a great experian thank you so much")
