from selenium import webdriver

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

    start_typing(driver)
