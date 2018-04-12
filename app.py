from selenium import webdriver;

def start_typing(driver):
    inputField = driver.find_element_by_id("inputfield");

    for i in range(345):
        try:
            text = driver.find_element_by_xpath("//span[@wordnr='" + str(i) + "']").text
            inputField.send_keys(text)
            inputField.send_keys(" ")
        except:
            print("Done")
            break

if __name__ == '__main__':
    driver = webdriver.Chrome('./drivers/chromedriver.exe')
    driver.set_page_load_timeout(10)
    driver.get("https://10fastfingers.com/typing-test/english")

    start_typing(driver)
