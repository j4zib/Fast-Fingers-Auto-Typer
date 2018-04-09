from selenium import webdriver;

driver = webdriver.Chrome('./drivers/chromedriver.exe')

driver.set_page_load_timeout(10)
driver.get("https://10fastfingers.com/typing-test/english")

for i in range(338):
    text = driver.find_element_by_xpath("//span[@wordnr='" + str(i) + "']").text + " "
    for letter in text:
        driver.find_element_by_id("inputfield").send_keys(letter)
